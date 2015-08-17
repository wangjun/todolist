angular.module 'app.controllers.index', []

.controller 'IndexController', ['$scope', 'events', ($scope, events) ->
  $scope.events = events
  console.log events
]