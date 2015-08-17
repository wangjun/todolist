from wtforms import Form, IntegerField
from todolist import utils


class PageForm(Form):
    index = IntegerField(
        default=0,
        filters=[utils.int_filter]
    )
    size = IntegerField(
        default=20,
        filters=[
            utils.int_filter,
            lambda x: x if x <= 100 else 100,
        ]
    )
