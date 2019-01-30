import sys

sys.path.append('../../Pdf4mePythonClientApi')
sys.path.append('../../Pdf4mePythonClientApiTest')

import unittest

from nose.tools import assert_raises, assert_equal

from pdf4me.client.pdf4me_client import Pdf4meClient
from pdf4me.client.pdfA_client import PdfAClient
from pdf4me.helper.file_reader import FileReader
from pdf4me.helper.pdf4me_exceptions import Pdf4meClientException
from pdf4me.model import CreatePdfA, Document, PdfAAction
from test_helper.check import Check
from test_helper.test_files import TestFiles


class PdfAClientTest(unittest.TestCase):
    pdf4me_client = Pdf4meClient()
    pdfA_client = PdfAClient(pdf4me_client)

    test_files = TestFiles()
    check = Check()
    file_reader = FileReader()

    def create_create_pdfA(self):
        create_pdfA = CreatePdfA(
            document=Document(
                doc_data=self.test_files.pdf_data
            ),
            pdf_a_action=PdfAAction(
                compliance='pdfA2u'
            )
        )

        return create_pdfA

    def test_pdfA_throws_exception(self):
        with assert_raises(Pdf4meClientException) as e:
            self.pdfA_client.pdfA(None)

        assert_equal(e.exception.msg, 'The create_pdfA parameter cannot be None.')

    def test_pdfA_document_throws_exception(self):
        # prepare args
        create_pdfA = self.create_create_pdfA()
        create_pdfA.document = None

        with assert_raises(Pdf4meClientException) as e:
            self.pdfA_client.pdfA(create_pdfA=create_pdfA)

        assert_equal(e.exception.msg, 'The create_pdfA document cannot be None.')

    def test_pdfA_document_data_throws_exception(self):
        # prepare args
        create_pdfA = self.create_create_pdfA()
        create_pdfA.document.doc_data = None

        with assert_raises(Pdf4meClientException) as e:
            self.pdfA_client.pdfA(create_pdfA=create_pdfA)

        assert_equal(e.exception.msg, 'The create_pdfA document cannot be None.')

    def test_pdfA_action_data_throws_exception(self):
        # prepare args
        create_pdfA = self.create_create_pdfA()
        create_pdfA.pdf_a_action = None

        with assert_raises(Pdf4meClientException) as e:
            self.pdfA_client.pdfA(create_pdfA=create_pdfA)

        assert_equal(e.exception.msg, 'The pdf_a_action cannot be None.')

    def test_pdfA_no_none_response(self):
        # request
        create_pdfA = self.create_create_pdfA()
        res = self.pdfA_client.pdfA(create_pdfA)

        # validation
        self.assertIsNotNone(res)
        self.assertIsNotNone(res['document'])
        self.assertIsNotNone(res['document']['doc_data'])

    def test_pdfA_doc_length(self):
        # request
        create_pdfA = self.create_create_pdfA()
        res = self.pdfA_client.pdfA(create_pdfA)

        # validation
        original_length = self.test_files.pdf_length
        pdfA = len(res['document']['doc_data'])

        self.assertTrue(self.check.below_not_zero(pdfA, original_length))

    def test_create_pdfA_no_none_response(self):
        # request
        res = self.pdfA_client.create_pdfA(
            pdf_compliance='pdfA2u',
            file=self.file_reader.get_file_handler(path=self.test_files.pdf_path)
        )

        # validation
        self.assertIsNotNone(res)

    def test_create_pdfA_doc_length(self):
        # request
        res = self.pdfA_client.create_pdfA(
            pdf_compliance='pdfA2u',
            file=self.file_reader.get_file_handler(path=self.test_files.pdf_path)
        )

        # validation
        original_length = self.test_files.pdf_length
        pdfA = self.check.get_doc_base64_length(res)

        self.assertTrue(self.check.below_not_zero(pdfA, original_length))

    def test_create_pdfA_without_compliance_no_none_response(self):
        # request
        res = self.pdfA_client.create_pdfA(
            file=self.file_reader.get_file_handler(path=self.test_files.pdf_path)
        )

        # validation
        self.assertIsNotNone(res)

    def test_create_pdfA_without_compliance_doc_length(self):
        # request
        res = self.pdfA_client.create_pdfA(
            file=self.file_reader.get_file_handler(path=self.test_files.pdf_path)
        )

        # validation
        original_length = self.test_files.pdf_length
        pdfA = self.check.get_doc_base64_length(res)

        self.assertTrue(self.check.below_not_zero(pdfA, original_length))
