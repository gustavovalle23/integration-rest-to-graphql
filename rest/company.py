import requests

from definitions.company import Company
from definitions.base.company import Company as CompanyDTO


def _request() -> dict:
    return requests.get(
        'https://sandbox.carrinhocerto.com.br/api/dados-empresa/v2/'
    ).json()


def get_data_company_from_rest() -> Company:
    data = _request()
    dto = CompanyDTO.parse_obj(data)
    return Company(**dict(dto))
