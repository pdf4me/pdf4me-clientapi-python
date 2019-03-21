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


class SigningProvider(object):
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
        'signing_provider_type': 'str',
        'identity': 'str',
        'profile': 'str',
        'secret': 'str',
        'client_id': 'str',
        'pin': 'str',
        'service_url': 'str'
    }

    attribute_map = {
        'signing_provider_type': 'signingProviderType',
        'identity': 'identity',
        'profile': 'profile',
        'secret': 'secret',
        'client_id': 'clientId',
        'pin': 'pin',
        'service_url': 'serviceUrl'
    }

    def __init__(self, signing_provider_type=None, identity=None, profile=None, secret=None, client_id=None, pin=None, service_url=None):  # noqa: E501
        """SigningProvider - a model defined in Swagger"""  # noqa: E501

        self._signing_provider_type = None
        self._identity = None
        self._profile = None
        self._secret = None
        self._client_id = None
        self._pin = None
        self._service_url = None
        self.discriminator = None

        if signing_provider_type is not None:
            self.signing_provider_type = signing_provider_type
        if identity is not None:
            self.identity = identity
        if profile is not None:
            self.profile = profile
        if secret is not None:
            self.secret = secret
        if client_id is not None:
            self.client_id = client_id
        if pin is not None:
            self.pin = pin
        if service_url is not None:
            self.service_url = service_url

    @property
    def signing_provider_type(self):
        """Gets the signing_provider_type of this SigningProvider.  # noqa: E501


        :return: The signing_provider_type of this SigningProvider.  # noqa: E501
        :rtype: str
        """
        return self._signing_provider_type

    @signing_provider_type.setter
    def signing_provider_type(self, signing_provider_type):
        """Sets the signing_provider_type of this SigningProvider.


        :param signing_provider_type: The signing_provider_type of this SigningProvider.  # noqa: E501
        :type: str
        """
        allowed_values = ["undef", "quoVadisSealsign", "swissSignSuisseID", "swisscomSigning"]  # noqa: E501
        if signing_provider_type not in allowed_values:
            raise ValueError(
                "Invalid value for `signing_provider_type` ({0}), must be one of {1}"  # noqa: E501
                .format(signing_provider_type, allowed_values)
            )

        self._signing_provider_type = signing_provider_type

    @property
    def identity(self):
        """Gets the identity of this SigningProvider.  # noqa: E501


        :return: The identity of this SigningProvider.  # noqa: E501
        :rtype: str
        """
        return self._identity

    @identity.setter
    def identity(self, identity):
        """Sets the identity of this SigningProvider.


        :param identity: The identity of this SigningProvider.  # noqa: E501
        :type: str
        """

        self._identity = identity

    @property
    def profile(self):
        """Gets the profile of this SigningProvider.  # noqa: E501


        :return: The profile of this SigningProvider.  # noqa: E501
        :rtype: str
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this SigningProvider.


        :param profile: The profile of this SigningProvider.  # noqa: E501
        :type: str
        """

        self._profile = profile

    @property
    def secret(self):
        """Gets the secret of this SigningProvider.  # noqa: E501


        :return: The secret of this SigningProvider.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this SigningProvider.


        :param secret: The secret of this SigningProvider.  # noqa: E501
        :type: str
        """

        self._secret = secret

    @property
    def client_id(self):
        """Gets the client_id of this SigningProvider.  # noqa: E501


        :return: The client_id of this SigningProvider.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this SigningProvider.


        :param client_id: The client_id of this SigningProvider.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def pin(self):
        """Gets the pin of this SigningProvider.  # noqa: E501


        :return: The pin of this SigningProvider.  # noqa: E501
        :rtype: str
        """
        return self._pin

    @pin.setter
    def pin(self, pin):
        """Sets the pin of this SigningProvider.


        :param pin: The pin of this SigningProvider.  # noqa: E501
        :type: str
        """

        self._pin = pin

    @property
    def service_url(self):
        """Gets the service_url of this SigningProvider.  # noqa: E501


        :return: The service_url of this SigningProvider.  # noqa: E501
        :rtype: str
        """
        return self._service_url

    @service_url.setter
    def service_url(self, service_url):
        """Sets the service_url of this SigningProvider.


        :param service_url: The service_url of this SigningProvider.  # noqa: E501
        :type: str
        """

        self._service_url = service_url

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
        if issubclass(SigningProvider, dict):
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
        if not isinstance(other, SigningProvider):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other