picToSoft.controller('GameCtrl', function($scope, $http, PictogramService){
    $scope.mock = {"pictogramas": [{"dica": "Quem descobriu brasil?", "topicos": [{"nome": "uml"}, {"nome": "figuras excentricas"}, {"nome": "Impeachment Dilma Roussef"}], "imagem": "images/pic001.png", "resposta": "KENT BECK", "tempo": 30, "letras": ["K", "E", "N", "T", "B", "E", "C", "K", "J", "I", "N", "C", "A"]}]};
    $scope.answerLetters = ['', '', '', '', '', '', '', ''];
    $scope.letterClick = function(index){
        for(i = 0; i<$scope.answerLetters.length; i++){
            if($scope.answerLetters[i] == ''){
                $scope.answerLetters[i] = $scope.mock.pictogramas[0].letras[index];
                break;
            }
        }
    }

    $scope.answerBoxClick = function(index){
        $scope.answerLetters[index] = '';
    }

    $scope.hint = function(){
        alert($scope.mock.pictogramas[0].dica);
    }
});
