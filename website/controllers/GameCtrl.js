picToSoft.controller('GameCtrl', function($scope, $http, PictogramService){            
    $scope.answerLetters = [];
    
    var inicializarLetrasDaResposta = function (resposta) {
        for(var x = 0; x < resposta.length; x++) {
            $scope.answerLetters.push('');
        }               
    };
    
    var verificarRespostaCerta = function () {
        var resposta = $scope.answerLetters.join('');
        
        if(resposta.length == $scope.pictogram.resposta.length) {                        
            if(resposta.toLowerCase() === $scope.pictogram.resposta.toLowerCase()) {
                $scope.respostaCerta = true;
                alert('resposta certa!');
            } else {
                $scope.respostaCerta = false;
                alert('resposta errada...');
            }
        }
    };
        
    PictogramService.random().then(function (response) {
       $scope.pictogram = response.data;   
       
       inicializarLetrasDaResposta(response.data.resposta);         
    });                        
            
    $scope.letterClick = function(index){
        for(i = 0; i<$scope.answerLetters.length; i++){
            if($scope.answerLetters[i] == ''){
                $scope.answerLetters[i] = $scope.pictogram.letras[index];
                break;
            }
        }
        
        verificarRespostaCerta();        
    };

    $scope.answerBoxClick = function(index){
        $scope.answerLetters[index] = '';
    };

    $scope.hint = function(){
        alert($scope.pictogram.dica);
    };            
});
