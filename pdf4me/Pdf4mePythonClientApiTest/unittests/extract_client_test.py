import sys

sys.path.append('../../Pdf4mePythonClientApi')
sys.path.append('../../Pdf4mePythonClientApiTest')

import unittest

from nose.tools import assert_raises, assert_equal

from pdf4me.client.extract_client import ExtractClient
from pdf4me.client.pdf4me_client import Pdf4meClient
from pdf4me.helper.file_reader import FileReader
from pdf4me.helper.pdf4me_exceptions import Pdf4meClientException
from pdf4me.model import Document, ExtractAction, Extract
from test_helper.check import Check
from test_helper.test_files import TestFiles


class ExtractClientTest(unittest.TestCase):
    pdf4me_client = Pdf4meClient()
    extract_client = ExtractClient(pdf4me_client)

    test_files = TestFiles()
    check = Check()
    file_reader = FileReader()

    def create_extract(self):
        extract = Extract(
            document=Document(
                doc_data=self.test_files.pdf_data
            ),
            extract_action=ExtractAction(
                extract_pages=[1, 4]
            )
        )

        return extract

    def test_extract_throws_exception(self):
        with assert_raises(Pdf4meClientException) as e:
            self.extract_client.extract(None)

        assert_equal(e.exception.msg, 'The extract parameter cannot be None.')

    def test_extract_document_throws_exception(self):
        # prepare args
        extract = self.create_extract()
        extract.document = None

        with assert_raises(Pdf4meClientException) as e:
            self.extract_client.extract(extract=extract)

        assert_equal(e.exception.msg, 'The extract document cannot be None.')

    def test_extract_document_data_throws_exception(self):
        # prepare args
        extract = self.create_extract()
        extract.document.doc_data = None

        with assert_raises(Pdf4meClientException) as e:
            self.extract_client.extract(extract=extract)

        assert_equal(e.exception.msg, 'The extract document cannot be None.')

    def test_extract_action_throws_exception(self):
        # prepare args
        extract = self.create_extract()
        extract.extract_action = None

        with assert_raises(Pdf4meClientException) as e:
            self.extract_client.extract(extract=extract)

        assert_equal(e.exception.msg, 'The extract_action cannot be None.')

    def test_extract_action_extract_pages_throws_exception(self):
        # prepare args
        extract = self.create_extract()
        extract.extract_action.extract_pages = None

        with assert_raises(Pdf4meClientException) as e:
            self.extract_client.extract(extract=extract)

        assert_equal(e.exception.msg, 'The extract_pages of extract_action cannot be None or empty.')

    def test_extract_action_extract_pages_throws_exception2(self):
        # prepare args
        extract = self.create_extract()
        extract.extract_action.extract_pages = []

        with assert_raises(Pdf4meClientException) as e:
            self.extract_client.extract(extract=extract)

        assert_equal(e.exception.msg, 'The extract_pages of extract_action cannot be None or empty.')

    def test_extract_no_none_response(self):
        # request
        extract = self.create_extract()
        res = self.extract_client.extract(extract=extract)

        # validation
        self.assertIsNotNone(res)
        self.assertIsNotNone(res['document'])
        self.assertIsNotNone(res['document']['doc_data'])

    def test_extract_doc_length(self):
        # request
        extract = self.create_extract()
        res = self.extract_client.extract(extract=extract)

        # validation
        original_length = self.test_files.pdf_length
        shortened_pdf = len(res['document']['doc_data'])

        self.assertTrue(self.check.below_not_zero(shortened_pdf, original_length))

    def test_extract_pages_no_none_response(self):
        # request
        res = self.extract_client.extract_pages(
            page_nrs='1,4',
            file=self.file_reader.get_file_handler(path=self.test_files.pdf_path)
        )

        # validation
        self.assertIsNotNone(res)

    def test_extract_pages_doc_length(self):
        # request
        res = self.extract_client.extract_pages(
            page_nrs='1,4',
            file=self.file_reader.get_file_handler(path=self.test_files.pdf_path)
        )

        # validation
        original_length = self.test_files.pdf_length
        shortened_pdf = self.check.get_doc_base64_length(res)

        self.assertTrue(self.check.below_not_zero(shortened_pdf, original_length))
