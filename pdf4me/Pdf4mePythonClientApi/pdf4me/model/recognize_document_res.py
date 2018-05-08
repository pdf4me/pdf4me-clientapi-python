# coding: utf-8

"""
    DmsApi

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from pdf4me.model.document import Document  # noqa: F401,E501


class RecognizeDocumentRes(object):
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
        'structured_data_json': 'str'
    }

    attribute_map = {
        'document': 'document',
        'structured_data_json': 'structuredDataJson'
    }

    def __init__(self, document=None, structured_data_json=None):  # noqa: E501
        """RecognizeDocumentRes - a model defined in Swagger"""  # noqa: E501

        self._document = None
        self._structured_data_json = None
        self.discriminator = None

        if document is not None:
            self.document = document
        if structured_data_json is not None:
            self.structured_data_json = structured_data_json

    @property
    def document(self):
        """Gets the document of this RecognizeDocumentRes.  # noqa: E501

        Stamped Document  # noqa: E501

        :return: The document of this RecognizeDocumentRes.  # noqa: E501
        :rtype: Document
        """
        return self._document

    @document.setter
    def document(self, document):
        """Sets the document of this RecognizeDocumentRes.

        Stamped Document  # noqa: E501

        :param document: The document of this RecognizeDocumentRes.  # noqa: E501
        :type: Document
        """

        self._document = document

    @property
    def structured_data_json(self):
        """Gets the structured_data_json of this RecognizeDocumentRes.  # noqa: E501


        :return: The structured_data_json of this RecognizeDocumentRes.  # noqa: E501
        :rtype: str
        """
        return self._structured_data_json

    @structured_data_json.setter
    def structured_data_json(self, structured_data_json):
        """Sets the structured_data_json of this RecognizeDocumentRes.


        :param structured_data_json: The structured_data_json of this RecognizeDocumentRes.  # noqa: E501
        :type: str
        """

        self._structured_data_json = structured_data_json

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RecognizeDocumentRes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other