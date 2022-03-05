import json
import requests

from definitions.company import Company, FacebookLogin, GoogleLogin


def _request() -> dict:
    return requests.get('https://sandbox.carrinhocerto.com.br/api/dados-empresa/v2/').json()


def get_data_company_from_rest():
    data = _request()

    return Company(
        logo=data['logo'],
        logo_mobile=data['logo_mobile'],
        dominio=data['dominio'],
        endereco_facebook=data['endereco_facebook'],
        endereco_twitter=data['endereco_twitter'],
        endereco_instagram=data['endereco_instagram'],
        endereco_youtube=data['endereco_youtube'],
        email_contato=data['email_contato'],
        ramo=data['ramo'],
        possui_politica_privacidade=data['possui_politica_privacidade'],
        qtd_lojas_ativas=data['qtd_lojas_ativas'],
        onesignal_app_id=data['onesignal_app_id'],
        build_minimo_app=data['build_minimo_app'],
        key_api_google=data['key_api_google'],
        facebook_login=FacebookLogin(
            client_id=data['facebook_login'].get('client_id', ''),
            secret=data['facebook_login'].get('secret', '')
        ),
        google_login=GoogleLogin(
            client_id=data['google_login'].get('client_id', ''),
            secret=data['google_login'].get('secret', '')
        ),
        loja_com_geolocalizacao=data['loja_com_geolocalizacao'],
        tags_observacao_produto=data['tags_observacao_produto'],
        data_nascimento_obrigatoria=data['data_nascimento_obrigatoria'],
        telefone_cadastro_inicial=data['telefone_cadastro_inicial'],
        imagem_bg_home=data['imagem_bg_home'],
        utilizar_google_places=data['utilizar_google_places'],
        script_analytics=data['script_analytics'],
        script_google_sent_to=data['script_google_sent_to'],
        script_chat=data['script_chat'],
        script_tag_manager_head=data['script_tag_manager_head'],
        script_tag_manager_body=data['script_tag_manager_body'],
        script_pixel_facebook=data['script_pixel_facebook'],
        script_google_merchant=data['script_google_merchant'],
        key_api_google_site=data['key_api_google_site'],
        filtro_por_geolocalizacao=data['filtro_por_geolocalizacao'],
    )
