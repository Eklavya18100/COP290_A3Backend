# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.orders import Orders  # noqa: E501
from swagger_server.test import BaseTestCase


class TestOrdersController(BaseTestCase):
    """OrdersController integration test stubs"""

    def test_delete_customer_order(self):
        """Test case for delete_customer_order

        deletes a specific customer's order by id of both
        """
        response = self.client.open(
            '/api//customers/{id}/orders/{orderid}'.format(id='id_example', orderid='orderid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_customer_order(self):
        """Test case for get_customer_order

        get a customer's specific order by id of both
        """
        response = self.client.open(
            '/api//customers/{id}/orders/{orderid}'.format(id='id_example', orderid='orderid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_customer_orders(self):
        """Test case for get_customer_orders

        get a list of all orders of a specific customers
        """
        response = self.client.open(
            '/api//customers/{id}/orders'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_customer_order(self):
        """Test case for patch_customer_order

        update the details of a customer's specific order by id of both
        """
        body = Orders()
        response = self.client.open(
            '/api//customers/{id}/orders/{orderid}'.format(id='id_example', orderid='orderid_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_order(self):
        """Test case for post_order

        create a new order for a customer with given id
        """
        body = Orders()
        response = self.client.open(
            '/api//customers/{id}/orders'.format(id='id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
