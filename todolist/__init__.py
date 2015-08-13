from pyramid.config import Configurator
from . import routers
from . import views, subscribers


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('plim.adapters.pyramid_renderer')
    config.add_static_view('static', 'static/dist', cache_max_age=3600)
    config.include(routers.add_routers)
    config.scan(views)
    config.scan(subscribers)
    return config.make_wsgi_app()
