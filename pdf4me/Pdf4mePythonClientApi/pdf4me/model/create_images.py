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
from pdf4me.model.image_action import ImageAction  # noqa: F401,E501


class CreateImages(object):
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
        'image_action': 'ImageAction',
        'job_id': 'str',
        'job_id_extern': 'str',
        'integrations': 'list[str]'
    }

    attribute_map = {
        'document': 'document',
        'image_action': 'imageAction',
        'job_id': 'jobId',
        'job_id_extern': 'jobIdExtern',
        'integrations': 'integrations'
    }

    def __init__(self, document=None, image_action=None, job_id=None, job_id_extern=None, integrations=None):  # noqa: E501
        """CreateImages - a model defined in Swagger"""  # noqa: E501

        self._document = None
        self._image_action = None
        self._job_id = None
        self._job_id_extern = None
        self._integrations = None
        self.discriminator = None

        self.document = document
        self.image_action = image_action
        if job_id is not None:
            self.job_id = job_id
        if job_id_extern is not None:
            self.job_id_extern = job_id_extern
        if integrations is not None:
            self.integrations = integrations

    @property
    def document(self):
        """Gets the document of this CreateImages.  # noqa: E501

        Stamped Document  # noqa: E501

        :return: The document of this CreateImages.  # noqa: E501
        :rtype: Document
        """
        return self._document

    @document.setter
    def document(self, document):
        """Sets the document of this CreateImages.

        Stamped Document  # noqa: E501

        :param document: The document of this CreateImages.  # noqa: E501
        :type: Document
        """
        if document is None:
            raise ValueError("Invalid value for `document`, must not be `None`")  # noqa: E501

        self._document = document

    @property
    def image_action(self):
        """Gets the image_action of this CreateImages.  # noqa: E501

        MrcAction configuration  # noqa: E501

        :return: The image_action of this CreateImages.  # noqa: E501
        :rtype: ImageAction
        """
        return self._image_action

    @image_action.setter
    def image_action(self, image_action):
        """Sets the image_action of this CreateImages.

        MrcAction configuration  # noqa: E501

        :param image_action: The image_action of this CreateImages.  # noqa: E501
        :type: ImageAction
        """
        if image_action is None:
            raise ValueError("Invalid value for `image_action`, must not be `None`")  # noqa: E501

        self._image_action = image_action

    @property
    def job_id(self):
        """Gets the job_id of this CreateImages.  # noqa: E501


        :return: The job_id of this CreateImages.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this CreateImages.


        :param job_id: The job_id of this CreateImages.  # noqa: E501
        :type: str
        """

        self._job_id = job_id

    @property
    def job_id_extern(self):
        """Gets the job_id_extern of this CreateImages.  # noqa: E501


        :return: The job_id_extern of this CreateImages.  # noqa: E501
        :rtype: str
        """
        return self._job_id_extern

    @job_id_extern.setter
    def job_id_extern(self, job_id_extern):
        """Sets the job_id_extern of this CreateImages.


        :param job_id_extern: The job_id_extern of this CreateImages.  # noqa: E501
        :type: str
        """

        self._job_id_extern = job_id_extern

    @property
    def integrations(self):
        """Gets the integrations of this CreateImages.  # noqa: E501


        :return: The integrations of this CreateImages.  # noqa: E501
        :rtype: list[str]
        """
        return self._integrations

    @integrations.setter
    def integrations(self, integrations):
        """Sets the integrations of this CreateImages.


        :param integrations: The integrations of this CreateImages.  # noqa: E501
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
        if issubclass(CreateImages, dict):
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
        if not isinstance(other, CreateImages):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
