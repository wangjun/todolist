angular.module 'app.controllers.index', []

.controller 'IndexController', ['$scope', 'events', ($scope, events) ->
  $scope.events = events
  $scope.$on 'new-event', (self, event) ->
    $scope.events.items.unshift event
    $scope.events.total += 1
]