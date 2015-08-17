angular.module 'app.controllers.base', []

.controller 'BaseController', ['$scope', '$injector', ($scope, $injector) ->
  $app = $injector.get '$app'
  $validator = $injector.get '$validator'
  $timeout = $injector.get '$timeout'

  $scope.logout = ($event) ->
    $event.preventDefault()
    $app.progress.start()
    $app.api.user.logout().success ->
      location.reload()
  $scope.modalLogin =
    email: 'kelp.chen@biideal.com.tw'
    password: null
    autoShow: no
    showModal: ($event) ->
      $event.preventDefault()
      $scope.modalLogin.show()
    submit: ($event) ->
      $event.preventDefault()
      $validator.validate($scope, 'modalLogin').success ->
        $app.progress.start()
        $app.api.user.login($scope.modalLogin.email, $scope.modalLogin.password).success (result) ->
          $app.progress.done()
          $app.setupUser result
          $scope.modalLogin.hide()
          $scope.modalLogin.password = ''
          $timeout ->
            $validator.reset $scope, 'modalLogin'

  dueDate = new Date()
  dueDate.setDate(dueDate.getDate() + 7)
  $scope.modalNewEvent =
    title: null
    due_date: dueDate
    description: null
    autoShow: no
    showModal: ($event) ->
      $event.preventDefault()
      $scope.modalNewEvent.show()
    submit: ($event) ->
      $event.preventDefault()
      $validator.validate($scope, 'modalNewEvent').success ->
        $app.progress.start()
        $app.api.event.addMyEvent($scope.modalNewEvent).success (result) ->
          $app.progress.done()
          $scope.modalNewEvent.title = ''
          $scope.modalNewEvent.due_date = new Date()
          $scope.modalNewEvent.due_date.setDate($scope.modalNewEvent.due_date.getDate() + 7)
          $scope.modalNewEvent.description = ''
          $timeout ->
            $validator.reset $scope, 'modalNewEvent'
          $scope.modalNewEvent.hide()
          $scope.$broadcast 'new-event', result
]