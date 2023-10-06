from aiohttp import web
from models.connectionsPools import MongoPoolConnection


async def check_rights(request):
    """Функция проверяет наличие прав на проведение операции"""
    if request.method == "GET":
        expected_params = {"restaurantid", "userid", "operation"}
        expected_len = len(expected_params)
        query_params = request.query

        if len(query_params) != expected_len:
            return web.json_response({
                "status": "error",
                "errors": f"Invalid length. Expected: {expected_len}",
                "access": False,
            })

        if query_params.keys() != expected_params:
            return web.json_response({
                "status": "error",
                "errors": f"Wrong params ",
                "access": False,
            })

        print(query_params, type(query_params), len(query_params))
        query_param = query_params.get('userid')
        print(query_param)
    return web.Response(text=f"Query param {query_params}")


async def change_rights(request):
    pass


async def give_role_to_new_worker(request):
    pass


async def simple_json_route(request):
    data = {'message': 'Hello, World!'}
    return web.json_response(data)
