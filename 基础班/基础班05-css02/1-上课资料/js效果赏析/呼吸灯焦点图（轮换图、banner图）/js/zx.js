//通用咨询
$(".zx li").mouseenter(function(){
	$(this).children("div").show();
})
$(".zx li").mouseleave(function(){
	$(this).children("div").stop().hide();
})	

/*点击返回顶部*/

$(window).scroll(function(){
	var toTop = $(window).scrollTop();
	if(toTop > 400){
		$("#back").show();
	}else{
		$("#back").hide();
	}
});
$("#back").click(function(){
	$("html,body").animate({"scrollTop":0},500);	
})
