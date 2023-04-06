# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.contractor_api_response import ContractorApiResponse  # noqa: E501
from swagger_server.models.login_response import LoginResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestContractorApiResponseController(BaseTestCase):
    """ContractorApiResponseController integration test stubs"""

    def test_delete_contractor(self):
        """Test case for delete_contractor

        deletes a specific contractor
        """
        response = self.client.open(
            '/api//contractors/{id}'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_contractor(self):
        """Test case for get_contractor

        get a contractor by id
        """
        response = self.client.open(
            '/api//contractors/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_contractors(self):
        """Test case for get_contractors

        get a list of all contractors
        """
        response = self.client.open(
            '/api//contractors',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_contractor(self):
        """Test case for patch_contractor

        update the details of a contractor by id
        """
        body = ContractorApiResponse()
        response = self.client.open(
            '/api//contractors/{id}'.format(id='id_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_contractor(self):
        """Test case for post_contractor

        create a new contractor
        """
        body = ContractorApiResponse()
        response = self.client.open(
            '/api//contractors',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
