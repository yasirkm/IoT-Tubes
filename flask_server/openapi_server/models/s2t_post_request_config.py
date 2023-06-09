# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class S2tPostRequestConfig(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, encoding=None, sample_rate_hertz=None, language_code=None):  # noqa: E501
        """S2tPostRequestConfig - a model defined in OpenAPI

        :param encoding: The encoding of this S2tPostRequestConfig.  # noqa: E501
        :type encoding: str
        :param sample_rate_hertz: The sample_rate_hertz of this S2tPostRequestConfig.  # noqa: E501
        :type sample_rate_hertz: int
        :param language_code: The language_code of this S2tPostRequestConfig.  # noqa: E501
        :type language_code: str
        """
        self.openapi_types = {
            'encoding': str,
            'sample_rate_hertz': int,
            'language_code': str
        }

        self.attribute_map = {
            'encoding': 'encoding',
            'sample_rate_hertz': 'sampleRateHertz',
            'language_code': 'languageCode'
        }

        self._encoding = encoding
        self._sample_rate_hertz = sample_rate_hertz
        self._language_code = language_code

    @classmethod
    def from_dict(cls, dikt) -> 'S2tPostRequestConfig':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _s2t_post_request_config of this S2tPostRequestConfig.  # noqa: E501
        :rtype: S2tPostRequestConfig
        """
        return util.deserialize_model(dikt, cls)

    @property
    def encoding(self):
        """Gets the encoding of this S2tPostRequestConfig.


        :return: The encoding of this S2tPostRequestConfig.
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """Sets the encoding of this S2tPostRequestConfig.


        :param encoding: The encoding of this S2tPostRequestConfig.
        :type encoding: str
        """

        self._encoding = encoding

    @property
    def sample_rate_hertz(self):
        """Gets the sample_rate_hertz of this S2tPostRequestConfig.


        :return: The sample_rate_hertz of this S2tPostRequestConfig.
        :rtype: int
        """
        return self._sample_rate_hertz

    @sample_rate_hertz.setter
    def sample_rate_hertz(self, sample_rate_hertz):
        """Sets the sample_rate_hertz of this S2tPostRequestConfig.


        :param sample_rate_hertz: The sample_rate_hertz of this S2tPostRequestConfig.
        :type sample_rate_hertz: int
        """

        self._sample_rate_hertz = sample_rate_hertz

    @property
    def language_code(self):
        """Gets the language_code of this S2tPostRequestConfig.


        :return: The language_code of this S2tPostRequestConfig.
        :rtype: str
        """
        return self._language_code

    @language_code.setter
    def language_code(self, language_code):
        """Sets the language_code of this S2tPostRequestConfig.


        :param language_code: The language_code of this S2tPostRequestConfig.
        :type language_code: str
        """

        self._language_code = language_code