# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.register_response import RegisterResponse  # noqa: E501
from swagger_server.models.user_login import UserLogin  # noqa: E501
from swagger_server.models.user_register import UserRegister  # noqa: E501
from swagger_server.models.verify_email import VerifyEmail  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUserController(BaseTestCase):
    """UserController integration test stubs"""

    def test_email_login(self):
        """Test case for email_login

        email login
        """
        body = UserLogin()
        response = self.client.open(
            '/api//user/emailLogin',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_email_register(self):
        """Test case for email_register

        registration
        """
        body = UserRegister()
        response = self.client.open(
            '/api//user/emailRegister',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_send_verification_mail(self):
        """Test case for send_verification_mail

        verification email
        """
        headers = [('authorization', 'authorization_example')]
        response = self.client.open(
            '/api//user/sendVerificationMail',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_verify_email(self):
        """Test case for verify_email

        verify email
        """
        body = VerifyEmail()
        response = self.client.open(
            '/api//user/verifyEmail',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
