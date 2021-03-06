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


class ApiListNotesResponse(object):
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
        'notes': 'list[ApiNote]',
        'next_page_token': 'str'
    }

    attribute_map = {
        'notes': 'notes',
        'next_page_token': 'next_page_token'
    }

    def __init__(self, notes=None, next_page_token=None):  # noqa: E501
        """ApiListNotesResponse - a model defined in Swagger"""  # noqa: E501

        self._notes = None
        self._next_page_token = None
        self.discriminator = None

        if notes is not None:
            self.notes = notes
        if next_page_token is not None:
            self.next_page_token = next_page_token

    @property
    def notes(self):
        """Gets the notes of this ApiListNotesResponse.  # noqa: E501


        :return: The notes of this ApiListNotesResponse.  # noqa: E501
        :rtype: list[ApiNote]
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this ApiListNotesResponse.


        :param notes: The notes of this ApiListNotesResponse.  # noqa: E501
        :type: list[ApiNote]
        """

        self._notes = notes

    @property
    def next_page_token(self):
        """Gets the next_page_token of this ApiListNotesResponse.  # noqa: E501

        The next pagination token in the list response. It should be used as page_token for the following request. An empty value means no more result.  # noqa: E501

        :return: The next_page_token of this ApiListNotesResponse.  # noqa: E501
        :rtype: str
        """
        return self._next_page_token

    @next_page_token.setter
    def next_page_token(self, next_page_token):
        """Sets the next_page_token of this ApiListNotesResponse.

        The next pagination token in the list response. It should be used as page_token for the following request. An empty value means no more result.  # noqa: E501

        :param next_page_token: The next_page_token of this ApiListNotesResponse.  # noqa: E501
        :type: str
        """

        self._next_page_token = next_page_token

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
        if issubclass(ApiListNotesResponse, dict):
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
        if not isinstance(other, ApiListNotesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
