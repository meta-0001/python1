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


class ApiNote(object):
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
        'short_description': 'str',
        'long_description': 'str',
        'kind': 'ApiNoteKind',
        'vulnerability_type': 'ApiVulnerabilityType',
        'build_type': 'ApiBuildType',
        'base_image': 'DockerImageBasis',
        'package': 'PackageManagerPackage',
        'deployable': 'ApiDeployable',
        'discovery': 'ApiDiscovery',
        'attestation_authority': 'ApiAttestationAuthority',
        'related_url': 'list[NoteRelatedUrl]',
        'expiration_time': 'datetime',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'operation_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'short_description': 'short_description',
        'long_description': 'long_description',
        'kind': 'kind',
        'vulnerability_type': 'vulnerability_type',
        'build_type': 'build_type',
        'base_image': 'base_image',
        'package': 'package',
        'deployable': 'deployable',
        'discovery': 'discovery',
        'attestation_authority': 'attestation_authority',
        'related_url': 'related_url',
        'expiration_time': 'expiration_time',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'operation_name': 'operation_name'
    }

    def __init__(self, name=None, short_description=None, long_description=None, kind=None, vulnerability_type=None, build_type=None, base_image=None, package=None, deployable=None, discovery=None, attestation_authority=None, related_url=None, expiration_time=None, create_time=None, update_time=None, operation_name=None):  # noqa: E501
        """ApiNote - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._short_description = None
        self._long_description = None
        self._kind = None
        self._vulnerability_type = None
        self._build_type = None
        self._base_image = None
        self._package = None
        self._deployable = None
        self._discovery = None
        self._attestation_authority = None
        self._related_url = None
        self._expiration_time = None
        self._create_time = None
        self._update_time = None
        self._operation_name = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if short_description is not None:
            self.short_description = short_description
        if long_description is not None:
            self.long_description = long_description
        if kind is not None:
            self.kind = kind
        if vulnerability_type is not None:
            self.vulnerability_type = vulnerability_type
        if build_type is not None:
            self.build_type = build_type
        if base_image is not None:
            self.base_image = base_image
        if package is not None:
            self.package = package
        if deployable is not None:
            self.deployable = deployable
        if discovery is not None:
            self.discovery = discovery
        if attestation_authority is not None:
            self.attestation_authority = attestation_authority
        if related_url is not None:
            self.related_url = related_url
        if expiration_time is not None:
            self.expiration_time = expiration_time
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if operation_name is not None:
            self.operation_name = operation_name

    @property
    def name(self):
        """Gets the name of this ApiNote.  # noqa: E501

        The name of the note in the form \"projects/{PROJECT_ID}/notes/{NOTE_ID}\".  # noqa: E501

        :return: The name of this ApiNote.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiNote.

        The name of the note in the form \"projects/{PROJECT_ID}/notes/{NOTE_ID}\".  # noqa: E501

        :param name: The name of this ApiNote.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def short_description(self):
        """Gets the short_description of this ApiNote.  # noqa: E501

        A one sentence description of this `Note`.  # noqa: E501

        :return: The short_description of this ApiNote.  # noqa: E501
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """Sets the short_description of this ApiNote.

        A one sentence description of this `Note`.  # noqa: E501

        :param short_description: The short_description of this ApiNote.  # noqa: E501
        :type: str
        """

        self._short_description = short_description

    @property
    def long_description(self):
        """Gets the long_description of this ApiNote.  # noqa: E501

        A detailed description of this `Note`.  # noqa: E501

        :return: The long_description of this ApiNote.  # noqa: E501
        :rtype: str
        """
        return self._long_description

    @long_description.setter
    def long_description(self, long_description):
        """Sets the long_description of this ApiNote.

        A detailed description of this `Note`.  # noqa: E501

        :param long_description: The long_description of this ApiNote.  # noqa: E501
        :type: str
        """

        self._long_description = long_description

    @property
    def kind(self):
        """Gets the kind of this ApiNote.  # noqa: E501

        Output only. This explicitly denotes which kind of note is specified. This field can be used as a filter in list requests.  # noqa: E501

        :return: The kind of this ApiNote.  # noqa: E501
        :rtype: ApiNoteKind
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this ApiNote.

        Output only. This explicitly denotes which kind of note is specified. This field can be used as a filter in list requests.  # noqa: E501

        :param kind: The kind of this ApiNote.  # noqa: E501
        :type: ApiNoteKind
        """

        self._kind = kind

    @property
    def vulnerability_type(self):
        """Gets the vulnerability_type of this ApiNote.  # noqa: E501

        A package vulnerability type of note.  # noqa: E501

        :return: The vulnerability_type of this ApiNote.  # noqa: E501
        :rtype: ApiVulnerabilityType
        """
        return self._vulnerability_type

    @vulnerability_type.setter
    def vulnerability_type(self, vulnerability_type):
        """Sets the vulnerability_type of this ApiNote.

        A package vulnerability type of note.  # noqa: E501

        :param vulnerability_type: The vulnerability_type of this ApiNote.  # noqa: E501
        :type: ApiVulnerabilityType
        """

        self._vulnerability_type = vulnerability_type

    @property
    def build_type(self):
        """Gets the build_type of this ApiNote.  # noqa: E501

        Build provenance type for a verifiable build.  # noqa: E501

        :return: The build_type of this ApiNote.  # noqa: E501
        :rtype: ApiBuildType
        """
        return self._build_type

    @build_type.setter
    def build_type(self, build_type):
        """Sets the build_type of this ApiNote.

        Build provenance type for a verifiable build.  # noqa: E501

        :param build_type: The build_type of this ApiNote.  # noqa: E501
        :type: ApiBuildType
        """

        self._build_type = build_type

    @property
    def base_image(self):
        """Gets the base_image of this ApiNote.  # noqa: E501

        A note describing a base image.  # noqa: E501

        :return: The base_image of this ApiNote.  # noqa: E501
        :rtype: DockerImageBasis
        """
        return self._base_image

    @base_image.setter
    def base_image(self, base_image):
        """Sets the base_image of this ApiNote.

        A note describing a base image.  # noqa: E501

        :param base_image: The base_image of this ApiNote.  # noqa: E501
        :type: DockerImageBasis
        """

        self._base_image = base_image

    @property
    def package(self):
        """Gets the package of this ApiNote.  # noqa: E501

        A note describing a package hosted by various package managers.  # noqa: E501

        :return: The package of this ApiNote.  # noqa: E501
        :rtype: PackageManagerPackage
        """
        return self._package

    @package.setter
    def package(self, package):
        """Sets the package of this ApiNote.

        A note describing a package hosted by various package managers.  # noqa: E501

        :param package: The package of this ApiNote.  # noqa: E501
        :type: PackageManagerPackage
        """

        self._package = package

    @property
    def deployable(self):
        """Gets the deployable of this ApiNote.  # noqa: E501

        A note describing something that can be deployed.  # noqa: E501

        :return: The deployable of this ApiNote.  # noqa: E501
        :rtype: ApiDeployable
        """
        return self._deployable

    @deployable.setter
    def deployable(self, deployable):
        """Sets the deployable of this ApiNote.

        A note describing something that can be deployed.  # noqa: E501

        :param deployable: The deployable of this ApiNote.  # noqa: E501
        :type: ApiDeployable
        """

        self._deployable = deployable

    @property
    def discovery(self):
        """Gets the discovery of this ApiNote.  # noqa: E501

        A note describing a provider/analysis type.  # noqa: E501

        :return: The discovery of this ApiNote.  # noqa: E501
        :rtype: ApiDiscovery
        """
        return self._discovery

    @discovery.setter
    def discovery(self, discovery):
        """Sets the discovery of this ApiNote.

        A note describing a provider/analysis type.  # noqa: E501

        :param discovery: The discovery of this ApiNote.  # noqa: E501
        :type: ApiDiscovery
        """

        self._discovery = discovery

    @property
    def attestation_authority(self):
        """Gets the attestation_authority of this ApiNote.  # noqa: E501

        A note describing an attestation role.  # noqa: E501

        :return: The attestation_authority of this ApiNote.  # noqa: E501
        :rtype: ApiAttestationAuthority
        """
        return self._attestation_authority

    @attestation_authority.setter
    def attestation_authority(self, attestation_authority):
        """Sets the attestation_authority of this ApiNote.

        A note describing an attestation role.  # noqa: E501

        :param attestation_authority: The attestation_authority of this ApiNote.  # noqa: E501
        :type: ApiAttestationAuthority
        """

        self._attestation_authority = attestation_authority

    @property
    def related_url(self):
        """Gets the related_url of this ApiNote.  # noqa: E501

        URLs associated with this note.  # noqa: E501

        :return: The related_url of this ApiNote.  # noqa: E501
        :rtype: list[NoteRelatedUrl]
        """
        return self._related_url

    @related_url.setter
    def related_url(self, related_url):
        """Sets the related_url of this ApiNote.

        URLs associated with this note.  # noqa: E501

        :param related_url: The related_url of this ApiNote.  # noqa: E501
        :type: list[NoteRelatedUrl]
        """

        self._related_url = related_url

    @property
    def expiration_time(self):
        """Gets the expiration_time of this ApiNote.  # noqa: E501

        Time of expiration for this note, null if note does not expire.  # noqa: E501

        :return: The expiration_time of this ApiNote.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, expiration_time):
        """Sets the expiration_time of this ApiNote.

        Time of expiration for this note, null if note does not expire.  # noqa: E501

        :param expiration_time: The expiration_time of this ApiNote.  # noqa: E501
        :type: datetime
        """

        self._expiration_time = expiration_time

    @property
    def create_time(self):
        """Gets the create_time of this ApiNote.  # noqa: E501

        Output only. The time this note was created. This field can be used as a filter in list requests.  # noqa: E501

        :return: The create_time of this ApiNote.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ApiNote.

        Output only. The time this note was created. This field can be used as a filter in list requests.  # noqa: E501

        :param create_time: The create_time of this ApiNote.  # noqa: E501
        :type: datetime
        """

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ApiNote.  # noqa: E501

        Output only. The time this note was last updated. This field can be used as a filter in list requests.  # noqa: E501

        :return: The update_time of this ApiNote.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ApiNote.

        Output only. The time this note was last updated. This field can be used as a filter in list requests.  # noqa: E501

        :param update_time: The update_time of this ApiNote.  # noqa: E501
        :type: datetime
        """

        self._update_time = update_time

    @property
    def operation_name(self):
        """Gets the operation_name of this ApiNote.  # noqa: E501

        The name of the `Operation` in the form \"projects/{PROJECT_ID}/operations/{OPERATION_ID}\".  # noqa: E501

        :return: The operation_name of this ApiNote.  # noqa: E501
        :rtype: str
        """
        return self._operation_name

    @operation_name.setter
    def operation_name(self, operation_name):
        """Sets the operation_name of this ApiNote.

        The name of the `Operation` in the form \"projects/{PROJECT_ID}/operations/{OPERATION_ID}\".  # noqa: E501

        :param operation_name: The operation_name of this ApiNote.  # noqa: E501
        :type: str
        """

        self._operation_name = operation_name

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
        if issubclass(ApiNote, dict):
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
        if not isinstance(other, ApiNote):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
