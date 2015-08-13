angular.module 'app.router', [
  'ui.router'
]

.config ['$stateProvider', '$urlRouterProvider', '$locationProvider', ($stateProvider, $urlRouterProvider, $locationProvider) ->
  # html5 mode
  $locationProvider.html5Mode
    enabled: yes
    requireBase: no

  # redirect other urls
  $urlRouterProvider.otherwise ($injector) ->
    $app = $injector.get '$app'
    $app.go 'web.index', null,
      reload: yes
      location: 'replace'


  # ---------------------------------------------------------
  #
  # ---------------------------------------------------------
  $stateProvider.state 'web',
    url: ''
    templateUrl: '/static/templates/layout.html'
    controller: 'BaseController'

  # ---------------------------------------------------------
  # /
  # ---------------------------------------------------------
  $stateProvider.state 'web.index',
    url: '/'
    resolve:
      title: -> "todolist"
    templateUrl: '/static/templates/index.html'
    controller: 'IndexController'
]