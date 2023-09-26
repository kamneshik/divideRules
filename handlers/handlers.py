from aiohttp import web
from models.connectionsPools import MongoPoolConnection


async def check_right(request):
    if request.method == "GET":
        query_params = request.query
        print(query_params)
        query_param = query_params.get('query_param')
    return web.Response(text=f"Query param {query_params}")


async def simple_json_route(request):
    data = {'message': 'Hello, World!'}
    return web.json_response(data)
