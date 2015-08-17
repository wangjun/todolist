from wtforms import Form, IntegerField, StringField
from todolist import utils


# ---------------------------------------------------------
# Form
# ---------------------------------------------------------
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

class SearchForm(PageForm):
    keyword = StringField(
        filters=[lambda x: x.strip() if isinstance(x, str) else None],
    )
    # ex: desc-create_time, asc-last_login_time
    sort = StringField(
        default='',
        filters=[lambda x: x.strip() if isinstance(x, str) else ''],
    )
