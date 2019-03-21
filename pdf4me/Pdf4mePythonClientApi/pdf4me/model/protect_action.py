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


class ProtectAction(object):
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
        'user_password': 'str',
        'owner_password': 'str',
        'unlock': 'bool',
        'permissions': 'list[str]'
    }

    attribute_map = {
        'user_password': 'userPassword',
        'owner_password': 'ownerPassword',
        'unlock': 'unlock',
        'permissions': 'permissions'
    }

    def __init__(self, user_password=None, owner_password=None, unlock=None, permissions=None):  # noqa: E501
        """ProtectAction - a model defined in Swagger"""  # noqa: E501

        self._user_password = None
        self._owner_password = None
        self._unlock = None
        self._permissions = None
        self.discriminator = None

        if user_password is not None:
            self.user_password = user_password
        if owner_password is not None:
            self.owner_password = owner_password
        if unlock is not None:
            self.unlock = unlock
        if permissions is not None:
            self.permissions = permissions

    @property
    def user_password(self):
        """Gets the user_password of this ProtectAction.  # noqa: E501


        :return: The user_password of this ProtectAction.  # noqa: E501
        :rtype: str
        """
        return self._user_password

    @user_password.setter
    def user_password(self, user_password):
        """Sets the user_password of this ProtectAction.


        :param user_password: The user_password of this ProtectAction.  # noqa: E501
        :type: str
        """

        self._user_password = user_password

    @property
    def owner_password(self):
        """Gets the owner_password of this ProtectAction.  # noqa: E501


        :return: The owner_password of this ProtectAction.  # noqa: E501
        :rtype: str
        """
        return self._owner_password

    @owner_password.setter
    def owner_password(self, owner_password):
        """Sets the owner_password of this ProtectAction.


        :param owner_password: The owner_password of this ProtectAction.  # noqa: E501
        :type: str
        """

        self._owner_password = owner_password

    @property
    def unlock(self):
        """Gets the unlock of this ProtectAction.  # noqa: E501


        :return: The unlock of this ProtectAction.  # noqa: E501
        :rtype: bool
        """
        return self._unlock

    @unlock.setter
    def unlock(self, unlock):
        """Sets the unlock of this ProtectAction.


        :param unlock: The unlock of this ProtectAction.  # noqa: E501
        :type: bool
        """

        self._unlock = unlock

    @property
    def permissions(self):
        """Gets the permissions of this ProtectAction.  # noqa: E501


        :return: The permissions of this ProtectAction.  # noqa: E501
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this ProtectAction.


        :param permissions: The permissions of this ProtectAction.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["all", "none", "copy", "annotate", "fillForms", "supportDisabilities", "assemble", "digitalPrint", "print", "modify"]  # noqa: E501
        if not set(permissions).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `permissions` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(permissions) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._permissions = permissions

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
        if issubclass(ProtectAction, dict):
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
        if not isinstance(other, ProtectAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
