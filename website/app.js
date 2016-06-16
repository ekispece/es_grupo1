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

    $routeProvider.when('/result', {
        templateUrl: 'views/result.html',
        controller: 'ResultCtrl'
    });         
})
.run(function ($rootScope) {
    $rootScope.api = 'https://der-werkstatt-shenrique-1.c9users.io';
});