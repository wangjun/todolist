from pyramid.view import view_config
from pyramid.httpexceptions import HTTPBadRequest
from todolist import utils
from todolist.forms.user import LoginForm
from todolist.models.user import User


@view_config(route_name='login', request_method='POST', renderer='json')
def login(request):
    form = LoginForm(**request.json)
    if not form.validate():
        raise HTTPBadRequest()

    user = User.query().filter(User.email == unicode(form.email.data)).first()
    if not user or user.password != utils.hash_password(form.password.data):
        raise HTTPBadRequest()

    request.session['user_id'] = user.id
    return user.dict()
