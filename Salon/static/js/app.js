
// $(function(){
//    $( "td img" ).animate({opacity: 0.25, height: 100, width: 150}, 5000);
// });
$( "td img" ).on( "mouseenter", function() {
   $( this ).animate({ opacity: 0.95, height: "200%", width: '100%', left: -350 }, 3000);
});
$( "td img" ).on( "click", function() {
   $( this ).animate({ height: '100%', width: '100%'}, 3000);
});
// //Слайдер картинок:
// var i = 8;
// $(function(){
// $('.pict:eq(2) img').on( "click", function() {
//    $(this).fadeOut(500, function(){
//       if (i <= 13){
//          i += 1;
//       $(this).attr('src', 'images/dest/Layer_' + i + '.png').fadeIn(5000);
//       }
//       else {
//          i = 9
//          $(this).attr('src', 'images/dest/Layer_' + i + '.png').fadeIn(5000);
//       }  
//    });
// });
// });

// // СЕЛЕКТОРЫ:
// // Базовые селекторы (#id, tagName, .class)
$(function(){
// $('#bt1').css({'background-color': 'red', 
// 'border': 'solid 15px green'});
// // Селекторы взаимодействия (parent, child, + ~ и т.д.)
// $('body .sect2').css('background-color', 'green');
// $('.pict + .opisan span').css('background-color', 'red'); //выбирает первый .opisan span идущий за .pict
// $('.pict ~').css('background-color', 'red'); //выбирает все ближайшие теги идущие за .pict
// $('.pict').parent().css('background-color', 'red');
// // Простые фильтры (:first, :last, even, odd, eq и т.д.)
// $('.pict:first').css('background-color', 'black');
// $('.pict:last').css('background-color', 'black');
// $('.pict:even').css('background-color', 'blue'); //выбирает все нечетные
// $('.pict:odd').css('background-color', 'beige'); //выбирает все четные
// $('.pict:eq(3)').css('background-color', 'black'); //выбирает элемент по счету начиная с 0
// // Фильтры по содержимому (:has, :parent, :empty и т.д.)
// $('.row:has(.cont1)').css('background-color', 'black');// выбирает элемент .row содержащий .cont
// $('.row:parent').css('background-color', 'black');// выбирает элемент .row в котором содержаться др дети
// $('.row:empty').css('backround-color', 'blue');// выбирает элемент .row в котором нет др детей
// // Фильтры по атрибутам ([name ~= value]  и т.д.)
// $('a[href^="http"]').css('color', 'green');//выбирает все ссылки начинающиеся на http
// $('a[href*=".ru"]').css('color', 'green');//выбирает все ссылки имеющие .ru
// $('img[src$="9.png"]').hide();//выбирает картинку адресс к которой заканчивается на 9.png
// $('img[src!="images/dest/Layer_13.png"]').hide();//выбирает все картинки кроме images/dest/Layer_13.png

// //СОБЫТИЯ:
// //Клики мышью (click, dblclick)
// $( "#bt1" ).on( "click", function() {
//    $(this).css('border', 'solid 15px white');
// });
// $( "#bt1" ).on( "dblclick", function() {
//    $(this).css('border', 'solid 15px black');
// });
// //Полеты над элементом (mouseenter, mouseleav и т.д.)
// $( "#bt1" ).on( "mouseenter", function() {// когда курсор наводится
//    $(this).css('border', 'solid 15px blue');
// });
// $( "#bt1" ).on( "mouseleave", function() {// когда курсор уходит
//    $(this).css('border', 'solid 15px black');
// });
// //Формы (focus, change и т.д.)
// $( "input" ).on( "focus", function() {
//    $(this).css('border', 'solid 15px black');
// });
// $( "input" ).on( "change", function() {
//    $(this).css('border', 'solid 15px blue');
//    $('.txt').text(', ' + $(this).val() + " !"); //вставляет текст в .txt
// });
// // Клавиатура (keypress, keydown, keyup)
// $( "input" ).on( "keypress", function() {//считывает вводимый в поле текст кроме крайнего знака
//    $('.txt').text(', ' + $(this).val() + " !"); //вставляет этот текст в .txt кроме крайнего знака
// });
// $( "input" ).on( "keydown", function() {//тоже самое что и keypress
//    $('.txt').text(', ' + $(this).val() + " !"); //вставляет этот текст в .txt кроме крайнего знака
// });
// $( "input" ).on( "keyup", function() {//считывает вводимый в поле текст
//    $('.txt').text(', ' + $(this).val() + " !"); //вставляет этот текст в .txt
// });
// //Базовая анимация
//    $('#bt1').hide(3000).delay(3000).show(5000);// delay - это задержка в мс
//    $('#bt1').animate({'height': '100px'}, 5000)
//    $( "#bt1" ).animate({opacity: 0.25, height: 100, width: 150}, 5000);
//    $( "#bt1" ).slideUp(5000).delay(3000).slideDown(5000);
// //Взаимодействие с атрибутами
// console.log($('.pict:eq(3) img').attr('src')); //Выводит в консоль src картинки
// $('.pict:eq(3) img').on( "click", function() {
//    $(this).fadeOut(500, function(){
//       $(this).attr('src', 'images/dest/Layer_9.png').fadeIn(5000);//Меняет атрибут 4 картинки на src="images/dest/Layer_9.png"
//    });
// });
// $('.pict:eq(1) img').attr('class', 'new')//Навешивает второй картинке дополнительный атрибут (class="new")
// Взаимодействие с классами
// $('#t2').on('dblclick', function() { 
// $('#t2').addClass('b');//при двойном клике на элемент #t2 его свойства меняются на свойства класса .b (им дополняются)
// });
// $('#t2').on("click", function() { 
//    $(this).removeClass('b');//при клике на элемент #t2 из его свойств убираются свойства класса .b
// });
// $('#t2').on("mouseenter", function() { 
//    $('.trans').toggleClass('trans b');//замена класса .trans на класс .b
// });
// $('#t2').on("click", function() { 
//    $('#t2').parent().toggleClass('b trans');//обратная замена класса .b на класс .trans
// });

// //Клонирование, добавление, перемещение элементов
// $('#t2').on("click", function() { 
//    $(this).text('Меняем текст <em>на курсивный шрифт</em>');
//    $(this).html('Меняем текст <em>на курсивный шрифт</em>');
//    $(this).append('Вводим в конец доп текст <em>с курсивным шрифтом</em>');
//    $(this).prepend('Вводим в начало доп текст <em>с курсивным шрифтом</em>');
//    $(this).after('<p>Новый абзац <em>с курсивным шрифтом</em> </p>');
//    $(this).wrap('<div class="container"></div>');// Оборачиваем #t2 в div class="container"
//    $(this).unwrap();//Убираем обертку с элемента #t2
//    $(this).empty();//Убираем все содержимое #t2
//    $(this).remove();//Убираем все содержимое #t2 и сам #t2
//    $(this).append('<br />'+ $(this).text());//Клонируем с новой строки изначальный текст
// });

});






// $(function(){
//    $('.row:has(.cont1)').hide();
// });

// var x = document.getElementsByClassName('x');
// var popu = document.getElementsByClassName('popu');
// var btn = document.getElementsByClassName('hed');

// function openPopu() {
//     popu.style.display = 'block';
// }

// function closePopu() {
//     popu.style.display = 'none';
// }

// x.addEventListener('click', closePopu);
// btn.addEventListener('click', openPopu);


// $(document).ready(function(){
//     $('.popu').hide()
//    });

// $(document).ready(function(){
//    $('.x').click(function(){
//     $('.popu').hide()
//    });
// });
// $(document).ready(function(){
//     $('.hed').click(function(){
//      $('.popu').show()
//     });
//  });
