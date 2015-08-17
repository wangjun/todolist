from pyramid.events import subscriber, BeforeRender
import transaction


@subscriber(BeforeRender)
def add_user(event):
    request = event.get('request')
    if hasattr(request, 'user') and request.user:
        event.update({
            'user': request.user.dict(),
        })
    else:
        event.update({
            'user': {
                'is_login': False,
            }
        })

@subscriber(BeforeRender)
def commit(event):
    transaction.commit()
