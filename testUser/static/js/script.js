$(document).ready(function(){
  $('.accordion').click(function(){
    $(this).toggleClass('active');
    $(this).next('.panel').slideToggle();
    $(this).next('.panel').find('.sub-accordion').removeClass('sub-active');
    $(this).next('.panel').find('.sub-panel').slideUp();
  });

  $('.sub-accordion').click(function(){
    $(this).toggleClass('sub-active');
    $(this).next('.sub-panel').slideToggle();
  });
});
