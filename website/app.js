var picToSoft = angular.module('picToSoft', [
    'ngRoute'
]).
config(function ($routeProvider) {
    $routeProvider.otherwise({redirectTo: '/'});
    
    $routeProvider.when('/', {
        templateUrl: 'views/start.html',
        controller: 'StartCtrl'       
    });
    
    $routeProvider.when('/help', {
        templateUrl: 'views/help.html',
        controller: 'HelpCtrl'
    });
    
    $routeProvider.when('/game', {
        templateUrl: 'views/game.html',
        controller: 'GameCtrl'
    });         
})
.run(function ($rootScope) {
    $rootScope.api = 'http://127.0.0.1:8080';
});