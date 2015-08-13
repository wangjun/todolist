from pyramid.events import subscriber, BeforeRender


@subscriber(BeforeRender)
def add_user(event):
    event.update({
        'user': {
            'name': 'x',
            'xx': True,
        },
    })
