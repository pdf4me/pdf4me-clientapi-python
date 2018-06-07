import sys

sys.path.append('../../Pdf4mePythonClientApi')
sys.path.append('../../Pdf4mePythonClientApiTest')

import unittest

from nose.tools import assert_raises, assert_equal

from pdf4me.client.image_client import ImageClient
from pdf4me.client.pdf4me_client import Pdf4meClient
from pdf4me.helper.file_reader import FileReader
from pdf4me.helper.pdf4me_exceptions import Pdf4meClientException
from pdf4me.model import CreateImages, Document, ImageAction, PageSelection
from test_helper.check import Check
from test_helper.test_files import TestFiles


class ImageClientTest(unittest.TestCase):
    pdf4me_client = Pdf4meClient()
    image_client = ImageClient(pdf4me_client)

    test_files = TestFiles()
    check = Check()
    file_reader = FileReader()

    def create_create_images(self):
        create_images = CreateImages(
            document=Document(
                doc_data=self.test_files.pdf_data
            ),
            image_action=ImageAction(
                width_pixel=4000,
                page_selection=PageSelection(
                    page_nrs=[1]
                ),
                image_extension='jpg'
            )
        )

        return create_images

    def test_create_images_throws_exception(self):
        with assert_raises(Pdf4meClientException) as e:
            self.image_client.create_images(None)

        assert_equal(e.exception.msg, 'The create_images parameter cannot be None.')

    def test_create_images_document_throws_exception(self):
        # prepare args
        create_images = self.create_create_images()
        create_images.document = None

        with assert_raises(Pdf4meClientException) as e:
            self.image_client.create_images(create_images=create_images)

        assert_equal(e.exception.msg, 'The create_images document cannot be None.')

    def test_create_images_document_data_throws_exception(self):
        # prepare args
        create_images = self.create_create_images()
        create_images.document.doc_data = None

        with assert_raises(Pdf4meClientException) as e:
            self.image_client.create_images(create_images=create_images)

        assert_equal(e.exception.msg, 'The create_images document cannot be None.')

    def test_create_images_action_throws_exception(self):
        # prepare args
        create_images = self.create_create_images()
        create_images.image_action = None

        with assert_raises(Pdf4meClientException) as e:
            self.image_client.create_images(create_images=create_images)

        assert_equal(e.exception.msg, 'The image_action cannot be None.')

    def test_create_images_action_page_selection_throws_exception(self):
        # prepare args
        create_images = self.create_create_images()
        create_images.image_action.page_selection = None

        with assert_raises(Pdf4meClientException) as e:
            self.image_client.create_images(create_images=create_images)

        assert_equal(e.exception.msg, 'The page_selection of the image_action cannot be None.')

    def test_create_images_no_none_response(self):
        # request
        create_images = self.create_create_images()
        res = self.image_client.create_images(create_images=create_images)

        # validation
        self.assertIsNotNone(res)
        self.assertIsNotNone(res['document'])
        self.assertIsNotNone(res['document']['pages'])
        self.assertIsNotNone(res['document']['pages'][0]['thumbnail'])

    def test_create_images_doc_length(self):
        # request
        create_images = self.create_create_images()
        res = self.image_client.create_images(create_images=create_images)

        # validation
        thumbnail_length = len(res['document']['pages'][0]['thumbnail'])
        self.assertIsNotNone(self.check.not_zero(thumbnail_length))

    def test_create_thumbnail_no_none_response(self):
        # request
        res = self.image_client.create_thumbnail(
            width=4000,
            page_nr='1',
            image_format='jpg',
            file=self.file_reader.get_file_handler(path=self.test_files.pdf_path)
        )

        # validation
        self.assertIsNotNone(res)

    def test_create_thumbnail_doc_length(self):
        # request
        res = self.image_client.create_thumbnail(
            width=4000,
            page_nr='1',
            image_format='jpg',
            file=self.file_reader.get_file_handler(path=self.test_files.pdf_path)
        )

        # validation
        self.assertTrue(self.check.not_zero(len(res)))
