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

from pdf4me.model.pdf_rotate import PdfRotate  # noqa: F401,E501


class RotateAction(object):
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
        'rotation_list': 'list[PdfRotate]'
    }

    attribute_map = {
        'rotation_list': 'rotationList'
    }

    def __init__(self, rotation_list=None):  # noqa: E501
        """RotateAction - a model defined in Swagger"""  # noqa: E501

        self._rotation_list = None
        self.discriminator = None

        if rotation_list is not None:
            self.rotation_list = rotation_list

    @property
    def rotation_list(self):
        """Gets the rotation_list of this RotateAction.  # noqa: E501


        :return: The rotation_list of this RotateAction.  # noqa: E501
        :rtype: list[PdfRotate]
        """
        return self._rotation_list

    @rotation_list.setter
    def rotation_list(self, rotation_list):
        """Sets the rotation_list of this RotateAction.


        :param rotation_list: The rotation_list of this RotateAction.  # noqa: E501
        :type: list[PdfRotate]
        """

        self._rotation_list = rotation_list

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
        if issubclass(RotateAction, dict):
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
        if not isinstance(other, RotateAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
