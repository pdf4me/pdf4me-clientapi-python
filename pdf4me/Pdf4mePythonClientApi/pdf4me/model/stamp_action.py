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


class StampAction(object):
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
        'page_sequence': 'str',
        'relative_pos_x': 'int',
        'relative_pos_y': 'int',
        'size_x': 'int',
        'size_y': 'int',
        'rotate': 'float',
        'autoorientation': 'bool',
        'alpha': 'float',
        'scale': 'str',
        'align_x': 'str',
        'align_y': 'str',
        'stamp_type': 'str',
        'text': 'Text',
        'image': 'Image',
        'action_id': 'str'
    }

    attribute_map = {
        'page_sequence': 'pageSequence',
        'relative_pos_x': 'relativePosX',
        'relative_pos_y': 'relativePosY',
        'size_x': 'sizeX',
        'size_y': 'sizeY',
        'rotate': 'rotate',
        'autoorientation': 'autoorientation',
        'alpha': 'alpha',
        'scale': 'scale',
        'align_x': 'alignX',
        'align_y': 'alignY',
        'stamp_type': 'stampType',
        'text': 'text',
        'image': 'image',
        'action_id': 'actionId'
    }

    def __init__(self, page_sequence=None, relative_pos_x=None, relative_pos_y=None, size_x=None, size_y=None, rotate=None, autoorientation=None, alpha=None, scale=None, align_x=None, align_y=None, stamp_type=None, text=None, image=None, action_id=None):  # noqa: E501
        """StampAction - a model defined in Swagger"""  # noqa: E501

        self._page_sequence = None
        self._relative_pos_x = None
        self._relative_pos_y = None
        self._size_x = None
        self._size_y = None
        self._rotate = None
        self._autoorientation = None
        self._alpha = None
        self._scale = None
        self._align_x = None
        self._align_y = None
        self._stamp_type = None
        self._text = None
        self._image = None
        self._action_id = None
        self.discriminator = None

        if page_sequence is not None:
            self.page_sequence = page_sequence
        if relative_pos_x is not None:
            self.relative_pos_x = relative_pos_x
        if relative_pos_y is not None:
            self.relative_pos_y = relative_pos_y
        if size_x is not None:
            self.size_x = size_x
        if size_y is not None:
            self.size_y = size_y
        if rotate is not None:
            self.rotate = rotate
        if autoorientation is not None:
            self.autoorientation = autoorientation
        self.alpha = alpha
        if scale is not None:
            self.scale = scale
        if align_x is not None:
            self.align_x = align_x
        if align_y is not None:
            self.align_y = align_y
        if stamp_type is not None:
            self.stamp_type = stamp_type
        if text is not None:
            self.text = text
        if image is not None:
            self.image = image
        if action_id is not None:
            self.action_id = action_id

    @property
    def page_sequence(self):
        """Gets the page_sequence of this StampAction.  # noqa: E501


        :return: The page_sequence of this StampAction.  # noqa: E501
        :rtype: str
        """
        return self._page_sequence

    @page_sequence.setter
    def page_sequence(self, page_sequence):
        """Sets the page_sequence of this StampAction.


        :param page_sequence: The page_sequence of this StampAction.  # noqa: E501
        :type: str
        """

        self._page_sequence = page_sequence

    @property
    def relative_pos_x(self):
        """Gets the relative_pos_x of this StampAction.  # noqa: E501


        :return: The relative_pos_x of this StampAction.  # noqa: E501
        :rtype: int
        """
        return self._relative_pos_x

    @relative_pos_x.setter
    def relative_pos_x(self, relative_pos_x):
        """Sets the relative_pos_x of this StampAction.


        :param relative_pos_x: The relative_pos_x of this StampAction.  # noqa: E501
        :type: int
        """

        self._relative_pos_x = relative_pos_x

    @property
    def relative_pos_y(self):
        """Gets the relative_pos_y of this StampAction.  # noqa: E501


        :return: The relative_pos_y of this StampAction.  # noqa: E501
        :rtype: int
        """
        return self._relative_pos_y

    @relative_pos_y.setter
    def relative_pos_y(self, relative_pos_y):
        """Sets the relative_pos_y of this StampAction.


        :param relative_pos_y: The relative_pos_y of this StampAction.  # noqa: E501
        :type: int
        """

        self._relative_pos_y = relative_pos_y

    @property
    def size_x(self):
        """Gets the size_x of this StampAction.  # noqa: E501


        :return: The size_x of this StampAction.  # noqa: E501
        :rtype: int
        """
        return self._size_x

    @size_x.setter
    def size_x(self, size_x):
        """Sets the size_x of this StampAction.


        :param size_x: The size_x of this StampAction.  # noqa: E501
        :type: int
        """

        self._size_x = size_x

    @property
    def size_y(self):
        """Gets the size_y of this StampAction.  # noqa: E501


        :return: The size_y of this StampAction.  # noqa: E501
        :rtype: int
        """
        return self._size_y

    @size_y.setter
    def size_y(self, size_y):
        """Sets the size_y of this StampAction.


        :param size_y: The size_y of this StampAction.  # noqa: E501
        :type: int
        """

        self._size_y = size_y

    @property
    def rotate(self):
        """Gets the rotate of this StampAction.  # noqa: E501


        :return: The rotate of this StampAction.  # noqa: E501
        :rtype: float
        """
        return self._rotate

    @rotate.setter
    def rotate(self, rotate):
        """Sets the rotate of this StampAction.


        :param rotate: The rotate of this StampAction.  # noqa: E501
        :type: float
        """

        self._rotate = rotate

    @property
    def autoorientation(self):
        """Gets the autoorientation of this StampAction.  # noqa: E501


        :return: The autoorientation of this StampAction.  # noqa: E501
        :rtype: bool
        """
        return self._autoorientation

    @autoorientation.setter
    def autoorientation(self, autoorientation):
        """Sets the autoorientation of this StampAction.


        :param autoorientation: The autoorientation of this StampAction.  # noqa: E501
        :type: bool
        """

        self._autoorientation = autoorientation

    @property
    def alpha(self):
        """Gets the alpha of this StampAction.  # noqa: E501

        The opacity of the stamp as a whole. 1.0 for fully opaque, 0.0 for fully transparent.  Default: 1.0  The PDF/A-1 standard does not allow transparency.Therefore, for PDF/A-1 conforming input files you must  not set alpha to a value other than 1.0  # noqa: E501

        :return: The alpha of this StampAction.  # noqa: E501
        :rtype: float
        """
        return self._alpha

    @alpha.setter
    def alpha(self, alpha):
        """Sets the alpha of this StampAction.

        The opacity of the stamp as a whole. 1.0 for fully opaque, 0.0 for fully transparent.  Default: 1.0  The PDF/A-1 standard does not allow transparency.Therefore, for PDF/A-1 conforming input files you must  not set alpha to a value other than 1.0  # noqa: E501

        :param alpha: The alpha of this StampAction.  # noqa: E501
        :type: float
        """
        # if alpha is None:
        #     raise ValueError("Invalid value for `alpha`, must not be `None`")  # noqa: E501

        self._alpha = alpha

    @property
    def scale(self):
        """Gets the scale of this StampAction.  # noqa: E501

        Modify scale of stamp. Allowed values for ‹scale_set› are:   - relToA4: Scale the stamp relative to the page size. For example, make stamp half as large on a A5 and  twice as large on a A3 page as specified.  # noqa: E501

        :return: The scale of this StampAction.  # noqa: E501
        :rtype: str
        """
        return self._scale

    @scale.setter
    def scale(self, scale):
        """Sets the scale of this StampAction.

        Modify scale of stamp. Allowed values for ‹scale_set› are:   - relToA4: Scale the stamp relative to the page size. For example, make stamp half as large on a A5 and  twice as large on a A3 page as specified.  # noqa: E501

        :param scale: The scale of this StampAction.  # noqa: E501
        :type: str
        """
        allowed_values = ["relToA4"]  # noqa: E501
        if scale not in allowed_values:
            raise ValueError(
                "Invalid value for `scale` ({0}), must be one of {1}"  # noqa: E501
                .format(scale, allowed_values)
            )

        self._scale = scale

    @property
    def align_x(self):
        """Gets the align_x of this StampAction.  # noqa: E501


        :return: The align_x of this StampAction.  # noqa: E501
        :rtype: str
        """
        return self._align_x

    @align_x.setter
    def align_x(self, align_x):
        """Sets the align_x of this StampAction.


        :param align_x: The align_x of this StampAction.  # noqa: E501
        :type: str
        """
        allowed_values = ["left", "center", "right"]  # noqa: E501
        if align_x not in allowed_values:
            raise ValueError(
                "Invalid value for `align_x` ({0}), must be one of {1}"  # noqa: E501
                .format(align_x, allowed_values)
            )

        self._align_x = align_x

    @property
    def align_y(self):
        """Gets the align_y of this StampAction.  # noqa: E501


        :return: The align_y of this StampAction.  # noqa: E501
        :rtype: str
        """
        return self._align_y

    @align_y.setter
    def align_y(self, align_y):
        """Sets the align_y of this StampAction.


        :param align_y: The align_y of this StampAction.  # noqa: E501
        :type: str
        """
        allowed_values = ["top", "middle", "bottom"]  # noqa: E501
        if align_y not in allowed_values:
            raise ValueError(
                "Invalid value for `align_y` ({0}), must be one of {1}"  # noqa: E501
                .format(align_y, allowed_values)
            )

        self._align_y = align_y

    @property
    def stamp_type(self):
        """Gets the stamp_type of this StampAction.  # noqa: E501


        :return: The stamp_type of this StampAction.  # noqa: E501
        :rtype: str
        """
        return self._stamp_type

    @stamp_type.setter
    def stamp_type(self, stamp_type):
        """Sets the stamp_type of this StampAction.


        :param stamp_type: The stamp_type of this StampAction.  # noqa: E501
        :type: str
        """
        allowed_values = ["annotation", "foreground", "background"]  # noqa: E501
        if stamp_type not in allowed_values:
            raise ValueError(
                "Invalid value for `stamp_type` ({0}), must be one of {1}"  # noqa: E501
                .format(stamp_type, allowed_values)
            )

        self._stamp_type = stamp_type

    @property
    def text(self):
        """Gets the text of this StampAction.  # noqa: E501


        :return: The text of this StampAction.  # noqa: E501
        :rtype: Text
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this StampAction.


        :param text: The text of this StampAction.  # noqa: E501
        :type: Text
        """

        self._text = text

    @property
    def image(self):
        """Gets the image of this StampAction.  # noqa: E501


        :return: The image of this StampAction.  # noqa: E501
        :rtype: Image
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this StampAction.


        :param image: The image of this StampAction.  # noqa: E501
        :type: Image
        """

        self._image = image

    @property
    def action_id(self):
        """Gets the action_id of this StampAction.  # noqa: E501


        :return: The action_id of this StampAction.  # noqa: E501
        :rtype: str
        """
        return self._action_id

    @action_id.setter
    def action_id(self, action_id):
        """Sets the action_id of this StampAction.


        :param action_id: The action_id of this StampAction.  # noqa: E501
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
        if issubclass(StampAction, dict):
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
        if not isinstance(other, StampAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
