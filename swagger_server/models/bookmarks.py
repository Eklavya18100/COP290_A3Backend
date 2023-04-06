# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Bookmarks(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, cus_uid: str=None, p_uid: str=None):  # noqa: E501
        """Bookmarks - a model defined in Swagger

        :param id: The id of this Bookmarks.  # noqa: E501
        :type id: str
        :param cus_uid: The cus_uid of this Bookmarks.  # noqa: E501
        :type cus_uid: str
        :param p_uid: The p_uid of this Bookmarks.  # noqa: E501
        :type p_uid: str
        """
        self.swagger_types = {
            'id': str,
            'cus_uid': str,
            'p_uid': str
        }

        self.attribute_map = {
            'id': 'id',
            'cus_uid': 'cus_uid',
            'p_uid': 'p_uid'
        }
        self._id = id
        self._cus_uid = cus_uid
        self._p_uid = p_uid

    @classmethod
    def from_dict(cls, dikt) -> 'Bookmarks':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Bookmarks of this Bookmarks.  # noqa: E501
        :rtype: Bookmarks
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Bookmarks.


        :return: The id of this Bookmarks.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Bookmarks.


        :param id: The id of this Bookmarks.
        :type id: str
        """

        self._id = id

    @property
    def cus_uid(self) -> str:
        """Gets the cus_uid of this Bookmarks.

        customer id of the one who placed the order  # noqa: E501

        :return: The cus_uid of this Bookmarks.
        :rtype: str
        """
        return self._cus_uid

    @cus_uid.setter
    def cus_uid(self, cus_uid: str):
        """Sets the cus_uid of this Bookmarks.

        customer id of the one who placed the order  # noqa: E501

        :param cus_uid: The cus_uid of this Bookmarks.
        :type cus_uid: str
        """

        self._cus_uid = cus_uid

    @property
    def p_uid(self) -> str:
        """Gets the p_uid of this Bookmarks.

        product id of the product bookamarked  # noqa: E501

        :return: The p_uid of this Bookmarks.
        :rtype: str
        """
        return self._p_uid

    @p_uid.setter
    def p_uid(self, p_uid: str):
        """Sets the p_uid of this Bookmarks.

        product id of the product bookamarked  # noqa: E501

        :param p_uid: The p_uid of this Bookmarks.
        :type p_uid: str
        """

        self._p_uid = p_uid
