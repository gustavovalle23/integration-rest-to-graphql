import requests

from definitions.product_search import ProductSearch
from definitions.base.product_search import ProductSearch as ProductSearchDTO


def _request(loja_id: int, q: str, page: int, menor_preco: float,
             maior_preco: float, ordem: str) -> dict:

    params = {
        'loja_id': loja_id,
        'q': q,
        'page': page,
        'menor_preco': menor_preco,
        'maior_preco': maior_preco,
        'ordem': ordem
    }

    return requests.get(
        f'https://sandbox.carrinhocerto.com.br/api/busca/v2/', params=params
    ).json()[0]


def get_data_product_search_from_rest(loja_id: int, q: str, page: int,
                                      menor_preco: float, maior_preco: float,
                                      ordem: str) -> ProductSearch:

    data = _request(loja_id, q, page, menor_preco, maior_preco, ordem)
    dto = ProductSearchDTO.parse_obj(data)
    return ProductSearch(**dict(dto))
