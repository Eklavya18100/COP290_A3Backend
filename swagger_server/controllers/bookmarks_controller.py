import connexion
import six

from swagger_server.models.bookmarks import Bookmarks  # noqa: E501
from swagger_server import util


def delete_customer_bookmark(id, bookmarkid):  # noqa: E501
    """deletes a specific customer&#x27;s bookmark by id of both

    deletes a specific customer&#x27;s bookmark by id of both # noqa: E501

    :param id: ID of customer whose bookmark needs to be deleted
    :type id: str
    :param bookmarkid: ID of bookmark that needs to be deleted
    :type bookmarkid: str

    :rtype: None
    """
    return 'do some magic!'


def get_customer_bookmark(id, bookmarkid):  # noqa: E501
    """get a customer&#x27;s specific bookmark by id of both

    retrieves a specific bookmark by id of customer and order # noqa: E501

    :param id: ID of customer
    :type id: str
    :param bookmarkid: ID of bookmark that needs to be fetched
    :type bookmarkid: str

    :rtype: Bookmarks
    """
    return 'do some magic!'


def get_customer_bookmarks(id):  # noqa: E501
    """get a list of all bookmarks of a specific customer

    fetches all bookmarks of a specific customer # noqa: E501

    :param id: ID of customer whose bookmark is needed
    :type id: str

    :rtype: List[Bookmarks]
    """
    return 'do some magic!'


def post_bookmark(body, id):  # noqa: E501
    """create a new bookmark for a customer with given id

    create a new bookamark for a customer with given id # noqa: E501

    :param body: creates a new bookmark for a specific customer
    :type body: dict | bytes
    :param id: ID of customer for which new bookmark has to be added
    :type id: str

    :rtype: Bookmarks
    """
    if connexion.request.is_json:
        body = Bookmarks.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
