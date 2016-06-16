picToSoft.controller('ResultCtrl', function ($rootScope) {
    $scope.metricas = $rootScope.metricas;    

    var obterTotalAcertos = function () {
        var count = 0;

        for(var index = 0; index < $scope.metricas.ultimaPartida.length; index++) {
            if ($scope.metricas.ultimaPartida[index].acertou)
                count++;
        }

        return count;
    };

    $scope.ultimaPartida = {
        acertos: obterTotalAcertos(),
        totalPerguntas: $rootScope.metricas.ultimaPartida.length
    };    
});