import fastapi

api = fastapi.FastAPI()

@api.get('/hello')
def api_hello():
    return {"hello":'from meeeeee!'}