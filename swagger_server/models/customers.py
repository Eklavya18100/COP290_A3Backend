# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Customers(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, cus_id: str=None, username: str=None, emailid: str=None, googleid: str=None, facebookid: str=None, phone_number: int=None, password: str=None):  # noqa: E501
        """Customers - a model defined in Swagger

        :param cus_id: The cus_id of this Customers.  # noqa: E501
        :type cus_id: str
        :param username: The username of this Customers.  # noqa: E501
        :type username: str
        :param emailid: The emailid of this Customers.  # noqa: E501
        :type emailid: str
        :param googleid: The googleid of this Customers.  # noqa: E501
        :type googleid: str
        :param facebookid: The facebookid of this Customers.  # noqa: E501
        :type facebookid: str
        :param phone_number: The phone_number of this Customers.  # noqa: E501
        :type phone_number: int
        :param password: The password of this Customers.  # noqa: E501
        :type password: str
        """
        self.swagger_types = {
            'cus_id': str,
            'username': str,
            'emailid': str,
            'googleid': str,
            'facebookid': str,
            'phone_number': int,
            'password': str
        }

        self.attribute_map = {
            'cus_id': 'cus_id',
            'username': 'username',
            'emailid': 'emailid',
            'googleid': 'googleid',
            'facebookid': 'facebookid',
            'phone_number': 'phone_number',
            'password': 'password'
        }
        self._cus_id = cus_id
        self._username = username
        self._emailid = emailid
        self._googleid = googleid
        self._facebookid = facebookid
        self._phone_number = phone_number
        self._password = password

    @classmethod
    def from_dict(cls, dikt) -> 'Customers':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Customers of this Customers.  # noqa: E501
        :rtype: Customers
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cus_id(self) -> str:
        """Gets the cus_id of this Customers.

        customer id  # noqa: E501

        :return: The cus_id of this Customers.
        :rtype: str
        """
        return self._cus_id

    @cus_id.setter
    def cus_id(self, cus_id: str):
        """Sets the cus_id of this Customers.

        customer id  # noqa: E501

        :param cus_id: The cus_id of this Customers.
        :type cus_id: str
        """

        self._cus_id = cus_id

    @property
    def username(self) -> str:
        """Gets the username of this Customers.


        :return: The username of this Customers.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this Customers.


        :param username: The username of this Customers.
        :type username: str
        """

        self._username = username

    @property
    def emailid(self) -> str:
        """Gets the emailid of this Customers.


        :return: The emailid of this Customers.
        :rtype: str
        """
        return self._emailid

    @emailid.setter
    def emailid(self, emailid: str):
        """Sets the emailid of this Customers.


        :param emailid: The emailid of this Customers.
        :type emailid: str
        """

        self._emailid = emailid

    @property
    def googleid(self) -> str:
        """Gets the googleid of this Customers.


        :return: The googleid of this Customers.
        :rtype: str
        """
        return self._googleid

    @googleid.setter
    def googleid(self, googleid: str):
        """Sets the googleid of this Customers.


        :param googleid: The googleid of this Customers.
        :type googleid: str
        """

        self._googleid = googleid

    @property
    def facebookid(self) -> str:
        """Gets the facebookid of this Customers.


        :return: The facebookid of this Customers.
        :rtype: str
        """
        return self._facebookid

    @facebookid.setter
    def facebookid(self, facebookid: str):
        """Sets the facebookid of this Customers.


        :param facebookid: The facebookid of this Customers.
        :type facebookid: str
        """

        self._facebookid = facebookid

    @property
    def phone_number(self) -> int:
        """Gets the phone_number of this Customers.


        :return: The phone_number of this Customers.
        :rtype: int
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number: int):
        """Sets the phone_number of this Customers.


        :param phone_number: The phone_number of this Customers.
        :type phone_number: int
        """

        self._phone_number = phone_number

    @property
    def password(self) -> str:
        """Gets the password of this Customers.


        :return: The password of this Customers.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """Sets the password of this Customers.


        :param password: The password of this Customers.
        :type password: str
        """

        self._password = password
