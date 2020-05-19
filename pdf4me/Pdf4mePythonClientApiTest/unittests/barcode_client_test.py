import sys

sys.path.append('../../Pdf4mePythonClientApi')
sys.path.append('../../Pdf4mePythonClientApiTest')

import unittest

from nose.tools import assert_raises, assert_equal

from pdf4me.client.barcode_client import BarcodeClient
from pdf4me.client.pdf4me_client import Pdf4meClient
from pdf4me.helper.file_reader import FileReader
from pdf4me.helper.pdf4me_exceptions import Pdf4meClientException
from pdf4me.model import ReadBarcodes, Document, ReadBarcodeAction
from test_helper.check import Check
from test_helper.test_files import TestFiles


class BarcodeClientTest(unittest.TestCase):
    pdf4me_client = Pdf4meClient()
    barcode_client = BarcodeClient(pdf4me_client)

    test_files = TestFiles()
    check = Check()
    file_reader = FileReader()

    def create_read_barcode(self):
        read_barcodes = ReadBarcodes(
            document=Document(
                doc_data=self.test_files.pdf_barcode_data
            ),
            read_barcode_action=ReadBarcodeAction(
                barcode_types=['all']
            )
        )

        return read_barcodes

    def test_barcode_throws_exception(self):
        with assert_raises(Pdf4meClientException) as e:
            self.barcode_client.read_barcodes(None)

        assert_equal(e.exception.msg, 'The read_barcodes parameter cannot be None.')

    def test_barcode_document_throws_exception(self):
        # prepare args
        read_barcode = self.create_read_barcode()
        read_barcode.document = None

        with assert_raises(Pdf4meClientException) as e:
            self.barcode_client.read_barcodes(read_barcodes=read_barcode)

        assert_equal(e.exception.msg, 'The read_barcodes document cannot be None.')

    def test_barcode_document_data_throws_exception(self):
        # prepare args
        read_barcodes = self.create_read_barcode()
        read_barcodes.document.doc_data = None

        with assert_raises(Pdf4meClientException) as e:
            self.barcode_client.read_barcodes(read_barcodes=read_barcodes)

        assert_equal(e.exception.msg, 'The read_barcodes document cannot be None.')

    def test_barcode_action_throws_exception(self):
        # prepare args
        read_barcodes = self.create_read_barcode()
        read_barcodes.read_barcode_action = None

        with assert_raises(Pdf4meClientException) as e:
            self.barcode_client.read_barcodes(read_barcodes=read_barcodes)

        assert_equal(e.exception.msg, 'The read_barcode_action cannot be None.')

    def test_barcode_no_none_response(self):
        # request
        read_barcodes = self.create_read_barcode()
        res = self.barcode_client.read_barcodes(read_barcodes=read_barcodes)

        # validation
        self.assertIsNotNone(res)
        self.assertIsNotNone(res['barcodes'])
        self.assertIsNotNone(res['barcodes'][0]['barcode_data'])

    def test_barcode_doc_length(self):
        # request
        read_barcodes = self.create_read_barcode()
        res = self.barcode_client.read_barcodes(read_barcodes=read_barcodes)

        # validation
        read_barcodes_text = len(res['barcodes'][0]['barcode_data'])

        self.assertTrue(self.check.not_zero(read_barcodes_text))

    def test_barcode_by_profile_no_none_response(self):
        # request
        res = self.barcode_client.read_barcodes_by_type(
            barcode_type='all',
            file=self.file_reader.get_file_handler(path=self.test_files.pdf_barcode_path)
        )

        # validation
        self.assertIsNotNone(res)

    def test_barcode_by_profile_doc_length(self):
        # request
        res = self.barcode_client.read_barcodes_by_type(
            barcode_type='all',
            file=self.file_reader.get_file_handler(path=self.test_files.pdf_barcode_path)
        )

        # validation
        read_barcodes_text = len(res['barcodes'][0]['barcode_data'])

        self.assertTrue(self.check.not_zero(read_barcodes_text))
