/* global Modernizr, $, _ */

(function(){
	'use strict';
	$('.go-up').click(function(e) {
		e.preventDefault();
		$('body').animate({scrollTop: 0}, 500);
	});
	$('.share-opener').click(function(e) {
		e.preventDefault();
		var shareContainerId = $(this).data('share-container-id');
		$('#' + shareContainerId).toggleClass(shareContainerId + '--hidden');
	});
})();
