picToSoft.directive('pictogramImage', function () {
    return {
        restrict: 'E',        
        scope: {
            source: '=',
            last: '='
        },
        templateUrl: 'views/pictogram-image.html',        
        link: function ($scope, $elem, attrs) {
            var $img = $('div');

            $img.css('background-')

            $scope.source = 'images/' + $scope.source;
        }
    };
})