from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel


class OrdemDisponiveis(BaseModel):
    relevancia: str
    mais_baratos: str
    mais_caros: str
    a_z: str
    z_a: str


class Infos(BaseModel):
    total_registros: int
    departamento: str
    ordem: str
    ordem_disponiveis: OrdemDisponiveis
    preco_menor: float
    preco_maior: float
    has_next: bool
    total_pages: int


class Marca(BaseModel):
    nome: str
    slug: str


class Modelo(BaseModel):
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


class Variacao(BaseModel):
    id: int
    nome: str
    percentual: float
    padrao: bool


class Produto(BaseModel):
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


class ProductSearch(BaseModel):
    infos: Infos
    produtos: List[Produto]
    marcas: List[Marca]
