

def add_routers(config):
    config.add_route('base_view', '/')
    config.add_route('login', '/api/login')
    config.add_route('get_my_information', '/api/me')
