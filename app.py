import fastapi
import database
import pydantic_models
import config

api = fastapi.FastAPI()

response = {"Ответ": "Который возвращает сервер"}


@api.get('/')
def index():
    return response


@api.get('/grem')
def grem():
    return 'hi,grem'


@api.get('/our/contacts')
def about_us():
    return {'hi': 'here is our contacts'}
