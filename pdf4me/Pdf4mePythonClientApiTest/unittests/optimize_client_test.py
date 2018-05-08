import sys
sys.path.append('../../Pdf4mePythonClientApi')
sys.path.append('../../Pdf4mePythonClientApiTest')

import unittest

from nose.tools import assert_raises, assert_equal

from pdf4me.client.optimize_client import OptimizeClient
from pdf4me.client.pdf4me_client import Pdf4meClient
from pdf4me.helper.file_reader import FileReader
from pdf4me.helper.pdf4me_exceptions import Pdf4meClientException
from pdf4me.model import Optimize, Document, OptimizeAction
from test_helper.check import Check
from test_helper.test_files import TestFiles


class OptimizeClientTest(unittest.TestCase):

    pdf4me_client = Pdf4meClient()
    optimize_client = OptimizeClient(pdf4me_client)

    test_files = TestFiles()
    check = Check()
    file_reader = FileReader()


    def create_optimize(self):

        optimize = Optimize(
            document=Document(
                doc_data=self.test_files.pdf_data
            ),
            optimize_action=OptimizeAction(
                use_profile=True,
                profile='default'
            )
        )

        return optimize

    def test_optimize_throws_exception(self):

        with assert_raises(Pdf4meClientException) as e:
            self.optimize_client.optimize(None)

        assert_equal(e.exception.msg, 'The optimize parameter cannot be None.')

    def test_optimize_document_throws_exception(self):

        # prepare args
        optimize = self.create_optimize()
        optimize.document = None

        with assert_raises(Pdf4meClientException) as e:
            self.optimize_client.optimize(optimize=optimize)

        assert_equal(e.exception.msg, 'The optimize document cannot be None.')

    def test_optimize_document_data_throws_exception(self):

        # prepare args
        optimize = self.create_optimize()
        optimize.document.doc_data = None

        with assert_raises(Pdf4meClientException) as e:
            self.optimize_client.optimize(optimize=optimize)

        assert_equal(e.exception.msg, 'The optimize document cannot be None.')

    def test_optimize_action_throws_exception(self):

        # prepare args
        optimize = self.create_optimize()
        optimize.optimize_action = None

        with assert_raises(Pdf4meClientException) as e:
            self.optimize_client.optimize(optimize=optimize)

        assert_equal(e.exception.msg, 'The optimize_action cannot be None.')

    def test_optimize_action_use_profile_throws_exception(self):

        # prepare args
        optimize = self.create_optimize()
        optimize.optimize_action.use_profile = False

        with assert_raises(Pdf4meClientException) as e:
            self.optimize_client.optimize(optimize=optimize)

        assert_equal(e.exception.msg, 'The use_profile parameter of optimize_action has to be set to true.')

    def test_optimize_no_none_response(self):

        # request
        optimize = self.create_optimize()
        res = self.optimize_client.optimize(optimize=optimize)

        # validation
        self.assertIsNotNone(res)
        self.assertIsNotNone(res['document'])
        self.assertIsNotNone(res['document']['doc_data'])

    def test_optimize_doc_length(self):

        # request
        optimize = self.create_optimize()
        res = self.optimize_client.optimize(optimize=optimize)

        # validation
        original_length = self.test_files.pdf_length
        optimized_pdf = len(res['document']['doc_data'])

        self.assertTrue(self.check.below_not_zero(optimized_pdf, original_length))

    def test_optimize_by_profile_no_none_response(self):

        # request
        res = self.optimize_client.optimize_by_profile(
            profile='default',
            file=self.file_reader.get_file_handler(path=self.test_files.pdf_path)
        )

        # validation
        self.assertIsNotNone(res)

    def test_optimize_by_profile_doc_length(self):

        # request
        res = self.optimize_client.optimize_by_profile(
            profile='default',
            file=self.file_reader.get_file_handler(path=self.test_files.pdf_path)
        )

        # validation
        original_length = self.test_files.pdf_length
        optimized_pdf = self.check.get_doc_base64_length(res)

        self.assertTrue(self.check.below_not_zero(optimized_pdf, original_length))
