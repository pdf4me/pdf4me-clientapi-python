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
from pdf4me.model.integration_call import IntegrationCall  # noqa: F401,E501


class ApiCallDetail(object):
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
        'job_id': 'str',
        'application_id': 'str',
        'application_name': 'str',
        'job_id_extern': 'str',
        'integration_calls': 'list[IntegrationCall]',
        'feature': 'str',
        'status': 'str',
        'ip_address': 'str',
        'api_cost': 'int',
        'call_type': 'str',
        'user_agent': 'str',
        'in_documents': 'list[Document]',
        'out_documents': 'list[Document]',
        'pages': 'int',
        'doc_size': 'int',
        'duration_ms': 'int',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'action_req_json': 'str',
        'action_res_json': 'str',
        'error_details': 'str'
    }

    attribute_map = {
        'job_id': 'jobId',
        'application_id': 'applicationId',
        'application_name': 'applicationName',
        'job_id_extern': 'jobIdExtern',
        'integration_calls': 'integrationCalls',
        'feature': 'feature',
        'status': 'status',
        'ip_address': 'ipAddress',
        'api_cost': 'apiCost',
        'call_type': 'callType',
        'user_agent': 'userAgent',
        'in_documents': 'inDocuments',
        'out_documents': 'outDocuments',
        'pages': 'pages',
        'doc_size': 'docSize',
        'duration_ms': 'durationMS',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'action_req_json': 'actionReqJson',
        'action_res_json': 'actionResJson',
        'error_details': 'errorDetails'
    }

    def __init__(self, job_id=None, application_id=None, application_name=None, job_id_extern=None, integration_calls=None, feature=None, status=None, ip_address=None, api_cost=None, call_type=None, user_agent=None, in_documents=None, out_documents=None, pages=None, doc_size=None, duration_ms=None, start_time=None, end_time=None, action_req_json=None, action_res_json=None, error_details=None):  # noqa: E501
        """ApiCallDetail - a model defined in Swagger"""  # noqa: E501

        self._job_id = None
        self._application_id = None
        self._application_name = None
        self._job_id_extern = None
        self._integration_calls = None
        self._feature = None
        self._status = None
        self._ip_address = None
        self._api_cost = None
        self._call_type = None
        self._user_agent = None
        self._in_documents = None
        self._out_documents = None
        self._pages = None
        self._doc_size = None
        self._duration_ms = None
        self._start_time = None
        self._end_time = None
        self._action_req_json = None
        self._action_res_json = None
        self._error_details = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if application_id is not None:
            self.application_id = application_id
        if application_name is not None:
            self.application_name = application_name
        if job_id_extern is not None:
            self.job_id_extern = job_id_extern
        if integration_calls is not None:
            self.integration_calls = integration_calls
        if feature is not None:
            self.feature = feature
        if status is not None:
            self.status = status
        if ip_address is not None:
            self.ip_address = ip_address
        if api_cost is not None:
            self.api_cost = api_cost
        if call_type is not None:
            self.call_type = call_type
        if user_agent is not None:
            self.user_agent = user_agent
        if in_documents is not None:
            self.in_documents = in_documents
        if out_documents is not None:
            self.out_documents = out_documents
        if pages is not None:
            self.pages = pages
        if doc_size is not None:
            self.doc_size = doc_size
        if duration_ms is not None:
            self.duration_ms = duration_ms
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if action_req_json is not None:
            self.action_req_json = action_req_json
        if action_res_json is not None:
            self.action_res_json = action_res_json
        if error_details is not None:
            self.error_details = error_details

    @property
    def job_id(self):
        """Gets the job_id of this ApiCallDetail.  # noqa: E501


        :return: The job_id of this ApiCallDetail.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ApiCallDetail.


        :param job_id: The job_id of this ApiCallDetail.  # noqa: E501
        :type: str
        """

        self._job_id = job_id

    @property
    def application_id(self):
        """Gets the application_id of this ApiCallDetail.  # noqa: E501


        :return: The application_id of this ApiCallDetail.  # noqa: E501
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this ApiCallDetail.


        :param application_id: The application_id of this ApiCallDetail.  # noqa: E501
        :type: str
        """

        self._application_id = application_id

    @property
    def application_name(self):
        """Gets the application_name of this ApiCallDetail.  # noqa: E501


        :return: The application_name of this ApiCallDetail.  # noqa: E501
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        """Sets the application_name of this ApiCallDetail.


        :param application_name: The application_name of this ApiCallDetail.  # noqa: E501
        :type: str
        """

        self._application_name = application_name

    @property
    def job_id_extern(self):
        """Gets the job_id_extern of this ApiCallDetail.  # noqa: E501


        :return: The job_id_extern of this ApiCallDetail.  # noqa: E501
        :rtype: str
        """
        return self._job_id_extern

    @job_id_extern.setter
    def job_id_extern(self, job_id_extern):
        """Sets the job_id_extern of this ApiCallDetail.


        :param job_id_extern: The job_id_extern of this ApiCallDetail.  # noqa: E501
        :type: str
        """

        self._job_id_extern = job_id_extern

    @property
    def integration_calls(self):
        """Gets the integration_calls of this ApiCallDetail.  # noqa: E501


        :return: The integration_calls of this ApiCallDetail.  # noqa: E501
        :rtype: list[IntegrationCall]
        """
        return self._integration_calls

    @integration_calls.setter
    def integration_calls(self, integration_calls):
        """Sets the integration_calls of this ApiCallDetail.


        :param integration_calls: The integration_calls of this ApiCallDetail.  # noqa: E501
        :type: list[IntegrationCall]
        """

        self._integration_calls = integration_calls

    @property
    def feature(self):
        """Gets the feature of this ApiCallDetail.  # noqa: E501


        :return: The feature of this ApiCallDetail.  # noqa: E501
        :rtype: str
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        """Sets the feature of this ApiCallDetail.


        :param feature: The feature of this ApiCallDetail.  # noqa: E501
        :type: str
        """

        self._feature = feature

    @property
    def status(self):
        """Gets the status of this ApiCallDetail.  # noqa: E501


        :return: The status of this ApiCallDetail.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ApiCallDetail.


        :param status: The status of this ApiCallDetail.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def ip_address(self):
        """Gets the ip_address of this ApiCallDetail.  # noqa: E501


        :return: The ip_address of this ApiCallDetail.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this ApiCallDetail.


        :param ip_address: The ip_address of this ApiCallDetail.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def api_cost(self):
        """Gets the api_cost of this ApiCallDetail.  # noqa: E501


        :return: The api_cost of this ApiCallDetail.  # noqa: E501
        :rtype: int
        """
        return self._api_cost

    @api_cost.setter
    def api_cost(self, api_cost):
        """Sets the api_cost of this ApiCallDetail.


        :param api_cost: The api_cost of this ApiCallDetail.  # noqa: E501
        :type: int
        """

        self._api_cost = api_cost

    @property
    def call_type(self):
        """Gets the call_type of this ApiCallDetail.  # noqa: E501


        :return: The call_type of this ApiCallDetail.  # noqa: E501
        :rtype: str
        """
        return self._call_type

    @call_type.setter
    def call_type(self, call_type):
        """Sets the call_type of this ApiCallDetail.


        :param call_type: The call_type of this ApiCallDetail.  # noqa: E501
        :type: str
        """

        self._call_type = call_type

    @property
    def user_agent(self):
        """Gets the user_agent of this ApiCallDetail.  # noqa: E501


        :return: The user_agent of this ApiCallDetail.  # noqa: E501
        :rtype: str
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        """Sets the user_agent of this ApiCallDetail.


        :param user_agent: The user_agent of this ApiCallDetail.  # noqa: E501
        :type: str
        """

        self._user_agent = user_agent

    @property
    def in_documents(self):
        """Gets the in_documents of this ApiCallDetail.  # noqa: E501


        :return: The in_documents of this ApiCallDetail.  # noqa: E501
        :rtype: list[Document]
        """
        return self._in_documents

    @in_documents.setter
    def in_documents(self, in_documents):
        """Sets the in_documents of this ApiCallDetail.


        :param in_documents: The in_documents of this ApiCallDetail.  # noqa: E501
        :type: list[Document]
        """

        self._in_documents = in_documents

    @property
    def out_documents(self):
        """Gets the out_documents of this ApiCallDetail.  # noqa: E501


        :return: The out_documents of this ApiCallDetail.  # noqa: E501
        :rtype: list[Document]
        """
        return self._out_documents

    @out_documents.setter
    def out_documents(self, out_documents):
        """Sets the out_documents of this ApiCallDetail.


        :param out_documents: The out_documents of this ApiCallDetail.  # noqa: E501
        :type: list[Document]
        """

        self._out_documents = out_documents

    @property
    def pages(self):
        """Gets the pages of this ApiCallDetail.  # noqa: E501


        :return: The pages of this ApiCallDetail.  # noqa: E501
        :rtype: int
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """Sets the pages of this ApiCallDetail.


        :param pages: The pages of this ApiCallDetail.  # noqa: E501
        :type: int
        """

        self._pages = pages

    @property
    def doc_size(self):
        """Gets the doc_size of this ApiCallDetail.  # noqa: E501


        :return: The doc_size of this ApiCallDetail.  # noqa: E501
        :rtype: int
        """
        return self._doc_size

    @doc_size.setter
    def doc_size(self, doc_size):
        """Sets the doc_size of this ApiCallDetail.


        :param doc_size: The doc_size of this ApiCallDetail.  # noqa: E501
        :type: int
        """

        self._doc_size = doc_size

    @property
    def duration_ms(self):
        """Gets the duration_ms of this ApiCallDetail.  # noqa: E501


        :return: The duration_ms of this ApiCallDetail.  # noqa: E501
        :rtype: int
        """
        return self._duration_ms

    @duration_ms.setter
    def duration_ms(self, duration_ms):
        """Sets the duration_ms of this ApiCallDetail.


        :param duration_ms: The duration_ms of this ApiCallDetail.  # noqa: E501
        :type: int
        """

        self._duration_ms = duration_ms

    @property
    def start_time(self):
        """Gets the start_time of this ApiCallDetail.  # noqa: E501


        :return: The start_time of this ApiCallDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ApiCallDetail.


        :param start_time: The start_time of this ApiCallDetail.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ApiCallDetail.  # noqa: E501


        :return: The end_time of this ApiCallDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ApiCallDetail.


        :param end_time: The end_time of this ApiCallDetail.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

    @property
    def action_req_json(self):
        """Gets the action_req_json of this ApiCallDetail.  # noqa: E501


        :return: The action_req_json of this ApiCallDetail.  # noqa: E501
        :rtype: str
        """
        return self._action_req_json

    @action_req_json.setter
    def action_req_json(self, action_req_json):
        """Sets the action_req_json of this ApiCallDetail.


        :param action_req_json: The action_req_json of this ApiCallDetail.  # noqa: E501
        :type: str
        """

        self._action_req_json = action_req_json

    @property
    def action_res_json(self):
        """Gets the action_res_json of this ApiCallDetail.  # noqa: E501


        :return: The action_res_json of this ApiCallDetail.  # noqa: E501
        :rtype: str
        """
        return self._action_res_json

    @action_res_json.setter
    def action_res_json(self, action_res_json):
        """Sets the action_res_json of this ApiCallDetail.


        :param action_res_json: The action_res_json of this ApiCallDetail.  # noqa: E501
        :type: str
        """

        self._action_res_json = action_res_json

    @property
    def error_details(self):
        """Gets the error_details of this ApiCallDetail.  # noqa: E501


        :return: The error_details of this ApiCallDetail.  # noqa: E501
        :rtype: str
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this ApiCallDetail.


        :param error_details: The error_details of this ApiCallDetail.  # noqa: E501
        :type: str
        """

        self._error_details = error_details

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
        if issubclass(ApiCallDetail, dict):
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
        if not isinstance(other, ApiCallDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other