from typing import Optional
from pydantic import BaseModel


class FacebookLogin(BaseModel):
    client_id: Optional[str]
    secret: Optional[str]


class GoogleLogin(BaseModel):
    client_id: Optional[str]
    secret: Optional[str]


class Company(BaseModel):
    logo: str
    logo_mobile: str
    dominio: str
    endereco_facebook: str
    endereco_twitter: str
    endereco_instagram: str
    endereco_youtube: str
    email_contato: str
    ramo: str
    possui_politica_privacidade: bool
    qtd_lojas_ativas: int
    onesignal_app_id: Optional[str]
    build_minimo_app: int
    key_api_google: str
    facebook_login: FacebookLogin
    google_login: GoogleLogin
    loja_com_geolocalizacao: bool
    tags_observacao_produto: str
    data_nascimento_obrigatoria: bool
    telefone_cadastro_inicial: bool
    imagem_bg_home: str
    utilizar_google_places: bool
    script_analytics: str
    script_google_sent_to: str
    script_chat: str
    script_tag_manager_head: str
    script_tag_manager_body: str
    script_pixel_facebook: str
    script_google_merchant: str
    key_api_google_site: str
    filtro_por_geolocalizacao: bool
