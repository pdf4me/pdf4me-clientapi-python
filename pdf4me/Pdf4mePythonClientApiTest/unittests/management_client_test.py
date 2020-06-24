import sys

sys.path.append('../../Pdf4mePythonClientApi')
sys.path.append('../../Pdf4mePythonClientApiTest')

import unittest

# from nose.tools import assert_raises, assert_equal

from pdf4me.client.management_client import ManagementClient
from pdf4me.client.pdf4me_client import Pdf4meClient
# from pdf4me.helper.file_reader import FileReader
# from pdf4me.helper.pdf4me_exceptions import Pdf4meClientException
from pdf4me.model import CreateImages, Document, ImageAction, PageSelection
# from test_helper.check import Check
# from test_helper.test_files import TestFiles


class ManagementClientTest(unittest.TestCase):
    pdf4me_client = Pdf4meClient()
    management_client = ManagementClient(pdf4me_client)

    def test_get_api_call_detail_no_none_response(self):
        # request
        res = self.management_client.get_api_call_detail('4e7dc9be-88aa-4b56-a218-a39b16f9783d')

        # validation
        self.assertIsNotNone(res)
        # print(res)



