from todolist.models.user import User


def authentication(user_id, request):
    user = User.query().get(user_id)
    request.user = user
    return ('group:normal')
