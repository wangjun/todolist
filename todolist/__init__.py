from pyramid.config import Configurator
from pyramid.authentication import SessionAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from sqlalchemy import engine_from_config
from . import routers, views, subscribers, db
from .factories import RootFactory
from .auth import authentication


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    db.session.configure(bind=engine)

    config = Configurator(
        settings=settings,
        root_factory=RootFactory,
        authentication_policy=SessionAuthenticationPolicy(
            callback=authentication,
        ),
        authorization_policy=ACLAuthorizationPolicy(),
    )
    config.include('plim.adapters.pyramid_renderer')
    config.include('pyramid_redis_sessions')
    config.add_static_view('static', 'static/dist', cache_max_age=3600)
    config.include(routers.add_routers)
    config.scan(views)
    config.scan(subscribers)
    return config.make_wsgi_app()
