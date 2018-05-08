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


class RGBSet(object):
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
        'red': 'int',
        'green': 'int',
        'blue': 'int'
    }

    attribute_map = {
        'red': 'red',
        'green': 'green',
        'blue': 'blue'
    }

    def __init__(self, red=None, green=None, blue=None):  # noqa: E501
        """RGBSet - a model defined in Swagger"""  # noqa: E501

        self._red = None
        self._green = None
        self._blue = None
        self.discriminator = None

        if red is not None:
            self.red = red
        if green is not None:
            self.green = green
        if blue is not None:
            self.blue = blue

    @property
    def red(self):
        """Gets the red of this RGBSet.  # noqa: E501


        :return: The red of this RGBSet.  # noqa: E501
        :rtype: int
        """
        return self._red

    @red.setter
    def red(self, red):
        """Sets the red of this RGBSet.


        :param red: The red of this RGBSet.  # noqa: E501
        :type: int
        """

        self._red = red

    @property
    def green(self):
        """Gets the green of this RGBSet.  # noqa: E501


        :return: The green of this RGBSet.  # noqa: E501
        :rtype: int
        """
        return self._green

    @green.setter
    def green(self, green):
        """Sets the green of this RGBSet.


        :param green: The green of this RGBSet.  # noqa: E501
        :type: int
        """

        self._green = green

    @property
    def blue(self):
        """Gets the blue of this RGBSet.  # noqa: E501


        :return: The blue of this RGBSet.  # noqa: E501
        :rtype: int
        """
        return self._blue

    @blue.setter
    def blue(self, blue):
        """Sets the blue of this RGBSet.


        :param blue: The blue of this RGBSet.  # noqa: E501
        :type: int
        """

        self._blue = blue

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
        if not isinstance(other, RGBSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other