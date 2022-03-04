from enum import Enum
from typing import Optional, List

import strawberry


@strawberry.type
class OrdemDisponiveis:
    relevância: str
    mais_baratos: str
    mais_caros: str
    a_z: str
    z_a: str

    def __init__(
            self, relevância: str, mais_baratos: str,
            mais_caros: str, a_z: str, z_a: str
    ) -> None:

        self.relevância = relevância
        self.mais_baratos = mais_baratos
        self.mais_caros = mais_caros
        self.a_z = a_z
        self.z_a = z_a


@strawberry.type
class Infos:
    total_registros: int
    ordem: str
    ordem_disponiveis: OrdemDisponiveis
    preco_menor: float
    preco_maior: float
    has_next: bool
    total_pages: int

    def __init__(
            self, total_registros: int, ordem: str,
            ordem_disponiveis: OrdemDisponiveis, preco_menor: float,
            preco_maior: float, has_next: bool, total_pages: int
    ) -> None:

        self.total_registros = total_registros
        self.ordem = ordem
        self.ordem_disponiveis = ordem_disponiveis
        self.preco_menor = preco_menor
        self.preco_maior = preco_maior
        self.has_next = has_next
        self.total_pages = total_pages


@strawberry.type
class Marca:
    nome: str
    slug: str

    def __init__(self, nome: str, slug: str) -> None:
        self.nome = nome
        self.slug = slug


@strawberry.type
class Departamento(Enum):
    BEBIDAS = 'Bebidas'
    CERVEJA = 'Cerveja'
    CERVEJAS = 'Cervejas'


@strawberry.type
class Modelo:
    nome: str
    slug: str
    medida: None
    departamento: Departamento
    departamento_id: int
    marca: Optional[str]
    descricao: str
    descricao_quantidade: str
    imagem: Optional[str]
    tabela_nutricional: Optional[str]
    apenas_retirada: bool
    prescricao_medica: bool
    bula: str
    principio_ativo: None
    peso_inicial: None
    peso_de_acrescimo: None

    def __init__(
            self, nome: str, slug: str, medida: None,
            departamento: Departamento, departamento_id: int,
            marca: Optional[str], descricao: str, descricao_quantidade: str,
            imagem: Optional[str], tabela_nutricional: Optional[str],
            apenas_retirada: bool, prescricao_medica: bool, bula: str,
            principio_ativo: None, peso_inicial: None, peso_de_acrescimo: None
    ) -> None:

        self.nome = nome
        self.slug = slug
        self.medida = medida
        self.departamento = departamento
        self.departamento_id = departamento_id
        self.marca = marca
        self.descricao = descricao
        self.descricao_quantidade = descricao_quantidade
        self.imagem = imagem
        self.tabela_nutricional = tabela_nutricional
        self.apenas_retirada = apenas_retirada
        self.prescricao_medica = prescricao_medica
        self.bula = bula
        self.principio_ativo = principio_ativo
        self.peso_inicial = peso_inicial
        self.peso_de_acrescimo = peso_de_acrescimo


@strawberry.type
class Variacao:
    id: int
    nome: str
    percentual: float
    padrao: bool

    def __init__(
        self, id: int, nome: str, percentual: float, padrao: bool
    ) -> None:

        self.id = id
        self.nome = nome
        self.percentual = percentual
        self.padrao = padrao


@strawberry.type
class Vencimento(Enum):
    EM_VALIDADE = 'em_validade'


@strawberry.type
class VencimentoPromocao(Enum):
    FORA_PROMOCAO = 'fora_promocao'


@strawberry.type
class Produto:
    id: int
    codigo: int
    preco: float
    preco_com_desconto: int
    data_validade_promocao: None
    vencimento_promocao: VencimentoPromocao
    limite_promocao_carrinho: int
    desconto: int
    data_validade: None
    vencimento: Vencimento
    estoque: float
    variacao: List[Variacao]
    modelo: Modelo


@strawberry.type
class ProductSearch:
    infos: Infos
    produtos: List[Produto]
    marcas: List[Marca]

    def __init__(
        self, infos: Infos, produtos: List[Produto], marcas: List[Marca]
    ) -> None:

        self.infos = infos
        self.produtos = produtos
        self.marcas = marcas
