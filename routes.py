from handlers.handlers import check_rights, change_rights, simple_json_route
from aiohttp import web


def setup_routes(app):
    app.router.add_get('/rights', check_rights)
    app.router.add_post('/rights', change_rights)
    app.router.add_get('/api/hello', simple_json_route)
