angular.module 'app.controllers.base', []

.controller 'BaseController', ['$scope', '$injector', ($scope, $injector) ->
  $app = $injector.get '$app'

  $app.api.user.login('kelp.chen@biideal.com.tw', '123').success (result) ->
    console.log result
  console.log 'x'
]