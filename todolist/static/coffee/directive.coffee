angular.module 'app.directive', []

# ---------------------------------------------------------
# app-modal
# ---------------------------------------------------------
.directive 'appModal', ['$injector', ($injector) ->
  ###
  app-modal="scope.modal"
  scope.modal:
    autoShow: {bool} If this modal should pop as automatic, it should be yes.
    show: -> {function} After link, it is a function for show the modal.
    hide: -> {function} After link, it is a function for hidden the modal.
    hiddenCallback: ($event) -> {function} After the modal hidden, it will be eval.
  ###
  $parse = $injector.get '$parse'

  return {
    restrict: 'A'
    link: (scope, element, attr) ->
      modal = $parse(attr.appModal) scope
      # setup hide function for scope.modal
      modal.hide = ->
        element.modal 'hide'
        return
      modal.show = ->
        element.modal 'show'
        return
      if modal.hiddenCallback
        # listen hidden event for scope.modal.hiddenCallback
        element.on 'hidden.bs.modal', (e) ->
          scope.$apply ->
            scope.$eval modal.hiddenCallback,
              $event: e
        element.on 'shown.bs.modal', ->
          # focus the first element
          $firstController = element.find('.form-control:not(.tt-hint):first')
          if $firstController.length
            $firstController.select()
          else
            element.find('[type=submit]').focus()
      if modal.autoShow
        # pop the modal
        element.modal 'show'
  }
]
