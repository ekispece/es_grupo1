picToSoft.controller('ResultCtrl', function ($scope, $rootScope, $location) {
    $scope.metricas = $rootScope.metricas;    

    var obterTotalAcertos = function () {
        var count = 0;

        for(var index = 0; index < $scope.metricas.ultimaPartida.length; index++) {
            if ($scope.metricas.ultimaPartida[index].acertou)
                count++;
        }

        return count;
    };

    $scope.ultimaPartida = {};
    $scope.ultimaPartida.acertos = obterTotalAcertos();
    $scope.ultimaPartida.totalPerguntas = $rootScope.metricas.ultimaPartida.length;    

    $scope.iniciarNovoJogo = function () {
        $location.path('/game');
    }    

    // FIX FOR BOOTSTRAP NAV
    $('.nav-tabs li a').click(function (e) {
        e.preventDefault();        
    });
});