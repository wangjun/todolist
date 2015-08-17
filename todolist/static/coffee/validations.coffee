angular.module 'app.validations', ['validator']

.run ['$injector', ($injector) ->
    $validator = $injector.get '$validator'

    $validator.register 'required',
        validator: /.+/
        error: 'This field is required'

    $validator.register 'email',
        validator: /(^$)|(^.+@[^.].*\.[a-z]{2,10}$)/
        error: 'Please enter a valid email'

    $validator.register 'min2',
        validator: (value='') ->
            value.length >= 2
        error: 'Please enter more than 1 characters'
    $validator.register 'min5',
        validator: (value='') ->
            value.length >= 5
        error: 'Please enter more than 4 characters'

    # confirm password
    $validator.register 'confirm',
        validator: (value, scope, element, attr, $injector) ->
            $parse = $injector.get '$parse'
            value is $parse(attr.password)(scope)
        error: 'Confirm password should be match with password'
]
