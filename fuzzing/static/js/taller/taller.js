/* global Modernizr, $, _ */

(function(){
    'use strict';
    var isIntroOpen = null,
        $header = $('#header'),
        $article = $('#main'),
        href,
        ANIMATION_DURATION = 600;

    isIntroOpen = !$header.hasClass('is-open');

    $('.intro-opener').click(function(e) {
        e.preventDefault();
        href = $(e.currentTarget).attr('href');
        if (isIntroOpen === true) {
            isIntroOpen = false;
            _.delay(function() {
                $article.addClass('is-active');
            }, ANIMATION_DURATION);
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
            }, ANIMATION_DURATION);
            $header.addClass('is-open');
            console.log('is-open', isIntroOpen);
            if (href !== '#') {
                _.delay(function() {
                    window.location.href = href;
                }, ANIMATION_DURATION);
            }
        } else {
            window.location.href = href;
        }
    });
})();
