//通用咨询
$(".zx li").mouseenter(function(){
	$(this).children("div").show();
})
$(".zx li").mouseleave(function(){
	$(this).children("div").stop().hide();
})	
$(window).scroll(function(){
	var sT = $(window).scrollTop();

	if(sT > 400){
		$("#back").css("visibility","visible");
	}else{
		$("#back").css("visibility","hidden");
	}
	var sT100 = sT + 100;
	$('.zx').stop().animate({'top':''+sT100+'px'},500);
	
});
$("#back").click(function(){
	$("html,body").animate(
		{
			"scrollTop":0
		},500
	);	
})
