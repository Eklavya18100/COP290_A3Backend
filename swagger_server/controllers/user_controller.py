import connexion
import six

from swagger_server.models.register_response import RegisterResponse  # noqa: E501
from swagger_server.models.user_login import UserLogin  # noqa: E501
from swagger_server.models.user_register import UserRegister  # noqa: E501
from swagger_server.models.verify_email import VerifyEmail  # noqa: E501
from swagger_server import util


def email_login(body):  # noqa: E501
    """email login

     # noqa: E501

    :param body: logs in the user
    :type body: dict | bytes

    :rtype: RegisterResponse
    """
    if connexion.request.is_json:
        body = UserLogin.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def email_register(body):  # noqa: E501
    """registration

     # noqa: E501

    :param body: registers the user
    :type body: dict | bytes

    :rtype: RegisterResponse
    """
    if connexion.request.is_json:
        body = UserRegister.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def send_verification_mail(authorization):  # noqa: E501
    """verification email

     # noqa: E501

    :param authorization: an authorization header
    :type authorization: str

    :rtype: None
    """
    return 'do some magic!'


def verify_email(body):  # noqa: E501
    """verify email

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = VerifyEmail.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
