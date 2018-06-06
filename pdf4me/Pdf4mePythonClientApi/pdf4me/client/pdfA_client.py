from pdf4me.helper.pdf4me_exceptions import Pdf4meClientException
from pdf4me.helper.response_checker import ResponseChecker
from pdf4me.model import CreatePdfA


class PdfAClient(object):

    def __init__(self, pdf4me_client):
        self.pdf4me_client = pdf4me_client

    def pdfA(self, create_pdfA):
        """The predefined PDF/A creation is carried out.

        :param create_pdfA: PDF/A configuration
        :type create_pdfA: CreatePdfA
        :return: CreatePdfARes, contains generated PDF/A.
        """

        # check create_pdfA validity
        self.__check_pdfA_object_validity(create_pdfA)

        res = self.pdf4me_client.custom_http.post_universal_object(universal_object=create_pdfA,
                                                                   controller='PdfA/PdfA')

        # check response for errors
        ResponseChecker().check_document_for_errors(res)

        return res

    def create_pdfA(self, file, pdf_compliance=None):
        """Converts PDF documents to the PDF/A format for long-term archiving.

        :param pdf_compliance: PDF/A compliance level
        :type pdf_compliance: str
        :param file: to be converted to PDF/A
        :type file: file handler, use the method get_file_handler from FileReader to obtain it
        :return: bytes of resulting file, can be directly written to file on disk
        """

        streams = [('file', file)]

        if (pdf_compliance is None):
            params = []
        else:
            params = [('pdfCompliance', pdf_compliance)]

        return self.pdf4me_client.custom_http.post_wrapper(octet_streams=streams, values=params,
                                                           controller='PdfA/CreatePdfA')

    def __check_pdfA_object_validity(self, create_pdfA):
        """checks whether the create_pdfA object contains the essential information to be
        processed by the server."""

        if create_pdfA is None:
            raise Pdf4meClientException('The create_pdfA parameter cannot be None.')
        elif create_pdfA.document is None or create_pdfA.document.doc_data is None:
            raise Pdf4meClientException('The create_pdfA document cannot be None.')
        elif create_pdfA.pdf_a_action is None:
            raise Pdf4meClientException('The pdf_a_action cannot be None.')
