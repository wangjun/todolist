from pyramid.view import view_config
from pyramid.httpexceptions import HTTPBadRequest
from pyramid.security import (
    remember,
    forget,
)
from todolist import utils
from todolist.forms.user import LoginForm
from todolist.models.user import User


@view_config(route_name='login', request_method='POST', renderer='json')
def login(request):
    form = LoginForm(**request.json)
    if not form.validate():
        raise HTTPBadRequest()

    user = User.query().filter(User.email == form.email.data).first()
    if not user or user.password != utils.hash_password(form.password.data):
        raise HTTPBadRequest()

    remember(request, user.id)
    return user.dict()

@view_config(route_name='logout', permission='login', request_method='POST', renderer='json')
def logout(request):
    forget(request)
    return {}

@view_config(route_name='get_my_information', permission='login', request_method='GET', renderer='json')
def get_my_information(request):
    return request.user.dict()
