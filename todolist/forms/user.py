from wtforms import Form, validators, StringField


class LoginForm(Form):
    email = StringField(
        validators=[
            validators.length(max=100),
            validators.data_required(),
        ],
        filters=[lambda x: x.strip().lower() if isinstance(x, basestring) else None],
    )
    password = StringField(
        validators=[
            validators.data_required(),
        ],
    )
