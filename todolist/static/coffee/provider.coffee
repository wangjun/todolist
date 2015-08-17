angular.module 'app.provider', []

.provider '$app', ->
  $http = null
  $rootScope = null
  $state = null

  @setupProvider = ($injector) =>
    $http = $injector.get '$http'
    $rootScope = $injector.get '$rootScope'
    $state = $injector.get '$state'

    $rootScope.$loadings =
      hasAny: () ->
        for key of @ when key isnt 'hasAny'
          return yes
        return no
    $rootScope.$user = @user


  @setupUser = (user={}) =>
    if @user?
      # update user
      for key, value of user
        @user[key] = value
    else
      @user = user
    @user.is_login ?= no
  @setupUser window.user

  @go = (stateName, params, options) ->
    if navigator.userAgent.toLowerCase().indexOf('phantomjs') >= 0
      location.href = $state.href stateName, params, options
    else
      $state.go stateName, params, options

  @progress =
    start: ->
      NProgress.start()
    done: ->
      NProgress.done()

  @httpId = 0
  @http = (args) =>
    ###
    @params args: $http args
        disableErrorMessage: {bool} If it is yes, I will not pop error message.
    ###
    httpId = @httpId++
    $rootScope.$loadings[httpId] =
      method: args.method
      url: args.url
    $http args
    .success ->
      delete $rootScope.$loadings[httpId]
    .error (data, status) =>
      delete $rootScope.$loadings[httpId]
      @progress.done()

  @api =
    user:
      login: (email, password) =>
        return @http
          method: 'post'
          url: '/api/login'
          data:
            email: email
            password: password
      logout: =>
        return @http
          method: 'post'
          url: '/api/logout'
    event:
      getMyEvents: (args) =>
        ###
        @params args:
          index: {int}
        ###
        return @http
          method: 'get'
          url: '/api/me/events'
          params:
            index: args.index


  @$get = ['$injector', ($injector) =>
    @setupProvider $injector

    return {
      user: @user
      setupUser: @setupUser
      go: @go
      progress: @progress
      api: @api
    }
  ]
  return
