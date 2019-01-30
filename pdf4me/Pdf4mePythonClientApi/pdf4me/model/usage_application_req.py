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


class UsageApplicationReq(object):
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
        'subscription_id': 'str',
        'application_id': 'str',
        'date_from': 'datetime',
        'trace_id': 'str',
        'job_id': 'str'
    }

    attribute_map = {
        'subscription_id': 'subscriptionId',
        'application_id': 'applicationId',
        'date_from': 'dateFrom',
        'trace_id': 'traceId',
        'job_id': 'jobId'
    }

    def __init__(self, subscription_id=None, application_id=None, date_from=None, trace_id=None, job_id=None):  # noqa: E501
        """UsageApplicationReq - a model defined in Swagger"""  # noqa: E501

        self._subscription_id = None
        self._application_id = None
        self._date_from = None
        self._trace_id = None
        self._job_id = None
        self.discriminator = None

        if subscription_id is not None:
            self.subscription_id = subscription_id
        if application_id is not None:
            self.application_id = application_id
        if date_from is not None:
            self.date_from = date_from
        if trace_id is not None:
            self.trace_id = trace_id
        if job_id is not None:
            self.job_id = job_id

    @property
    def subscription_id(self):
        """Gets the subscription_id of this UsageApplicationReq.  # noqa: E501


        :return: The subscription_id of this UsageApplicationReq.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this UsageApplicationReq.


        :param subscription_id: The subscription_id of this UsageApplicationReq.  # noqa: E501
        :type: str
        """

        self._subscription_id = subscription_id

    @property
    def application_id(self):
        """Gets the application_id of this UsageApplicationReq.  # noqa: E501


        :return: The application_id of this UsageApplicationReq.  # noqa: E501
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this UsageApplicationReq.


        :param application_id: The application_id of this UsageApplicationReq.  # noqa: E501
        :type: str
        """

        self._application_id = application_id

    @property
    def date_from(self):
        """Gets the date_from of this UsageApplicationReq.  # noqa: E501


        :return: The date_from of this UsageApplicationReq.  # noqa: E501
        :rtype: datetime
        """
        return self._date_from

    @date_from.setter
    def date_from(self, date_from):
        """Sets the date_from of this UsageApplicationReq.


        :param date_from: The date_from of this UsageApplicationReq.  # noqa: E501
        :type: datetime
        """

        self._date_from = date_from

    @property
    def trace_id(self):
        """Gets the trace_id of this UsageApplicationReq.  # noqa: E501


        :return: The trace_id of this UsageApplicationReq.  # noqa: E501
        :rtype: str
        """
        return self._trace_id

    @trace_id.setter
    def trace_id(self, trace_id):
        """Sets the trace_id of this UsageApplicationReq.


        :param trace_id: The trace_id of this UsageApplicationReq.  # noqa: E501
        :type: str
        """

        self._trace_id = trace_id

    @property
    def job_id(self):
        """Gets the job_id of this UsageApplicationReq.  # noqa: E501


        :return: The job_id of this UsageApplicationReq.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this UsageApplicationReq.


        :param job_id: The job_id of this UsageApplicationReq.  # noqa: E501
        :type: str
        """

        self._job_id = job_id

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
        if issubclass(UsageApplicationReq, dict):
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
        if not isinstance(other, UsageApplicationReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
