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


class Pdf4meAction(object):
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
        'action_id': 'str',
        'action_type': 'str',
        'user_action': 'str',
        'action_config': 'str',
        'action_properties': 'list[KeyValuePairStringObject]'
    }

    attribute_map = {
        'action_id': 'actionId',
        'action_type': 'actionType',
        'user_action': 'userAction',
        'action_config': 'actionConfig',
        'action_properties': 'actionProperties'
    }

    def __init__(self, action_id=None, action_type=None, user_action=None, action_config=None, action_properties=None):  # noqa: E501
        """Pdf4meAction - a model defined in Swagger"""  # noqa: E501

        self._action_id = None
        self._action_type = None
        self._user_action = None
        self._action_config = None
        self._action_properties = None
        self.discriminator = None

        if action_id is not None:
            self.action_id = action_id
        if action_type is not None:
            self.action_type = action_type
        if user_action is not None:
            self.user_action = user_action
        if action_config is not None:
            self.action_config = action_config
        if action_properties is not None:
            self.action_properties = action_properties

    @property
    def action_id(self):
        """Gets the action_id of this Pdf4meAction.  # noqa: E501


        :return: The action_id of this Pdf4meAction.  # noqa: E501
        :rtype: str
        """
        return self._action_id

    @action_id.setter
    def action_id(self, action_id):
        """Sets the action_id of this Pdf4meAction.


        :param action_id: The action_id of this Pdf4meAction.  # noqa: E501
        :type: str
        """

        self._action_id = action_id

    @property
    def action_type(self):
        """Gets the action_type of this Pdf4meAction.  # noqa: E501


        :return: The action_type of this Pdf4meAction.  # noqa: E501
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this Pdf4meAction.


        :param action_type: The action_type of this Pdf4meAction.  # noqa: E501
        :type: str
        """
        allowed_values = ["undef", "user", "optimize", "pdfA", "ocrDocument", "ocrBusCard", "convertToPdf", "stamp", "split", "merge", "scanMrc", "createThumbnail", "createImage", "extract", "barCode"]  # noqa: E501
        if action_type not in allowed_values:
            raise ValueError(
                "Invalid value for `action_type` ({0}), must be one of {1}"  # noqa: E501
                .format(action_type, allowed_values)
            )

        self._action_type = action_type

    @property
    def user_action(self):
        """Gets the user_action of this Pdf4meAction.  # noqa: E501


        :return: The user_action of this Pdf4meAction.  # noqa: E501
        :rtype: str
        """
        return self._user_action

    @user_action.setter
    def user_action(self, user_action):
        """Sets the user_action of this Pdf4meAction.


        :param user_action: The user_action of this Pdf4meAction.  # noqa: E501
        :type: str
        """

        self._user_action = user_action

    @property
    def action_config(self):
        """Gets the action_config of this Pdf4meAction.  # noqa: E501


        :return: The action_config of this Pdf4meAction.  # noqa: E501
        :rtype: str
        """
        return self._action_config

    @action_config.setter
    def action_config(self, action_config):
        """Sets the action_config of this Pdf4meAction.


        :param action_config: The action_config of this Pdf4meAction.  # noqa: E501
        :type: str
        """

        self._action_config = action_config

    @property
    def action_properties(self):
        """Gets the action_properties of this Pdf4meAction.  # noqa: E501


        :return: The action_properties of this Pdf4meAction.  # noqa: E501
        :rtype: list[KeyValuePairStringObject]
        """
        return self._action_properties

    @action_properties.setter
    def action_properties(self, action_properties):
        """Sets the action_properties of this Pdf4meAction.


        :param action_properties: The action_properties of this Pdf4meAction.  # noqa: E501
        :type: list[KeyValuePairStringObject]
        """

        self._action_properties = action_properties

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
        if issubclass(Pdf4meAction, dict):
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
        if not isinstance(other, Pdf4meAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
