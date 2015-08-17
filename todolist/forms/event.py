from wtforms import Form, validators, StringField, DateTimeField
from todolist import utils


class EventForm(Form):
    title = StringField(
        validators=[
            validators.length(max=100),
            validators.data_required(),
        ],
        filters=[lambda x: x.strip() if isinstance(x, basestring) else None],
    )
    description = StringField(
        filters=[lambda x: x.strip() if isinstance(x, basestring) else None],
    )
    due_date = DateTimeField(
        filters=[utils.parse_ios_format]
    )
