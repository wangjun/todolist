from pyramid.view import view_config
from pyramid.httpexceptions import HTTPBadRequest
from todolist.forms import PageForm
from todolist.models import PageList
from todolist.models.event import Event


@view_config(route_name='get_my_events', permission='login', request_method='GET', renderer='json')
def get_my_events(request):
    """
    GET /api/me/events
    :param request:
    :return:
    """
    form = PageForm(**request.GET)
    if not form.validate():
        raise HTTPBadRequest()

    query = Event.query().filter(Event.user_id == request.user.id)\
        .order_by(Event.created_at.desc())\
        .limit(form.size.data).offset(form.index.data * form.size.data)
    events = query.all()
    total = query.count()
    return PageList(form.index.data, form.size.data, total, events).dict()
