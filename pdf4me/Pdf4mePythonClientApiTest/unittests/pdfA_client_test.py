import sys

sys.path.append('../../Pdf4mePythonClientApi')
sys.path.append('../../Pdf4mePythonClientApiTest')

import unittest

from nose.tools import assert_raises, assert_equal

from pdf4me.client.pdf4me_client import Pdf4meClient
from pdf4me.client.pdfA_client import PdfAClient
from pdf4me.helper.file_reader import FileReader
from pdf4me.helper.pdf4me_exceptions import Pdf4meClientException
from pdf4me.model import CreatePdfA, Document, PdfAAction, Rotate, RotateAction, PdfRotate, Protect, ProtectAction, \
    Validate, ValidateAction, Repair, RepairAction
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

    # Rotate
    def create_rotate(self):
        rotate = Rotate(
            document=Document(
                doc_data=self.test_files.pdf_data
            ),
            rotate_action=RotateAction(
                rotation_list=[
                    PdfRotate(
                        page_nr=2,
                        rotation_type='clockwise'
                    )
                ]
            )
        )

        return rotate

    def test_rotate_throws_exception(self):
        create_rotate: Rotate = None
        with assert_raises(Pdf4meClientException) as e:
            self.pdfA_client.rotate(rotate=create_rotate)

        assert_equal(e.exception.msg, 'The rotate parameter cannot be None.')

    def test_rotate_document_throws_exception(self):
        # prepare args
        create_rotate = self.create_rotate()
        create_rotate.document = None

        with assert_raises(Pdf4meClientException) as e:
            self.pdfA_client.rotate(rotate=create_rotate)

        assert_equal(e.exception.msg, 'The rotate document cannot be None.')

    def test_rotate_document_data_throws_exception(self):
        # prepare args
        create_rotate = self.create_rotate()
        create_rotate.document.doc_data = None

        with assert_raises(Pdf4meClientException) as e:
            self.pdfA_client.rotate(rotate=create_rotate)

        assert_equal(e.exception.msg, 'The rotate document cannot be None.')

    def test_rotate_action_data_throws_exception(self):
        # prepare args
        create_rotate = self.create_rotate()
        create_rotate.rotate_action = None

        with assert_raises(Pdf4meClientException) as e:
            self.pdfA_client.rotate(rotate=create_rotate)

        assert_equal(e.exception.msg, 'The rotate_action cannot be None.')

    def test_rotate_no_none_response(self):
        # request
        create_rotate = self.create_rotate()
        res = self.pdfA_client.rotate(create_rotate)

        # validation
        self.assertIsNotNone(res)
        self.assertIsNotNone(res['document'])
        self.assertIsNotNone(res['document']['doc_data'])

    def test_rotate_doc_length(self):
        # request
        create_rotate = self.create_rotate()
        res = self.pdfA_client.rotate(create_rotate)

        # validation
        original_length = self.test_files.pdf_length
        rotate = len(res['document']['doc_data'])

        self.assertTrue(self.check.below_not_zero(rotate, original_length))

    def test_rotate_page_no_none_response(self):
        # request
        res = self.pdfA_client.rotate_page(
            page_nr='2',
            rotate='clockwise',
            file=self.file_reader.get_file_handler(path=self.test_files.pdf_path)
        )

        # validation
        self.assertIsNotNone(res)

    def test_rotate_page_doc_length(self):
        # request
        res = self.pdfA_client.rotate_page(
            page_nr='2',
            rotate='clockwise',
            file=self.file_reader.get_file_handler(path=self.test_files.pdf_path)
        )

        # validation
        original_length = self.test_files.pdf_length
        rotate = self.check.get_doc_base64_length(res)

        self.assertTrue(self.check.below_not_zero(rotate, original_length))

    # def test_rotate_page_without_compliance_no_none_response(self):
    #     # request
    #     res = self.pdfA_client.rotate_page(
    #         file=self.file_reader.get_file_handler(path=self.test_files.pdf_path)
    #     )
    #
    #     # validation
    #     self.assertIsNotNone(res)
    #
    # def test_rotate_page_without_compliance_doc_length(self):
    #     # request
    #     res = self.pdfA_client.rotate_page(
    #         file=self.file_reader.get_file_handler(path=self.test_files.pdf_path)
    #     )
    #
    #     # validation
    #     original_length = self.test_files.pdf_length
    #     pdfA = self.check.get_doc_base64_length(res)
    #
    #     self.assertTrue(self.check.below_not_zero(pdfA, original_length))

    def test_rotate_document_no_none_response(self):
        # request
        res = self.pdfA_client.rotate_document(
            rotate='clockwise',
            file=self.file_reader.get_file_handler(path=self.test_files.pdf_path)
        )

        # validation
        self.assertIsNotNone(res)

    def test_rotate_document_doc_length(self):
        # request
        res = self.pdfA_client.rotate_document(
            rotate='clockwise',
            file=self.file_reader.get_file_handler(path=self.test_files.pdf_path)
        )

        # validation
        original_length = self.test_files.pdf_length
        rotate = self.check.get_doc_base64_length(res)

        self.assertTrue(self.check.below_not_zero(rotate, original_length))

    # Protect
    def create_protect(self):
        protect = Protect(
            document=Document(
                doc_data=self.test_files.pdf_data
            ),
            protect_action=ProtectAction(
                user_password='pdf4me',
                owner_password='pdf4me',
                # unlock=None,
                # permissions=None
            )
        )

        return protect

    def test_protect_throws_exception(self):
        create_protect: Protect = None
        with assert_raises(Pdf4meClientException) as e:
            self.pdfA_client.protect(protect=create_protect)

        assert_equal(e.exception.msg, 'The protect parameter cannot be None.')

    def test_protect_document_throws_exception(self):
        # prepare args
        create_protect = self.create_protect()
        create_protect.document = None

        with assert_raises(Pdf4meClientException) as e:
            self.pdfA_client.protect(protect=create_protect)

        assert_equal(e.exception.msg, 'The protect document cannot be None.')

    def test_protect_document_data_throws_exception(self):
        # prepare args
        create_protect = self.create_protect()
        create_protect.document.doc_data = None

        with assert_raises(Pdf4meClientException) as e:
            self.pdfA_client.protect(protect=create_protect)

        assert_equal(e.exception.msg, 'The protect document cannot be None.')

    def test_protect_action_data_throws_exception(self):
        # prepare args
        create_protect = self.create_protect()
        create_protect.protect_action = None

        with assert_raises(Pdf4meClientException) as e:
            self.pdfA_client.protect(protect=create_protect)

        assert_equal(e.exception.msg, 'The protect_action cannot be None.')

    def test_protect_no_none_response(self):
        # request
        create_protect = self.create_protect()
        res = self.pdfA_client.protect(create_protect)

        # validation
        self.assertIsNotNone(res)
        self.assertIsNotNone(res['document'])
        self.assertIsNotNone(res['document']['doc_data'])

    def test_protect_doc_length(self):
        # request
        create_protect = self.create_protect()
        res = self.pdfA_client.protect(create_protect)

        # validation
        original_length = self.test_files.pdf_length
        protect = len(res['document']['doc_data'])

        self.assertTrue(self.check.below_not_zero(protect, original_length))

    def test_protect_document_no_none_response(self):
        # request
        res = self.pdfA_client.protect_document(
            password='pdf4me',
            permissions='all',
            file=self.file_reader.get_file_handler(path=self.test_files.pdf_path)
        )

        # validation
        self.assertIsNotNone(res)

    def test_protect_document_doc_length(self):
        # request
        res = self.pdfA_client.protect_document(
            password='pdf4me',
            permissions='all',
            file=self.file_reader.get_file_handler(path=self.test_files.pdf_path)
        )

        # validation
        original_length = self.test_files.pdf_length
        protect = self.check.get_doc_base64_length(res)

        self.assertTrue(self.check.below_not_zero(protect, original_length))

    def test_unlock_document_no_none_response(self):
        # request
        res = self.pdfA_client.unlock_document(
            password='pdf4me',
            file=self.file_reader.get_file_handler(path=self.test_files.pdf_path)
        )

        # validation
        self.assertIsNotNone(res)

    def test_unlock_document_doc_length(self):
        # request
        res = self.pdfA_client.unlock_document(
            password='pdf4me',
            file=self.file_reader.get_file_handler(path=self.test_files.pdf_path)
        )

        # validation
        original_length = self.test_files.pdf_length
        unlock = self.check.get_doc_base64_length(res)

        self.assertTrue(self.check.below_not_zero(unlock, original_length))

    # Validate
    def create_validate(self):
        validate = Validate(
            document=Document(
                doc_data=self.test_files.pdf_data
            ),
            validate_action=ValidateAction(
                pdf_conformance='pdfA2u'
            )
        )

        return validate

    def test_validate_throws_exception(self):
        create_validate: Validate = None
        with assert_raises(Pdf4meClientException) as e:
            self.pdfA_client.validate(validate=create_validate)

        assert_equal(e.exception.msg, 'The validate parameter cannot be None.')

    def test_validate_document_throws_exception(self):
        # prepare args
        create_validate = self.create_validate()
        create_validate.document = None

        with assert_raises(Pdf4meClientException) as e:
            self.pdfA_client.validate(validate=create_validate)

        assert_equal(e.exception.msg, 'The validate document cannot be None.')

    def test_validate_document_data_throws_exception(self):
        # prepare args
        create_validate = self.create_validate()
        create_validate.document.doc_data = None

        with assert_raises(Pdf4meClientException) as e:
            self.pdfA_client.validate(validate=create_validate)

        assert_equal(e.exception.msg, 'The validate document cannot be None.')

    def test_validate_action_data_throws_exception(self):
        # prepare args
        create_validate = self.create_validate()
        create_validate.validate_action = None

        with assert_raises(Pdf4meClientException) as e:
            self.pdfA_client.validate(validate=create_validate)

        assert_equal(e.exception.msg, 'The validate_action cannot be None.')

    def test_validate_no_none_response(self):
        # request
        create_validate = self.create_validate()
        res = self.pdfA_client.validate(create_validate)

        # validation
        self.assertIsNotNone(res)

    def test_validate_pdfValidation_length(self):
        # request
        create_validate = self.create_validate()
        res = self.pdfA_client.validate(create_validate)

        # validation
        self.assertIsNotNone(res)
        self.assertIsNotNone(res['pdfValidation'])
        validate = len(res['pdfValidation']['validations'])
        self.assertTrue(self.check.not_zero(validate))

    def test_validate_document_no_none_response(self):
        # request
        res = self.pdfA_client.validate_document(
            pdf_compliance='pdfA2u',
            file=self.file_reader.get_file_handler(path=self.test_files.pdf_path)
        )

        # validation
        self.assertIsNotNone(res)

    def test_validate_document_pdfValidation_length(self):
        # request
        res = self.pdfA_client.validate_document(
            pdf_compliance='pdfA2u',
            file=self.file_reader.get_file_handler(path=self.test_files.pdf_path)
        )

        # validation
        self.assertIsNotNone(res)
        self.assertIsNotNone(res['pdfValidation'])
        validate = len(res['pdfValidation']['validations'])
        self.assertTrue(self.check.not_zero(validate))

    # Repair
    def create_repair(self):
        repair = Repair(
            document=Document(
                doc_data=self.test_files.pdf_data
            ),
            repair_action=RepairAction(

            )
        )

        return repair

    def test_repair_throws_exception(self):
        create_repair: Repair = None
        with assert_raises(Pdf4meClientException) as e:
            self.pdfA_client.repair(repair=create_repair)

        assert_equal(e.exception.msg, 'The repair parameter cannot be None.')

    def test_repair_document_throws_exception(self):
        # prepare args
        create_repair = self.create_repair()
        create_repair.document = None

        with assert_raises(Pdf4meClientException) as e:
            self.pdfA_client.repair(repair=create_repair)

        assert_equal(e.exception.msg, 'The repair document cannot be None.')

    def test_repair_document_data_throws_exception(self):
        # prepare args
        create_repair = self.create_repair()
        create_repair.document.doc_data = None

        with assert_raises(Pdf4meClientException) as e:
            self.pdfA_client.repair(repair=create_repair)

        assert_equal(e.exception.msg, 'The repair document cannot be None.')

    def test_repair_no_none_response(self):
        # request
        create_repair = self.create_repair()
        res = self.pdfA_client.repair(create_repair)

        # validation
        self.assertIsNotNone(res)
        self.assertIsNotNone(res['document'])
        self.assertIsNotNone(res['document']['doc_data'])

    def test_repair_doc_length(self):
        # request
        create_repair = self.create_repair()
        res = self.pdfA_client.repair(create_repair)

        # validation
        original_length = self.test_files.pdf_length
        repair = len(res['document']['doc_data'])

        self.assertTrue(self.check.below_not_zero(repair, original_length))

    def test_repair_document_no_none_response(self):
        # request
        res = self.pdfA_client.repair_document(
            file=self.file_reader.get_file_handler(path=self.test_files.pdf_path)
        )

        # validation
        self.assertIsNotNone(res)

    def test_repair_document_doc_length(self):
        # request
        res = self.pdfA_client.repair_document(
            file=self.file_reader.get_file_handler(path=self.test_files.pdf_path)
        )

        # validation
        original_length = self.test_files.pdf_length
        repair = self.check.get_doc_base64_length(res)

        self.assertTrue(self.check.below_not_zero(repair, original_length))
