function test(){
  var tabsNewAnim = $('.nav-top');
  var selectorNewAnim = $('.nav-top').find('li').length;
  var activeItemNewAnim = tabsNewAnim.find('.active');
  var activeWidthNewAnimHeight = activeItemNewAnim.innerHeight();
  var activeWidthNewAnimWidth = activeItemNewAnim.innerWidth();
  var itemPosNewAnimTop = activeItemNewAnim.position();
  var itemPosNewAnimLeft = activeItemNewAnim.position();


  $(".selector").css({
    "top":itemPosNewAnimTop.top + "px",
    "left":itemPosNewAnimLeft.left + "px",
    "height": activeWidthNewAnimHeight + "px",
    "width": activeWidthNewAnimWidth + "px"
  });



  $(".nav-top").on("click","li",function(e){
    $('.nav-top ul li').removeClass("active");
    $(this).addClass('active');
    var activeWidthNewAnimHeight = $(this).innerHeight();
    var activeWidthNewAnimWidth = $(this).innerWidth();
    var itemPosNewAnimTop = $(this).position();
    var itemPosNewAnimLeft = $(this).position();

    $(".selector").css({
      "top":itemPosNewAnimTop.top + "px",
      "left":itemPosNewAnimLeft.left + "px",
      "height": activeWidthNewAnimHeight + "px",
      "width": activeWidthNewAnimWidth + "px"
    });
  });
}
$(document).ready(function(){
  setTimeout(function(){ test(); });
});
$(window).on('resize', function(){
  setTimeout(function(){ test(); }, 250);
});

$(".nav-top-toggler").click(function(){
  setTimeout(function(){ test(); });
});

const navTopToggler = document.querySelector(".nav-top-toggler");
const navTop = document.querySelector(".nav-top");

navTopToggler.onclick = function() {
    navTop.classList.toggle("active");
}
