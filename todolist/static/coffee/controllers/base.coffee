angular.module 'app.controllers.base', []

.controller 'BaseController', ['$scope', '$injector', ($scope, $injector) ->
  $app = $injector.get '$app'

  $scope.modalLogin =
    email: null
    password: null
    autoShow: yes
    showModal: ($event) ->
      $event.preventDefault()
      $scope.modalLogin.show()
    submit: ($event) ->
      $event.preventDefault()
      $app.progress.start()
      $app.api.user.login('kelp.chen@biideal.com.tw', '123').success (result) ->
        $app.progress.done()
        console.log result
]