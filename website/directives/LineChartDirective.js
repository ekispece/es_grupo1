picToSoft.directive('lineChart', function () {
    return {
        restrict: 'A',
        scope: {
            points: '=',
            tabs: '='
        },
        link: function ($scope, $elem, $attrs) {            
            var data = new google.visualization.DataTable(),
                chart = new google.visualization.LineChart($elem[0]),
                rows = [],
                options = {};
                                        
            
            data.addColumn('number', 'Partida');
            data.addColumn('number', 'Acertos');

            for (var index = 0; index < $scope.points.length; index++) {
                rows.push([$scope.points[index].x, $scope.points[index].y]);
            }

            data.addRows(rows);

            options = {
                hAxis: {
                    title: 'Partidas'
                },
                vAxis: {
                    title: 'Acertos',
                    viewWindow: {
                        min: 0
                    }
                },
                series: {
                    1: {curveType: 'function'}
                }
            };

            // FIX FOR DRAWING ON HIDDEN DIV

            if(!$elem.hasClass('active')) {
                google.visualization.events.addListener(chart, 'ready', function () {
                    $elem.removeClass('active');
                });

                $elem.addClass('active');
            }

            // END FIX

            chart.draw(data, options);                 
        }
    };
})