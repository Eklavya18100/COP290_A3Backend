import connexion
import six

from swagger_server.models.product_api_response import ProductApiResponse  # noqa: E501
from swagger_server import util


def delete_product(id):  # noqa: E501
    """deletes a specific product

    deletes a specific product by id # noqa: E501

    :param id: ID of product that needs to be deleted
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def get_product(id):  # noqa: E501
    """get a product by id

    retrieves a specific product by id. # noqa: E501

    :param id: ID of product that needs to be fetched
    :type id: str

    :rtype: ProductApiResponse
    """
    return 'do some magic!'


def get_product_by_tags(location=None, category=None):  # noqa: E501
    """gets all products matching the tags

    gets all products matching the tags # noqa: E501

    :param location: location name
    :type location: str
    :param category: category name
    :type category: str

    :rtype: ProductApiResponse
    """
    return 'do some magic!'


def get_products():  # noqa: E501
    """get a list of all products

    retrieves all products. # noqa: E501


    :rtype: List[ProductApiResponse]
    """
    return 'do some magic!'


def patch_product(body, id):  # noqa: E501
    """update the details of a product by id

    updates the details of a product by passing parameters to be changed # noqa: E501

    :param body: updates a new product
    :type body: dict | bytes
    :param id: ID of product that needs to be updated
    :type id: str

    :rtype: ProductApiResponse
    """
    if connexion.request.is_json:
        body = ProductApiResponse.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def post_product(body):  # noqa: E501
    """create a new product

    create a new product # noqa: E501

    :param body: creates a new product
    :type body: dict | bytes

    :rtype: ProductApiResponse
    """
    if connexion.request.is_json:
        body = ProductApiResponse.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
