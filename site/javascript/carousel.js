(function($, doc, win){
    var Carousel = function(){
        var carousel = $('.carousel'),
            left = $('.left.arrow'),
            right = $('.right.arrow');

        var slideWidth = 960,
            current = 0,
            max = 2;

        var slide = function(){
            carousel.css('marginLeft', [
                '-', slideWidth * current, 'px'
            ].join(''));
        };

        left.on('click', function(){
            if (current === 0) return;

            current--, slide();
        });

        right.on('click', function(){
            if (current === max) return;

            current++, slide();
        });
    };

    $(function(){
        Carousel();
    });
})(jQuery, document, window);