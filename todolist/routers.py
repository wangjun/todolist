

def add_routers(config):
    config.add_route('base_view', '/')

    # login, logout
    config.add_route('login', '/api/login')
    config.add_route('logout', '/api/logout')

    # /api/me
    config.add_route('my_information', '/api/me')
    config.add_route('my_events', '/api/me/events')
    config.add_route('my_event', '/api/me/events/{event_id:\d*}')
