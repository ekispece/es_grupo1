var picToSoft = angular.module('picToSoft', []);
picToSoft.controller('main', function($scope, $http){
    $scope.mock = {"pictogramas": [{"dica": "Quem descobriu brasil?", "topicos": [{"nome": "uml"}, {"nome": "figuras excentricas"}, {"nome": "Impeachment Dilma Roussef"}], "imagem": "images/pic001.png", "resposta": "KENT BECK", "tempo": 30, "letras": ["K", "E", "N", "T", "B", "E", "C", "K", "J", "I", "N", "C", "A"]}]};
    // $http.get('http://localhost:8000/pictograms').success(function(data){
    //     $scope.mock = data;
    // });
});
