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

from pdf4me.model.document import Document  # noqa: F401,E501
from pdf4me.model.merge_action import MergeAction  # noqa: F401,E501


class Merge(object):
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
        'documents': 'list[Document]',
        'merge_action': 'MergeAction',
        'job_id': 'str',
        'job_id_ext': 'str',
        'integrations': 'list[str]'
    }

    attribute_map = {
        'documents': 'documents',
        'merge_action': 'mergeAction',
        'job_id': 'jobId',
        'job_id_ext': 'jobIdExt',
        'integrations': 'integrations'
    }

    def __init__(self, documents=None, merge_action=None, job_id=None, job_id_ext=None, integrations=None):  # noqa: E501
        """Merge - a model defined in Swagger"""  # noqa: E501

        self._documents = None
        self._merge_action = None
        self._job_id = None
        self._job_id_ext = None
        self._integrations = None
        self.discriminator = None

        self.documents = documents
        if merge_action is not None:
            self.merge_action = merge_action
        if job_id is not None:
            self.job_id = job_id
        if job_id_ext is not None:
            self.job_id_ext = job_id_ext
        if integrations is not None:
            self.integrations = integrations

    @property
    def documents(self):
        """Gets the documents of this Merge.  # noqa: E501


        :return: The documents of this Merge.  # noqa: E501
        :rtype: list[Document]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """Sets the documents of this Merge.


        :param documents: The documents of this Merge.  # noqa: E501
        :type: list[Document]
        """
        # if documents is None:
        #     raise ValueError("Invalid value for `documents`, must not be `None`")  # noqa: E501

        self._documents = documents

    @property
    def merge_action(self):
        """Gets the merge_action of this Merge.  # noqa: E501


        :return: The merge_action of this Merge.  # noqa: E501
        :rtype: MergeAction
        """
        return self._merge_action

    @merge_action.setter
    def merge_action(self, merge_action):
        """Sets the merge_action of this Merge.


        :param merge_action: The merge_action of this Merge.  # noqa: E501
        :type: MergeAction
        """

        self._merge_action = merge_action

    @property
    def job_id(self):
        """Gets the job_id of this Merge.  # noqa: E501


        :return: The job_id of this Merge.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this Merge.


        :param job_id: The job_id of this Merge.  # noqa: E501
        :type: str
        """

        self._job_id = job_id

    @property
    def job_id_ext(self):
        """Gets the job_id_ext of this Merge.  # noqa: E501


        :return: The job_id_ext of this Merge.  # noqa: E501
        :rtype: str
        """
        return self._job_id_ext

    @job_id_ext.setter
    def job_id_ext(self, job_id_ext):
        """Sets the job_id_ext of this Merge.


        :param job_id_ext: The job_id_ext of this Merge.  # noqa: E501
        :type: str
        """

        self._job_id_ext = job_id_ext

    @property
    def integrations(self):
        """Gets the integrations of this Merge.  # noqa: E501


        :return: The integrations of this Merge.  # noqa: E501
        :rtype: list[str]
        """
        return self._integrations

    @integrations.setter
    def integrations(self, integrations):
        """Sets the integrations of this Merge.


        :param integrations: The integrations of this Merge.  # noqa: E501
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
        if issubclass(Merge, dict):
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
        if not isinstance(other, Merge):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
