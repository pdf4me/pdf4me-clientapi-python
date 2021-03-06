# coding: utf-8

"""
    Pdf4me

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ReadBarcodeAction(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'barcode_types': 'list[str]',
        'barcode_orientation': 'list[str]',
        'barcodes_to_read': 'int',
        'scan_interval': 'int',
        'quiet_zone_size': 'str',
        'pdf_reading_type': 'str',
        'pdf_render_dpi': 'int',
        'threshold_mode': 'str',
        'threshold_count': 'int',
        'threshold_step': 'int',
        'scan_page': 'int',
        'i2of5_checksum': 'bool',
        'code11_checksum': 'bool',
        'code39_checksum': 'bool',
        'code93_checksum': 'bool',
        'image_despeckle': 'int',
        'image_erode': 'int',
        'image_dilate': 'int',
        'image_sharp': 'int',
        'image_invert': 'int',
        'action_id': 'str'
    }

    attribute_map = {
        'barcode_types': 'barcodeTypes',
        'barcode_orientation': 'barcodeOrientation',
        'barcodes_to_read': 'barcodesToRead',
        'scan_interval': 'scanInterval',
        'quiet_zone_size': 'quietZoneSize',
        'pdf_reading_type': 'pdfReadingType',
        'pdf_render_dpi': 'pdfRenderDPI',
        'threshold_mode': 'thresholdMode',
        'threshold_count': 'thresholdCount',
        'threshold_step': 'thresholdStep',
        'scan_page': 'scanPage',
        'i2of5_checksum': 'i2of5Checksum',
        'code11_checksum': 'code11Checksum',
        'code39_checksum': 'code39Checksum',
        'code93_checksum': 'code93Checksum',
        'image_despeckle': 'imageDespeckle',
        'image_erode': 'imageErode',
        'image_dilate': 'imageDilate',
        'image_sharp': 'imageSharp',
        'image_invert': 'imageInvert',
        'action_id': 'actionId'
    }

    def __init__(self, barcode_types=None, barcode_orientation=None, barcodes_to_read=None, scan_interval=None, quiet_zone_size=None, pdf_reading_type=None, pdf_render_dpi=None, threshold_mode=None, threshold_count=None, threshold_step=None, scan_page=None, i2of5_checksum=None, code11_checksum=None, code39_checksum=None, code93_checksum=None, image_despeckle=None, image_erode=None, image_dilate=None, image_sharp=None, image_invert=None, action_id=None):  # noqa: E501
        """ReadBarcodeAction - a model defined in Swagger"""  # noqa: E501

        self._barcode_types = None
        self._barcode_orientation = None
        self._barcodes_to_read = None
        self._scan_interval = None
        self._quiet_zone_size = None
        self._pdf_reading_type = None
        self._pdf_render_dpi = None
        self._threshold_mode = None
        self._threshold_count = None
        self._threshold_step = None
        self._scan_page = None
        self._i2of5_checksum = None
        self._code11_checksum = None
        self._code39_checksum = None
        self._code93_checksum = None
        self._image_despeckle = None
        self._image_erode = None
        self._image_dilate = None
        self._image_sharp = None
        self._image_invert = None
        self._action_id = None
        self.discriminator = None

        if barcode_types is not None:
            self.barcode_types = barcode_types
        if barcode_orientation is not None:
            self.barcode_orientation = barcode_orientation
        if barcodes_to_read is not None:
            self.barcodes_to_read = barcodes_to_read
        if scan_interval is not None:
            self.scan_interval = scan_interval
        if quiet_zone_size is not None:
            self.quiet_zone_size = quiet_zone_size
        if pdf_reading_type is not None:
            self.pdf_reading_type = pdf_reading_type
        if pdf_render_dpi is not None:
            self.pdf_render_dpi = pdf_render_dpi
        if threshold_mode is not None:
            self.threshold_mode = threshold_mode
        if threshold_count is not None:
            self.threshold_count = threshold_count
        if threshold_step is not None:
            self.threshold_step = threshold_step
        if scan_page is not None:
            self.scan_page = scan_page
        if i2of5_checksum is not None:
            self.i2of5_checksum = i2of5_checksum
        if code11_checksum is not None:
            self.code11_checksum = code11_checksum
        if code39_checksum is not None:
            self.code39_checksum = code39_checksum
        if code93_checksum is not None:
            self.code93_checksum = code93_checksum
        if image_despeckle is not None:
            self.image_despeckle = image_despeckle
        if image_erode is not None:
            self.image_erode = image_erode
        if image_dilate is not None:
            self.image_dilate = image_dilate
        if image_sharp is not None:
            self.image_sharp = image_sharp
        if image_invert is not None:
            self.image_invert = image_invert
        if action_id is not None:
            self.action_id = action_id

    @property
    def barcode_types(self):
        """Gets the barcode_types of this ReadBarcodeAction.  # noqa: E501


        :return: The barcode_types of this ReadBarcodeAction.  # noqa: E501
        :rtype: list[str]
        """
        return self._barcode_types

    @barcode_types.setter
    def barcode_types(self, barcode_types):
        """Sets the barcode_types of this ReadBarcodeAction.


        :param barcode_types: The barcode_types of this ReadBarcodeAction.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["all", "unknown", "code11", "code39", "code93", "code128", "codabar", "inter2of5", "patchCode", "ean8", "upce", "ean13", "upca", "plus2", "plus5", "pdf417", "dataMatrix", "qrCode", "postnet", "planet", "rm4SCC", "australiaPost", "intelligentMail", "code39Extended", "microQRCode", "all_2D", "pharmaCode", "ucc128", "rss14", "rssLimited", "rssExpanded", "all_1D"]  # noqa: E501
        if not set(barcode_types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `barcode_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(barcode_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._barcode_types = barcode_types

    @property
    def barcode_orientation(self):
        """Gets the barcode_orientation of this ReadBarcodeAction.  # noqa: E501


        :return: The barcode_orientation of this ReadBarcodeAction.  # noqa: E501
        :rtype: list[str]
        """
        return self._barcode_orientation

    @barcode_orientation.setter
    def barcode_orientation(self, barcode_orientation):
        """Sets the barcode_orientation of this ReadBarcodeAction.


        :param barcode_orientation: The barcode_orientation of this ReadBarcodeAction.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["unknown", "leftToRight", "rightToLeft", "topToBottom", "bottomToTop", "all"]  # noqa: E501
        if not set(barcode_orientation).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `barcode_orientation` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(barcode_orientation) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._barcode_orientation = barcode_orientation

    @property
    def barcodes_to_read(self):
        """Gets the barcodes_to_read of this ReadBarcodeAction.  # noqa: E501


        :return: The barcodes_to_read of this ReadBarcodeAction.  # noqa: E501
        :rtype: int
        """
        return self._barcodes_to_read

    @barcodes_to_read.setter
    def barcodes_to_read(self, barcodes_to_read):
        """Sets the barcodes_to_read of this ReadBarcodeAction.


        :param barcodes_to_read: The barcodes_to_read of this ReadBarcodeAction.  # noqa: E501
        :type: int
        """

        self._barcodes_to_read = barcodes_to_read

    @property
    def scan_interval(self):
        """Gets the scan_interval of this ReadBarcodeAction.  # noqa: E501


        :return: The scan_interval of this ReadBarcodeAction.  # noqa: E501
        :rtype: int
        """
        return self._scan_interval

    @scan_interval.setter
    def scan_interval(self, scan_interval):
        """Sets the scan_interval of this ReadBarcodeAction.


        :param scan_interval: The scan_interval of this ReadBarcodeAction.  # noqa: E501
        :type: int
        """

        self._scan_interval = scan_interval

    @property
    def quiet_zone_size(self):
        """Gets the quiet_zone_size of this ReadBarcodeAction.  # noqa: E501


        :return: The quiet_zone_size of this ReadBarcodeAction.  # noqa: E501
        :rtype: str
        """
        return self._quiet_zone_size

    @quiet_zone_size.setter
    def quiet_zone_size(self, quiet_zone_size):
        """Sets the quiet_zone_size of this ReadBarcodeAction.


        :param quiet_zone_size: The quiet_zone_size of this ReadBarcodeAction.  # noqa: E501
        :type: str
        """
        allowed_values = ["extraSmall", "small", "normal", "large"]  # noqa: E501
        if quiet_zone_size not in allowed_values:
            raise ValueError(
                "Invalid value for `quiet_zone_size` ({0}), must be one of {1}"  # noqa: E501
                .format(quiet_zone_size, allowed_values)
            )

        self._quiet_zone_size = quiet_zone_size

    @property
    def pdf_reading_type(self):
        """Gets the pdf_reading_type of this ReadBarcodeAction.  # noqa: E501


        :return: The pdf_reading_type of this ReadBarcodeAction.  # noqa: E501
        :rtype: str
        """
        return self._pdf_reading_type

    @pdf_reading_type.setter
    def pdf_reading_type(self, pdf_reading_type):
        """Sets the pdf_reading_type of this ReadBarcodeAction.


        :param pdf_reading_type: The pdf_reading_type of this ReadBarcodeAction.  # noqa: E501
        :type: str
        """
        allowed_values = ["render", "images"]  # noqa: E501
        if pdf_reading_type not in allowed_values:
            raise ValueError(
                "Invalid value for `pdf_reading_type` ({0}), must be one of {1}"  # noqa: E501
                .format(pdf_reading_type, allowed_values)
            )

        self._pdf_reading_type = pdf_reading_type

    @property
    def pdf_render_dpi(self):
        """Gets the pdf_render_dpi of this ReadBarcodeAction.  # noqa: E501


        :return: The pdf_render_dpi of this ReadBarcodeAction.  # noqa: E501
        :rtype: int
        """
        return self._pdf_render_dpi

    @pdf_render_dpi.setter
    def pdf_render_dpi(self, pdf_render_dpi):
        """Sets the pdf_render_dpi of this ReadBarcodeAction.


        :param pdf_render_dpi: The pdf_render_dpi of this ReadBarcodeAction.  # noqa: E501
        :type: int
        """

        self._pdf_render_dpi = pdf_render_dpi

    @property
    def threshold_mode(self):
        """Gets the threshold_mode of this ReadBarcodeAction.  # noqa: E501


        :return: The threshold_mode of this ReadBarcodeAction.  # noqa: E501
        :rtype: str
        """
        return self._threshold_mode

    @threshold_mode.setter
    def threshold_mode(self, threshold_mode):
        """Sets the threshold_mode of this ReadBarcodeAction.


        :param threshold_mode: The threshold_mode of this ReadBarcodeAction.  # noqa: E501
        :type: str
        """
        allowed_values = ["automatic", "fixed", "multiple", "adaptive"]  # noqa: E501
        if threshold_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `threshold_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(threshold_mode, allowed_values)
            )

        self._threshold_mode = threshold_mode

    @property
    def threshold_count(self):
        """Gets the threshold_count of this ReadBarcodeAction.  # noqa: E501


        :return: The threshold_count of this ReadBarcodeAction.  # noqa: E501
        :rtype: int
        """
        return self._threshold_count

    @threshold_count.setter
    def threshold_count(self, threshold_count):
        """Sets the threshold_count of this ReadBarcodeAction.


        :param threshold_count: The threshold_count of this ReadBarcodeAction.  # noqa: E501
        :type: int
        """

        self._threshold_count = threshold_count

    @property
    def threshold_step(self):
        """Gets the threshold_step of this ReadBarcodeAction.  # noqa: E501


        :return: The threshold_step of this ReadBarcodeAction.  # noqa: E501
        :rtype: int
        """
        return self._threshold_step

    @threshold_step.setter
    def threshold_step(self, threshold_step):
        """Sets the threshold_step of this ReadBarcodeAction.


        :param threshold_step: The threshold_step of this ReadBarcodeAction.  # noqa: E501
        :type: int
        """

        self._threshold_step = threshold_step

    @property
    def scan_page(self):
        """Gets the scan_page of this ReadBarcodeAction.  # noqa: E501


        :return: The scan_page of this ReadBarcodeAction.  # noqa: E501
        :rtype: int
        """
        return self._scan_page

    @scan_page.setter
    def scan_page(self, scan_page):
        """Sets the scan_page of this ReadBarcodeAction.


        :param scan_page: The scan_page of this ReadBarcodeAction.  # noqa: E501
        :type: int
        """

        self._scan_page = scan_page

    @property
    def i2of5_checksum(self):
        """Gets the i2of5_checksum of this ReadBarcodeAction.  # noqa: E501


        :return: The i2of5_checksum of this ReadBarcodeAction.  # noqa: E501
        :rtype: bool
        """
        return self._i2of5_checksum

    @i2of5_checksum.setter
    def i2of5_checksum(self, i2of5_checksum):
        """Sets the i2of5_checksum of this ReadBarcodeAction.


        :param i2of5_checksum: The i2of5_checksum of this ReadBarcodeAction.  # noqa: E501
        :type: bool
        """

        self._i2of5_checksum = i2of5_checksum

    @property
    def code11_checksum(self):
        """Gets the code11_checksum of this ReadBarcodeAction.  # noqa: E501


        :return: The code11_checksum of this ReadBarcodeAction.  # noqa: E501
        :rtype: bool
        """
        return self._code11_checksum

    @code11_checksum.setter
    def code11_checksum(self, code11_checksum):
        """Sets the code11_checksum of this ReadBarcodeAction.


        :param code11_checksum: The code11_checksum of this ReadBarcodeAction.  # noqa: E501
        :type: bool
        """

        self._code11_checksum = code11_checksum

    @property
    def code39_checksum(self):
        """Gets the code39_checksum of this ReadBarcodeAction.  # noqa: E501


        :return: The code39_checksum of this ReadBarcodeAction.  # noqa: E501
        :rtype: bool
        """
        return self._code39_checksum

    @code39_checksum.setter
    def code39_checksum(self, code39_checksum):
        """Sets the code39_checksum of this ReadBarcodeAction.


        :param code39_checksum: The code39_checksum of this ReadBarcodeAction.  # noqa: E501
        :type: bool
        """

        self._code39_checksum = code39_checksum

    @property
    def code93_checksum(self):
        """Gets the code93_checksum of this ReadBarcodeAction.  # noqa: E501


        :return: The code93_checksum of this ReadBarcodeAction.  # noqa: E501
        :rtype: bool
        """
        return self._code93_checksum

    @code93_checksum.setter
    def code93_checksum(self, code93_checksum):
        """Sets the code93_checksum of this ReadBarcodeAction.


        :param code93_checksum: The code93_checksum of this ReadBarcodeAction.  # noqa: E501
        :type: bool
        """

        self._code93_checksum = code93_checksum

    @property
    def image_despeckle(self):
        """Gets the image_despeckle of this ReadBarcodeAction.  # noqa: E501


        :return: The image_despeckle of this ReadBarcodeAction.  # noqa: E501
        :rtype: int
        """
        return self._image_despeckle

    @image_despeckle.setter
    def image_despeckle(self, image_despeckle):
        """Sets the image_despeckle of this ReadBarcodeAction.


        :param image_despeckle: The image_despeckle of this ReadBarcodeAction.  # noqa: E501
        :type: int
        """

        self._image_despeckle = image_despeckle

    @property
    def image_erode(self):
        """Gets the image_erode of this ReadBarcodeAction.  # noqa: E501


        :return: The image_erode of this ReadBarcodeAction.  # noqa: E501
        :rtype: int
        """
        return self._image_erode

    @image_erode.setter
    def image_erode(self, image_erode):
        """Sets the image_erode of this ReadBarcodeAction.


        :param image_erode: The image_erode of this ReadBarcodeAction.  # noqa: E501
        :type: int
        """

        self._image_erode = image_erode

    @property
    def image_dilate(self):
        """Gets the image_dilate of this ReadBarcodeAction.  # noqa: E501


        :return: The image_dilate of this ReadBarcodeAction.  # noqa: E501
        :rtype: int
        """
        return self._image_dilate

    @image_dilate.setter
    def image_dilate(self, image_dilate):
        """Sets the image_dilate of this ReadBarcodeAction.


        :param image_dilate: The image_dilate of this ReadBarcodeAction.  # noqa: E501
        :type: int
        """

        self._image_dilate = image_dilate

    @property
    def image_sharp(self):
        """Gets the image_sharp of this ReadBarcodeAction.  # noqa: E501


        :return: The image_sharp of this ReadBarcodeAction.  # noqa: E501
        :rtype: int
        """
        return self._image_sharp

    @image_sharp.setter
    def image_sharp(self, image_sharp):
        """Sets the image_sharp of this ReadBarcodeAction.


        :param image_sharp: The image_sharp of this ReadBarcodeAction.  # noqa: E501
        :type: int
        """

        self._image_sharp = image_sharp

    @property
    def image_invert(self):
        """Gets the image_invert of this ReadBarcodeAction.  # noqa: E501


        :return: The image_invert of this ReadBarcodeAction.  # noqa: E501
        :rtype: int
        """
        return self._image_invert

    @image_invert.setter
    def image_invert(self, image_invert):
        """Sets the image_invert of this ReadBarcodeAction.


        :param image_invert: The image_invert of this ReadBarcodeAction.  # noqa: E501
        :type: int
        """

        self._image_invert = image_invert

    @property
    def action_id(self):
        """Gets the action_id of this ReadBarcodeAction.  # noqa: E501


        :return: The action_id of this ReadBarcodeAction.  # noqa: E501
        :rtype: str
        """
        return self._action_id

    @action_id.setter
    def action_id(self, action_id):
        """Sets the action_id of this ReadBarcodeAction.


        :param action_id: The action_id of this ReadBarcodeAction.  # noqa: E501
        :type: str
        """

        self._action_id = action_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ReadBarcodeAction, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ReadBarcodeAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
