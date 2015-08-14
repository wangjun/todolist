from pyramid.view import view_config


@view_config(route_name='login', request_method='POST', renderer='json')
def login(request):
    return {'project': 'todolist'}
