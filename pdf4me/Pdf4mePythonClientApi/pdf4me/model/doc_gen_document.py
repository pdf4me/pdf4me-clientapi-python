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


class DocGenDocument(object):
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
        'merge_data': 'MergeData',
        'paper': 'str',
        'print_mode': 'str',
        'document_id': 'str',
        'name': 'str',
        'file_name': 'str',
        'file_extension': 'str',
        'doc_status': 'str',
        'pages': 'list[Page]',
        'doc_data': 'str',
        'doc_metadata': 'DocMetadata',
        'doc_logs': 'list[DocLog]',
        'document_url': 'str',
        'scan_pages': 'list[ScanPage]',
        'order': 'int'
    }

    attribute_map = {
        'merge_data': 'mergeData',
        'paper': 'Paper',
        'print_mode': 'printMode',
        'document_id': 'documentId',
        'name': 'name',
        'file_name': 'fileName',
        'file_extension': 'fileExtension',
        'doc_status': 'docStatus',
        'pages': 'pages',
        'doc_data': 'docData',
        'doc_metadata': 'docMetadata',
        'doc_logs': 'docLogs',
        'document_url': 'documentUrl',
        'scan_pages': 'scanPages',
        'order': 'order'
    }

    def __init__(self, merge_data=None, paper=None, print_mode=None, document_id=None, name=None, file_name=None, file_extension=None, doc_status=None, pages=None, doc_data=None, doc_metadata=None, doc_logs=None, document_url=None, scan_pages=None, order=None):  # noqa: E501
        """DocGenDocument - a model defined in Swagger"""  # noqa: E501

        self._merge_data = None
        self._paper = None
        self._print_mode = None
        self._document_id = None
        self._name = None
        self._file_name = None
        self._file_extension = None
        self._doc_status = None
        self._pages = None
        self._doc_data = None
        self._doc_metadata = None
        self._doc_logs = None
        self._document_url = None
        self._scan_pages = None
        self._order = None
        self.discriminator = None

        if merge_data is not None:
            self.merge_data = merge_data
        if paper is not None:
            self.paper = paper
        if print_mode is not None:
            self.print_mode = print_mode
        if document_id is not None:
            self.document_id = document_id
        if name is not None:
            self.name = name
        if file_name is not None:
            self.file_name = file_name
        if file_extension is not None:
            self.file_extension = file_extension
        if doc_status is not None:
            self.doc_status = doc_status
        if pages is not None:
            self.pages = pages
        if doc_data is not None:
            self.doc_data = doc_data
        if doc_metadata is not None:
            self.doc_metadata = doc_metadata
        if doc_logs is not None:
            self.doc_logs = doc_logs
        if document_url is not None:
            self.document_url = document_url
        if scan_pages is not None:
            self.scan_pages = scan_pages
        if order is not None:
            self.order = order

    @property
    def merge_data(self):
        """Gets the merge_data of this DocGenDocument.  # noqa: E501


        :return: The merge_data of this DocGenDocument.  # noqa: E501
        :rtype: MergeData
        """
        return self._merge_data

    @merge_data.setter
    def merge_data(self, merge_data):
        """Sets the merge_data of this DocGenDocument.


        :param merge_data: The merge_data of this DocGenDocument.  # noqa: E501
        :type: MergeData
        """

        self._merge_data = merge_data

    @property
    def paper(self):
        """Gets the paper of this DocGenDocument.  # noqa: E501


        :return: The paper of this DocGenDocument.  # noqa: E501
        :rtype: str
        """
        return self._paper

    @paper.setter
    def paper(self, paper):
        """Sets the paper of this DocGenDocument.


        :param paper: The paper of this DocGenDocument.  # noqa: E501
        :type: str
        """

        self._paper = paper

    @property
    def print_mode(self):
        """Gets the print_mode of this DocGenDocument.  # noqa: E501


        :return: The print_mode of this DocGenDocument.  # noqa: E501
        :rtype: str
        """
        return self._print_mode

    @print_mode.setter
    def print_mode(self, print_mode):
        """Sets the print_mode of this DocGenDocument.


        :param print_mode: The print_mode of this DocGenDocument.  # noqa: E501
        :type: str
        """
        allowed_values = ["undef", "simplex", "duplex"]  # noqa: E501
        if print_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `print_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(print_mode, allowed_values)
            )

        self._print_mode = print_mode

    @property
    def document_id(self):
        """Gets the document_id of this DocGenDocument.  # noqa: E501

        DocumentId  # noqa: E501

        :return: The document_id of this DocGenDocument.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this DocGenDocument.

        DocumentId  # noqa: E501

        :param document_id: The document_id of this DocGenDocument.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def name(self):
        """Gets the name of this DocGenDocument.  # noqa: E501

        Give filename inlcuding filetype  # noqa: E501

        :return: The name of this DocGenDocument.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DocGenDocument.

        Give filename inlcuding filetype  # noqa: E501

        :param name: The name of this DocGenDocument.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def file_name(self):
        """Gets the file_name of this DocGenDocument.  # noqa: E501


        :return: The file_name of this DocGenDocument.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this DocGenDocument.


        :param file_name: The file_name of this DocGenDocument.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def file_extension(self):
        """Gets the file_extension of this DocGenDocument.  # noqa: E501


        :return: The file_extension of this DocGenDocument.  # noqa: E501
        :rtype: str
        """
        return self._file_extension

    @file_extension.setter
    def file_extension(self, file_extension):
        """Sets the file_extension of this DocGenDocument.


        :param file_extension: The file_extension of this DocGenDocument.  # noqa: E501
        :type: str
        """

        self._file_extension = file_extension

    @property
    def doc_status(self):
        """Gets the doc_status of this DocGenDocument.  # noqa: E501

        Returns the Status of the Document  # noqa: E501

        :return: The doc_status of this DocGenDocument.  # noqa: E501
        :rtype: str
        """
        return self._doc_status

    @doc_status.setter
    def doc_status(self, doc_status):
        """Sets the doc_status of this DocGenDocument.

        Returns the Status of the Document  # noqa: E501

        :param doc_status: The doc_status of this DocGenDocument.  # noqa: E501
        :type: str
        """

        self._doc_status = doc_status

    @property
    def pages(self):
        """Gets the pages of this DocGenDocument.  # noqa: E501

        Description of pages  # noqa: E501

        :return: The pages of this DocGenDocument.  # noqa: E501
        :rtype: list[Page]
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """Sets the pages of this DocGenDocument.

        Description of pages  # noqa: E501

        :param pages: The pages of this DocGenDocument.  # noqa: E501
        :type: list[Page]
        """

        self._pages = pages

    @property
    def doc_data(self):
        """Gets the doc_data of this DocGenDocument.  # noqa: E501


        :return: The doc_data of this DocGenDocument.  # noqa: E501
        :rtype: str
        """
        return self._doc_data

    @doc_data.setter
    def doc_data(self, doc_data):
        """Sets the doc_data of this DocGenDocument.


        :param doc_data: The doc_data of this DocGenDocument.  # noqa: E501
        :type: str
        """
        if doc_data is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', doc_data):  # noqa: E501
            raise ValueError(r"Invalid value for `doc_data`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._doc_data = doc_data

    @property
    def doc_metadata(self):
        """Gets the doc_metadata of this DocGenDocument.  # noqa: E501


        :return: The doc_metadata of this DocGenDocument.  # noqa: E501
        :rtype: DocMetadata
        """
        return self._doc_metadata

    @doc_metadata.setter
    def doc_metadata(self, doc_metadata):
        """Sets the doc_metadata of this DocGenDocument.


        :param doc_metadata: The doc_metadata of this DocGenDocument.  # noqa: E501
        :type: DocMetadata
        """

        self._doc_metadata = doc_metadata

    @property
    def doc_logs(self):
        """Gets the doc_logs of this DocGenDocument.  # noqa: E501


        :return: The doc_logs of this DocGenDocument.  # noqa: E501
        :rtype: list[DocLog]
        """
        return self._doc_logs

    @doc_logs.setter
    def doc_logs(self, doc_logs):
        """Sets the doc_logs of this DocGenDocument.


        :param doc_logs: The doc_logs of this DocGenDocument.  # noqa: E501
        :type: list[DocLog]
        """

        self._doc_logs = doc_logs

    @property
    def document_url(self):
        """Gets the document_url of this DocGenDocument.  # noqa: E501


        :return: The document_url of this DocGenDocument.  # noqa: E501
        :rtype: str
        """
        return self._document_url

    @document_url.setter
    def document_url(self, document_url):
        """Sets the document_url of this DocGenDocument.


        :param document_url: The document_url of this DocGenDocument.  # noqa: E501
        :type: str
        """

        self._document_url = document_url

    @property
    def scan_pages(self):
        """Gets the scan_pages of this DocGenDocument.  # noqa: E501


        :return: The scan_pages of this DocGenDocument.  # noqa: E501
        :rtype: list[ScanPage]
        """
        return self._scan_pages

    @scan_pages.setter
    def scan_pages(self, scan_pages):
        """Sets the scan_pages of this DocGenDocument.


        :param scan_pages: The scan_pages of this DocGenDocument.  # noqa: E501
        :type: list[ScanPage]
        """

        self._scan_pages = scan_pages

    @property
    def order(self):
        """Gets the order of this DocGenDocument.  # noqa: E501


        :return: The order of this DocGenDocument.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this DocGenDocument.


        :param order: The order of this DocGenDocument.  # noqa: E501
        :type: int
        """

        self._order = order

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
        if issubclass(DocGenDocument, dict):
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
        if not isinstance(other, DocGenDocument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
