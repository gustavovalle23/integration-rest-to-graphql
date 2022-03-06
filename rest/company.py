import requests

from definitions.company import Company, FacebookLogin, GoogleLogin


def _request() -> dict:
    return requests.get('https://sandbox.carrinhocerto.com.br/api/dados-empresa/v2/').json()


def get_data_company_from_rest() -> Company:
    data = _request()

    return Company(
        data['logo'],
        data['logo_mobile'],
        data['dominio'],
        data['endereco_facebook'],
        data['endereco_twitter'],
        data['endereco_instagram'],
        data['endereco_youtube'],
        data['email_contato'],
        data['ramo'],
        data['possui_politica_privacidade'],
        data['qtd_lojas_ativas'],
        data['onesignal_app_id'],
        data['build_minimo_app'],
        data['key_api_google'],
        FacebookLogin(
            client_id=data['facebook_login'].get('client_id', ''),
            secret=data['facebook_login'].get('secret', '')
        ),
        GoogleLogin(
            data['google_login'].get('client_id', ''),
            data['google_login'].get('secret', '')
        ),
        data['loja_com_geolocalizacao'],
        data['tags_observacao_produto'],
        data['data_nascimento_obrigatoria'],
        data['telefone_cadastro_inicial'],
        data['imagem_bg_home'],
        data['utilizar_google_places'],
        data['script_analytics'],
        data['script_google_sent_to'],
        data['script_chat'],
        data['script_tag_manager_head'],
        data['script_tag_manager_body'],
        data['script_pixel_facebook'],
        data['script_google_merchant'],
        data['key_api_google_site'],
        data['filtro_por_geolocalizacao'],
    )
