from typing import Optional
import strawberry


@strawberry.type
class Estado:
    nome: str
    uf: str
    ibge: int


@strawberry.type
class Cidade:
    nome: str
    ibge: int
    estado: Estado


@strawberry.type
class Store:
    id: int
    clube_id: Optional[str]
    logo_mobile: str
    logo: str
    nome: str
    slug: str
    matriz: bool
    telefone: str
    whatsapp: str
    cidade: Cidade
    cep: str
    bairro: str
    rua: str
    numero: int
    complemento: Optional[str]
    tipo_logistica: str
    pagamento_online_retirada: bool
    observacao_carrinho: str
    tags_observacao_produto: str
    exige_numero_valido_compra_online: bool
    label_alternativa_resumo: Optional[str]
    exibir_alternativa_resumo: bool
    latitude: str
    longitude: str
    liberar_loja_vendas_externas: bool
    pagina_sugestao_produto: bool
    usar_clearsale: bool

