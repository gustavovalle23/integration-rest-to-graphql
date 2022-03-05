import json
import requests

from definitions.product_search import (
    Infos, Marca, Modelo, OrdemDisponiveis, ProductSearch, Produto, Variacao
)


def _request(loja_id: int, q: str, page: int,
             menor_preco: float, maior_preco: float, ordem: str) -> dict:

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

    with open('productSearch.json') as json_file:
        data: dict = json.load(json_file)[0]

    # data = _request(loja_id, q, page, menor_preco, maior_preco, ordem)
    infos = data['infos']
    produtos = data['produtos']
    marcas = data['marcas']

    return ProductSearch(
        Infos(
            infos['total_registros'],
            infos['ordem'],
            OrdemDisponiveis(
                infos['ordem_disponiveis']['Relevância'],
                infos['ordem_disponiveis']['Mais baratos'],
                infos['ordem_disponiveis']['Mais Caros'],
                infos['ordem_disponiveis']['A-Z'],
                infos['ordem_disponiveis']['Z-A']
            ),
            infos['preco_menor'],
            infos['preco_maior'],
            infos['has_next'],
            infos['total_pages']
        ),
        [Produto(
            produto['id'],
            produto['codigo'],
            produto['preco'],
            produto['preco_com_desconto'],
            produto['data_validade_promocao'],
            produto['vencimento_promocao'],
            produto['limite_promocao_carrinho'],
            produto['desconto'],
            produto['data_validade'],
            produto['vencimento'],
            produto['estoque'],
            [Variacao(
                variacao['id'],
                variacao['nome'],
                variacao['percentual'],
                variacao['padrao']
            ) for variacao in produto['variacao']],
            Modelo(
                produto['modelo']['nome'],
                produto['modelo']['slug'],
                produto['modelo']['medida'],
                produto['modelo']['departamento'],
                produto['modelo']['departamento_id'],
                produto['modelo']['marca'],
                produto['modelo']['descricao'],
                produto['modelo']['descricao_quantidade'],
                produto['modelo']['imagem'],
                produto['modelo']['tabela_nutricional'],
                produto['modelo']['apenas_retirada'],
                produto['modelo']['prescricao_medica'],
                produto['modelo']['bula'],
                produto['modelo']['principio_ativo'],
                produto['modelo']['peso_inicial'],
                produto['modelo']['peso_de_acrescimo']
            )
        ) for produto in produtos],
        [Marca(
            marca['nome'],
            marca['slug']
        ) for marca in marcas]
    )
