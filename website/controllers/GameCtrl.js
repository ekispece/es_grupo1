picToSoft.controller('GameCtrl', function($scope, $http, $location, PictogramService, $rootScope){
    var pictogramas = [];
    var indicePictogramas = 0;

    $scope.letrasDaResposta = [];

    var montarObjetoResumoJogo = function () {
        var resumo = {};

        resumo.respostas = [];

        for (var index = 0; index < pictogramas.length; index++) {
            resumo.respostas.push({
                id: pictogramas[index].data._id,
                acertou: pictogramas[index].acertou
            });
        }

        return resumo;
    }

    var verificarFimDoJogo = function () {
        if(indicePictogramas == pictogramas.length) {
            var resumo = montarObjetoResumoJogo();

            PictogramService.finalizarPartida(resumo).then(function (response) {
                $rootScope.metricas = {};

                $rootScope.metricas.historico = response.data;
                $rootScope.metricas.ultimaPartida = resumo.respostas;

                $location.path('/result');
            });
        } else {
            inicializarJogo();
        }
    };

    var verificarRespostaCerta = function () {
        var resposta = $scope.letrasDaResposta.join('');

        if(resposta.length == $scope.pictograma.resposta.length) {
            if(resposta.toLowerCase() === $scope.pictograma.resposta.toLowerCase()) {
                alert('resposta certa!');
                pictogramas[indicePictogramas].acertou = true;
            } else {
                alert('resposta errada...');
                pictogramas[indicePictogramas].acertou = false;
            }

            indicePictogramas++;

            verificarFimDoJogo();
        }
    };

    var inicializarLetrasDaResposta = function (resposta) {
        $scope.letrasDaResposta = [];

        for(var x = 0; x < $scope.pictograma.resposta.length; x++) {
            $scope.letrasDaResposta.push('');
        }
    };

    var inicializarJogo = function () {
        $scope.pictograma = pictogramas[indicePictogramas].data;

        inicializarLetrasDaResposta();
    };

    $scope.clickLetra = function(index){
        for(var i = 0; i < $scope.letrasDaResposta.length; i++){
            if($scope.letrasDaResposta[i] == ''){
                $scope.letrasDaResposta[i] = $scope.pictograma.letras[index];
                break;
            }
        }

        $scope.pictograma.letras.splice(index, 1);

        verificarRespostaCerta();
    };

    $scope.clickLetraResposta = function(index){
        if($scope.letrasDaResposta[index] !== '')
            $scope.pictograma.letras.push($scope.letrasDaResposta[index]);

        $scope.letrasDaResposta[index] = '';
    };

    PictogramService.iniciarPartida().then(function (response) {
       var respostaApi = response.data;

       for(var index = 0; index < respostaApi.length; index++) {
           pictogramas.push({
               data: respostaApi[index],
               acertou: false
           });
       }

       inicializarJogo();
    });
});