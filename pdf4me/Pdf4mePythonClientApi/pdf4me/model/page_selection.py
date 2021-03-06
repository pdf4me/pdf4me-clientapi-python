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


class PageSelection(object):
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
        'page_nrs': 'list[int]',
        'page_ids': 'list[str]',
        'page_sequence': 'str'
    }

    attribute_map = {
        'page_nrs': 'pageNrs',
        'page_ids': 'pageIds',
        'page_sequence': 'pageSequence'
    }

    def __init__(self, page_nrs=None, page_ids=None, page_sequence=None):  # noqa: E501
        """PageSelection - a model defined in Swagger"""  # noqa: E501

        self._page_nrs = None
        self._page_ids = None
        self._page_sequence = None
        self.discriminator = None

        if page_nrs is not None:
            self.page_nrs = page_nrs
        if page_ids is not None:
            self.page_ids = page_ids
        if page_sequence is not None:
            self.page_sequence = page_sequence

    @property
    def page_nrs(self):
        """Gets the page_nrs of this PageSelection.  # noqa: E501

        Give a list of PageNrs to apply the action.<br />  PageNrs overruels PageIds and PageSequence  # noqa: E501

        :return: The page_nrs of this PageSelection.  # noqa: E501
        :rtype: list[int]
        """
        return self._page_nrs

    @page_nrs.setter
    def page_nrs(self, page_nrs):
        """Sets the page_nrs of this PageSelection.

        Give a list of PageNrs to apply the action.<br />  PageNrs overruels PageIds and PageSequence  # noqa: E501

        :param page_nrs: The page_nrs of this PageSelection.  # noqa: E501
        :type: list[int]
        """

        self._page_nrs = page_nrs

    @property
    def page_ids(self):
        """Gets the page_ids of this PageSelection.  # noqa: E501

        Give a List of PagesIds to apply the action.<br />  PageIds overrules the PageSequence  # noqa: E501

        :return: The page_ids of this PageSelection.  # noqa: E501
        :rtype: list[str]
        """
        return self._page_ids

    @page_ids.setter
    def page_ids(self, page_ids):
        """Sets the page_ids of this PageSelection.

        Give a List of PagesIds to apply the action.<br />  PageIds overrules the PageSequence  # noqa: E501

        :param page_ids: The page_ids of this PageSelection.  # noqa: E501
        :type: list[str]
        """

        self._page_ids = page_ids

    @property
    def page_sequence(self):
        """Gets the page_sequence of this PageSelection.  # noqa: E501

        {default: PageSelection.All}  # noqa: E501

        :return: The page_sequence of this PageSelection.  # noqa: E501
        :rtype: str
        """
        return self._page_sequence

    @page_sequence.setter
    def page_sequence(self, page_sequence):
        """Sets the page_sequence of this PageSelection.

        {default: PageSelection.All}  # noqa: E501

        :param page_sequence: The page_sequence of this PageSelection.  # noqa: E501
        :type: str
        """
        allowed_values = ["all", "first", "last", "odd", "even", "notFirst", "notLast"]  # noqa: E501
        if page_sequence not in allowed_values:
            raise ValueError(
                "Invalid value for `page_sequence` ({0}), must be one of {1}"  # noqa: E501
                .format(page_sequence, allowed_values)
            )

        self._page_sequence = page_sequence

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
        if issubclass(PageSelection, dict):
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
        if not isinstance(other, PageSelection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
