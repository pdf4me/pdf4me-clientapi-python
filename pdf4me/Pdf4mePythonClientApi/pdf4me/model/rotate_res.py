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


class RotateRes(object):
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
        'document': 'Document',
        'in_doc_metadata': 'DocMetadata',
        'trace_id': 'str',
        'job_id': 'str',
        'subscription_usage': 'SubscriptionUsage'
    }

    attribute_map = {
        'document': 'document',
        'in_doc_metadata': 'inDocMetadata',
        'trace_id': 'traceId',
        'job_id': 'jobId',
        'subscription_usage': 'subscriptionUsage'
    }

    def __init__(self, document=None, in_doc_metadata=None, trace_id=None, job_id=None, subscription_usage=None):  # noqa: E501
        """RotateRes - a model defined in Swagger"""  # noqa: E501

        self._document = None
        self._in_doc_metadata = None
        self._trace_id = None
        self._job_id = None
        self._subscription_usage = None
        self.discriminator = None

        if document is not None:
            self.document = document
        if in_doc_metadata is not None:
            self.in_doc_metadata = in_doc_metadata
        if trace_id is not None:
            self.trace_id = trace_id
        if job_id is not None:
            self.job_id = job_id
        if subscription_usage is not None:
            self.subscription_usage = subscription_usage

    @property
    def document(self):
        """Gets the document of this RotateRes.  # noqa: E501


        :return: The document of this RotateRes.  # noqa: E501
        :rtype: Document
        """
        return self._document

    @document.setter
    def document(self, document):
        """Sets the document of this RotateRes.


        :param document: The document of this RotateRes.  # noqa: E501
        :type: Document
        """

        self._document = document

    @property
    def in_doc_metadata(self):
        """Gets the in_doc_metadata of this RotateRes.  # noqa: E501


        :return: The in_doc_metadata of this RotateRes.  # noqa: E501
        :rtype: DocMetadata
        """
        return self._in_doc_metadata

    @in_doc_metadata.setter
    def in_doc_metadata(self, in_doc_metadata):
        """Sets the in_doc_metadata of this RotateRes.


        :param in_doc_metadata: The in_doc_metadata of this RotateRes.  # noqa: E501
        :type: DocMetadata
        """

        self._in_doc_metadata = in_doc_metadata

    @property
    def trace_id(self):
        """Gets the trace_id of this RotateRes.  # noqa: E501


        :return: The trace_id of this RotateRes.  # noqa: E501
        :rtype: str
        """
        return self._trace_id

    @trace_id.setter
    def trace_id(self, trace_id):
        """Sets the trace_id of this RotateRes.


        :param trace_id: The trace_id of this RotateRes.  # noqa: E501
        :type: str
        """

        self._trace_id = trace_id

    @property
    def job_id(self):
        """Gets the job_id of this RotateRes.  # noqa: E501


        :return: The job_id of this RotateRes.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this RotateRes.


        :param job_id: The job_id of this RotateRes.  # noqa: E501
        :type: str
        """

        self._job_id = job_id

    @property
    def subscription_usage(self):
        """Gets the subscription_usage of this RotateRes.  # noqa: E501


        :return: The subscription_usage of this RotateRes.  # noqa: E501
        :rtype: SubscriptionUsage
        """
        return self._subscription_usage

    @subscription_usage.setter
    def subscription_usage(self, subscription_usage):
        """Sets the subscription_usage of this RotateRes.


        :param subscription_usage: The subscription_usage of this RotateRes.  # noqa: E501
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
        if issubclass(RotateRes, dict):
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
        if not isinstance(other, RotateRes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
