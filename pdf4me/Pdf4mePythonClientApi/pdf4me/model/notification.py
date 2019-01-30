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


class Notification(object):
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
        'get_notification': 'bool',
        'connection_id': 'str',
        'app_async_proc_type': 'str',
        'integrations': 'list[str]'
    }

    attribute_map = {
        'get_notification': 'getNotification',
        'connection_id': 'connectionId',
        'app_async_proc_type': 'appAsyncProcType',
        'integrations': 'integrations'
    }

    def __init__(self, get_notification=None, connection_id=None, app_async_proc_type=None, integrations=None):  # noqa: E501
        """Notification - a model defined in Swagger"""  # noqa: E501

        self._get_notification = None
        self._connection_id = None
        self._app_async_proc_type = None
        self._integrations = None
        self.discriminator = None

        if get_notification is not None:
            self.get_notification = get_notification
        if connection_id is not None:
            self.connection_id = connection_id
        if app_async_proc_type is not None:
            self.app_async_proc_type = app_async_proc_type
        if integrations is not None:
            self.integrations = integrations

    @property
    def get_notification(self):
        """Gets the get_notification of this Notification.  # noqa: E501

        Run execution in asynchronous way, get notified over Online WebHook  # noqa: E501

        :return: The get_notification of this Notification.  # noqa: E501
        :rtype: bool
        """
        return self._get_notification

    @get_notification.setter
    def get_notification(self, get_notification):
        """Sets the get_notification of this Notification.

        Run execution in asynchronous way, get notified over Online WebHook  # noqa: E501

        :param get_notification: The get_notification of this Notification.  # noqa: E501
        :type: bool
        """

        self._get_notification = get_notification

    @property
    def connection_id(self):
        """Gets the connection_id of this Notification.  # noqa: E501

        Will be used for Online WebHook  # noqa: E501

        :return: The connection_id of this Notification.  # noqa: E501
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """Sets the connection_id of this Notification.

        Will be used for Online WebHook  # noqa: E501

        :param connection_id: The connection_id of this Notification.  # noqa: E501
        :type: str
        """

        self._connection_id = connection_id

    @property
    def app_async_proc_type(self):
        """Gets the app_async_proc_type of this Notification.  # noqa: E501


        :return: The app_async_proc_type of this Notification.  # noqa: E501
        :rtype: str
        """
        return self._app_async_proc_type

    @app_async_proc_type.setter
    def app_async_proc_type(self, app_async_proc_type):
        """Sets the app_async_proc_type of this Notification.


        :param app_async_proc_type: The app_async_proc_type of this Notification.  # noqa: E501
        :type: str
        """

        self._app_async_proc_type = app_async_proc_type

    @property
    def integrations(self):
        """Gets the integrations of this Notification.  # noqa: E501


        :return: The integrations of this Notification.  # noqa: E501
        :rtype: list[str]
        """
        return self._integrations

    @integrations.setter
    def integrations(self, integrations):
        """Sets the integrations of this Notification.


        :param integrations: The integrations of this Notification.  # noqa: E501
        :type: list[str]
        """

        self._integrations = integrations

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
        if issubclass(Notification, dict):
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
        if not isinstance(other, Notification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
