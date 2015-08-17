from pyramid.view import view_config
from pyramid.httpexceptions import HTTPBadRequest, HTTPNotFound, HTTPForbidden
from todolist.forms.page import PageForm
from todolist.forms.event import EventForm
from todolist.models.page_list import PageList
from todolist.models.event import Event


@view_config(route_name='my_events', permission='login', request_method='GET', renderer='json')
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

@view_config(route_name='my_events', permission='login', request_method='POST', renderer='json')
def add_my_event(request):
    """
    POST /api/me/events
    :param request:
    :return:
    """
    form = EventForm(**request.json)
    if not form.validate():
        raise HTTPBadRequest()

    event = Event()
    event.title = form.title.data
    event.description = form.description.data
    event.due_date = form.due_date.data
    event.user_id = request.user.id
    event.save()
    return event.dict()

@view_config(route_name='my_event', permission='login', request_method='DELETE', renderer='json')
def delete_my_event(request):
    """
    DELETE /api/me/events/<event_id>
    :param request:
    :param event_id:
    :return:
    """
    event = Event.query().get(request.matchdict.get('event_id'))
    if not event:
        raise HTTPNotFound()
    if event.user_id != request.user.id:
        raise HTTPForbidden()
    event.delete()

    return {}
