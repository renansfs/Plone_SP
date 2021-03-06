(function(window, factory) {
  var cycle2SlideShow = factory(window, window.document);
  window.cycle2SlideShow = cycle2SlideShow;
  if (typeof module == 'object' && module.exports){
    module.exports = cycle2SlideShow;
  }
}
(window, function l(window, document) {
  'use strict';
  var Cycle2SlideShow = (function() {
    function Cycle2SlideShow(el) {
      $(el).data('cycle2slideshow', this);
      this.$player = $('.cycle-player', el);
      this.$thumbsContainer = $('.cycle-carrossel', el);
      this.$thumbs = $('.cycle-carrossel .thumb-itens', el)
      this.$imgs = $('.cycle-player img', el);
      this.$slideshows = $('.cycle-slideshow', el);
      this.aspectRatio = parseFloat($(el).attr('data-aspect-ratio'));
      if (isNaN(this.aspectRatio)) {
        this.aspectRatio = 3 / 2;
      }
      this.maxWidth = this.$player.width();
      this.maxHeight = this.maxWidth / this.aspectRatio;
      this.bindEvents();
      this.fixImageSize();
      this.centerImage();
      $(el).fadeTo('slow', 1);
    }
    Cycle2SlideShow.prototype.bindEvents = function() {
      this.$player.on('cycle-next cycle-prev', $.proxy(this.syncSlideshows, this));
      this.$player.on('cycle-before', $.proxy(this.cycleBefore, this));
      this.$thumbs.on('click', $.proxy(this.thumbsClick, this));
    };
    Cycle2SlideShow.prototype.fixImageSize = function() {
      this.$player.css({
        'width': this.maxWidth,
        'height': this.maxHeight
      });
      this.$imgs.css({
        'max-width': this.maxWidth,
        'max-height': this.maxHeight
      });
    };
    Cycle2SlideShow.prototype.centerImage = function(img) {
      if (typeof(img) === 'undefined') {
        var img = this.$imgs[0].parentElement;
        if ($(img).hasClass('cycle-sentinel')) {
          img = this.$imgs[1].parentElement;
        }
      }
      var img_height = $(img).height()
      if (img_height < this.maxHeight) {
        var margin = parseInt((this.maxHeight - img_height) / 2);
        $(img).css('margin-top', margin);
      }
    };
    Cycle2SlideShow.prototype.syncSlideshows = function(e, opts) {
      e.preventDefault();
      this.$slideshows.cycle('goto', opts.currSlide);
    };
    Cycle2SlideShow.prototype.cycleBefore = function(e, opts, outSlide, inSlide) {
      e.preventDefault();
      this.centerImage(inSlide);
    };
    Cycle2SlideShow.prototype.thumbsClick = function(e) {
      e.preventDefault();
      var index = this.$thumbsContainer.data('cycle.API').getSlideIndex(e.currentTarget);
      this.$slideshows.cycle('goto', index);
    };
    return Cycle2SlideShow;
  })();
  return Cycle2SlideShow;
}));
