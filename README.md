# Integration System between Rest API and GraphQL

> This project use [FastAPI](https://fastapi.tiangolo.com/) as web framework and [Strawberry](https://strawberry.rocks/) as GraphQL library

## Dependencies

All the dependencies for this project are listed in [requirements.txt](requirements.txt).

In order to make your global Python dependencies untouched locally use the [virtualenv](https://virtualenv.pypa.io/en/latest/):

```sh
# Create a virtual env
python3 -m venv venv

# Activate the virtual env
source venv/bin/activate

# Install dependencies inside virtual env
pip3 install -r requirements.txt

# To exit the virtual env you could execute the following command
deactivate
```

## Running server

To run server, just run:
```sh
python3 main.py
```
Or for auto reload:
```sh
uvicorn main:app --reload
```

## GraphQL
> To convert REST models in GraphQL types, strawberry provides dataclasses that make it easy

Types:
```graphql
type Cidade {
  nome: String!
  ibge: Int!
  estado: Estado!
}

type Company {
  logo: String!
  logoMobile: String!
  dominio: String!
  enderecoFacebook: String!
  enderecoTwitter: String!
  enderecoInstagram: String!
  enderecoYoutube: String!
  emailContato: String!
  ramo: String!
  possuiPoliticaPrivacidade: Boolean!
  qtdLojasAtivas: Int!
  onesignalAppId: String!
  buildMinimoApp: Int!
  keyApiGoogle: String!
  facebookLogin: FacebookLogin!
  googleLogin: GoogleLogin!
  lojaComGeolocalizacao: Boolean!
  tagsObservacaoProduto: String!
  dataNascimentoObrigatoria: Boolean!
  telefoneCadastroInicial: Boolean!
  imagemBgHome: String!
  utilizarGooglePlaces: Boolean!
  scriptAnalytics: String!
  scriptGoogleSentTo: String!
  scriptChat: String!
  scriptTagManagerHead: String!
  scriptTagManagerBody: String!
  scriptPixelFacebook: String!
  scriptGoogleMerchant: String!
  keyApiGoogleSite: String!
  filtroPorGeolocalizacao: Boolean!
}

"""Date with time (isoformat)"""
scalar DateTime

type Estado {
  nome: String!
  uf: String!
  ibge: Int!
}

type FacebookLogin {
  clientId: String!
  secret: String!
}

type GoogleLogin {
  clientId: String!
  secret: String!
}

type Infos {
  totalRegistros: Int!
  ordem: String!
  ordemDisponiveis: OrdemDisponiveis!
  precoMenor: Float!
  precoMaior: Float!
  hasNext: Boolean!
  totalPages: Int!
}

type Marca {
  nome: String!
  slug: String!
}

type Modelo {
  nome: String!
  slug: String!
  medida: Float
  departamento: String!
  departamentoId: Int!
  marca: String
  descricao: String!
  descricaoQuantidade: String!
  imagem: String
  tabelaNutricional: String
  apenasRetirada: Boolean!
  prescricaoMedica: Boolean!
  bula: String!
  principioAtivo: String
  pesoInicial: Float
  pesoDeAcrescimo: Float
}

type OrdemDisponiveis {
  relevancia: String!
  maisBaratos: String!
  maisCaros: String!
  aZ: String!
  zA: String!
}

type ProductSearch {
  infos: Infos!
  produtos: [Produto!]!
  marcas: [Marca!]!
}

type Produto {
  id: Int!
  codigo: Int!
  preco: Float!
  precoComDesconto: Int!
  dataValidadePromocao: DateTime
  vencimentoPromocao: String!
  limitePromocaoCarrinho: Int!
  desconto: Int!
  dataValidade: DateTime
  vencimento: String!
  estoque: Float!
  variacao: [Variacao!]!
  modelo: Modelo!
}

type Query {
  dadosEmpresa: Company!
  dadosLoja(id: Int!): Store!
  listingOfSearch(lojaId: Int!, q: String!, page: Int!, menorPreco: Float!, maiorPreco: Float!, ordem: String!): ProductSearch!
  listingDepartment(lojaId: Int!, departamentoId: Int!): ProductSearch!
}

type Store {
  id: Int!
  clubeId: String
  logoMobile: String!
  logo: String!
  nome: String!
  slug: String!
  matriz: Boolean!
  telefone: String!
  whatsapp: String!
  cidade: Cidade!
  cep: String!
  bairro: String!
  rua: String!
  numero: Int!
  complemento: String
  tipoLogistica: String!
  pagamentoOnlineRetirada: Boolean!
  observacaoCarrinho: String!
  tagsObservacaoProduto: String!
  exigeNumeroValidoCompraOnline: Boolean!
  labelAlternativaResumo: String!
  exibirAlternativaResumo: Boolean!
  latitude: String!
  longitude: String!
  liberarLojaVendasExternas: Boolean!
  paginaSugestaoProduto: Boolean!
  usarClearsale: Boolean!
}

type Variacao {
  id: Int!
  nome: String!
  percentual: Float!
  padrao: Boolean!
}
````


Example of query: [example.graphql](example.graphql).