import fastapi
from fastapi import FastAPI
import pydantic_models
from database import crud

# import copy
# from database import crud
# import pydantic_models
# import config
# import fastapi
# from fastapi import FastAPI, Query, Body
api = FastAPI()


@api.put('/user/{user_id}')
def update_user(user_id: int,
                user: pydantic_models.User_to_update = fastapi.Body()):  # используя fastapi.Body() мы явно указываем, что отправляем информацию в теле запроса
    """Обновляем юзера"""
    if user_id == user.id:
        return crud.update_user(user).to_dict()


@api.delete('/user/{user_id}')
@crud.db_session
def delete_user(
        user_id: int = fastapi.Path()):  # используя fastapi.Path() мы явно указываем, что переменную нужно брать из пути
    """
    Удаляем юзера
    :param user_id:
    :return:
    """
    crud.get_user_by_id(user_id).delete()
    return True


@api.post('/user/create')
def create_user(user: pydantic_models.User_to_create):
    """
    Создаем Юзера
    :param user:
    :return:
    """
    return crud.create_user(tg_id=user.tg_ID,
                            nick=user.nick if user.nick else None).to_dict()


@api.get('/get_info_by_user_id/{user_id:int}')
@crud.db_session
def get_info_about_user(user_id):
    """
    Получаем инфу по юзеру
    :param user_id:
    :return:
    """
    return crud.get_user_info(crud.User[user_id])


@api.get('/get_user_balance_by_id/{user_id:int}')
@crud.db_session
def get_user_balance_by_id(user_id):
    """
    Получаем баланс юзера
    :param user_id:
    :return:
    """
    crud.update_wallet_balance(crud.User[user_id].wallet)
    return crud.User[user_id].wallet.balance


@api.get('/get_total_balance')
@crud.db_session
def get_total_balance():
    """
    Получаем общий баланс

    :return:
    """
    balance = 0.0
    crud.update_all_wallets()
    for user in crud.User.select()[:]:
        balance += user.wallet.balance
    return balance


@api.get("/users")
@crud.db_session
def get_users():
    """
    Получаем всех юзеров
    :return:
    """
    users = []
    for user in crud.User.select()[:]:
        users.append(user.to_dict())
    return users


@api.get("/user_by_tg_id/{tg_id:int}")
@crud.db_session
def get_user_by_tg_id(tg_id):
    """
    Получаем юзера по айди его ТГ
    :param tg_id:
    :return:
    """
    user = crud.get_user_info(crud.User.get(tg_ID=tg_id))
    return user
# @api.put('/user/{user_id}')
# def update_user(user_id: int, user: pydantic_models.User = fastapi.Body()): # используя fastapi.Body() мы явно указываем, что отправляем информацию в теле запроса
#     for index, u in enumerate(fake_database['users']): # так как в нашей бд юзеры хранятся в списке, нам нужно найти их индексы внутри этого списка
#         if u['id'] == user_id:
#             fake_database['users'][index] = user    # обновляем юзера в бд по соответствующему ему индексу из списка users
#             return user
# @api.delete('/user/{user_id}')
# def delete_user(user_id: int = fastapi.Path()): # используя fastapi.Path() мы явно указываем, что переменную нужно брать из пути
#     for index, u in enumerate(fake_database['users']): # так как в нашей бд юзеры хранятся в списке, нам нужно найти их индексы внутри этого списка
#         if u['id'] == user_id:
#             old_db = copy.deepcopy(fake_database) # делаем полную копию объекта в переменную old_db, чтобы было с чем сравнить
#             del fake_database['users'][index]    # удаляем юзера из бд
#             return {'old_db' : old_db,
#                     'new_db': fake_database}


# @api.post('/user/create')
# def create_user(user: pydantic_models.User):
#     fake_database['users'].append(user)
#     return {'User Created!': user}


# @api.get('/get_info_by_user_id/{id:int}')
# def get_info_about_user(id):
#     return fake_database['users'][id-1]


# @api.get('/get_user_balance_by_id/{id:int}')
# def get_user_balance_by_id(id):
#     return fake_database['users'][id-1]['balance']


# @api.get('/get_total_balance')
# def get_total_balance():
#     total_balance: float = 0.0
#     for user in fake_database['users']:
#         total_balance += pydantic_models.User(**user).balance
#     return total_balance


