picToSoft.factory('PictogramService', ['$http', function ($http) {
	'use strict';

	var PictogramService = {};

	PictogramService.random = function () {
		return $http.get('https://der-werkstatt-shenrique-1.c9users.io/pictograma');
	};

	return PictogramService;
}]);