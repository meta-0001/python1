# coding: utf-8

"""
    An API to insert and retrieve metadata on cloud artifacts.

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1alpha1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GooglelongrunningOperation(object):
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
        'name': 'str',
        'metadata': 'ProtobufAny',
        'done': 'bool',
        'error': 'RpcStatus',
        'response': 'ProtobufAny'
    }

    attribute_map = {
        'name': 'name',
        'metadata': 'metadata',
        'done': 'done',
        'error': 'error',
        'response': 'response'
    }

    def __init__(self, name=None, metadata=None, done=None, error=None, response=None):  # noqa: E501
        """GooglelongrunningOperation - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._metadata = None
        self._done = None
        self._error = None
        self._response = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if metadata is not None:
            self.metadata = metadata
        if done is not None:
            self.done = done
        if error is not None:
            self.error = error
        if response is not None:
            self.response = response

    @property
    def name(self):
        """Gets the name of this GooglelongrunningOperation.  # noqa: E501

        The server-assigned name, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the `name` should have the format of `operations/some/unique/name`.  # noqa: E501

        :return: The name of this GooglelongrunningOperation.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GooglelongrunningOperation.

        The server-assigned name, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the `name` should have the format of `operations/some/unique/name`.  # noqa: E501

        :param name: The name of this GooglelongrunningOperation.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def metadata(self):
        """Gets the metadata of this GooglelongrunningOperation.  # noqa: E501

        Service-specific metadata associated with the operation.  It typically contains progress information and common metadata such as create time. Some services might not provide such metadata.  Any method that returns a long-running operation should document the metadata type, if any.  # noqa: E501

        :return: The metadata of this GooglelongrunningOperation.  # noqa: E501
        :rtype: ProtobufAny
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this GooglelongrunningOperation.

        Service-specific metadata associated with the operation.  It typically contains progress information and common metadata such as create time. Some services might not provide such metadata.  Any method that returns a long-running operation should document the metadata type, if any.  # noqa: E501

        :param metadata: The metadata of this GooglelongrunningOperation.  # noqa: E501
        :type: ProtobufAny
        """

        self._metadata = metadata

    @property
    def done(self):
        """Gets the done of this GooglelongrunningOperation.  # noqa: E501

        If the value is `false`, it means the operation is still in progress. If `true`, the operation is completed, and either `error` or `response` is available.  # noqa: E501

        :return: The done of this GooglelongrunningOperation.  # noqa: E501
        :rtype: bool
        """
        return self._done

    @done.setter
    def done(self, done):
        """Sets the done of this GooglelongrunningOperation.

        If the value is `false`, it means the operation is still in progress. If `true`, the operation is completed, and either `error` or `response` is available.  # noqa: E501

        :param done: The done of this GooglelongrunningOperation.  # noqa: E501
        :type: bool
        """

        self._done = done

    @property
    def error(self):
        """Gets the error of this GooglelongrunningOperation.  # noqa: E501

        The error result of the operation in case of failure or cancellation.  # noqa: E501

        :return: The error of this GooglelongrunningOperation.  # noqa: E501
        :rtype: RpcStatus
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this GooglelongrunningOperation.

        The error result of the operation in case of failure or cancellation.  # noqa: E501

        :param error: The error of this GooglelongrunningOperation.  # noqa: E501
        :type: RpcStatus
        """

        self._error = error

    @property
    def response(self):
        """Gets the response of this GooglelongrunningOperation.  # noqa: E501

        The normal response of the operation in case of success.  If the original method returns no data on success, such as `Delete`, the response is `google.protobuf.Empty`.  If the original method is standard `Get`/`Create`/`Update`, the response should be the resource.  For other methods, the response should have the type `XxxResponse`, where `Xxx` is the original method name.  For example, if the original method name is `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.  # noqa: E501

        :return: The response of this GooglelongrunningOperation.  # noqa: E501
        :rtype: ProtobufAny
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this GooglelongrunningOperation.

        The normal response of the operation in case of success.  If the original method returns no data on success, such as `Delete`, the response is `google.protobuf.Empty`.  If the original method is standard `Get`/`Create`/`Update`, the response should be the resource.  For other methods, the response should have the type `XxxResponse`, where `Xxx` is the original method name.  For example, if the original method name is `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.  # noqa: E501

        :param response: The response of this GooglelongrunningOperation.  # noqa: E501
        :type: ProtobufAny
        """

        self._response = response

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
        if issubclass(GooglelongrunningOperation, dict):
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
        if not isinstance(other, GooglelongrunningOperation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
