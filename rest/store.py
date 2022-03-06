import json
import requests

from definitions.store import Cidade, Estado, Store


def _request(id: int) -> dict:
    params = {'loja_id': id}
    return requests.get(
        f'https://sandbox.carrinhocerto.com.br/api/dados-loja/v2/',
        params=params
    ).json()[0]


def get_data_loja_from_rest(id) -> Store:
    data = _request(id)

    return Store(
        data['id'],
        data['clube_id'],
        data['logo_mobile'],
        data['logo'],
        data['nome'],
        data['slug'],
        data['matriz'],
        data['telefone'],
        data['whatsapp'],
        Cidade(
            data['cidade']['nome'],
            data['cidade']['ibge'],
            Estado(
                data['cidade']['estado']['nome'],
                data['cidade']['estado']['uf'],
                data['cidade']['estado']['ibge'],
            )
        ),
        data['cep'],
        data['bairro'],
        data['rua'],
        data['numero'],
        data['complemento'],
        data['tipo_logistica'],
        data['pagamento_online_retirada'],
        data['observacao_carrinho'],
        data['tags_observacao_produto'],
        data['exige_numero_valido_compra_online'],
        data['label_alternativa_resumo'],
        data['exibir_alternativa_resumo'],
        data['latitude'],
        data['longitude'],
        data['liberar_loja_vendas_externas'],
        data['pagina_sugestao_produto'],
        data['usar_clearsale']
    )
