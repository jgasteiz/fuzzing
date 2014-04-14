var fuzzing = {};

fuzzing.app = angular.module('fuzzingCMS', []);
fuzzing.app.config(function ($interpolateProvider) {
	$interpolateProvider.startSymbol('[[').endSymbol(']]');
});

fuzzing.app.controller('PageListCtrl', function($scope) {

	$scope.search = '';

	$scope.isExcludedByFilter = function(name) {
		var search = $scope.search.toLowerCase();
		name = name.toLowerCase();

		return !(name.indexOf(search) !== -1);
	}
});