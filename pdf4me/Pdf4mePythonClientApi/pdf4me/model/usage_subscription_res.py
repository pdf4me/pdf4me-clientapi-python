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


class UsageSubscriptionRes(object):
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
        'usage_subscription_list': 'list[UsageSubscription]',
        'trace_id': 'str',
        'job_id': 'str',
        'subscription_usage': 'SubscriptionUsage'
    }

    attribute_map = {
        'usage_subscription_list': 'usageSubscriptionList',
        'trace_id': 'traceId',
        'job_id': 'jobId',
        'subscription_usage': 'subscriptionUsage'
    }

    def __init__(self, usage_subscription_list=None, trace_id=None, job_id=None, subscription_usage=None):  # noqa: E501
        """UsageSubscriptionRes - a model defined in Swagger"""  # noqa: E501

        self._usage_subscription_list = None
        self._trace_id = None
        self._job_id = None
        self._subscription_usage = None
        self.discriminator = None

        if usage_subscription_list is not None:
            self.usage_subscription_list = usage_subscription_list
        if trace_id is not None:
            self.trace_id = trace_id
        if job_id is not None:
            self.job_id = job_id
        if subscription_usage is not None:
            self.subscription_usage = subscription_usage

    @property
    def usage_subscription_list(self):
        """Gets the usage_subscription_list of this UsageSubscriptionRes.  # noqa: E501


        :return: The usage_subscription_list of this UsageSubscriptionRes.  # noqa: E501
        :rtype: list[UsageSubscription]
        """
        return self._usage_subscription_list

    @usage_subscription_list.setter
    def usage_subscription_list(self, usage_subscription_list):
        """Sets the usage_subscription_list of this UsageSubscriptionRes.


        :param usage_subscription_list: The usage_subscription_list of this UsageSubscriptionRes.  # noqa: E501
        :type: list[UsageSubscription]
        """

        self._usage_subscription_list = usage_subscription_list

    @property
    def trace_id(self):
        """Gets the trace_id of this UsageSubscriptionRes.  # noqa: E501


        :return: The trace_id of this UsageSubscriptionRes.  # noqa: E501
        :rtype: str
        """
        return self._trace_id

    @trace_id.setter
    def trace_id(self, trace_id):
        """Sets the trace_id of this UsageSubscriptionRes.


        :param trace_id: The trace_id of this UsageSubscriptionRes.  # noqa: E501
        :type: str
        """

        self._trace_id = trace_id

    @property
    def job_id(self):
        """Gets the job_id of this UsageSubscriptionRes.  # noqa: E501


        :return: The job_id of this UsageSubscriptionRes.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this UsageSubscriptionRes.


        :param job_id: The job_id of this UsageSubscriptionRes.  # noqa: E501
        :type: str
        """

        self._job_id = job_id

    @property
    def subscription_usage(self):
        """Gets the subscription_usage of this UsageSubscriptionRes.  # noqa: E501


        :return: The subscription_usage of this UsageSubscriptionRes.  # noqa: E501
        :rtype: SubscriptionUsage
        """
        return self._subscription_usage

    @subscription_usage.setter
    def subscription_usage(self, subscription_usage):
        """Sets the subscription_usage of this UsageSubscriptionRes.


        :param subscription_usage: The subscription_usage of this UsageSubscriptionRes.  # noqa: E501
        :type: SubscriptionUsage
        """

        self._subscription_usage = subscription_usage

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
        if issubclass(UsageSubscriptionRes, dict):
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
        if not isinstance(other, UsageSubscriptionRes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
