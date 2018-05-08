from pdf4me.helper.pdf4me_exceptions import Pdf4meBackendException, Pdf4meClientException


class ResponseChecker(object):

    def check_document_for_errors(self, res, is_doc=None):
        """Checks document logs for error reports, in case an error is found a Pdf4meBackendException is thrown."""

        if res is None:
            raise Pdf4meBackendException('Server Error')

        # check for error message
        self.__check_for_error_message(res)

        if is_doc is True:
            doc_logs = res['doc_logs']
        else:
            doc_logs = res['document']['doc_logs']

        for i in range(len(doc_logs)):
            current_log = doc_logs[i]
            if current_log['doc_log_level'] == 3:  # 3: corresponds to the enum 'error'
                raise Pdf4meBackendException(current_log['message'])

    def check_documents_for_errors(self, res):
        """Checks document logs for error reports, in case an error is found a Pdf4meBackendException is thrown."""

        if res is None:
            raise Pdf4meBackendException('Server Error')

        # check for error message
        self.__check_for_error_message(res)

        docs = res['documents']

        for i in range(len(docs)):
            self.check_document_for_errors(docs[i], is_doc=True)

    @staticmethod
    def __check_for_error_message(res):
        """Checks whether the server sent an error message, e.g. because of Api Call Limit Reached."""

        error_message = res.get('error_message')

        if error_message is not None:
            raise Pdf4meClientException(error_message)
