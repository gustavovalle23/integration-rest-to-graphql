import requests

from definitions.store import Store
from definitions.base.store import (Store as StoreDTO)


def _request(id: int) -> dict:
    params = {'loja_id': id}
    return requests.get(
        f'https://sandbox.carrinhocerto.com.br/api/dados-loja/v2/',
        params=params
    ).json()[0]


def get_data_loja_from_rest(id) -> Store:
    data = _request(id)
    dto = StoreDTO.parse_obj(data)
    return Store(**dict(dto))
