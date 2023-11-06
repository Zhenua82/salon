
$(document).ready(function() {
   $('.boxx').attr('class', 'boxx i_animat');
   // Инициализируем Waypoints для .box
   $('.boxx').waypoint(function(direction) {
      // $('.boxx').addClass('i_animat')
     if (direction === 'down') {
       // Если пользователь скроллит вниз, добавляем класс 'animated' для анимации
       $(this.element).removeClass('i_animat');
     } else {
       // Если пользователь скроллит вверх, удаляем класс 'animated'
       $(this.element).addClass('i_animat');
     }
   }, {
     offset: '-5%' // Срабатывать при достижении середины экрана
   });
 });

$(function(){
   $('.popu').hide();
});

$(function(){
   $('td img').on("click", function(){
    $('.popu').show();
    var m = $(this).attr('src');
   //  $('.img-big img').attr('src', m)
   //  console.log('m='+m);
    $('.ramka-1').css('background-image', 'url( '+ m +')');
   });
});

$(function(){
   $('.ramka-1').on( "click", function() {
      $('.popu').hide();
   });
});

// $(function(){
//    $( ".x" ).on( "click", function() {
//       $('.popu').hide();
//    });
// });

$( ".list-group-item-action" ).on( "mouseenter", function() {
   $( this ).css({'color': '#004d00', 'box-shadow': '5px 5px 20px red'} );
});
$( ".list-group-item-action" ).on( "mouseleave", function() {
   $( this ).css({'color': '#cc0066', 'box-shadow': 'none'} );
});

// var i = 0;
// $( "td:odd img" ).on( "click", function() {
//    $( this ).css({ 'transform': 'translateX(-50%)'});
//    $( this ).animate({ height: "200%", width: '200%' }, function() {
//       i += 1;
//       $( this ).css({ 'position': 'relative', 'z-index': i })});
//       $( this ).on( "dblclick", function() {
//          $( this ).animate({ height: '100%', width: '100%'}, 1000, function() {$( this ).css({ 'transform': 'translateX(0%)'})});
//       });
// });

// $( "td:even img" ).on( "click", function() {
//    $( this ).animate({ height: "200%", width: '200%' }, function() {
//       i += 1;
//       $( this ).css({ 'position': 'relative', 'z-index': i })});
//       $( this ).on( "dblclick", function() {
//          $( this ).animate({ height: '100%', width: '100%'}, 1000, function() {$( this ).css({ 'transform': 'translateX(0%)'})});
//       });
// });