from pyramid.security import (
    Everyone,
    Authenticated,
    Allow,
    )


class RootFactory(object):
    __acl__ = [
        (Allow, Everyone, 'everyone'),
        (Allow, Authenticated, 'login'),
    ]

    def __init__(self, request):
        pass  # pragma: no cover