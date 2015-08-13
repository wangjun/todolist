angular.module 'app.provider', []

.provider '$app', ->
  $http = null

  @setupProvider = ($injector) ->
    $http = $injector.get '$http'

  @setupUser = (user={}) =>
    if @user?
      # update user
      for key, value of user
        @user[key] = value
    else
      @user = user
    @user.is_login ?= no
  @setupUser window.user

  @$get = ['$injector', ($injector) =>
    @setupProvider $injector

    return {
      user: @user
      setupUser: @setupUser
    }
  ]
  return
