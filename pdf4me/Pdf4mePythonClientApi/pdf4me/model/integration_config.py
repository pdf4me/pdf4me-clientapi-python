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

from pdf4me.model.key_value_pair_string_object import KeyValuePairStringObject  # noqa: F401,E501


class IntegrationConfig(object):
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
        'config_params': 'list[KeyValuePairStringObject]'
    }

    attribute_map = {
        'config_params': 'configParams'
    }

    def __init__(self, config_params=None):  # noqa: E501
        """IntegrationConfig - a model defined in Swagger"""  # noqa: E501

        self._config_params = None
        self.discriminator = None

        if config_params is not None:
            self.config_params = config_params

    @property
    def config_params(self):
        """Gets the config_params of this IntegrationConfig.  # noqa: E501


        :return: The config_params of this IntegrationConfig.  # noqa: E501
        :rtype: list[KeyValuePairStringObject]
        """
        return self._config_params

    @config_params.setter
    def config_params(self, config_params):
        """Sets the config_params of this IntegrationConfig.


        :param config_params: The config_params of this IntegrationConfig.  # noqa: E501
        :type: list[KeyValuePairStringObject]
        """

        self._config_params = config_params

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
        if issubclass(IntegrationConfig, dict):
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
        if not isinstance(other, IntegrationConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
