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


class Transform(object):
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
        'a': 'int',
        'b': 'int',
        'c': 'int',
        'd': 'int',
        'x': 'int',
        'y': 'int'
    }

    attribute_map = {
        'a': 'a',
        'b': 'b',
        'c': 'c',
        'd': 'd',
        'x': 'x',
        'y': 'y'
    }

    def __init__(self, a=None, b=None, c=None, d=None, x=None, y=None):  # noqa: E501
        """Transform - a model defined in Swagger"""  # noqa: E501

        self._a = None
        self._b = None
        self._c = None
        self._d = None
        self._x = None
        self._y = None
        self.discriminator = None

        if a is not None:
            self.a = a
        if b is not None:
            self.b = b
        if c is not None:
            self.c = c
        if d is not None:
            self.d = d
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    @property
    def a(self):
        """Gets the a of this Transform.  # noqa: E501


        :return: The a of this Transform.  # noqa: E501
        :rtype: int
        """
        return self._a

    @a.setter
    def a(self, a):
        """Sets the a of this Transform.


        :param a: The a of this Transform.  # noqa: E501
        :type: int
        """

        self._a = a

    @property
    def b(self):
        """Gets the b of this Transform.  # noqa: E501


        :return: The b of this Transform.  # noqa: E501
        :rtype: int
        """
        return self._b

    @b.setter
    def b(self, b):
        """Sets the b of this Transform.


        :param b: The b of this Transform.  # noqa: E501
        :type: int
        """

        self._b = b

    @property
    def c(self):
        """Gets the c of this Transform.  # noqa: E501


        :return: The c of this Transform.  # noqa: E501
        :rtype: int
        """
        return self._c

    @c.setter
    def c(self, c):
        """Sets the c of this Transform.


        :param c: The c of this Transform.  # noqa: E501
        :type: int
        """

        self._c = c

    @property
    def d(self):
        """Gets the d of this Transform.  # noqa: E501


        :return: The d of this Transform.  # noqa: E501
        :rtype: int
        """
        return self._d

    @d.setter
    def d(self, d):
        """Sets the d of this Transform.


        :param d: The d of this Transform.  # noqa: E501
        :type: int
        """

        self._d = d

    @property
    def x(self):
        """Gets the x of this Transform.  # noqa: E501


        :return: The x of this Transform.  # noqa: E501
        :rtype: int
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this Transform.


        :param x: The x of this Transform.  # noqa: E501
        :type: int
        """

        self._x = x

    @property
    def y(self):
        """Gets the y of this Transform.  # noqa: E501


        :return: The y of this Transform.  # noqa: E501
        :rtype: int
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this Transform.


        :param y: The y of this Transform.  # noqa: E501
        :type: int
        """

        self._y = y

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
        if not isinstance(other, Transform):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
