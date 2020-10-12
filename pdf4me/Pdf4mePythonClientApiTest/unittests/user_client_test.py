import sys

sys.path.append('../../Pdf4mePythonClientApi')
sys.path.append('../../Pdf4mePythonClientApiTest')

import unittest

# from nose.tools import assert_raises, assert_equal

from pdf4me.client.user_client import UserClient
from pdf4me.client.pdf4me_client import Pdf4meClient
# from pdf4me.helper.file_reader import FileReader
# from pdf4me.helper.pdf4me_exceptions import Pdf4meClientException
from pdf4me.model import CreateImages, Document, ImageAction, PageSelection
# from test_helper.check import Check
# from test_helper.test_files import TestFiles


class UserClientTest(unittest.TestCase):
    pdf4me_client = Pdf4meClient()
    user_client = UserClient(pdf4me_client)

    def test_get_customer_no_none_response(self):
        # request
        res = self.user_client.get_customer()

        # validation
        self.assertIsNotNone(res)
        # print(res)

    def test_get_email(self):
        # request
        res = self.user_client.get_email()

        # validation
        self.assertIsNotNone(res)
        print(res)




