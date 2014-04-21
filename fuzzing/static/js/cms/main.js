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

	$scope.openModal = function(url) {
		$scope.modalOpen = true;
		$scope.previewUrl = url;
	}
});

fuzzing.app.directive('modal', function() {
	return {
		scope: {
			open: '=',
			url: '='
		},
		template:
			'<div class="modal fade" tabindex="-1" role="dialog">' +
				'<div class="modal-dialog modal-lg">' +
					'<div class="modal-content">' +
						'<div class="modal-header">' +
							'<button type="button" class="close" ng-click="closeModal()">×</button>' +
							'<h4 class="modal-title" id="myLargeModalLabel">Preview</h4>' +
						'</div>' +
						'<div class="modal-body"></div>' +
					'</div>' +
				'</div>' +
			'</div>',
		link: function(scope, element) {

			var $modal = $(element).find('.modal');

			var _getPreview = function() {
				return '<iframe src="' + scope.url + '" height="100%" width="100%"></iframe>';
			};

			scope.closeModal = function() {
				$modal.modal('hide');
				scope.open = false;
			};

			scope.$watch('open', function(newValue) {
				if (newValue === true) {
					$modal.modal({
						backdrop: 'static',
						keyboard: false
					});
					$modal.find('.modal-body').html(_getPreview());
				}
			});
		}
	}
});