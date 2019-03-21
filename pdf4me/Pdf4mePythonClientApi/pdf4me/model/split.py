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
from pdf4me.model.split_action import SplitAction  # noqa: F401,E501


class Split(object):
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
        'split_action': 'SplitAction',
        'job_id': 'str',
        'job_id_ext': 'str',
        'integrations': 'list[str]'
    }

    attribute_map = {
        'document': 'document',
        'split_action': 'splitAction',
        'job_id': 'jobId',
        'job_id_ext': 'jobIdExt',
        'integrations': 'integrations'
    }

    def __init__(self, document=None, split_action=None, job_id=None, job_id_ext=None, integrations=None):  # noqa: E501
        """Split - a model defined in Swagger"""  # noqa: E501

        self._document = None
        self._split_action = None
        self._job_id = None
        self._job_id_ext = None
        self._integrations = None
        self.discriminator = None

        self.document = document
        self.split_action = split_action
        if job_id is not None:
            self.job_id = job_id
        if job_id_ext is not None:
            self.job_id_ext = job_id_ext
        if integrations is not None:
            self.integrations = integrations

    @property
    def document(self):
        """Gets the document of this Split.  # noqa: E501


        :return: The document of this Split.  # noqa: E501
        :rtype: Document
        """
        return self._document

    @document.setter
    def document(self, document):
        """Sets the document of this Split.


        :param document: The document of this Split.  # noqa: E501
        :type: Document
        """
        # if document is None:
        #     raise ValueError("Invalid value for `document`, must not be `None`")  # noqa: E501

        self._document = document

    @property
    def split_action(self):
        """Gets the split_action of this Split.  # noqa: E501


        :return: The split_action of this Split.  # noqa: E501
        :rtype: SplitAction
        """
        return self._split_action

    @split_action.setter
    def split_action(self, split_action):
        """Sets the split_action of this Split.


        :param split_action: The split_action of this Split.  # noqa: E501
        :type: SplitAction
        """
        # if split_action is None:
        #     raise ValueError("Invalid value for `split_action`, must not be `None`")  # noqa: E501

        self._split_action = split_action

    @property
    def job_id(self):
        """Gets the job_id of this Split.  # noqa: E501


        :return: The job_id of this Split.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this Split.


        :param job_id: The job_id of this Split.  # noqa: E501
        :type: str
        """

        self._job_id = job_id

    @property
    def job_id_ext(self):
        """Gets the job_id_ext of this Split.  # noqa: E501


        :return: The job_id_ext of this Split.  # noqa: E501
        :rtype: str
        """
        return self._job_id_ext

    @job_id_ext.setter
    def job_id_ext(self, job_id_ext):
        """Sets the job_id_ext of this Split.


        :param job_id_ext: The job_id_ext of this Split.  # noqa: E501
        :type: str
        """

        self._job_id_ext = job_id_ext

    @property
    def integrations(self):
        """Gets the integrations of this Split.  # noqa: E501


        :return: The integrations of this Split.  # noqa: E501
        :rtype: list[str]
        """
        return self._integrations

    @integrations.setter
    def integrations(self, integrations):
        """Sets the integrations of this Split.


        :param integrations: The integrations of this Split.  # noqa: E501
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
        if issubclass(Split, dict):
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
        if not isinstance(other, Split):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
