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


class ApiCommand(object):
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
        'env': 'list[str]',
        'args': 'list[str]',
        'dir': 'str',
        'id': 'str',
        'wait_for': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'env': 'env',
        'args': 'args',
        'dir': 'dir',
        'id': 'id',
        'wait_for': 'wait_for'
    }

    def __init__(self, name=None, env=None, args=None, dir=None, id=None, wait_for=None):  # noqa: E501
        """ApiCommand - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._env = None
        self._args = None
        self._dir = None
        self._id = None
        self._wait_for = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if env is not None:
            self.env = env
        if args is not None:
            self.args = args
        if dir is not None:
            self.dir = dir
        if id is not None:
            self.id = id
        if wait_for is not None:
            self.wait_for = wait_for

    @property
    def name(self):
        """Gets the name of this ApiCommand.  # noqa: E501

        Name of the command, as presented on the command line, or if the command is packaged as a Docker container, as presented to `docker pull`.  # noqa: E501

        :return: The name of this ApiCommand.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiCommand.

        Name of the command, as presented on the command line, or if the command is packaged as a Docker container, as presented to `docker pull`.  # noqa: E501

        :param name: The name of this ApiCommand.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def env(self):
        """Gets the env of this ApiCommand.  # noqa: E501

        Environment variables set before running this Command.  # noqa: E501

        :return: The env of this ApiCommand.  # noqa: E501
        :rtype: list[str]
        """
        return self._env

    @env.setter
    def env(self, env):
        """Sets the env of this ApiCommand.

        Environment variables set before running this Command.  # noqa: E501

        :param env: The env of this ApiCommand.  # noqa: E501
        :type: list[str]
        """

        self._env = env

    @property
    def args(self):
        """Gets the args of this ApiCommand.  # noqa: E501

        Command-line arguments used when executing this Command.  # noqa: E501

        :return: The args of this ApiCommand.  # noqa: E501
        :rtype: list[str]
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this ApiCommand.

        Command-line arguments used when executing this Command.  # noqa: E501

        :param args: The args of this ApiCommand.  # noqa: E501
        :type: list[str]
        """

        self._args = args

    @property
    def dir(self):
        """Gets the dir of this ApiCommand.  # noqa: E501

        Working directory (relative to project source root) used when running this Command.  # noqa: E501

        :return: The dir of this ApiCommand.  # noqa: E501
        :rtype: str
        """
        return self._dir

    @dir.setter
    def dir(self, dir):
        """Sets the dir of this ApiCommand.

        Working directory (relative to project source root) used when running this Command.  # noqa: E501

        :param dir: The dir of this ApiCommand.  # noqa: E501
        :type: str
        """

        self._dir = dir

    @property
    def id(self):
        """Gets the id of this ApiCommand.  # noqa: E501

        Optional unique identifier for this Command, used in wait_for to reference this Command as a dependency.  # noqa: E501

        :return: The id of this ApiCommand.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiCommand.

        Optional unique identifier for this Command, used in wait_for to reference this Command as a dependency.  # noqa: E501

        :param id: The id of this ApiCommand.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def wait_for(self):
        """Gets the wait_for of this ApiCommand.  # noqa: E501

        The ID(s) of the Command(s) that this Command depends on.  # noqa: E501

        :return: The wait_for of this ApiCommand.  # noqa: E501
        :rtype: list[str]
        """
        return self._wait_for

    @wait_for.setter
    def wait_for(self, wait_for):
        """Sets the wait_for of this ApiCommand.

        The ID(s) of the Command(s) that this Command depends on.  # noqa: E501

        :param wait_for: The wait_for of this ApiCommand.  # noqa: E501
        :type: list[str]
        """

        self._wait_for = wait_for

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
        if issubclass(ApiCommand, dict):
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
        if not isinstance(other, ApiCommand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