# @api.get("/users/")
# def get_users(skip: int = 0, limit: int = 10):
#     return fake_database['users'][skip: skip + limit]


# @api.get("/user/{user_id}")
# def read_user(user_id: str, query: str | None = None):
#     if query:
#         return {"item_id": user_id, "query": query}
#     return {"item_id": user_id}

# import fastapi
# from fastapi import Request     # позволяет нам перехватывать запрос и получать по нему всю информацию
# import database
# import pydantic_models
# import config
#
# api = fastapi.FastAPI()
#
# response = {"Ответ": "Который возвращает сервер"}
# fake_database = {'users':[
#     {
#         "id":1,             # тут тип данных - число
#         "name":"Anna",      # тут строка
#         "nick":"Anny42",    # и тут
#         "balance": 15300    # а тут float
#      },
#
#     {
#         "id":2,             # у второго пользователя
#         "name":"Dima",      # такие же
#         "nick":"dimon2319", # типы
#         "balance": 160.23     # данных
#      }
#     ,{
#         "id":3,             # у третьего
#         "name":"Vladimir",  # юзера
#         "nick":"Vova777",   # мы специально сделаем
#         "balance": "25000"     # нестандартный тип данных в его балансе
#      }
# ],}
#
#
# #@api.get('/')
# #def index():
# #    return response
#
#
# @api.get('/grem')
# def grem():
#     return 'hi,grem'
#
#
# @api.get('/user/{nick}')      # переменные в пути заключаются в фигурные скобки
# def get_nick(nick):           # в функцию передаем эту переменную и работаем с ней дальше
#     return {"user":nick}      # при запросе страницы вернет строку, которую мы вписали после последнего слеша
#
#
# @api.get('/userid/{id:int}')  # мы можем задавать тип данных прямо в пути через двоеточие
# def get_id(id):               # тут в пути обязательно должно быть число, иначе возникнет ошибка
#     return {"user":id}
#
#
# @api.get('/user_id/{id}')
# def get_id2(id: int):         # либо же его можно задавать как тайп-хинт прямо в функции
#     return {"user":id}      # возвращается число, а не строка, как было бы без объявления типа данных
#
#
# @api.get('/user_id_str/{id:str}')
# def get_id2(id):
#     return {"user":id}         # тут id - это уже строка, так как мы объявили тип данных
#
#
# @api.get('/test/{id:int}/{text:str}/{custom_path:path}')
# def get_test(id, text, custom_path):
#     return {"id":id,
#             "meow":text,
#             "custom_path": custom_path}
#
#
# @api.get('/get_info_by_user_id/{id:int}')
# def get_info_about_user(id):
#     return fake_database['users'][id-1]
#
# @api.get('/get_user_balance_by_id/{id:int}')
# def get_user_balance(id):
#     return fake_database['users'][id-1]['balance']
#
# #@api.get('/get_total_balance')
# #def get_total_balance():
# #    total_balance: float = 0.0
# #    for user in fake_database['users']:
# #        total_balance += user['balance']
# #    return total_balance
#
#
# @api.get('/get_total_balance')
# def get_total_balance():
#     total_balance: float = 0.0
#     for user in fake_database['users']:
#         total_balance += pydantic_models.User(**user).balance
#     return total_balance
#
#
# @api.get("/users/")
# def get_users(skip: int = 0, limit: int = 10):        #http://127.0.0.1:8000/users/?skip=0&limit=10
#     return fake_database['users'][skip: skip + limit]


# @api.get("/user/{user_id}")
# def read_user(user_id: str, query: str | None = None):
#    """
#    Тут значение по умолчанию для query будет None
#    """
#    if query:
#        return {"user_id": user_id, "query": query}
#    return {"user_id": user_id}


# @api.get('/')       # метод для обработки get запросов
# @api.post('/')      # метод для обработки post запросов
# @api.put('/')       # метод для обработки put запросов
# @api.delete('/')    # метод для обработки delete запросов
# def index(request: Request):  # тут request - будет объектом в котором хранится вся информация о запросе
#     return {"Request" : [request.method,    # тут наш API вернет клиенту метод, с которым этот запрос был совершен
#                          request.headers]}  # а тут в ответ вернутся все хедеры клиентского запроса
