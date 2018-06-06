import sys
sys.path.append('../../Pdf4mePythonClientApi')
sys.path.append('../../Pdf4mePythonClientApiTest')

import unittest

from nose.tools import assert_raises, assert_equal

from pdf4me.client.merge_client import MergeClient
from pdf4me.client.pdf4me_client import Pdf4meClient
from pdf4me.helper.file_reader import FileReader
from pdf4me.helper.pdf4me_exceptions import Pdf4meClientException
from pdf4me.model import Merge, Document, MergeAction
from Pdf4mePythonClientApiTest.test_helper.check import Check
from Pdf4mePythonClientApiTest.test_helper.test_files import TestFiles


class MergeClientTest(unittest.TestCase):

    pdf4me_client = Pdf4meClient()
    merge_client = MergeClient(pdf4me_client)

    test_files = TestFiles()
    check = Check()
    file_reader = FileReader()


    def create_merge(self):

        merge = Merge(
            documents=[
                Document(
                    doc_data=self.test_files.pdf_data
                ),
                Document(
                    doc_data=self.test_files.pdf_data_2
                )
            ],
            merge_action=MergeAction()
        )

        return merge

    def test_merge_throws_exception(self):

        with assert_raises(Pdf4meClientException) as e:
            self.merge_client.merge(None)

        assert_equal(e.exception.msg, 'The merge parameter cannot be None.')

    def test_merge_documents_throws_exception(self):

        # prepare args
        merge = self.create_merge()
        merge.documents = None

        with assert_raises(Pdf4meClientException) as e:
            self.merge_client.merge(merge=merge)

        assert_equal(e.exception.msg, 'The merge documents cannot be None.')

    def test_merge_documents_less_than_2_throws_exception(self):

        # prepare args
        merge = self.create_merge()
        merge.documents = [Document(doc_data=self.test_files.pdf_data)]

        with assert_raises(Pdf4meClientException) as e:
            self.merge_client.merge(merge=merge)

        assert_equal(e.exception.msg, 'The merge documents must contain at least two documents.')

    def test_merge_document1_throws_exception(self):

        # prepare args
        merge = self.create_merge()
        merge.documents[0] = None

        with assert_raises(Pdf4meClientException) as e:
            self.merge_client.merge(merge=merge)

        assert_equal(e.exception.msg, 'The merge documents cannot be None nor can the document.docData.')

    def test_merge_document2_throws_exception(self):

        # prepare args
        merge = self.create_merge()
        merge.documents[1] = None

        with assert_raises(Pdf4meClientException) as e:
            self.merge_client.merge(merge=merge)

        assert_equal(e.exception.msg, 'The merge documents cannot be None nor can the document.docData.')

    def test_merge_document1_data_throws_exception(self):

        # prepare args
        merge = self.create_merge()
        merge.documents[0].doc_data = None

        with assert_raises(Pdf4meClientException) as e:
            self.merge_client.merge(merge=merge)

        assert_equal(e.exception.msg, 'The merge documents cannot be None nor can the document.docData.')

    def test_merge_document2_data_throws_exception(self):

        # prepare args
        merge = self.create_merge()
        merge.documents[1].doc_data = None

        with assert_raises(Pdf4meClientException) as e:
            self.merge_client.merge(merge=merge)

        assert_equal(e.exception.msg, 'The merge documents cannot be None nor can the document.docData.')

    def test_merge_action_throws_exception(self):

        # prepare args
        merge = self.create_merge()
        merge.merge_action = None

        with assert_raises(Pdf4meClientException) as e:
            self.merge_client.merge(merge=merge)

        assert_equal(e.exception.msg, 'The merge_action cannot be None.')

    def test_merge_no_none_response(self):

        # request
        merge = self.create_merge()
        res = self.merge_client.merge(merge=merge)

        # validation
        self.assertIsNotNone(res)
        self.assertIsNotNone(res['document'])
        self.assertIsNotNone(res['document']['doc_data'])

    def test_merge_doc_length(self):

        # request
        merge = self.create_merge()
        res = self.merge_client.merge(merge=merge)

        # validation
        mergeLength = len(res['document']['doc_data'])
        originals = self.test_files.pdf_length + self.test_files.pdf_length_2
        shorterDoc = min(self.test_files.pdf_length, self.test_files.pdf_length_2)

        self.assertTrue(self.check.below_not_zero(mergeLength, originals))
        self.assertTrue(self.check.above(mergeLength, shorterDoc))

    def test_merge_2_pdfs_no_none_response(self):

        # request
        res = self.merge_client.merge_2_pdfs(
            file1=self.file_reader.get_file_handler(path=self.test_files.pdf_path),
            file2=self.file_reader.get_file_handler(path=self.test_files.pdf_path_2)
        )

        # validation
        self.assertIsNotNone(res)

    def test_merge_2_pdfs_doc_length(self):
        # request
        res = self.merge_client.merge_2_pdfs(
            file1=self.file_reader.get_file_handler(path=self.test_files.pdf_path),
            file2=self.file_reader.get_file_handler(path=self.test_files.pdf_path_2)
        )

        # validation
        mergeLength = self.check.get_doc_base64_length(res)
        originals = self.test_files.pdf_length + self.test_files.pdf_length_2
        shorterDoc = min(self.test_files.pdf_length, self.test_files.pdf_length_2)

        self.assertTrue(self.check.below_not_zero(mergeLength, originals))
        self.assertTrue(self.check.above(mergeLength, shorterDoc))
