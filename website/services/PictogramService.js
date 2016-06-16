picToSoft.factory('PictogramService', function ($http, $rootScope) {
	'use strict';

	var PictogramService = {};

	PictogramService.iniciarPartida = function () {
		return $http.get($rootScope.api + '/pictograma');
	};

	PictogramService.finalizarPartida = function (data) {
		return $http.post($rootScope.api + '/finaliza', data);
	};

	return PictogramService;
});