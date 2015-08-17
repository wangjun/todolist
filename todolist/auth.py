from pyramid.security import unauthenticated_userid
from todolist.models.user import User


def authentication(request):
    user_id = unauthenticated_userid(request)
    user = User.query().get(user_id)
    return user

def find_user_group(user_id, request):
    if request.user:
        return ('group:normal',)
    else:
        return ()
