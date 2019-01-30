import sys

sys.path.append('../../Pdf4mePythonClientApi')
sys.path.append('../../Pdf4mePythonClientApiTest')

import unittest

from nose.tools import assert_raises, assert_equal

from pdf4me.client.pdf4me_client import Pdf4meClient
from pdf4me.client.split_client import SplitClient
from pdf4me.helper.file_reader import FileReader
from pdf4me.helper.pdf4me_exceptions import Pdf4meClientException
from pdf4me.model import Document, Split, SplitAction
from test_helper.check import Check
from test_helper.test_files import TestFiles


class SplitClientTest(unittest.TestCase):
    pdf4me_client = Pdf4meClient()
    split_client = SplitClient(pdf4me_client)

    test_files = TestFiles()
    check = Check()
    file_reader = FileReader()

    def create_split(self):
        split = Split(
            document=Document(
                doc_data=self.test_files.pdf_data
            ),
            split_action=SplitAction(
                split_after_page=2
            )
        )

        return split

    def test_split_throws_exception(self):
        with assert_raises(Pdf4meClientException) as e:
            self.split_client.split(None)

        assert_equal(e.exception.msg, 'The split parameter cannot be None.')

    def test_split_document_throws_exception(self):
        # prepare args
        split = self.create_split()
        split.document = None

        with assert_raises(Pdf4meClientException) as e:
            self.split_client.split(split=split)

        assert_equal(e.exception.msg, 'The split document cannot be None.')

    def test_split_document_data_throws_exception(self):
        # prepare args
        split = self.create_split()
        split.document.doc_data = None

        with assert_raises(Pdf4meClientException) as e:
            self.split_client.split(split=split)

        assert_equal(e.exception.msg, 'The split document cannot be None.')

    def test_split_action_throws_exception(self):
        # prepare args
        split = self.create_split()
        split.split_action = None

        with assert_raises(Pdf4meClientException) as e:
            self.split_client.split(split=split)

        assert_equal(e.exception.msg, 'The split_action cannot be None.')

    def test_split_action_split_after_page_1_throws_exception(self):
        # prepare args
        split = self.create_split()
        split.split_action.split_after_page = None

        with assert_raises(Pdf4meClientException) as e:
            self.split_client.split(split=split)

        assert_equal(e.exception.msg, 'The split_after_page of split_action cannot be None or zero.'
                                      'The first page of a PDF corresponds to page number one.')

    def test_split_action_split_after_page_2_throws_exception(self):
        # prepare args
        split = self.create_split()
        split.split_action.split_after_page = 0

        with assert_raises(Pdf4meClientException) as e:
            self.split_client.split(split=split)

        assert_equal(e.exception.msg, 'The split_after_page of split_action cannot be None or zero.'
                                      'The first page of a PDF corresponds to page number one.')

    def test_split_no_none_response(self):
        # request
        split = self.create_split()
        res = self.split_client.split(split=split)

        print(res)
        # validation
        self.assertIsNotNone(res)
        self.assertIsNotNone(res['documents'])
        self.assertIsNotNone(res['documents'][0])
        self.assertIsNotNone(res['documents'][0]['doc_data'])
        self.assertIsNotNone(res['documents'][1])
        self.assertIsNotNone(res['documents'][1]['doc_data'])

    def test_split_doc_length(self):
        # request
        split = self.create_split()
        res = self.split_client.split(split=split)

        # validation
        original_length = self.test_files.pdf_length
        pdf1 = len(res['documents'][0]['doc_data'])
        pdf2 = len(res['documents'][1]['doc_data'])

        self.assertTrue(self.check.below_not_zero(pdf1, original_length))
        self.assertTrue(self.check.below_not_zero(pdf2, original_length))

    def test_split_by_page_nr_no_none_response(self):
        # request
        pdf_1, pdf_2 = self.split_client.split_by_page_nr(
            page_nr=2,
            file=self.file_reader.get_file_handler(path=self.test_files.pdf_path)
        )

        # validation
        self.assertIsNotNone(pdf_1)
        self.assertIsNotNone(pdf_2)

    def test_split_by_page_nr_doc_length(self):
        # request
        pdf_1, pdf_2 = self.split_client.split_by_page_nr(
            page_nr=2,
            file=self.file_reader.get_file_handler(path=self.test_files.pdf_path)
        )

        # validation
        original_length = self.test_files.pdf_length
        pdf_1_length = len(pdf_1)
        pdf_2_length = len(pdf_2)

        self.assertTrue(self.check.below_not_zero(pdf_1_length, original_length))
        self.assertTrue(self.check.below_not_zero(pdf_2_length, original_length))


print("test")
