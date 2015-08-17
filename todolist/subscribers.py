from pyramid.events import subscriber, BeforeRender


@subscriber(BeforeRender)
def add_user(event):
    request = event.get('request')
    if request.user:
        event.update({
            'user': request.user.dict(),
        })
    else:
        event.update({
            'user': {
                'is_login': False,
            }
        })
