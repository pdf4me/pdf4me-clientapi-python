from test_helper.test_files import TestFiles
from test_helper.check import Check
from pdf4me.model import ReadBarcodes, Document, ReadBarcodeAction, AddBarcode, AddBarcodeAction, BarcodeColor, \
    SplitByBarcodeReq, SplitByBarcodeAction
from pdf4me.helper.pdf4me_exceptions import Pdf4meClientException
from pdf4me.helper.file_reader import FileReader
from pdf4me.client.pdf4me_client import Pdf4meClient
from pdf4me.client.barcode_client import BarcodeClient
from nose.tools import assert_raises, assert_equal
import unittest
import sys

sys.path.append('../../Pdf4mePythonClientApi')
sys.path.append('../../Pdf4mePythonClientApiTest')


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

        assert_equal(e.exception.msg,
                     'The read_barcodes parameter cannot be None.')

    def test_barcode_document_throws_exception(self):
        # prepare args
        read_barcode = self.create_read_barcode()
        read_barcode.document = None

        with assert_raises(Pdf4meClientException) as e:
            self.barcode_client.read_barcodes(read_barcodes=read_barcode)

        assert_equal(e.exception.msg,
                     'The read_barcodes document cannot be None.')

    def test_barcode_document_data_throws_exception(self):
        # prepare args
        read_barcodes = self.create_read_barcode()
        read_barcodes.document.doc_data = None

        with assert_raises(Pdf4meClientException) as e:
            self.barcode_client.read_barcodes(read_barcodes=read_barcodes)

        assert_equal(e.exception.msg,
                     'The read_barcodes document cannot be None.')

    def test_barcode_action_throws_exception(self):
        # prepare args
        read_barcodes = self.create_read_barcode()
        read_barcodes.read_barcode_action = None

        with assert_raises(Pdf4meClientException) as e:
            self.barcode_client.read_barcodes(read_barcodes=read_barcodes)

        assert_equal(e.exception.msg,
                     'The read_barcode_action cannot be None.')

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
            file=self.file_reader.get_file_handler(
                path=self.test_files.pdf_barcode_path)
        )

        # validation
        self.assertIsNotNone(res)

    def test_barcode_by_profile_doc_length(self):
        # request
        res = self.barcode_client.read_barcodes_by_type(
            barcode_type='all',
            file=self.file_reader.get_file_handler(
                path=self.test_files.pdf_barcode_path)
        )

        # validation
        read_barcodes_text = len(res['barcodes'][0]['barcode_data'])

        self.assertTrue(self.check.not_zero(read_barcodes_text))

    def create_add_barcode(self):
        add_barcode = AddBarcode(
            document=Document(
                doc_data=self.test_files.pdf_data
            ),
            add_barcode_action=AddBarcodeAction(
                barcode_type='qrCode',
                value='welcome to pdf4me',
                height=100,
                width=100,
                align_x='center',
                align_y='middle',
                margin_x=0,
                margin_y=0,
                page_sequence='1',
                rotate='30',
                barcode_color=BarcodeColor(
                    red=0,
                    green=0,
                    blue=0,
                    alpha=100,
                ),
                background_color=BarcodeColor(
                    red=1,
                    green=1,
                    blue=1,
                    alpha=100,
                ),
            )
        )

        return add_barcode

    def test_add_barcode_throws_exception(self):
        with assert_raises(Pdf4meClientException) as e:
            self.barcode_client.add_barcode(None)

        assert_equal(e.exception.msg,
                     'The add_barcode parameter cannot be None.')

    def test_add_barcode_document_throws_exception(self):
        # prepare args
        add_barcode = self.create_add_barcode()
        add_barcode.document = None

        with assert_raises(Pdf4meClientException) as e:
            self.barcode_client.add_barcode(add_barcode=add_barcode)

        assert_equal(e.exception.msg,
                     'The add_barcode document cannot be None.')

    def test_add_barcode_document_data_throws_exception(self):
        # prepare args
        add_barcode = self.create_add_barcode()
        add_barcode.document.doc_data = None

        with assert_raises(Pdf4meClientException) as e:
            self.barcode_client.add_barcode(add_barcode=add_barcode)

        assert_equal(e.exception.msg,
                     'The add_barcode document cannot be None.')

    def test_add_barcode_action_throws_exception(self):
        # prepare args
        add_barcode = self.create_add_barcode()
        add_barcode.add_barcode_action = None

        with assert_raises(Pdf4meClientException) as e:
            self.barcode_client.add_barcode(add_barcode=add_barcode)

        assert_equal(e.exception.msg, 'The add_barcode_action cannot be None.')

    def test_add_barcode_no_none_response(self):
        # request
        add_barcode = self.create_add_barcode()
        res = self.barcode_client.add_barcode(add_barcode=add_barcode)

        # validation
        self.assertIsNotNone(res)
        self.assertIsNotNone(res['document'])
        self.assertIsNotNone(res['document']['doc_data'])

    def test_add_barcode_doc_length(self):
        # request
        add_barcode = self.create_add_barcode()
        res = self.barcode_client.add_barcode(add_barcode=add_barcode)

        # validation
        add_barcode_pdf = len(res['document']['doc_data'])

        self.assertTrue(self.check.not_zero(add_barcode_pdf))

    def test_add_barcode_by_type_no_none_respoonse(self):
        # request
        res = self.barcode_client.add_barcode_by_type(
            barcode_type='qrCode',
            text='EXAMPLE TEXT',
            pages='all',
            align_x='center',
            align_y='middle',
            height=100,
            width=100,
            file=self.file_reader.get_file_handler(
                path=self.test_files.pdf_path),
        )

        # validation
        self.assertIsNotNone(res)

    def test_add_barcode_by_type_doc_length(self):
        # request
        res = self.barcode_client.add_barcode_by_type(
            barcode_type='qrCode',
            text='EXAMPLE TEXT',
            pages='all',
            align_x='center',
            align_y='middle',
            height=100,
            width=100,
            file=self.file_reader.get_file_handler(
                path=self.test_files.pdf_path),
        )

        # validation
        barcoded_pdf_length = self.check.get_doc_base64_length(res)

        self.check.not_zero(barcoded_pdf_length)

    def test_create_barcode_by_type_no_none_respoonse(self):
        # request
        res = self.barcode_client.create_barcode_by_type(
            barcode_type='qrCode',
            content='EXAMPLE TEXT',
        )

        # validation
        self.assertIsNotNone(res)

    def test_create_barcode_by_type_doc_length(self):
        # request
        res = self.barcode_client.create_barcode_by_type(
            barcode_type='qrCode',
            content='EXAMPLE TEXT',
        )

        # validation
        barcode_length = self.check.get_doc_base64_length(res)

        self.check.not_zero(barcode_length)

    def create_split_by_barcode_req(self):
        split_by_barcode = SplitByBarcodeReq(
            document=Document(
                doc_data=self.test_files.pdf_barcode_data
            ),
            split_by_barcode_action=SplitByBarcodeAction(
                barcode_string='ara',
                barcode_filter='contains',
                barcode_type='any',
                split_barcode_page='after',
            )
        )

        return split_by_barcode

    def test_split_by_barcode_throws_exception(self):
        with assert_raises(Pdf4meClientException) as e:
            self.barcode_client.split_by_barcode(None)

        assert_equal(e.exception.msg,
                     'The split_by_barcode_req parameter cannot be None.')

    def test_asplit_by_barcode_document_throws_exception(self):
        # prepare args
        split_by_barcode_req = self.create_split_by_barcode_req()
        split_by_barcode_req.document = None

        with assert_raises(Pdf4meClientException) as e:
            self.barcode_client.split_by_barcode(
                split_by_barcode_req=split_by_barcode_req)

        assert_equal(e.exception.msg,
                     'The split_by_barcode_req document cannot be None.')

    def test_split_by_barcode_document_data_throws_exception(self):
        # prepare args
        split_by_barcode_req = self.create_split_by_barcode_req()
        split_by_barcode_req.document.doc_data = None

        with assert_raises(Pdf4meClientException) as e:
            self.barcode_client.split_by_barcode(
                split_by_barcode_req=split_by_barcode_req)

        assert_equal(e.exception.msg,
                     'The split_by_barcode_req document cannot be None.')

    def test_split_by_barcode_action_throws_exception(self):
        # prepare args
        split_by_barcode_req = self.create_split_by_barcode_req()
        split_by_barcode_req.split_by_barcode_action = None

        with assert_raises(Pdf4meClientException) as e:
            self.barcode_client.split_by_barcode(
                split_by_barcode_req=split_by_barcode_req)

        assert_equal(e.exception.msg,
                     'The split_by_barcode_action cannot be None.')

    def test_split_by_barcode_no_none_response(self):
        # request
        split_by_barcode_req = self.create_split_by_barcode_req()
        res = self.barcode_client.split_by_barcode(
            split_by_barcode_req=split_by_barcode_req)

        # validation
        self.assertIsNotNone(res)
        self.assertIsNotNone(res['splitted_documents'])
        self.assertIsNotNone(res['splitted_documents'][0]['doc_data'])
        self.assertIsNotNone(res['splitted_documents'][1]['doc_data'])

    def test_split_by_barcode_doc_length(self):
        # request
        split_by_barcode_req = self.create_split_by_barcode_req()
        res = self.barcode_client.split_by_barcode(
            split_by_barcode_req=split_by_barcode_req)

        # validation
        doc_count = len(res['splitted_documents'])

        self.assertTrue(doc_count == 2)

        split_by_barcode_pdf_1 = len(res['splitted_documents'][0]['doc_data'])
        split_by_barcode_pdf_2 = len(res['splitted_documents'][1]['doc_data'])

        self.assertTrue(self.check.not_zero(split_by_barcode_pdf_1))
        self.assertTrue(self.check.not_zero(split_by_barcode_pdf_2))
