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


class IntegrationCall(object):
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
        'integration_name': 'str',
        'integration_type': 'str',
        'integration_id': 'str',
        'status': 'str',
        'error_message': 'str',
        'retries': 'int',
        'last_call_time': 'datetime'
    }

    attribute_map = {
        'integration_name': 'integrationName',
        'integration_type': 'integrationType',
        'integration_id': 'integrationId',
        'status': 'status',
        'error_message': 'errorMessage',
        'retries': 'retries',
        'last_call_time': 'lastCallTime'
    }

    def __init__(self, integration_name=None, integration_type=None, integration_id=None, status=None, error_message=None, retries=None, last_call_time=None):  # noqa: E501
        """IntegrationCall - a model defined in Swagger"""  # noqa: E501

        self._integration_name = None
        self._integration_type = None
        self._integration_id = None
        self._status = None
        self._error_message = None
        self._retries = None
        self._last_call_time = None
        self.discriminator = None

        if integration_name is not None:
            self.integration_name = integration_name
        if integration_type is not None:
            self.integration_type = integration_type
        if integration_id is not None:
            self.integration_id = integration_id
        if status is not None:
            self.status = status
        if error_message is not None:
            self.error_message = error_message
        if retries is not None:
            self.retries = retries
        if last_call_time is not None:
            self.last_call_time = last_call_time

    @property
    def integration_name(self):
        """Gets the integration_name of this IntegrationCall.  # noqa: E501


        :return: The integration_name of this IntegrationCall.  # noqa: E501
        :rtype: str
        """
        return self._integration_name

    @integration_name.setter
    def integration_name(self, integration_name):
        """Sets the integration_name of this IntegrationCall.


        :param integration_name: The integration_name of this IntegrationCall.  # noqa: E501
        :type: str
        """

        self._integration_name = integration_name

    @property
    def integration_type(self):
        """Gets the integration_type of this IntegrationCall.  # noqa: E501


        :return: The integration_type of this IntegrationCall.  # noqa: E501
        :rtype: str
        """
        return self._integration_type

    @integration_type.setter
    def integration_type(self, integration_type):
        """Sets the integration_type of this IntegrationCall.


        :param integration_type: The integration_type of this IntegrationCall.  # noqa: E501
        :type: str
        """

        self._integration_type = integration_type

    @property
    def integration_id(self):
        """Gets the integration_id of this IntegrationCall.  # noqa: E501


        :return: The integration_id of this IntegrationCall.  # noqa: E501
        :rtype: str
        """
        return self._integration_id

    @integration_id.setter
    def integration_id(self, integration_id):
        """Sets the integration_id of this IntegrationCall.


        :param integration_id: The integration_id of this IntegrationCall.  # noqa: E501
        :type: str
        """

        self._integration_id = integration_id

    @property
    def status(self):
        """Gets the status of this IntegrationCall.  # noqa: E501


        :return: The status of this IntegrationCall.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IntegrationCall.


        :param status: The status of this IntegrationCall.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def error_message(self):
        """Gets the error_message of this IntegrationCall.  # noqa: E501


        :return: The error_message of this IntegrationCall.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this IntegrationCall.


        :param error_message: The error_message of this IntegrationCall.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def retries(self):
        """Gets the retries of this IntegrationCall.  # noqa: E501


        :return: The retries of this IntegrationCall.  # noqa: E501
        :rtype: int
        """
        return self._retries

    @retries.setter
    def retries(self, retries):
        """Sets the retries of this IntegrationCall.


        :param retries: The retries of this IntegrationCall.  # noqa: E501
        :type: int
        """

        self._retries = retries

    @property
    def last_call_time(self):
        """Gets the last_call_time of this IntegrationCall.  # noqa: E501


        :return: The last_call_time of this IntegrationCall.  # noqa: E501
        :rtype: datetime
        """
        return self._last_call_time

    @last_call_time.setter
    def last_call_time(self, last_call_time):
        """Sets the last_call_time of this IntegrationCall.


        :param last_call_time: The last_call_time of this IntegrationCall.  # noqa: E501
        :type: datetime
        """

        self._last_call_time = last_call_time

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
        if issubclass(IntegrationCall, dict):
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
        if not isinstance(other, IntegrationCall):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
