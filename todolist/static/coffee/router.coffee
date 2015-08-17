angular.module 'app.router', [
  'ui.router'
]

.run ['$injector', ($injector) ->
  $rootScope = $injector.get '$rootScope'
  $state = $injector.get '$state'
  $app = $injector.get '$app'

  $rootScope.$state = $state

  # ui.router state change event
  changeStartEvent = null
  $rootScope.$on '$stateChangeStart', ->
    $app.progress.start()
  $rootScope.$on '$stateChangeSuccess', ->
    $app.progress.done()
  $rootScope.$on '$stateChangeError', ->
    $app.progress.done()
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
    url: '/?index'
    resolve:
      title: -> "todolist"
      events: ['$app', '$stateParams', ($app, $stateParams) ->
        if not $app.user.is_login
          return {
            items: []
            total: 0
          }

        args =
          index: $stateParams.index
        return $app.api.event.getMyEvents(args).then (response) ->
          return response.data
      ]
    templateUrl: '/static/templates/index.html'
    controller: 'IndexController'
]