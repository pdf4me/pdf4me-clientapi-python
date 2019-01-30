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

from pdf4me.model.convert_to_pdf_action import ConvertToPdfAction  # noqa: F401,E501
from pdf4me.model.document import Document  # noqa: F401,E501


class ConvertToPdf(object):
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
        'convert_to_pdf_action': 'ConvertToPdfAction',
        'job_id': 'str',
        'job_id_extern': 'str',
        'integrations': 'list[str]'
    }

    attribute_map = {
        'document': 'document',
        'convert_to_pdf_action': 'convertToPdfAction',
        'job_id': 'jobId',
        'job_id_extern': 'jobIdExtern',
        'integrations': 'integrations'
    }

    def __init__(self, document=None, convert_to_pdf_action=None, job_id=None, job_id_extern=None, integrations=None):  # noqa: E501
        """ConvertToPdf - a model defined in Swagger"""  # noqa: E501

        self._document = None
        self._convert_to_pdf_action = None
        self._job_id = None
        self._job_id_extern = None
        self._integrations = None
        self.discriminator = None

        self.document = document
        if convert_to_pdf_action is not None:
            self.convert_to_pdf_action = convert_to_pdf_action
        if job_id is not None:
            self.job_id = job_id
        if job_id_extern is not None:
            self.job_id_extern = job_id_extern
        if integrations is not None:
            self.integrations = integrations

    @property
    def document(self):
        """Gets the document of this ConvertToPdf.  # noqa: E501

        Document containing the data  # noqa: E501

        :return: The document of this ConvertToPdf.  # noqa: E501
        :rtype: Document
        """
        return self._document

    @document.setter
    def document(self, document):
        """Sets the document of this ConvertToPdf.

        Document containing the data  # noqa: E501

        :param document: The document of this ConvertToPdf.  # noqa: E501
        :type: Document
        """
        # if document is None:
        #     raise ValueError("Invalid value for `document`, must not be `None`")  # noqa: E501

        self._document = document

    @property
    def convert_to_pdf_action(self):
        """Gets the convert_to_pdf_action of this ConvertToPdf.  # noqa: E501

        Conversion configuration  # noqa: E501

        :return: The convert_to_pdf_action of this ConvertToPdf.  # noqa: E501
        :rtype: ConvertToPdfAction
        """
        return self._convert_to_pdf_action

    @convert_to_pdf_action.setter
    def convert_to_pdf_action(self, convert_to_pdf_action):
        """Sets the convert_to_pdf_action of this ConvertToPdf.

        Conversion configuration  # noqa: E501

        :param convert_to_pdf_action: The convert_to_pdf_action of this ConvertToPdf.  # noqa: E501
        :type: ConvertToPdfAction
        """

        self._convert_to_pdf_action = convert_to_pdf_action

    @property
    def job_id(self):
        """Gets the job_id of this ConvertToPdf.  # noqa: E501


        :return: The job_id of this ConvertToPdf.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ConvertToPdf.


        :param job_id: The job_id of this ConvertToPdf.  # noqa: E501
        :type: str
        """

        self._job_id = job_id

    @property
    def job_id_extern(self):
        """Gets the job_id_extern of this ConvertToPdf.  # noqa: E501


        :return: The job_id_extern of this ConvertToPdf.  # noqa: E501
        :rtype: str
        """
        return self._job_id_extern

    @job_id_extern.setter
    def job_id_extern(self, job_id_extern):
        """Sets the job_id_extern of this ConvertToPdf.


        :param job_id_extern: The job_id_extern of this ConvertToPdf.  # noqa: E501
        :type: str
        """

        self._job_id_extern = job_id_extern

    @property
    def integrations(self):
        """Gets the integrations of this ConvertToPdf.  # noqa: E501


        :return: The integrations of this ConvertToPdf.  # noqa: E501
        :rtype: list[str]
        """
        return self._integrations

    @integrations.setter
    def integrations(self, integrations):
        """Sets the integrations of this ConvertToPdf.


        :param integrations: The integrations of this ConvertToPdf.  # noqa: E501
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
        if issubclass(ConvertToPdf, dict):
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
        if not isinstance(other, ConvertToPdf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
