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


class PdfValidationEvent(object):
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
        'page_nr': 'int',
        'object_nr': 'int',
        'error_code': 'str',
        'error_message': 'str'
    }

    attribute_map = {
        'page_nr': 'pageNr',
        'object_nr': 'objectNr',
        'error_code': 'errorCode',
        'error_message': 'errorMessage'
    }

    def __init__(self, page_nr=None, object_nr=None, error_code=None, error_message=None):  # noqa: E501
        """PdfValidationEvent - a model defined in Swagger"""  # noqa: E501

        self._page_nr = None
        self._object_nr = None
        self._error_code = None
        self._error_message = None
        self.discriminator = None

        if page_nr is not None:
            self.page_nr = page_nr
        if object_nr is not None:
            self.object_nr = object_nr
        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message

    @property
    def page_nr(self):
        """Gets the page_nr of this PdfValidationEvent.  # noqa: E501


        :return: The page_nr of this PdfValidationEvent.  # noqa: E501
        :rtype: int
        """
        return self._page_nr

    @page_nr.setter
    def page_nr(self, page_nr):
        """Sets the page_nr of this PdfValidationEvent.


        :param page_nr: The page_nr of this PdfValidationEvent.  # noqa: E501
        :type: int
        """

        self._page_nr = page_nr

    @property
    def object_nr(self):
        """Gets the object_nr of this PdfValidationEvent.  # noqa: E501


        :return: The object_nr of this PdfValidationEvent.  # noqa: E501
        :rtype: int
        """
        return self._object_nr

    @object_nr.setter
    def object_nr(self, object_nr):
        """Sets the object_nr of this PdfValidationEvent.


        :param object_nr: The object_nr of this PdfValidationEvent.  # noqa: E501
        :type: int
        """

        self._object_nr = object_nr

    @property
    def error_code(self):
        """Gets the error_code of this PdfValidationEvent.  # noqa: E501


        :return: The error_code of this PdfValidationEvent.  # noqa: E501
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this PdfValidationEvent.


        :param error_code: The error_code of this PdfValidationEvent.  # noqa: E501
        :type: str
        """

        self._error_code = error_code

    @property
    def error_message(self):
        """Gets the error_message of this PdfValidationEvent.  # noqa: E501


        :return: The error_message of this PdfValidationEvent.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this PdfValidationEvent.


        :param error_message: The error_message of this PdfValidationEvent.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

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
        if issubclass(PdfValidationEvent, dict):
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
        if not isinstance(other, PdfValidationEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other