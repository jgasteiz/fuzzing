/* global Modernizr, $, _ */

(function(){
	'use strict';
	var isIntroOpen = null,
		$intro = $('.header__logo'),
		$header = $('#header'),
		$article = $('#main'),
		href;

	isIntroOpen = !$header.hasClass('is-open');

	$('.intro-opener').click(function(e) {
		e.preventDefault();
		href = $(e.currentTarget).attr('href');
		if (isIntroOpen === true) {
			isIntroOpen = false;
			_.delay(function() {
				$article.addClass('is-active');
			}, 800);
			$header.addClass('is-open');
		} else {
			isIntroOpen = true;
			$article.removeClass('is-active');
			$header.removeClass('is-open');
		}
	});
	$('.nav-opener').click(function(e) {
		e.preventDefault();
		href = $(e.currentTarget).attr('href');
		if (isIntroOpen === true) {
			isIntroOpen = false;
			_.delay(function() {
				$article.addClass('is-active');
			}, 800);
			$header.addClass('is-open');
			console.log('is-open', isIntroOpen);
			if (href !== '#') {
				_.delay(function() {
					window.location.href = href;
				}, 800);
			}
		} else {
			window.location.href = href;
		}
	});
})();
