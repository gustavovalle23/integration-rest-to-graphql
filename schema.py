from typing import List
import strawberry

from definitions.company import Company
from definitions.store import Store
from rest.company import get_data_company_from_rest
from rest.store import get_data_loja_from_rest


@strawberry.type
class Query:
    
    @strawberry.field
    def dados_empresa() -> Company:
        return get_data_company_from_rest()

    @strawberry.field
    def dados_loja(id: int) -> Store:
        return get_data_loja_from_rest(id)
