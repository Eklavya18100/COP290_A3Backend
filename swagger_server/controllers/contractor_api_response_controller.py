import connexion
import six

from swagger_server.models.contractor_api_response import ContractorApiResponse  # noqa: E501
from swagger_server.models.login_response import LoginResponse  # noqa: E501
from swagger_server import util


def delete_contractor(id):  # noqa: E501
    """deletes a specific contractor

    deletes a specific contractor by id # noqa: E501

    :param id: ID of contractor that needs to be deleted
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def get_contractor(id):  # noqa: E501
    """get a contractor by id

    retrieves a specific contractor by id. # noqa: E501

    :param id: ID of contractor that needs to be fetched
    :type id: str

    :rtype: ContractorApiResponse
    """
    return 'do some magic!'


def get_contractors():  # noqa: E501
    """get a list of all contractors

    retrieves all contractors. # noqa: E501


    :rtype: List[ContractorApiResponse]
    """
    return 'do some magic!'


def patch_contractor(body, id):  # noqa: E501
    """update the details of a contractor by id

    updates the details of a contractor by passing parameters to be changed # noqa: E501

    :param body: updates a new contractor
    :type body: dict | bytes
    :param id: ID of contractor that needs to be updated
    :type id: str

    :rtype: ContractorApiResponse
    """
    if connexion.request.is_json:
        body = ContractorApiResponse.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def post_contractor(body):  # noqa: E501
    """create a new contractor

    create a new contractor given all details of contractor while signing up # noqa: E501

    :param body: creates a new contractor
    :type body: dict | bytes

    :rtype: LoginResponse
    """
    if connexion.request.is_json:
        body = ContractorApiResponse.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
