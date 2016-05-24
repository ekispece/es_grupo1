picToSoft.controller('StartCtrl', function($scope, $location){
    $scope.startGame = function () {
        $location.path('/game');
    };
});