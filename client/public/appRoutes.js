angular
    .module('appRoutes', ["ui.router"])
    .config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider){
    
    $stateProvider.state({
        name: 'retail',
        url: '/',
        templateUrl: 'public/components/taskmanager/templates/taskmanager.template',
        controller: 'TaskmanagerController'
    });

    $urlRouterProvider.otherwise('/');
}]);
