from datetime import datetime
from typing import Optional, List, Any
from enum import Enum

import strawberry


@strawberry.type
class OrdemDisponiveis:
    relevancia: str
    mais_baratos: str
    mais_caros: str
    a_z: str
    z_a: str


@strawberry.type
class Infos:
    total_registros: int
    departamento: str # check the possibility of Optional in product_search
    ordem: str
    ordem_disponiveis: OrdemDisponiveis
    preco_menor: float
    preco_maior: float
    has_next: bool
    total_pages: int


@strawberry.type
class Marca:
    nome: str
    slug: str


@strawberry.type
class Modelo:
    nome: str
    slug: str
    medida: Optional[float]
    departamento: str
    departamento_id: int
    marca: Optional[str]
    descricao: str
    descricao_quantidade: str
    imagem: Optional[str]
    tabela_nutricional: Optional[str]
    apenas_retirada: bool
    prescricao_medica: bool
    bula: str
    principio_ativo: Optional[str]
    peso_inicial: Optional[float]
    peso_de_acrescimo: Optional[float]


@strawberry.type
class Variacao:
    id: int
    nome: str
    percentual: float
    padrao: bool


@strawberry.type
class Produto:
    id: int
    codigo: int
    preco: float
    preco_com_desconto: int
    data_validade_promocao: Optional[datetime]
    vencimento_promocao: str
    limite_promocao_carrinho: int
    desconto: int
    data_validade: Optional[datetime]
    vencimento: str
    estoque: float
    variacao: List[Variacao]
    modelo: Modelo


@strawberry.type
class ProductSearch:
    infos: Infos
    produtos: List[Produto]
    marcas: List[Marca]
