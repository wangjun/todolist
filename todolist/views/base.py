from pyramid.view import view_config


@view_config(route_name='base_view', renderer='todolist:templates/base.plim')
def base_view(request):
    return {'project': 'todolist'}
