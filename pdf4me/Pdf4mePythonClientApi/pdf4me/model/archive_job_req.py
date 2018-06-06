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

from pdf4me.model.archive_config import ArchiveConfig  # noqa: F401,E501
from pdf4me.model.execution_trigger import ExecutionTrigger  # noqa: F401,E501
from pdf4me.model.storage_folder import StorageFolder  # noqa: F401,E501


class ArchiveJobReq(object):
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
        'source_folder': 'StorageFolder',
        'execution_trigger': 'ExecutionTrigger',
        'archive_config': 'ArchiveConfig',
        'target_folder': 'StorageFolder'
    }

    attribute_map = {
        'job_id': 'jobId',
        'source_folder': 'sourceFolder',
        'execution_trigger': 'executionTrigger',
        'archive_config': 'archiveConfig',
        'target_folder': 'targetFolder'
    }

    def __init__(self, job_id=None, source_folder=None, execution_trigger=None, archive_config=None, target_folder=None):  # noqa: E501
        """ArchiveJobReq - a model defined in Swagger"""  # noqa: E501

        self._job_id = None
        self._source_folder = None
        self._execution_trigger = None
        self._archive_config = None
        self._target_folder = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        self.source_folder = source_folder
        self.execution_trigger = execution_trigger
        self.archive_config = archive_config
        self.target_folder = target_folder

    @property
    def job_id(self):
        """Gets the job_id of this ArchiveJobReq.  # noqa: E501


        :return: The job_id of this ArchiveJobReq.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ArchiveJobReq.


        :param job_id: The job_id of this ArchiveJobReq.  # noqa: E501
        :type: str
        """

        self._job_id = job_id

    @property
    def source_folder(self):
        """Gets the source_folder of this ArchiveJobReq.  # noqa: E501


        :return: The source_folder of this ArchiveJobReq.  # noqa: E501
        :rtype: StorageFolder
        """
        return self._source_folder

    @source_folder.setter
    def source_folder(self, source_folder):
        """Sets the source_folder of this ArchiveJobReq.


        :param source_folder: The source_folder of this ArchiveJobReq.  # noqa: E501
        :type: StorageFolder
        """
        if source_folder is None:
            raise ValueError("Invalid value for `source_folder`, must not be `None`")  # noqa: E501

        self._source_folder = source_folder

    @property
    def execution_trigger(self):
        """Gets the execution_trigger of this ArchiveJobReq.  # noqa: E501


        :return: The execution_trigger of this ArchiveJobReq.  # noqa: E501
        :rtype: ExecutionTrigger
        """
        return self._execution_trigger

    @execution_trigger.setter
    def execution_trigger(self, execution_trigger):
        """Sets the execution_trigger of this ArchiveJobReq.


        :param execution_trigger: The execution_trigger of this ArchiveJobReq.  # noqa: E501
        :type: ExecutionTrigger
        """
        if execution_trigger is None:
            raise ValueError("Invalid value for `execution_trigger`, must not be `None`")  # noqa: E501

        self._execution_trigger = execution_trigger

    @property
    def archive_config(self):
        """Gets the archive_config of this ArchiveJobReq.  # noqa: E501


        :return: The archive_config of this ArchiveJobReq.  # noqa: E501
        :rtype: ArchiveConfig
        """
        return self._archive_config

    @archive_config.setter
    def archive_config(self, archive_config):
        """Sets the archive_config of this ArchiveJobReq.


        :param archive_config: The archive_config of this ArchiveJobReq.  # noqa: E501
        :type: ArchiveConfig
        """
        if archive_config is None:
            raise ValueError("Invalid value for `archive_config`, must not be `None`")  # noqa: E501

        self._archive_config = archive_config

    @property
    def target_folder(self):
        """Gets the target_folder of this ArchiveJobReq.  # noqa: E501


        :return: The target_folder of this ArchiveJobReq.  # noqa: E501
        :rtype: StorageFolder
        """
        return self._target_folder

    @target_folder.setter
    def target_folder(self, target_folder):
        """Sets the target_folder of this ArchiveJobReq.


        :param target_folder: The target_folder of this ArchiveJobReq.  # noqa: E501
        :type: StorageFolder
        """
        if target_folder is None:
            raise ValueError("Invalid value for `target_folder`, must not be `None`")  # noqa: E501

        self._target_folder = target_folder

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
        if not isinstance(other, ArchiveJobReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
