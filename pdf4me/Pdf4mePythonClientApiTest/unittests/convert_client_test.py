
import sys
sys.path.append('../../Pdf4mePythonClientApi')
sys.path.append('../../Pdf4mePythonClientApiTest')

from pdf4me.client.convert_client import ConvertClient
from pdf4me.client.pdf4me_client import Pdf4meClient
from pdf4me.helper.file_reader import FileReader
from pdf4me.helper.pdf4me_exceptions import Pdf4meClientException
from pdf4me.model import ConvertToPdf, Document, ConvertToPdfAction
from test_helper.check import Check
from test_helper.test_files import TestFiles

import unittest

from nose.tools import assert_raises, assert_equal


class ConvertClientTest(unittest.TestCase):

    pdf4me_client = Pdf4meClient()
    convert_client = ConvertClient(pdf4me_client)

    test_files = TestFiles()
    check = Check()
    file_reader = FileReader()

    def create_convert_to_pdf(self, file, file_name):

        convert_to_pdf = ConvertToPdf(
            document=Document(
                doc_data=file,
                name=file_name
            ),
            convert_to_pdf_action=ConvertToPdfAction()
        )

        return convert_to_pdf

    def test_convert_to_pdf_throws_exception(self):

        with assert_raises(Pdf4meClientException) as e:
            self.convert_client.convert_to_pdf(None)

        assert_equal(e.exception.msg, 'The convert_to_pdf parameter cannot be None.')

    def test_convert_to_pdf_document_throws_exception(self):

        # prepare args
        convert_to_pdf = self.create_convert_to_pdf(self.test_files.text_data, self.test_files.text_name)
        convert_to_pdf._document = None

        with assert_raises(Pdf4meClientException) as e:
            self.convert_client.convert_to_pdf(convert_to_pdf=convert_to_pdf)

        assert_equal(e.exception.msg, 'The convert_to_pdf document cannot be None.')

    def test_convert_to_pdf_document_data_throws_exception(self):

        # prepare args
        convert_to_pdf = self.create_convert_to_pdf(self.test_files.text_data, self.test_files.text_name)
        convert_to_pdf.document.doc_data = None

        with assert_raises(Pdf4meClientException) as e:
            self.convert_client.convert_to_pdf(convert_to_pdf=convert_to_pdf)

        assert_equal(e.exception.msg, 'The convert_to_pdf document cannot be None.')

    def test_convert_to_pdf_action_throws_exception(self):

        # prepare args
        convert_to_pdf = self.create_convert_to_pdf(self.test_files.text_data, self.test_files.text_name)
        convert_to_pdf.convert_to_pdf_action = None

        with assert_raises(Pdf4meClientException) as e:
            self.convert_client.convert_to_pdf(convert_to_pdf=convert_to_pdf)

        assert_equal(e.exception.msg, 'The convert_to_pdf_action cannot be None.')

    """text file"""

    def test_convert_to_pdf_text_no_none_response(self):

        # request
        convert_to_pdf = self.create_convert_to_pdf(self.test_files.text_data, self.test_files.text_name)
        res = self.convert_client.convert_to_pdf(convert_to_pdf=convert_to_pdf)

        # validation
        self.assertIsNotNone(res)
        self.assertIsNotNone(res['document'])
        self.assertIsNotNone(res['document']['doc_data'])

    def test_convert_to_pdf_text_doc_length(self):

        # request
        convert_to_pdf = self.create_convert_to_pdf(self.test_files.text_data, self.test_files.text_name)
        res = self.convert_client.convert_to_pdf(convert_to_pdf=convert_to_pdf)

        # validation
        original_length = self.test_files.text_length
        pdf_length = len(res['document']['doc_data'])

        self.assertTrue(self.check.above(pdf_length, original_length))

    """word doc"""

    def test_convert_to_pdf_word_no_none_response(self):
        # request
        convert_to_pdf = self.create_convert_to_pdf(self.test_files.word_data, self.test_files.word_name)
        res = self.convert_client.convert_to_pdf(convert_to_pdf=convert_to_pdf)

        # validation
        self.assertIsNotNone(res)
        self.assertIsNotNone(res['document'])
        self.assertIsNotNone(res['document']['doc_data'])

    def test_convert_to_pdf_word_doc_length(self):
        # request
        convert_to_pdf = self.create_convert_to_pdf(self.test_files.word_data, self.test_files.word_name)
        res = self.convert_client.convert_to_pdf(convert_to_pdf=convert_to_pdf)

        # validation
        original_length = self.test_files.word_length
        pdf_length = len(res['document']['doc_data'])

        self.assertTrue(self.check.above(pdf_length, original_length))

    """excel doc"""

    def test_convert_to_pdf_excel_no_none_response(self):
        # request
        convert_to_pdf = self.create_convert_to_pdf(self.test_files.excel_data, self.test_files.excel_name)
        res = self.convert_client.convert_to_pdf(convert_to_pdf=convert_to_pdf)

        # validation
        self.assertIsNotNone(res)
        self.assertIsNotNone(res['document'])
        self.assertIsNotNone(res['document']['doc_data'])

    def test_convert_to_pdf_excel_doc_length(self):
        # request
        convert_to_pdf = self.create_convert_to_pdf(self.test_files.excel_data, self.test_files.excel_name)
        res = self.convert_client.convert_to_pdf(convert_to_pdf=convert_to_pdf)

        # validation
        original_length = self.test_files.excel_length
        pdf_length = len(res['document']['doc_data'])

        self.assertTrue(self.check.above(pdf_length, original_length))

    """eml"""

    def test_convert_to_pdf_eml_no_none_response(self):
        # request
        convert_to_pdf = self.create_convert_to_pdf(self.test_files.eml_data, self.test_files.eml_name)
        res = self.convert_client.convert_to_pdf(convert_to_pdf=convert_to_pdf)

        # validation
        self.assertIsNotNone(res)
        self.assertIsNotNone(res['document'])
        self.assertIsNotNone(res['document']['doc_data'])

    def test_convert_to_pdf_eml_doc_length(self):
        # request
        convert_to_pdf = self.create_convert_to_pdf(self.test_files.eml_data, self.test_files.eml_name)
        res = self.convert_client.convert_to_pdf(convert_to_pdf=convert_to_pdf)

        # validation
        original_length = self.test_files.eml_length
        pdf_length = len(res['document']['doc_data'])

        self.assertTrue(self.check.above(pdf_length, original_length))

    """msg"""

    def test_convert_to_pdf_msg_no_none_response(self):
        # request
        convert_to_pdf = self.create_convert_to_pdf(self.test_files.msg_data, self.test_files.msg_name)
        res = self.convert_client.convert_to_pdf(convert_to_pdf=convert_to_pdf)

        # validation
        self.assertIsNotNone(res)
        self.assertIsNotNone(res['document'])
        self.assertIsNotNone(res['document']['doc_data'])

    def test_convert_to_pdf_msg_doc_length(self):
        # request
        convert_to_pdf = self.create_convert_to_pdf(self.test_files.msg_data, self.test_files.msg_name)
        res = self.convert_client.convert_to_pdf(convert_to_pdf=convert_to_pdf)

        # validation
        original_length = self.test_files.msg_length
        pdf_length = len(res['document']['doc_data'])

        self.assertTrue(self.check.above(pdf_length, original_length))

    """jpg"""

    def test_convert_to_pdf_jpg_no_none_response(self):
        # request
        convert_to_pdf = self.create_convert_to_pdf(self.test_files.jpg_data, self.test_files.jpg_name)
        res = self.convert_client.convert_to_pdf(convert_to_pdf=convert_to_pdf)

        # validation
        self.assertIsNotNone(res)
        self.assertIsNotNone(res['document'])
        self.assertIsNotNone(res['document']['doc_data'])

    def test_convert_to_pdf_jpg_doc_length(self):
        # request
        convert_to_pdf = self.create_convert_to_pdf(self.test_files.jpg_data, self.test_files.jpg_name)
        res = self.convert_client.convert_to_pdf(convert_to_pdf=convert_to_pdf)

        # validation
        original_length = self.test_files.jpg_length
        pdf_length = len(res['document']['doc_data'])

        self.assertTrue(self.check.above(pdf_length, original_length))

    """zip"""

    def test_convert_to_pdf_zip_no_none_response(self):
        # request
        convert_to_pdf = self.create_convert_to_pdf(self.test_files.zip_data, self.test_files.zip_name)
        res = self.convert_client.convert_to_pdf(convert_to_pdf=convert_to_pdf)

        # validation
        self.assertIsNotNone(res)
        self.assertIsNotNone(res['document'])
        self.assertIsNotNone(res['document']['doc_data'])

    def test_convert_to_pdf_zip_doc_length(self):
        # request
        convert_to_pdf = self.create_convert_to_pdf(self.test_files.zip_data, self.test_files.zip_name)
        res = self.convert_client.convert_to_pdf(convert_to_pdf=convert_to_pdf)

        # validation
        original_length = self.test_files.zip_length
        pdf_length = len(res['document']['doc_data'])

        self.assertTrue(self.check.below_not_zero(pdf_length, original_length))

    """convert_file_to_pdf"""

    """text file"""

    def test_convert_file_to_pdf_text_no_none_response(self):

        # request
        res = self.convert_client.convert_file_to_pdf(
            file=self.file_reader.get_file_handler(self.test_files.text_path),
            file_name=self.test_files.text_name
        )

        # validation
        self.assertIsNotNone(res)

    def test_convert_file_to_pdf_text_doc_length(self):

        # request
        res = self.convert_client.convert_file_to_pdf(
            file=self.file_reader.get_file_handler(self.test_files.text_path),
            file_name=self.test_files.text_name
        )

        # validation
        original_length = self.test_files.text_length
        pdf_length = self.check.get_doc_base64_length(res)

        self.assertTrue(self.check.above(pdf_length, original_length))

    """word doc"""

    def test_convert_file_to_pdf_word_no_none_response(self):
        # request
        res = self.convert_client.convert_file_to_pdf(
            file=self.file_reader.get_file_handler(self.test_files.word_path),
            file_name=self.test_files.word_name
        )

        # validation
        self.assertIsNotNone(res)

    def test_convert_file_to_pdf_word_doc_length(self):
        # request
        res = self.convert_client.convert_file_to_pdf(
            file=self.file_reader.get_file_handler(self.test_files.word_path),
            file_name=self.test_files.word_name
        )

        # validation
        original_length = self.test_files.word_length
        pdf_length = self.check.get_doc_base64_length(res)

        self.assertTrue(self.check.above(pdf_length, original_length))

    """excel doc"""

    def test_convert_file_to_pdf_excel_no_none_response(self):
        # request
        res = self.convert_client.convert_file_to_pdf(
            file=self.file_reader.get_file_handler(self.test_files.excel_path),
            file_name=self.test_files.excel_name
        )

        # validation
        self.assertIsNotNone(res)

    def test_convert_file_to_pdf_excel_doc_length(self):
        # request
        res = self.convert_client.convert_file_to_pdf(
            file=self.file_reader.get_file_handler(self.test_files.excel_path),
            file_name=self.test_files.excel_name
        )

        # validation
        original_length = self.test_files.excel_length
        pdf_length = self.check.get_doc_base64_length(res)

        self.assertTrue(self.check.above(pdf_length, original_length))

    """eml"""

    def test_convert_file_to_pdf_eml_no_none_response(self):
        # request
        res = self.convert_client.convert_file_to_pdf(
            file=self.file_reader.get_file_handler(self.test_files.eml_path),
            file_name=self.test_files.eml_name
        )

        # validation
        self.assertIsNotNone(res)

    def test_convert_file_to_pdf_eml_doc_length(self):
        # request
        res = self.convert_client.convert_file_to_pdf(
            file=self.file_reader.get_file_handler(self.test_files.eml_path),
            file_name=self.test_files.eml_name
        )

        # validation
        original_length = self.test_files.eml_length
        pdf_length = self.check.get_doc_base64_length(res)

        self.assertTrue(self.check.above(pdf_length, original_length))

    """msg"""

    def test_convert_file_to_pdf_msg_no_none_response(self):
        # request
        res = self.convert_client.convert_file_to_pdf(
            file=self.file_reader.get_file_handler(self.test_files.msg_path),
            file_name=self.test_files.msg_name
        )

        # validation
        self.assertIsNotNone(res)

    def test_convert_file_to_pdf_msg_doc_length(self):
        # request
        res = self.convert_client.convert_file_to_pdf(
            file=self.file_reader.get_file_handler(self.test_files.msg_path),
            file_name=self.test_files.msg_name
        )

        # validation
        original_length = self.test_files.msg_length
        pdf_length = self.check.get_doc_base64_length(res)

        self.assertTrue(self.check.above(pdf_length, original_length))

    """jpg"""

    def test_convert_file_to_pdf_jpg_no_none_response(self):
        # request
        res = self.convert_client.convert_file_to_pdf(
            file=self.file_reader.get_file_handler(self.test_files.jpg_path),
            file_name=self.test_files.jpg_name
        )

        # validation
        self.assertIsNotNone(res)

    def test_convert_file_to_pdf_jpg_doc_length(self):
        # request
        res = self.convert_client.convert_file_to_pdf(
            file=self.file_reader.get_file_handler(self.test_files.jpg_path),
            file_name=self.test_files.jpg_name
        )

        # validation
        original_length = self.test_files.jpg_length
        pdf_length = self.check.get_doc_base64_length(res)

        self.assertTrue(self.check.above(pdf_length, original_length))

    """zip"""

    def test_convert_file_to_pdf_zip_no_none_response(self):
        # request
        res = self.convert_client.convert_file_to_pdf(
            file=self.file_reader.get_file_handler(self.test_files.zip_path),
            file_name=self.test_files.zip_name
        )

        # validation
        self.assertIsNotNone(res)

    def test_convert_file_to_pdf_zip_doc_length(self):
        # request
        res = self.convert_client.convert_file_to_pdf(
            file=self.file_reader.get_file_handler(self.test_files.zip_path),
            file_name=self.test_files.zip_name
        )

        # validation
        original_length = self.test_files.zip_length
        pdf_length = self.check.get_doc_base64_length(res)

        self.assertTrue(self.check.below_not_zero(pdf_length, original_length))
