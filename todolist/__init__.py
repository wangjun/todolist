from pyramid.config import Configurator
from pyramid.authentication import SessionAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from . import routers
from . import views, subscribers
from .factories import RootFactory


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(
        settings=settings,
        root_factory=RootFactory,
        authentication_policy=SessionAuthenticationPolicy(),
        authorization_policy=ACLAuthorizationPolicy(),
    )
    config.include('plim.adapters.pyramid_renderer')
    config.include('pyramid_redis_sessions')
    config.add_static_view('static', 'static/dist', cache_max_age=3600)
    config.include(routers.add_routers)
    config.scan(views)
    config.scan(subscribers)
    return config.make_wsgi_app()
