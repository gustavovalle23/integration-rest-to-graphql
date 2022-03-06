import requests

from definitions.product_department import ProductSearch
from definitions.base.product_search import ProductSearch as ProductSearchDTO


def _request(loja_id: int, departamento_id: int) -> dict:

    params = {'departamento_id': departamento_id, 'loja_id': loja_id}
    return requests.get(
        'https://sandbox.carrinhocerto.com.br/api/produtos-departamento/v2/',
        params=params
    ).json()[0]


def get_data_product_department_from_rest(loja_id: int,
                                      departamento_id: int) -> ProductSearch:

    data = _request(loja_id, departamento_id)
    dto = ProductSearchDTO.parse_obj(data)
    return ProductSearch(**dict(dto))
