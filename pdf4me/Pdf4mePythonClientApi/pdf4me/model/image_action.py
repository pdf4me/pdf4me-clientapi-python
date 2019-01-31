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

from pdf4me.model.custom_cms_config import CustomCMSConfig  # noqa: F401,E501
from pdf4me.model.key_value_pair_string_string import KeyValuePairStringString  # noqa: F401,E501
from pdf4me.model.page_selection import PageSelection  # noqa: F401,E501


class ImageAction(object):
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
        'page_selection': 'PageSelection',
        'center': 'bool',
        'fit_page': 'bool',
        'bits_per_pixel': 'int',
        'bilevel_threshold': 'int',
        'width_pixel': 'int',
        'height_pixel': 'int',
        'width_point': 'int',
        'height_point': 'int',
        'render_options': 'list[str]',
        'rotate_mode': 'str',
        'preserve_aspect_ratio': 'bool',
        'image_quality': 'int',
        'cms_engine': 'str',
        'custom_cms_config': 'CustomCMSConfig',
        'dithering': 'str',
        'dpi': 'int',
        'fill_order': 'str',
        'filter_ratio': 'int',
        'image_extension': 'str',
        'color_space': 'str',
        'compression': 'str',
        'custom_properties': 'list[KeyValuePairStringString]'
    }

    attribute_map = {
        'page_selection': 'pageSelection',
        'center': 'center',
        'fit_page': 'fitPage',
        'bits_per_pixel': 'bitsPerPixel',
        'bilevel_threshold': 'bilevelThreshold',
        'width_pixel': 'widthPixel',
        'height_pixel': 'heightPixel',
        'width_point': 'widthPoint',
        'height_point': 'heightPoint',
        'render_options': 'renderOptions',
        'rotate_mode': 'rotateMode',
        'preserve_aspect_ratio': 'preserveAspectRatio',
        'image_quality': 'imageQuality',
        'cms_engine': 'cmsEngine',
        'custom_cms_config': 'customCMSConfig',
        'dithering': 'dithering',
        'dpi': 'dpi',
        'fill_order': 'fillOrder',
        'filter_ratio': 'filterRatio',
        'image_extension': 'imageExtension',
        'color_space': 'colorSpace',
        'compression': 'compression',
        'custom_properties': 'customProperties'
    }

    def __init__(self, page_selection=None, center=None, fit_page=None, bits_per_pixel=None, bilevel_threshold=None, width_pixel=None, height_pixel=None, width_point=None, height_point=None, render_options=None, rotate_mode=None, preserve_aspect_ratio=None, image_quality=None, cms_engine=None, custom_cms_config=None, dithering=None, dpi=None, fill_order=None, filter_ratio=None, image_extension=None, color_space=None, compression=None, custom_properties=None):  # noqa: E501
        """ImageAction - a model defined in Swagger"""  # noqa: E501

        self._page_selection = None
        self._center = None
        self._fit_page = None
        self._bits_per_pixel = None
        self._bilevel_threshold = None
        self._width_pixel = None
        self._height_pixel = None
        self._width_point = None
        self._height_point = None
        self._render_options = None
        self._rotate_mode = None
        self._preserve_aspect_ratio = None
        self._image_quality = None
        self._cms_engine = None
        self._custom_cms_config = None
        self._dithering = None
        self._dpi = None
        self._fill_order = None
        self._filter_ratio = None
        self._image_extension = None
        self._color_space = None
        self._compression = None
        self._custom_properties = None
        self.discriminator = None

        self.page_selection = page_selection
        if center is not None:
            self.center = center
        if fit_page is not None:
            self.fit_page = fit_page
        if bits_per_pixel is not None:
            self.bits_per_pixel = bits_per_pixel
        if bilevel_threshold is not None:
            self.bilevel_threshold = bilevel_threshold
        if width_pixel is not None:
            self.width_pixel = width_pixel
        if height_pixel is not None:
            self.height_pixel = height_pixel
        if width_point is not None:
            self.width_point = width_point
        if height_point is not None:
            self.height_point = height_point
        if render_options is not None:
            self.render_options = render_options
        if rotate_mode is not None:
            self.rotate_mode = rotate_mode
        if preserve_aspect_ratio is not None:
            self.preserve_aspect_ratio = preserve_aspect_ratio
        if image_quality is not None:
            self.image_quality = image_quality
        if cms_engine is not None:
            self.cms_engine = cms_engine
        if custom_cms_config is not None:
            self.custom_cms_config = custom_cms_config
        if dithering is not None:
            self.dithering = dithering
        if dpi is not None:
            self.dpi = dpi
        if fill_order is not None:
            self.fill_order = fill_order
        if filter_ratio is not None:
            self.filter_ratio = filter_ratio
        if image_extension is not None:
            self.image_extension = image_extension
        if color_space is not None:
            self.color_space = color_space
        if compression is not None:
            self.compression = compression
        if custom_properties is not None:
            self.custom_properties = custom_properties

    @property
    def page_selection(self):
        """Gets the page_selection of this ImageAction.  # noqa: E501

        Set the Pages wo apply the convertion.    {default: PageSelection.All}  # noqa: E501

        :return: The page_selection of this ImageAction.  # noqa: E501
        :rtype: PageSelection
        """
        return self._page_selection

    @page_selection.setter
    def page_selection(self, page_selection):
        """Sets the page_selection of this ImageAction.

        Set the Pages wo apply the convertion.    {default: PageSelection.All}  # noqa: E501

        :param page_selection: The page_selection of this ImageAction.  # noqa: E501
        :type: PageSelection
        """
        # if page_selection is None:
        #     raise ValueError("Invalid value for `page_selection`, must not be `None`")  # noqa: E501

        self._page_selection = page_selection

    @property
    def center(self):
        """Gets the center of this ImageAction.  # noqa: E501

        Set or get the center mode. When set to True, the document is horizontally and vertically centered on the page.  When set to False, the document is printed to the upper left corner of the page.    {default: false}  # noqa: E501

        :return: The center of this ImageAction.  # noqa: E501
        :rtype: bool
        """
        return self._center

    @center.setter
    def center(self, center):
        """Sets the center of this ImageAction.

        Set or get the center mode. When set to True, the document is horizontally and vertically centered on the page.  When set to False, the document is printed to the upper left corner of the page.    {default: false}  # noqa: E501

        :param center: The center of this ImageAction.  # noqa: E501
        :type: bool
        """

        self._center = center

    @property
    def fit_page(self):
        """Gets the fit_page of this ImageAction.  # noqa: E501

        set the fit page mode. If set to True, the page is scaled to fit the image (in either width or height). If set to  False, the page is rendered with its true size.  {default: true}  # noqa: E501

        :return: The fit_page of this ImageAction.  # noqa: E501
        :rtype: bool
        """
        return self._fit_page

    @fit_page.setter
    def fit_page(self, fit_page):
        """Sets the fit_page of this ImageAction.

        set the fit page mode. If set to True, the page is scaled to fit the image (in either width or height). If set to  False, the page is rendered with its true size.  {default: true}  # noqa: E501

        :param fit_page: The fit_page of this ImageAction.  # noqa: E501
        :type: bool
        """

        self._fit_page = fit_page

    @property
    def bits_per_pixel(self):
        """Gets the bits_per_pixel of this ImageAction.  # noqa: E501

        Get or set the color depth. Bi-tonal: 1, gray scale: 8, RGB true color: 24, CMYK: 32.    {default: 24}  # noqa: E501

        :return: The bits_per_pixel of this ImageAction.  # noqa: E501
        :rtype: int
        """
        return self._bits_per_pixel

    @bits_per_pixel.setter
    def bits_per_pixel(self, bits_per_pixel):
        """Sets the bits_per_pixel of this ImageAction.

        Get or set the color depth. Bi-tonal: 1, gray scale: 8, RGB true color: 24, CMYK: 32.    {default: 24}  # noqa: E501

        :param bits_per_pixel: The bits_per_pixel of this ImageAction.  # noqa: E501
        :type: int
        """

        self._bits_per_pixel = bits_per_pixel

    @property
    def bilevel_threshold(self):
        """Gets the bilevel_threshold of this ImageAction.  # noqa: E501

        Set the threshold for converting from gray to bi-tonal when Dithering is eDitherNone. Value must be in  the range of 0 to 255.    {default: 181}  # noqa: E501

        :return: The bilevel_threshold of this ImageAction.  # noqa: E501
        :rtype: int
        """
        return self._bilevel_threshold

    @bilevel_threshold.setter
    def bilevel_threshold(self, bilevel_threshold):
        """Sets the bilevel_threshold of this ImageAction.

        Set the threshold for converting from gray to bi-tonal when Dithering is eDitherNone. Value must be in  the range of 0 to 255.    {default: 181}  # noqa: E501

        :param bilevel_threshold: The bilevel_threshold of this ImageAction.  # noqa: E501
        :type: int
        """

        self._bilevel_threshold = bilevel_threshold

    @property
    def width_pixel(self):
        """Gets the width_pixel of this ImageAction.  # noqa: E501


        :return: The width_pixel of this ImageAction.  # noqa: E501
        :rtype: int
        """
        return self._width_pixel

    @width_pixel.setter
    def width_pixel(self, width_pixel):
        """Sets the width_pixel of this ImageAction.


        :param width_pixel: The width_pixel of this ImageAction.  # noqa: E501
        :type: int
        """

        self._width_pixel = width_pixel

    @property
    def height_pixel(self):
        """Gets the height_pixel of this ImageAction.  # noqa: E501


        :return: The height_pixel of this ImageAction.  # noqa: E501
        :rtype: int
        """
        return self._height_pixel

    @height_pixel.setter
    def height_pixel(self, height_pixel):
        """Sets the height_pixel of this ImageAction.


        :param height_pixel: The height_pixel of this ImageAction.  # noqa: E501
        :type: int
        """

        self._height_pixel = height_pixel

    @property
    def width_point(self):
        """Gets the width_point of this ImageAction.  # noqa: E501


        :return: The width_point of this ImageAction.  # noqa: E501
        :rtype: int
        """
        return self._width_point

    @width_point.setter
    def width_point(self, width_point):
        """Sets the width_point of this ImageAction.


        :param width_point: The width_point of this ImageAction.  # noqa: E501
        :type: int
        """

        self._width_point = width_point

    @property
    def height_point(self):
        """Gets the height_point of this ImageAction.  # noqa: E501


        :return: The height_point of this ImageAction.  # noqa: E501
        :rtype: int
        """
        return self._height_point

    @height_point.setter
    def height_point(self, height_point):
        """Sets the height_point of this ImageAction.


        :param height_point: The height_point of this ImageAction.  # noqa: E501
        :type: int
        """

        self._height_point = height_point

    @property
    def render_options(self):
        """Gets the render_options of this ImageAction.  # noqa: E501

        Set a specific rendering option.  # noqa: E501

        :return: The render_options of this ImageAction.  # noqa: E501
        :rtype: list[str]
        """
        return self._render_options

    @render_options.setter
    def render_options(self, render_options):
        """Sets the render_options of this ImageAction.

        Set a specific rendering option.  # noqa: E501

        :param render_options: The render_options of this ImageAction.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["noAntialiasing", "noInterpolation", "noLowPassFilter", "noHinting", "printingMode", "noBPC", "fitPaths", "useBoxFilter"]  # noqa: E501
        if not set(render_options).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `render_options` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(render_options) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._render_options = render_options

    @property
    def rotate_mode(self):
        """Gets the rotate_mode of this ImageAction.  # noqa: E501

        Set the rotation mode of the page.    Attribute: Set the rotation to the viewing rotation attribute of the PDF page, i.e. rendering the  page with the same rotation as it is displayed in a PDF viewer.    {default: Attribute}  # noqa: E501

        :return: The rotate_mode of this ImageAction.  # noqa: E501
        :rtype: str
        """
        return self._rotate_mode

    @rotate_mode.setter
    def rotate_mode(self, rotate_mode):
        """Sets the rotate_mode of this ImageAction.

        Set the rotation mode of the page.    Attribute: Set the rotation to the viewing rotation attribute of the PDF page, i.e. rendering the  page with the same rotation as it is displayed in a PDF viewer.    {default: Attribute}  # noqa: E501

        :param rotate_mode: The rotate_mode of this ImageAction.  # noqa: E501
        :type: str
        """
        allowed_values = ["none", "attribute", "portrait", "landscape"]  # noqa: E501
        if rotate_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `rotate_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(rotate_mode, allowed_values)
            )

        self._rotate_mode = rotate_mode

    @property
    def preserve_aspect_ratio(self):
        """Gets the preserve_aspect_ratio of this ImageAction.  # noqa: E501

        If True a uniform up- or down-scaling is applied, i.e. the output image has the same ratio of width to height as the  input file and its size will fit into the defined dimensions, given by SetBitmapDimensions.    {default: true}  # noqa: E501

        :return: The preserve_aspect_ratio of this ImageAction.  # noqa: E501
        :rtype: bool
        """
        return self._preserve_aspect_ratio

    @preserve_aspect_ratio.setter
    def preserve_aspect_ratio(self, preserve_aspect_ratio):
        """Sets the preserve_aspect_ratio of this ImageAction.

        If True a uniform up- or down-scaling is applied, i.e. the output image has the same ratio of width to height as the  input file and its size will fit into the defined dimensions, given by SetBitmapDimensions.    {default: true}  # noqa: E501

        :param preserve_aspect_ratio: The preserve_aspect_ratio of this ImageAction.  # noqa: E501
        :type: bool
        """

        self._preserve_aspect_ratio = preserve_aspect_ratio

    @property
    def image_quality(self):
        """Gets the image_quality of this ImageAction.  # noqa: E501

        Set the quality index of lossy compression types. This value ranges from 1 to 100 and is applied to JPEG and  JPEG2000 compression.For JPEG2000, a quality index of 100 means lossless compression.JPEG compression is  always lossy.    {default: 80}  # noqa: E501

        :return: The image_quality of this ImageAction.  # noqa: E501
        :rtype: int
        """
        return self._image_quality

    @image_quality.setter
    def image_quality(self, image_quality):
        """Sets the image_quality of this ImageAction.

        Set the quality index of lossy compression types. This value ranges from 1 to 100 and is applied to JPEG and  JPEG2000 compression.For JPEG2000, a quality index of 100 means lossless compression.JPEG compression is  always lossy.    {default: 80}  # noqa: E501

        :param image_quality: The image_quality of this ImageAction.  # noqa: E501
        :type: int
        """

        self._image_quality = image_quality

    @property
    def cms_engine(self):
        """Gets the cms_engine of this ImageAction.  # noqa: E501

        Set the Color Management System (CMS) Engine.     {default: 80}  # noqa: E501

        :return: The cms_engine of this ImageAction.  # noqa: E501
        :rtype: str
        """
        return self._cms_engine

    @cms_engine.setter
    def cms_engine(self, cms_engine):
        """Sets the cms_engine of this ImageAction.

        Set the Color Management System (CMS) Engine.     {default: 80}  # noqa: E501

        :param cms_engine: The cms_engine of this ImageAction.  # noqa: E501
        :type: str
        """
        allowed_values = ["none", "neugebauer", "lcms", "customCMSConfig"]  # noqa: E501
        if cms_engine not in allowed_values:
            raise ValueError(
                "Invalid value for `cms_engine` ({0}), must be one of {1}"  # noqa: E501
                .format(cms_engine, allowed_values)
            )

        self._cms_engine = cms_engine

    @property
    def custom_cms_config(self):
        """Gets the custom_cms_config of this ImageAction.  # noqa: E501

        Set the Color Management System (CMS) Engine.     {default: 80}  # noqa: E501

        :return: The custom_cms_config of this ImageAction.  # noqa: E501
        :rtype: CustomCMSConfig
        """
        return self._custom_cms_config

    @custom_cms_config.setter
    def custom_cms_config(self, custom_cms_config):
        """Sets the custom_cms_config of this ImageAction.

        Set the Color Management System (CMS) Engine.     {default: 80}  # noqa: E501

        :param custom_cms_config: The custom_cms_config of this ImageAction.  # noqa: E501
        :type: CustomCMSConfig
        """

        self._custom_cms_config = custom_cms_config

    @property
    def dithering(self):
        """Gets the dithering of this ImageAction.  # noqa: E501

        Set the dithering algorithm.Dithering refers to the procedure of simulating colors or grayscales.This is mainly  useful for low color depth (e.g.black and white or indexed) images.  The supported values for TPDFDithering are listed in the corresponding enumeration.  {default: DitherFloydSteinberg}  # noqa: E501

        :return: The dithering of this ImageAction.  # noqa: E501
        :rtype: str
        """
        return self._dithering

    @dithering.setter
    def dithering(self, dithering):
        """Sets the dithering of this ImageAction.

        Set the dithering algorithm.Dithering refers to the procedure of simulating colors or grayscales.This is mainly  useful for low color depth (e.g.black and white or indexed) images.  The supported values for TPDFDithering are listed in the corresponding enumeration.  {default: DitherFloydSteinberg}  # noqa: E501

        :param dithering: The dithering of this ImageAction.  # noqa: E501
        :type: str
        """
        allowed_values = ["none", "floydSteinberg", "halftone", "pattern", "g3Optimized", "g4Optimized", "atkinson"]  # noqa: E501
        if dithering not in allowed_values:
            raise ValueError(
                "Invalid value for `dithering` ({0}), must be one of {1}"  # noqa: E501
                .format(dithering, allowed_values)
            )

        self._dithering = dithering

    @property
    def dpi(self):
        """Gets the dpi of this ImageAction.  # noqa: E501

        <p>              Get or set the resolution of the image in DPI (dots per inch).              Set Both the resolutions for the x- and y-axis are set to the same value.              </p>  <p>              Setting DPI is redundant to setting the specialized properties XDPI and YDPI.              </p>  {default: 150}  # noqa: E501

        :return: The dpi of this ImageAction.  # noqa: E501
        :rtype: int
        """
        return self._dpi

    @dpi.setter
    def dpi(self, dpi):
        """Sets the dpi of this ImageAction.

        <p>              Get or set the resolution of the image in DPI (dots per inch).              Set Both the resolutions for the x- and y-axis are set to the same value.              </p>  <p>              Setting DPI is redundant to setting the specialized properties XDPI and YDPI.              </p>  {default: 150}  # noqa: E501

        :param dpi: The dpi of this ImageAction.  # noqa: E501
        :type: int
        """

        self._dpi = dpi

    @property
    def fill_order(self):
        """Gets the fill_order of this ImageAction.  # noqa: E501

        Set the bit fill order.  MSB (Most significant bit) or LSB (Least significant bit) first.    {default: MostSignificantBit}  # noqa: E501

        :return: The fill_order of this ImageAction.  # noqa: E501
        :rtype: str
        """
        return self._fill_order

    @fill_order.setter
    def fill_order(self, fill_order):
        """Sets the fill_order of this ImageAction.

        Set the bit fill order.  MSB (Most significant bit) or LSB (Least significant bit) first.    {default: MostSignificantBit}  # noqa: E501

        :param fill_order: The fill_order of this ImageAction.  # noqa: E501
        :type: str
        """
        allowed_values = ["mostSignificantBit", "leastSignificantBit"]  # noqa: E501
        if fill_order not in allowed_values:
            raise ValueError(
                "Invalid value for `fill_order` ({0}), must be one of {1}"  # noqa: E501
                .format(fill_order, allowed_values)
            )

        self._fill_order = fill_order

    @property
    def filter_ratio(self):
        """Gets the filter_ratio of this ImageAction.  # noqa: E501

        <p>              This property is used to enable and parameterize super-sampling, a technique to initially render the image at a              higher resolution and then sample it down to the target resolution.As a result of that process the final image              appears smoother, i.e.anti-aliased.              </p>  <p>              Applying super-sampling improves the image quality when rendering at low target resolutions(72 DPI or less); the              higher the target resolution the less the visual impact.              This property requires memory and CPU time quadratically to the ratio, therefore only small values, such as 2 or 3              should be used.              </p>  <p>              If a too high value (in combination with the original image size) is set, it is ignored.              </p>  {default: 1}  # noqa: E501

        :return: The filter_ratio of this ImageAction.  # noqa: E501
        :rtype: int
        """
        return self._filter_ratio

    @filter_ratio.setter
    def filter_ratio(self, filter_ratio):
        """Sets the filter_ratio of this ImageAction.

        <p>              This property is used to enable and parameterize super-sampling, a technique to initially render the image at a              higher resolution and then sample it down to the target resolution.As a result of that process the final image              appears smoother, i.e.anti-aliased.              </p>  <p>              Applying super-sampling improves the image quality when rendering at low target resolutions(72 DPI or less); the              higher the target resolution the less the visual impact.              This property requires memory and CPU time quadratically to the ratio, therefore only small values, such as 2 or 3              should be used.              </p>  <p>              If a too high value (in combination with the original image size) is set, it is ignored.              </p>  {default: 1}  # noqa: E501

        :param filter_ratio: The filter_ratio of this ImageAction.  # noqa: E501
        :type: int
        """

        self._filter_ratio = filter_ratio

    @property
    def image_extension(self):
        """Gets the image_extension of this ImageAction.  # noqa: E501

        Set output Type for image file.  # noqa: E501

        :return: The image_extension of this ImageAction.  # noqa: E501
        :rtype: str
        """
        return self._image_extension

    @image_extension.setter
    def image_extension(self, image_extension):
        """Sets the image_extension of this ImageAction.

        Set output Type for image file.  # noqa: E501

        :param image_extension: The image_extension of this ImageAction.  # noqa: E501
        :type: str
        """
        allowed_values = ["jpg", "jpeg", "bmp", "gif", "jb2", "jp2", "jpf", "jpx", "png", "tif", "tiff"]  # noqa: E501
        if image_extension not in allowed_values:
            raise ValueError(
                "Invalid value for `image_extension` ({0}), must be one of {1}"  # noqa: E501
                .format(image_extension, allowed_values)
            )

        self._image_extension = image_extension

    @property
    def color_space(self):
        """Gets the color_space of this ImageAction.  # noqa: E501

        Set color space of the output image, see enumeration TPDFColorSpace.  For black white bi-tonal images, a gray color space must be selected    {default: ColorRGB}  # noqa: E501

        :return: The color_space of this ImageAction.  # noqa: E501
        :rtype: str
        """
        return self._color_space

    @color_space.setter
    def color_space(self, color_space):
        """Sets the color_space of this ImageAction.

        Set color space of the output image, see enumeration TPDFColorSpace.  For black white bi-tonal images, a gray color space must be selected    {default: ColorRGB}  # noqa: E501

        :param color_space: The color_space of this ImageAction.  # noqa: E501
        :type: str
        """
        allowed_values = ["rGB", "rGBA", "gray", "grayA", "cMYK", "yCbCr", "yCbCrK", "palette", "lAB", "cMYK_Konly", "cMYKA"]  # noqa: E501
        if color_space not in allowed_values:
            raise ValueError(
                "Invalid value for `color_space` ({0}), must be one of {1}"  # noqa: E501
                .format(color_space, allowed_values)
            )

        self._color_space = color_space

    @property
    def compression(self):
        """Gets the compression of this ImageAction.  # noqa: E501

        Get or set the compression type of TIFF images. For any other image format, the compression is automatically  defined by the file extension(the file name).  The supported values for TPDFCompression are listed in the corresponding enumeration.                {default: ComprLZW}  # noqa: E501

        :return: The compression of this ImageAction.  # noqa: E501
        :rtype: str
        """
        return self._compression

    @compression.setter
    def compression(self, compression):
        """Sets the compression of this ImageAction.

        Get or set the compression type of TIFF images. For any other image format, the compression is automatically  defined by the file extension(the file name).  The supported values for TPDFCompression are listed in the corresponding enumeration.                {default: ComprLZW}  # noqa: E501

        :param compression: The compression of this ImageAction.  # noqa: E501
        :type: str
        """
        allowed_values = ["lZW", "jPEG", "flate", "raw", "group3", "group3_2D", "group4", "jBIG2", "jPEG2000", "tIFFJPEG"]  # noqa: E501
        if compression not in allowed_values:
            raise ValueError(
                "Invalid value for `compression` ({0}), must be one of {1}"  # noqa: E501
                .format(compression, allowed_values)
            )

        self._compression = compression

    @property
    def custom_properties(self):
        """Gets the custom_properties of this ImageAction.  # noqa: E501


        :return: The custom_properties of this ImageAction.  # noqa: E501
        :rtype: list[KeyValuePairStringString]
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        """Sets the custom_properties of this ImageAction.


        :param custom_properties: The custom_properties of this ImageAction.  # noqa: E501
        :type: list[KeyValuePairStringString]
        """

        self._custom_properties = custom_properties

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
        if issubclass(ImageAction, dict):
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
        if not isinstance(other, ImageAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
