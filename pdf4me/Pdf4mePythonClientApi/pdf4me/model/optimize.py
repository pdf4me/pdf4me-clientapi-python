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
from pdf4me.model.optimize_action import OptimizeAction  # noqa: F401,E501


class Optimize(object):
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
        'optimize_action': 'OptimizeAction',
        'job_id': 'str',
        'job_id_extern': 'str',
        'integrations': 'list[str]'
    }

    attribute_map = {
        'document': 'document',
        'optimize_action': 'optimizeAction',
        'job_id': 'jobId',
        'job_id_extern': 'jobIdExtern',
        'integrations': 'integrations'
    }

    def __init__(self, document=None, optimize_action=None, job_id=None, job_id_extern=None, integrations=None):  # noqa: E501
        """Optimize - a model defined in Swagger"""  # noqa: E501

        self._document = None
        self._optimize_action = None
        self._job_id = None
        self._job_id_extern = None
        self._integrations = None
        self.discriminator = None

        self.document = document
        if optimize_action is not None:
            self.optimize_action = optimize_action
        if job_id is not None:
            self.job_id = job_id
        if job_id_extern is not None:
            self.job_id_extern = job_id_extern
        if integrations is not None:
            self.integrations = integrations

    @property
    def document(self):
        """Gets the document of this Optimize.  # noqa: E501

        Give the document to change or use JobId/DocumentId to reference an uploaded document.  # noqa: E501

        :return: The document of this Optimize.  # noqa: E501
        :rtype: Document
        """
        return self._document

    @document.setter
    def document(self, document):
        """Sets the document of this Optimize.

        Give the document to change or use JobId/DocumentId to reference an uploaded document.  # noqa: E501

        :param document: The document of this Optimize.  # noqa: E501
        :type: Document
        """
        if document is None:
            raise ValueError("Invalid value for `document`, must not be `None`")  # noqa: E501

        self._document = document

    @property
    def optimize_action(self):
        """Gets the optimize_action of this Optimize.  # noqa: E501

        Give an image stamp  # noqa: E501

        :return: The optimize_action of this Optimize.  # noqa: E501
        :rtype: OptimizeAction
        """
        return self._optimize_action

    @optimize_action.setter
    def optimize_action(self, optimize_action):
        """Sets the optimize_action of this Optimize.

        Give an image stamp  # noqa: E501

        :param optimize_action: The optimize_action of this Optimize.  # noqa: E501
        :type: OptimizeAction
        """

        self._optimize_action = optimize_action

    @property
    def job_id(self):
        """Gets the job_id of this Optimize.  # noqa: E501


        :return: The job_id of this Optimize.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this Optimize.


        :param job_id: The job_id of this Optimize.  # noqa: E501
        :type: str
        """

        self._job_id = job_id

    @property
    def job_id_extern(self):
        """Gets the job_id_extern of this Optimize.  # noqa: E501


        :return: The job_id_extern of this Optimize.  # noqa: E501
        :rtype: str
        """
        return self._job_id_extern

    @job_id_extern.setter
    def job_id_extern(self, job_id_extern):
        """Sets the job_id_extern of this Optimize.


        :param job_id_extern: The job_id_extern of this Optimize.  # noqa: E501
        :type: str
        """

        self._job_id_extern = job_id_extern

    @property
    def integrations(self):
        """Gets the integrations of this Optimize.  # noqa: E501


        :return: The integrations of this Optimize.  # noqa: E501
        :rtype: list[str]
        """
        return self._integrations

    @integrations.setter
    def integrations(self, integrations):
        """Sets the integrations of this Optimize.


        :param integrations: The integrations of this Optimize.  # noqa: E501
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
        if issubclass(Optimize, dict):
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
        if not isinstance(other, Optimize):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
