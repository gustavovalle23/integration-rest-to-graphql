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
        id=data['id'],
        clube_id=data['clube_id'],
        logo_mobile=data['logo_mobile'],
        logo=data['logo'],
        nome=data['nome'],
        slug=data['slug'],
        matriz=data['matriz'],
        telefone=data['telefone'],
        whatsapp=data['whatsapp'],
        cidade=Cidade(
            nome=data['cidade']['nome'],
            ibge=data['cidade']['ibge'],
            estado=Estado(
                nome=data['cidade']['estado']['nome'],
                uf=data['cidade']['estado']['uf'],
                ibge=data['cidade']['estado']['ibge'],
            )
        ),
        cep=data['cep'],
        bairro=data['bairro'],
        rua=data['rua'],
        numero=data['numero'],
        complemento=data['complemento'],
        tipo_logistica=data['tipo_logistica'],
        pagamento_online_retirada=data['pagamento_online_retirada'],
        observacao_carrinho=data['observacao_carrinho'],
        tags_observacao_produto=data['tags_observacao_produto'],
        exige_numero_valido_compra_online=data['exige_numero_valido_compra_online'],
        label_alternativa_resumo=data['label_alternativa_resumo'],
        exibir_alternativa_resumo=data['exibir_alternativa_resumo'],
        latitude=data['latitude'],
        longitude=data['longitude'],
        liberar_loja_vendas_externas=data['liberar_loja_vendas_externas'],
        pagina_sugestao_produto=data['pagina_sugestao_produto'],
        usar_clearsale=data['usar_clearsale']
    )
