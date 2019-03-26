from pdf4me.helper.pdf4me_exceptions import Pdf4meClientException
from pdf4me.model import ReadBarcodes


class BarcodeClient(object):

    def __init__(self, pdf4me_client):
        self.pdf4me_client = pdf4me_client

    def read_barcodes(self, read_barcodes):
        """The predefined stamp is carried out.

        :param read_barcodes: read barcode configuration
        :type read_barcodes: ReadBarcodes
        :return: ReadBarcodeRes, contains the barcode
        """

        # check read_barcodes validity
        self.__check_read_barcodes_object_validity(read_barcodes)

        res = self.pdf4me_client.custom_http.post_universal_object(universal_object=read_barcodes,
                                                                   controller='Barcode/ReadBarcodes')

        return res

    def read_barcodes_by_type(self, barcode_type, file):
        """Reads barcodes from the file based on the barcode type

        :param barcode_type: barcode type
        :type barcode_type: str: ( 'all','unknown','code11','code39','code93','code128','codabar','inter2of5',
                                'patchcode','ean8','upce','ean13','upca','plus2','plus5','pdf417','datamatrix','qrcode',
                                'postnet','planet','rm4scc','australiapost','intelligentmail','code39extended',
                                'microqrcode','all_2d','pharmacode','ucc128','rss14','rsslimited','rssexpanded','all_1d')
        :param file: to be read barcode form
        :type file: file handler, use the method get_file_handler from FileReader to obtain it
        :return: bytes of resulting file, can be directly written to file on disk
        """

        streams = [('file', file)]
        params = [('barcodeType', barcode_type)]

        return self.pdf4me_client.custom_http.post_wrapper(octet_streams=streams, values=params,
                                                           controller='Barcode/ReadBarcodesByType')

    def __check_read_barcodes_object_validity(self, read_barcodes):
        """checks whether the stamp object contains the essential information to be
        processed by the server."""

        if read_barcodes is None:
            raise Pdf4meClientException('The read_barcodes parameter cannot be None.')
        elif read_barcodes.document is None or read_barcodes.document.doc_data is None:
            raise Pdf4meClientException('The stamp document cannot be None.')
        # elif read_barcodes.barcode_action is None:
        #     raise Pdf4meClientException('The stamp_action cannot be None.')
