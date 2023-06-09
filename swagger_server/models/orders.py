# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Orders(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, cus_uid: str=None, order_date: datetime=None, p_uid: str=None, scheduling_status: str=None, payment_status: str=None, exchange_emails: str=None):  # noqa: E501
        """Orders - a model defined in Swagger

        :param id: The id of this Orders.  # noqa: E501
        :type id: str
        :param cus_uid: The cus_uid of this Orders.  # noqa: E501
        :type cus_uid: str
        :param order_date: The order_date of this Orders.  # noqa: E501
        :type order_date: datetime
        :param p_uid: The p_uid of this Orders.  # noqa: E501
        :type p_uid: str
        :param scheduling_status: The scheduling_status of this Orders.  # noqa: E501
        :type scheduling_status: str
        :param payment_status: The payment_status of this Orders.  # noqa: E501
        :type payment_status: str
        :param exchange_emails: The exchange_emails of this Orders.  # noqa: E501
        :type exchange_emails: str
        """
        self.swagger_types = {
            'id': str,
            'cus_uid': str,
            'order_date': datetime,
            'p_uid': str,
            'scheduling_status': str,
            'payment_status': str,
            'exchange_emails': str
        }

        self.attribute_map = {
            'id': 'id',
            'cus_uid': 'cus_uid',
            'order_date': 'order_date',
            'p_uid': 'p_uid',
            'scheduling_status': 'scheduling_status',
            'payment_status': 'payment_status',
            'exchange_emails': 'exchange_emails'
        }
        self._id = id
        self._cus_uid = cus_uid
        self._order_date = order_date
        self._p_uid = p_uid
        self._scheduling_status = scheduling_status
        self._payment_status = payment_status
        self._exchange_emails = exchange_emails

    @classmethod
    def from_dict(cls, dikt) -> 'Orders':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Orders of this Orders.  # noqa: E501
        :rtype: Orders
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Orders.


        :return: The id of this Orders.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Orders.


        :param id: The id of this Orders.
        :type id: str
        """

        self._id = id

    @property
    def cus_uid(self) -> str:
        """Gets the cus_uid of this Orders.

        customer id of the one who placed the order  # noqa: E501

        :return: The cus_uid of this Orders.
        :rtype: str
        """
        return self._cus_uid

    @cus_uid.setter
    def cus_uid(self, cus_uid: str):
        """Sets the cus_uid of this Orders.

        customer id of the one who placed the order  # noqa: E501

        :param cus_uid: The cus_uid of this Orders.
        :type cus_uid: str
        """

        self._cus_uid = cus_uid

    @property
    def order_date(self) -> datetime:
        """Gets the order_date of this Orders.


        :return: The order_date of this Orders.
        :rtype: datetime
        """
        return self._order_date

    @order_date.setter
    def order_date(self, order_date: datetime):
        """Sets the order_date of this Orders.


        :param order_date: The order_date of this Orders.
        :type order_date: datetime
        """

        self._order_date = order_date

    @property
    def p_uid(self) -> str:
        """Gets the p_uid of this Orders.

        product id of the product ordered  # noqa: E501

        :return: The p_uid of this Orders.
        :rtype: str
        """
        return self._p_uid

    @p_uid.setter
    def p_uid(self, p_uid: str):
        """Sets the p_uid of this Orders.

        product id of the product ordered  # noqa: E501

        :param p_uid: The p_uid of this Orders.
        :type p_uid: str
        """

        self._p_uid = p_uid

    @property
    def scheduling_status(self) -> str:
        """Gets the scheduling_status of this Orders.

        status of meeting scheduled  # noqa: E501

        :return: The scheduling_status of this Orders.
        :rtype: str
        """
        return self._scheduling_status

    @scheduling_status.setter
    def scheduling_status(self, scheduling_status: str):
        """Sets the scheduling_status of this Orders.

        status of meeting scheduled  # noqa: E501

        :param scheduling_status: The scheduling_status of this Orders.
        :type scheduling_status: str
        """
        allowed_values = ["completed", "confirmed", "pending"]  # noqa: E501
        if scheduling_status not in allowed_values:
            raise ValueError(
                "Invalid value for `scheduling_status` ({0}), must be one of {1}"
                .format(scheduling_status, allowed_values)
            )

        self._scheduling_status = scheduling_status

    @property
    def payment_status(self) -> str:
        """Gets the payment_status of this Orders.

        status of payment, if order confirmed on meeting  # noqa: E501

        :return: The payment_status of this Orders.
        :rtype: str
        """
        return self._payment_status

    @payment_status.setter
    def payment_status(self, payment_status: str):
        """Sets the payment_status of this Orders.

        status of payment, if order confirmed on meeting  # noqa: E501

        :param payment_status: The payment_status of this Orders.
        :type payment_status: str
        """
        allowed_values = ["meeting pending", "completed", "pending"]  # noqa: E501
        if payment_status not in allowed_values:
            raise ValueError(
                "Invalid value for `payment_status` ({0}), must be one of {1}"
                .format(payment_status, allowed_values)
            )

        self._payment_status = payment_status

    @property
    def exchange_emails(self) -> str:
        """Gets the exchange_emails of this Orders.

        email communication b/w customer and contractor  # noqa: E501

        :return: The exchange_emails of this Orders.
        :rtype: str
        """
        return self._exchange_emails

    @exchange_emails.setter
    def exchange_emails(self, exchange_emails: str):
        """Sets the exchange_emails of this Orders.

        email communication b/w customer and contractor  # noqa: E501

        :param exchange_emails: The exchange_emails of this Orders.
        :type exchange_emails: str
        """

        self._exchange_emails = exchange_emails
