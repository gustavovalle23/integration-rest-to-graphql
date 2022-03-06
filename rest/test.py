# class Cidade:
#     def __init__(self, nome) -> None:
#         self.nome = nome

#     def __str__(self) -> str:
#         return f'{self.nome}'


# class Store:
#     def __init__(self, id: int, cidade: Cidade) -> None:
#         self.id = id
#         self.cidade = cidade

#     def __str__(self) -> str:
#         return f'{self.id} - {self.cidade}'


# if __name__ == '__main__':
#     a = {'id': 1, 'cidade': {'nome': 'RP'}}
#     store = Store(**a)
#     print(store)


from typing import Optional
from pydantic import BaseModel


class City(BaseModel):
    nome: str


class StoreDTO(BaseModel):
    id: int
    club_id: Optional[int]
    logo_mobile: str
    city: City


a = {'id': 1, 'club_id': None,
     'logo_mobile': '//us-southea',
     'city': {'nome': 'RP'}}


s = StoreDTO.parse_obj(a)
print(dict(s))
