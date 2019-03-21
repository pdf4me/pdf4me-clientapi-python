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

from pdf4me.model.doc_action import DocAction  # noqa: F401,E501
from pdf4me.model.doc_log import DocLog  # noqa: F401,E501
from pdf4me.model.doc_metadata import DocMetadata  # noqa: F401,E501
from pdf4me.model.page import Page  # noqa: F401,E501


class Pdf4meDocument(object):
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
        'document_type': 'str',
        'blob_ref': 'str',
        'job_id': 'str',
        'ref_document_id': 'str',
        'ref_doc_action': 'DocAction',
        'document_id': 'str',
        'user_id': 'str',
        'name': 'str',
        'file_name': 'str',
        'file_extension': 'str',
        'ratio': 'float',
        'doc_status': 'str',
        'in_execution': 'bool',
        'order': 'int',
        'show_doc': 'bool',
        'doc_data': 'str',
        'thumbnail': 'str',
        'pages': 'list[Page]',
        'thumbnails': 'list[str]',
        'doc_logs': 'list[DocLog]',
        'doc_metadata': 'DocMetadata',
        'original_doc_metadata': 'DocMetadata',
        'storage_provider_broker': 'str',
        'storage_provider': 'str',
        'storage_account_id': 'str',
        'storage_provider_id': 'str',
        'storage_provider_folder_id': 'str',
        'document_url': 'str'
    }

    attribute_map = {
        'document_type': 'documentType',
        'blob_ref': 'blobRef',
        'job_id': 'jobId',
        'ref_document_id': 'refDocumentId',
        'ref_doc_action': 'refDocAction',
        'document_id': 'documentId',
        'user_id': 'userId',
        'name': 'name',
        'file_name': 'fileName',
        'file_extension': 'fileExtension',
        'ratio': 'ratio',
        'doc_status': 'docStatus',
        'in_execution': 'inExecution',
        'order': 'order',
        'show_doc': 'showDoc',
        'doc_data': 'docData',
        'thumbnail': 'thumbnail',
        'pages': 'pages',
        'thumbnails': 'thumbnails',
        'doc_logs': 'docLogs',
        'doc_metadata': 'docMetadata',
        'original_doc_metadata': 'originalDocMetadata',
        'storage_provider_broker': 'storageProviderBroker',
        'storage_provider': 'storageProvider',
        'storage_account_id': 'storageAccountId',
        'storage_provider_id': 'storageProviderId',
        'storage_provider_folder_id': 'storageProviderFolderId',
        'document_url': 'documentUrl'
    }

    def __init__(self, document_type=None, blob_ref=None, job_id=None, ref_document_id=None, ref_doc_action=None, document_id=None, user_id=None, name=None, file_name=None, file_extension=None, ratio=None, doc_status=None, in_execution=None, order=None, show_doc=None, doc_data=None, thumbnail=None, pages=None, thumbnails=None, doc_logs=None, doc_metadata=None, original_doc_metadata=None, storage_provider_broker=None, storage_provider=None, storage_account_id=None, storage_provider_id=None, storage_provider_folder_id=None, document_url=None):  # noqa: E501
        """Pdf4meDocument - a model defined in Swagger"""  # noqa: E501

        self._document_type = None
        self._blob_ref = None
        self._job_id = None
        self._ref_document_id = None
        self._ref_doc_action = None
        self._document_id = None
        self._user_id = None
        self._name = None
        self._file_name = None
        self._file_extension = None
        self._ratio = None
        self._doc_status = None
        self._in_execution = None
        self._order = None
        self._show_doc = None
        self._doc_data = None
        self._thumbnail = None
        self._pages = None
        self._thumbnails = None
        self._doc_logs = None
        self._doc_metadata = None
        self._original_doc_metadata = None
        self._storage_provider_broker = None
        self._storage_provider = None
        self._storage_account_id = None
        self._storage_provider_id = None
        self._storage_provider_folder_id = None
        self._document_url = None
        self.discriminator = None

        if document_type is not None:
            self.document_type = document_type
        if blob_ref is not None:
            self.blob_ref = blob_ref
        if job_id is not None:
            self.job_id = job_id
        if ref_document_id is not None:
            self.ref_document_id = ref_document_id
        if ref_doc_action is not None:
            self.ref_doc_action = ref_doc_action
        if document_id is not None:
            self.document_id = document_id
        if user_id is not None:
            self.user_id = user_id
        if name is not None:
            self.name = name
        if file_name is not None:
            self.file_name = file_name
        if file_extension is not None:
            self.file_extension = file_extension
        if ratio is not None:
            self.ratio = ratio
        if doc_status is not None:
            self.doc_status = doc_status
        if in_execution is not None:
            self.in_execution = in_execution
        if order is not None:
            self.order = order
        if show_doc is not None:
            self.show_doc = show_doc
        if doc_data is not None:
            self.doc_data = doc_data
        if thumbnail is not None:
            self.thumbnail = thumbnail
        if pages is not None:
            self.pages = pages
        if thumbnails is not None:
            self.thumbnails = thumbnails
        if doc_logs is not None:
            self.doc_logs = doc_logs
        if doc_metadata is not None:
            self.doc_metadata = doc_metadata
        if original_doc_metadata is not None:
            self.original_doc_metadata = original_doc_metadata
        if storage_provider_broker is not None:
            self.storage_provider_broker = storage_provider_broker
        if storage_provider is not None:
            self.storage_provider = storage_provider
        if storage_account_id is not None:
            self.storage_account_id = storage_account_id
        if storage_provider_id is not None:
            self.storage_provider_id = storage_provider_id
        if storage_provider_folder_id is not None:
            self.storage_provider_folder_id = storage_provider_folder_id
        if document_url is not None:
            self.document_url = document_url

    @property
    def document_type(self):
        """Gets the document_type of this Pdf4meDocument.  # noqa: E501


        :return: The document_type of this Pdf4meDocument.  # noqa: E501
        :rtype: str
        """
        return self._document_type

    @document_type.setter
    def document_type(self, document_type):
        """Sets the document_type of this Pdf4meDocument.


        :param document_type: The document_type of this Pdf4meDocument.  # noqa: E501
        :type: str
        """
        allowed_values = ["uploadDoc", "converted", "stamped", "ocr", "split", "optimize", "merge"]  # noqa: E501
        if document_type not in allowed_values:
            raise ValueError(
                "Invalid value for `document_type` ({0}), must be one of {1}"  # noqa: E501
                .format(document_type, allowed_values)
            )

        self._document_type = document_type

    @property
    def blob_ref(self):
        """Gets the blob_ref of this Pdf4meDocument.  # noqa: E501


        :return: The blob_ref of this Pdf4meDocument.  # noqa: E501
        :rtype: str
        """
        return self._blob_ref

    @blob_ref.setter
    def blob_ref(self, blob_ref):
        """Sets the blob_ref of this Pdf4meDocument.


        :param blob_ref: The blob_ref of this Pdf4meDocument.  # noqa: E501
        :type: str
        """

        self._blob_ref = blob_ref

    @property
    def job_id(self):
        """Gets the job_id of this Pdf4meDocument.  # noqa: E501


        :return: The job_id of this Pdf4meDocument.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this Pdf4meDocument.


        :param job_id: The job_id of this Pdf4meDocument.  # noqa: E501
        :type: str
        """

        self._job_id = job_id

    @property
    def ref_document_id(self):
        """Gets the ref_document_id of this Pdf4meDocument.  # noqa: E501


        :return: The ref_document_id of this Pdf4meDocument.  # noqa: E501
        :rtype: str
        """
        return self._ref_document_id

    @ref_document_id.setter
    def ref_document_id(self, ref_document_id):
        """Sets the ref_document_id of this Pdf4meDocument.


        :param ref_document_id: The ref_document_id of this Pdf4meDocument.  # noqa: E501
        :type: str
        """

        self._ref_document_id = ref_document_id

    @property
    def ref_doc_action(self):
        """Gets the ref_doc_action of this Pdf4meDocument.  # noqa: E501


        :return: The ref_doc_action of this Pdf4meDocument.  # noqa: E501
        :rtype: DocAction
        """
        return self._ref_doc_action

    @ref_doc_action.setter
    def ref_doc_action(self, ref_doc_action):
        """Sets the ref_doc_action of this Pdf4meDocument.


        :param ref_doc_action: The ref_doc_action of this Pdf4meDocument.  # noqa: E501
        :type: DocAction
        """

        self._ref_doc_action = ref_doc_action

    @property
    def document_id(self):
        """Gets the document_id of this Pdf4meDocument.  # noqa: E501


        :return: The document_id of this Pdf4meDocument.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this Pdf4meDocument.


        :param document_id: The document_id of this Pdf4meDocument.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def user_id(self):
        """Gets the user_id of this Pdf4meDocument.  # noqa: E501


        :return: The user_id of this Pdf4meDocument.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Pdf4meDocument.


        :param user_id: The user_id of this Pdf4meDocument.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def name(self):
        """Gets the name of this Pdf4meDocument.  # noqa: E501


        :return: The name of this Pdf4meDocument.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Pdf4meDocument.


        :param name: The name of this Pdf4meDocument.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def file_name(self):
        """Gets the file_name of this Pdf4meDocument.  # noqa: E501


        :return: The file_name of this Pdf4meDocument.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this Pdf4meDocument.


        :param file_name: The file_name of this Pdf4meDocument.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def file_extension(self):
        """Gets the file_extension of this Pdf4meDocument.  # noqa: E501


        :return: The file_extension of this Pdf4meDocument.  # noqa: E501
        :rtype: str
        """
        return self._file_extension

    @file_extension.setter
    def file_extension(self, file_extension):
        """Sets the file_extension of this Pdf4meDocument.


        :param file_extension: The file_extension of this Pdf4meDocument.  # noqa: E501
        :type: str
        """

        self._file_extension = file_extension

    @property
    def ratio(self):
        """Gets the ratio of this Pdf4meDocument.  # noqa: E501


        :return: The ratio of this Pdf4meDocument.  # noqa: E501
        :rtype: float
        """
        return self._ratio

    @ratio.setter
    def ratio(self, ratio):
        """Sets the ratio of this Pdf4meDocument.


        :param ratio: The ratio of this Pdf4meDocument.  # noqa: E501
        :type: float
        """

        self._ratio = ratio

    @property
    def doc_status(self):
        """Gets the doc_status of this Pdf4meDocument.  # noqa: E501


        :return: The doc_status of this Pdf4meDocument.  # noqa: E501
        :rtype: str
        """
        return self._doc_status

    @doc_status.setter
    def doc_status(self, doc_status):
        """Sets the doc_status of this Pdf4meDocument.


        :param doc_status: The doc_status of this Pdf4meDocument.  # noqa: E501
        :type: str
        """
        allowed_values = ["undef", "error", "finished", "uploaded", "loading", "loaded", "converting", "converted", "optimizing", "optimized", "doingOcr", "ocred", "doingZip", "stamping", "stamped", "processing", "signed"]  # noqa: E501
        if doc_status not in allowed_values:
            raise ValueError(
                "Invalid value for `doc_status` ({0}), must be one of {1}"  # noqa: E501
                .format(doc_status, allowed_values)
            )

        self._doc_status = doc_status

    @property
    def in_execution(self):
        """Gets the in_execution of this Pdf4meDocument.  # noqa: E501


        :return: The in_execution of this Pdf4meDocument.  # noqa: E501
        :rtype: bool
        """
        return self._in_execution

    @in_execution.setter
    def in_execution(self, in_execution):
        """Sets the in_execution of this Pdf4meDocument.


        :param in_execution: The in_execution of this Pdf4meDocument.  # noqa: E501
        :type: bool
        """

        self._in_execution = in_execution

    @property
    def order(self):
        """Gets the order of this Pdf4meDocument.  # noqa: E501


        :return: The order of this Pdf4meDocument.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this Pdf4meDocument.


        :param order: The order of this Pdf4meDocument.  # noqa: E501
        :type: int
        """

        self._order = order

    @property
    def show_doc(self):
        """Gets the show_doc of this Pdf4meDocument.  # noqa: E501


        :return: The show_doc of this Pdf4meDocument.  # noqa: E501
        :rtype: bool
        """
        return self._show_doc

    @show_doc.setter
    def show_doc(self, show_doc):
        """Sets the show_doc of this Pdf4meDocument.


        :param show_doc: The show_doc of this Pdf4meDocument.  # noqa: E501
        :type: bool
        """

        self._show_doc = show_doc

    @property
    def doc_data(self):
        """Gets the doc_data of this Pdf4meDocument.  # noqa: E501


        :return: The doc_data of this Pdf4meDocument.  # noqa: E501
        :rtype: str
        """
        return self._doc_data

    @doc_data.setter
    def doc_data(self, doc_data):
        """Sets the doc_data of this Pdf4meDocument.


        :param doc_data: The doc_data of this Pdf4meDocument.  # noqa: E501
        :type: str
        """
        if doc_data is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', doc_data):  # noqa: E501
            raise ValueError(r"Invalid value for `doc_data`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._doc_data = doc_data

    @property
    def thumbnail(self):
        """Gets the thumbnail of this Pdf4meDocument.  # noqa: E501


        :return: The thumbnail of this Pdf4meDocument.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """Sets the thumbnail of this Pdf4meDocument.


        :param thumbnail: The thumbnail of this Pdf4meDocument.  # noqa: E501
        :type: str
        """
        if thumbnail is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', thumbnail):  # noqa: E501
            raise ValueError(r"Invalid value for `thumbnail`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._thumbnail = thumbnail

    @property
    def pages(self):
        """Gets the pages of this Pdf4meDocument.  # noqa: E501


        :return: The pages of this Pdf4meDocument.  # noqa: E501
        :rtype: list[Page]
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """Sets the pages of this Pdf4meDocument.


        :param pages: The pages of this Pdf4meDocument.  # noqa: E501
        :type: list[Page]
        """

        self._pages = pages

    @property
    def thumbnails(self):
        """Gets the thumbnails of this Pdf4meDocument.  # noqa: E501


        :return: The thumbnails of this Pdf4meDocument.  # noqa: E501
        :rtype: list[str]
        """
        return self._thumbnails

    @thumbnails.setter
    def thumbnails(self, thumbnails):
        """Sets the thumbnails of this Pdf4meDocument.


        :param thumbnails: The thumbnails of this Pdf4meDocument.  # noqa: E501
        :type: list[str]
        """

        self._thumbnails = thumbnails

    @property
    def doc_logs(self):
        """Gets the doc_logs of this Pdf4meDocument.  # noqa: E501


        :return: The doc_logs of this Pdf4meDocument.  # noqa: E501
        :rtype: list[DocLog]
        """
        return self._doc_logs

    @doc_logs.setter
    def doc_logs(self, doc_logs):
        """Sets the doc_logs of this Pdf4meDocument.


        :param doc_logs: The doc_logs of this Pdf4meDocument.  # noqa: E501
        :type: list[DocLog]
        """

        self._doc_logs = doc_logs

    @property
    def doc_metadata(self):
        """Gets the doc_metadata of this Pdf4meDocument.  # noqa: E501


        :return: The doc_metadata of this Pdf4meDocument.  # noqa: E501
        :rtype: DocMetadata
        """
        return self._doc_metadata

    @doc_metadata.setter
    def doc_metadata(self, doc_metadata):
        """Sets the doc_metadata of this Pdf4meDocument.


        :param doc_metadata: The doc_metadata of this Pdf4meDocument.  # noqa: E501
        :type: DocMetadata
        """

        self._doc_metadata = doc_metadata

    @property
    def original_doc_metadata(self):
        """Gets the original_doc_metadata of this Pdf4meDocument.  # noqa: E501


        :return: The original_doc_metadata of this Pdf4meDocument.  # noqa: E501
        :rtype: DocMetadata
        """
        return self._original_doc_metadata

    @original_doc_metadata.setter
    def original_doc_metadata(self, original_doc_metadata):
        """Sets the original_doc_metadata of this Pdf4meDocument.


        :param original_doc_metadata: The original_doc_metadata of this Pdf4meDocument.  # noqa: E501
        :type: DocMetadata
        """

        self._original_doc_metadata = original_doc_metadata

    @property
    def storage_provider_broker(self):
        """Gets the storage_provider_broker of this Pdf4meDocument.  # noqa: E501


        :return: The storage_provider_broker of this Pdf4meDocument.  # noqa: E501
        :rtype: str
        """
        return self._storage_provider_broker

    @storage_provider_broker.setter
    def storage_provider_broker(self, storage_provider_broker):
        """Sets the storage_provider_broker of this Pdf4meDocument.


        :param storage_provider_broker: The storage_provider_broker of this Pdf4meDocument.  # noqa: E501
        :type: str
        """
        allowed_values = ["undef", "kloudless"]  # noqa: E501
        if storage_provider_broker not in allowed_values:
            raise ValueError(
                "Invalid value for `storage_provider_broker` ({0}), must be one of {1}"  # noqa: E501
                .format(storage_provider_broker, allowed_values)
            )

        self._storage_provider_broker = storage_provider_broker

    @property
    def storage_provider(self):
        """Gets the storage_provider of this Pdf4meDocument.  # noqa: E501


        :return: The storage_provider of this Pdf4meDocument.  # noqa: E501
        :rtype: str
        """
        return self._storage_provider

    @storage_provider.setter
    def storage_provider(self, storage_provider):
        """Sets the storage_provider of this Pdf4meDocument.


        :param storage_provider: The storage_provider of this Pdf4meDocument.  # noqa: E501
        :type: str
        """
        allowed_values = ["undef", "local", "url", "oneDrive", "dropbox", "googleDrive", "kloudless"]  # noqa: E501
        if storage_provider not in allowed_values:
            raise ValueError(
                "Invalid value for `storage_provider` ({0}), must be one of {1}"  # noqa: E501
                .format(storage_provider, allowed_values)
            )

        self._storage_provider = storage_provider

    @property
    def storage_account_id(self):
        """Gets the storage_account_id of this Pdf4meDocument.  # noqa: E501


        :return: The storage_account_id of this Pdf4meDocument.  # noqa: E501
        :rtype: str
        """
        return self._storage_account_id

    @storage_account_id.setter
    def storage_account_id(self, storage_account_id):
        """Sets the storage_account_id of this Pdf4meDocument.


        :param storage_account_id: The storage_account_id of this Pdf4meDocument.  # noqa: E501
        :type: str
        """

        self._storage_account_id = storage_account_id

    @property
    def storage_provider_id(self):
        """Gets the storage_provider_id of this Pdf4meDocument.  # noqa: E501


        :return: The storage_provider_id of this Pdf4meDocument.  # noqa: E501
        :rtype: str
        """
        return self._storage_provider_id

    @storage_provider_id.setter
    def storage_provider_id(self, storage_provider_id):
        """Sets the storage_provider_id of this Pdf4meDocument.


        :param storage_provider_id: The storage_provider_id of this Pdf4meDocument.  # noqa: E501
        :type: str
        """

        self._storage_provider_id = storage_provider_id

    @property
    def storage_provider_folder_id(self):
        """Gets the storage_provider_folder_id of this Pdf4meDocument.  # noqa: E501


        :return: The storage_provider_folder_id of this Pdf4meDocument.  # noqa: E501
        :rtype: str
        """
        return self._storage_provider_folder_id

    @storage_provider_folder_id.setter
    def storage_provider_folder_id(self, storage_provider_folder_id):
        """Sets the storage_provider_folder_id of this Pdf4meDocument.


        :param storage_provider_folder_id: The storage_provider_folder_id of this Pdf4meDocument.  # noqa: E501
        :type: str
        """

        self._storage_provider_folder_id = storage_provider_folder_id

    @property
    def document_url(self):
        """Gets the document_url of this Pdf4meDocument.  # noqa: E501


        :return: The document_url of this Pdf4meDocument.  # noqa: E501
        :rtype: str
        """
        return self._document_url

    @document_url.setter
    def document_url(self, document_url):
        """Sets the document_url of this Pdf4meDocument.


        :param document_url: The document_url of this Pdf4meDocument.  # noqa: E501
        :type: str
        """

        self._document_url = document_url

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
        if issubclass(Pdf4meDocument, dict):
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
        if not isinstance(other, Pdf4meDocument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
