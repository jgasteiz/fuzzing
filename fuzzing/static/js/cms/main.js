var fuzzing = {};

fuzzing.app = angular.module('fuzzingCMS', []);
fuzzing.app.config(function ($interpolateProvider) {
	$interpolateProvider.startSymbol('[[').endSymbol(']]');
});

fuzzing.app.controller('PageListCtrl', function($scope) {

	/**
	 * Dictionary with the visible page sections in the cms.
	 *
	 * @type {{}}
	 * @private
	 */
	var _visiblePageSections = {};

	$scope.search = '';

	/**
	 * Function for filtering page names in the cms page list section.
	 *
	 * @param name
	 * @returns {boolean}
	 */
	$scope.isExcludedByFilter = function(name) {
		var search = $scope.search.toLowerCase();
		name = name.toLowerCase();
		return !(name.indexOf(search) !== -1);
	};

	/**
	 * Return visibility of a page sections area.
	 *
	 * @param pageId
	 * @returns {*}
	 */
	$scope.sectionActive = function(pageId) {
		return _visiblePageSections[pageId]
	};

	/**
	 * Toggles page sections area visibility.
	 *
	 * @param pageId
	 */
	$scope.toggleSections = function(pageId) {
		_visiblePageSections[pageId] = !_visiblePageSections[pageId];
	};
});