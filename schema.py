from typing import List
import strawberry

from definitions.company import Company
from definitions.product_search import ProductSearch
from definitions.store import Store
from rest.company import get_data_company_from_rest
from rest.product_search import get_data_product_search_from_rest
from rest.store import get_data_loja_from_rest


@strawberry.type
class Query:

    @strawberry.field
    def dados_empresa() -> Company:
        return get_data_company_from_rest()

    @strawberry.field
    def dados_loja(id: int) -> Store:
        return get_data_loja_from_rest(id)

    @strawberry.field
    def listing_of_search(loja_id: int, q: str, page: int,
                          menor_preco: float, maior_preco: float,
                          ordem: str) -> ProductSearch:
        return get_data_product_search_from_rest(loja_id, q, page, menor_preco,
                                                 maior_preco, ordem)
