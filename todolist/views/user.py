from pyramid.view import view_config
from todolist.models.user import User


@view_config(route_name='login', request_method='POST', renderer='json')
def login(request):
    user = User.query().filter(User.email == 'kelp.chen@biideal.com.tw').first()
    return {'project': user.password}
