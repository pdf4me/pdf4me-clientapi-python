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


class PdfRotate(object):
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
        'page_nr': 'int',
        'rotation_type': 'str'
    }

    attribute_map = {
        'page_nr': 'pageNr',
        'rotation_type': 'rotationType'
    }

    def __init__(self, page_nr=None, rotation_type=None):  # noqa: E501
        """PdfRotate - a model defined in Swagger"""  # noqa: E501

        self._page_nr = None
        self._rotation_type = None
        self.discriminator = None

        if page_nr is not None:
            self.page_nr = page_nr
        if rotation_type is not None:
            self.rotation_type = rotation_type

    @property
    def page_nr(self):
        """Gets the page_nr of this PdfRotate.  # noqa: E501


        :return: The page_nr of this PdfRotate.  # noqa: E501
        :rtype: int
        """
        return self._page_nr

    @page_nr.setter
    def page_nr(self, page_nr):
        """Sets the page_nr of this PdfRotate.


        :param page_nr: The page_nr of this PdfRotate.  # noqa: E501
        :type: int
        """

        self._page_nr = page_nr

    @property
    def rotation_type(self):
        """Gets the rotation_type of this PdfRotate.  # noqa: E501


        :return: The rotation_type of this PdfRotate.  # noqa: E501
        :rtype: str
        """
        return self._rotation_type

    @rotation_type.setter
    def rotation_type(self, rotation_type):
        """Sets the rotation_type of this PdfRotate.


        :param rotation_type: The rotation_type of this PdfRotate.  # noqa: E501
        :type: str
        """
        allowed_values = ["noRotation", "clockwise", "counterClockwise", "upsideDown"]  # noqa: E501
        if rotation_type not in allowed_values:
            raise ValueError(
                "Invalid value for `rotation_type` ({0}), must be one of {1}"  # noqa: E501
                .format(rotation_type, allowed_values)
            )

        self._rotation_type = rotation_type

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
        if issubclass(PdfRotate, dict):
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
        if not isinstance(other, PdfRotate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other