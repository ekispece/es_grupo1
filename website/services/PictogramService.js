picToSoft.factory('PictogramService', function ($http, $rootScope) {
	'use strict';

	var PictogramService = {};

	PictogramService.random = function () {
		return $http.get($rootScope.api + '/pictograma');
	};

	return PictogramService;
});