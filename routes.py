from handlers.handlers import check_right, simple_json_route
from aiohttp import web


def setup_routes(app):
    app.router.add_get('/', check_right)
    app.router.add_get('/api/hello', simple_json_route)
