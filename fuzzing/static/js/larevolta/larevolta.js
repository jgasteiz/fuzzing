/* global Modernizr, $, _ */

(function(){
	'use strict';
	$('.go-up').click(function(e) {
		e.preventDefault();
		$('body').animate({scrollTop: 0}, 500);
	});
})();
