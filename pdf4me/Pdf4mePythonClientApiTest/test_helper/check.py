import base64


class Check(object):

    def below_not_zero(self, length, limit):
        """Checks whether the length is less (or equal) than the limit and not equal to zero."""

        if length <= limit and length != 0:
            return True
        else:
            return False

    def above(self, length, limit):
        """Checks whether the length is longer (or equal) than the limit."""

        if length >= limit:
            return True
        else:
            return False

    def not_zero(self, length):
        """Checks whether the length is greater than zero."""

        if length > 0:
            return True
        else:
            return False

    def get_doc_base64_length(self, doc):
        """Returns the length of the documents content in base64 format."""
        return len(base64.b64encode(doc).decode('utf-8'))
