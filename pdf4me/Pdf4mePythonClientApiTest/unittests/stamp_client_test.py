import sys

sys.path.append('../../Pdf4mePythonClientApi')
sys.path.append('../../Pdf4mePythonClientApiTest')

import unittest

from nose.tools import assert_raises, assert_equal

from pdf4me.client.pdf4me_client import Pdf4meClient
from pdf4me.client.stamp_client import StampClient
from pdf4me.helper.file_reader import FileReader
from pdf4me.helper.pdf4me_exceptions import Pdf4meClientException
from pdf4me.model import Document, Stamp, StampAction, Text
from test_helper.check import Check
from test_helper.test_files import TestFiles


class StampClientTest(unittest.TestCase):
    pdf4me_client = Pdf4meClient()
    stamp_client = StampClient(pdf4me_client)

    test_files = TestFiles()
    check = Check()
    file_reader = FileReader()

    def create_stamp(self):
        stamp = Stamp(
            document=Document(
                doc_data=self.test_files.pdf_data
            ),
            stamp_action=StampAction(
                text=Text(
                    value='EXAMPLE TEXT'
                ),
                alpha=1.0,
                page_sequence='all',
                align_x='center',
                align_y='middle'
            )
        )

        return stamp

    def test_stamp_throws_exception(self):
        with assert_raises(Pdf4meClientException) as e:
            self.stamp_client.stamp(None)

        assert_equal(e.exception.msg, 'The stamp parameter cannot be None.')

    def test_stamp_document_throws_exception(self):
        # prepare args
        stamp = self.create_stamp()
        stamp.document = None

        with assert_raises(Pdf4meClientException) as e:
            self.stamp_client.stamp(stamp=stamp)

        assert_equal(e.exception.msg, 'The stamp document cannot be None.')

    def test_stamp_document_data_throws_exception(self):
        # prepare args
        stamp = self.create_stamp()
        stamp.document.doc_data = None

        with assert_raises(Pdf4meClientException) as e:
            self.stamp_client.stamp(stamp=stamp)

        assert_equal(e.exception.msg, 'The stamp document cannot be None.')

    def test_stamp_action_throws_exception(self):
        # prepare args
        stamp = self.create_stamp()
        stamp.stamp_action = None

        with assert_raises(Pdf4meClientException) as e:
            self.stamp_client.stamp(stamp=stamp)

        assert_equal(e.exception.msg, 'The stamp_action cannot be None.')

    def test_stamp_action_alpha_throws_exception(self):
        # prepare args
        stamp = self.create_stamp()
        stamp.stamp_action.alpha = None

        with assert_raises(Pdf4meClientException) as e:
            self.stamp_client.stamp(stamp=stamp)

        assert_equal(e.exception.msg, 'The alpha parameter of stamp_action cannot be None.')

    def test_stamp_action_text_and_image_throws_exception(self):
        # prepare args
        stamp = self.create_stamp()
        stamp.stamp_action.text = None
        stamp.stamp_action.image = None

        with assert_raises(Pdf4meClientException) as e:
            self.stamp_client.stamp(stamp=stamp)

        assert_equal(e.exception.msg, 'The image and text parameter of stampAction cannot both be None.')

    def test_stamp_no_none_response(self):
        # request
        stamp = self.create_stamp()
        res = self.stamp_client.stamp(stamp)

        # validation
        self.assertIsNotNone(res)
        self.assertIsNotNone(res['document'])
        self.assertIsNotNone(res['document']['doc_data'])

    def test_stamp_doc_length(self):
        # request
        stamp = self.create_stamp()
        res = self.stamp_client.stamp(stamp)

        # validation
        stamped_pdf_length = len(res['document']['doc_data'])

        self.check.not_zero(stamped_pdf_length)

    def test_text_stamp_no_none_respoonse(self):
        # request
        res = self.stamp_client.text_stamp(
            text='EXAMPLE TEXT',
            pages='all',
            align_x='center',
            align_y='middle',
            file=self.file_reader.get_file_handler(path=self.test_files.pdf_path)
        )

        # validation
        self.assertIsNotNone(res)

    def test_text_stamp_doc_length(self):
        # request
        res = self.stamp_client.text_stamp(
            text='EXAMPLE TEXT',
            pages='all',
            align_x='center',
            align_y='middle',
            file=self.file_reader.get_file_handler(path=self.test_files.pdf_path)
        )

        # validation
        stamped_pdf_length = self.check.get_doc_base64_length(res)

        self.check.not_zero(stamped_pdf_length)
