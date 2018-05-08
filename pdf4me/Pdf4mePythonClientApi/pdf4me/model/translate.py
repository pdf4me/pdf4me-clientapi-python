# coding: utf-8

"""
    DmsApi

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Translate(object):
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
        'offset_x': 'int',
        'offset_y': 'int'
    }

    attribute_map = {
        'offset_x': 'offsetX',
        'offset_y': 'offsetY'
    }

    def __init__(self, offset_x=None, offset_y=None):  # noqa: E501
        """Translate - a model defined in Swagger"""  # noqa: E501

        self._offset_x = None
        self._offset_y = None
        self.discriminator = None

        self.offset_x = offset_x
        self.offset_y = offset_y

    @property
    def offset_x(self):
        """Gets the offset_x of this Translate.  # noqa: E501


        :return: The offset_x of this Translate.  # noqa: E501
        :rtype: int
        """
        return self._offset_x

    @offset_x.setter
    def offset_x(self, offset_x):
        """Sets the offset_x of this Translate.


        :param offset_x: The offset_x of this Translate.  # noqa: E501
        :type: int
        """
        if offset_x is None:
            raise ValueError("Invalid value for `offset_x`, must not be `None`")  # noqa: E501

        self._offset_x = offset_x

    @property
    def offset_y(self):
        """Gets the offset_y of this Translate.  # noqa: E501


        :return: The offset_y of this Translate.  # noqa: E501
        :rtype: int
        """
        return self._offset_y

    @offset_y.setter
    def offset_y(self, offset_y):
        """Sets the offset_y of this Translate.


        :param offset_y: The offset_y of this Translate.  # noqa: E501
        :type: int
        """
        if offset_y is None:
            raise ValueError("Invalid value for `offset_y`, must not be `None`")  # noqa: E501

        self._offset_y = offset_y

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Translate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other