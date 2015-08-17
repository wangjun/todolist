angular.module 'app.controllers.index', []

.controller 'IndexController', ['$scope', '$injector', 'events', ($scope, $injector, events) ->
  $app = $injector.get '$app'

  $scope.events = events
  $scope.$on 'new-event', (self, event) ->
    $scope.events.items.unshift event
    $scope.events.total += 1
  $scope.deleteEvent = ($event, index) ->
    $event.preventDefault()
    event = $scope.events.items[index]
    $app.progress.start()
    $app.api.event.deleteMyEvent(event.id).success ->
      $app.progress.done()
      $scope.events.items.splice index, 1
      $scope.events.total -= 1
]