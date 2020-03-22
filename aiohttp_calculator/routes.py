import pathlib

from aiohttp import web

from aiohttp_calculator.main.views import index, compute, results

PROJECT_PATH = pathlib.Path(__file__).parent


def init_routes(app: web.Application) -> None:
    add_route = app.router.add_route

    add_route('*', '/', index, name='index')
    add_route('*', '/compute', compute, name='compute')
    add_route('*', '/results', results, name='results')

    # added static dir
    app.router.add_static(
        '/static/',
        path=(PROJECT_PATH / 'static'),
        name='static',
    )
