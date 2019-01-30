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

from pdf4me.model.key_value_pair_string_string import KeyValuePairStringString  # noqa: F401,E501


class ExtractAction(object):
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
        'extract_pages': 'list[int]',
        'custom_properties': 'list[KeyValuePairStringString]'
    }

    attribute_map = {
        'extract_pages': 'extractPages',
        'custom_properties': 'customProperties'
    }

    def __init__(self, extract_pages=None, custom_properties=None):  # noqa: E501
        """ExtractAction - a model defined in Swagger"""  # noqa: E501

        self._extract_pages = None
        self._custom_properties = None
        self.discriminator = None

        self.extract_pages = extract_pages
        if custom_properties is not None:
            self.custom_properties = custom_properties

    @property
    def extract_pages(self):
        """Gets the extract_pages of this ExtractAction.  # noqa: E501


        :return: The extract_pages of this ExtractAction.  # noqa: E501
        :rtype: list[int]
        """
        return self._extract_pages

    @extract_pages.setter
    def extract_pages(self, extract_pages):
        """Sets the extract_pages of this ExtractAction.


        :param extract_pages: The extract_pages of this ExtractAction.  # noqa: E501
        :type: list[int]
        """
        if extract_pages is None:
            raise ValueError("Invalid value for `extract_pages`, must not be `None`")  # noqa: E501

        self._extract_pages = extract_pages

    @property
    def custom_properties(self):
        """Gets the custom_properties of this ExtractAction.  # noqa: E501


        :return: The custom_properties of this ExtractAction.  # noqa: E501
        :rtype: list[KeyValuePairStringString]
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        """Sets the custom_properties of this ExtractAction.


        :param custom_properties: The custom_properties of this ExtractAction.  # noqa: E501
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
        if issubclass(ExtractAction, dict):
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
        if not isinstance(other, ExtractAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
