$(function(){
	//右下角弹出广告(父级)
	$('.webimclosebutton').click(function(){
		$(this).parent().hide();
	})
	
	//突出展示
	$('.fast_r ul li').hover(function(){
		$(this).siblings().stop().fadeTo('500','0.5');
	},function(){
		$(this).siblings().stop().fadeTo('500','1');
	})
	
	//显示模态窗口
    $('.loginBtn').click(function(event) {
      $('.down,.up').stop().fadeIn('slow');
    });
    $('.closeBtn').click(function(event) {
      $('.down,.up').hide();
    });
    //列表展示 
   	$('#czimg ul li').hover(function(){
 		$(this).children('.slideup_p').stop().animate({'bottom':'0'},500);
   	},function(){
 		$(this).children('.slideup_p').stop().animate({'bottom':'-44px'},500);
   	})
   	
	//电梯跳转效果
	$(".coursefd ul li").click(function(){
		$("html,body").animate(
			{
				"scrollTop":$(".lay_conke").eq($(this).index()).offset().top - 50
			},500);
		$(this).addClass('cur').siblings().removeClass('cur');
	});
	
	
	
	var sT = $(window).scrollTop();
	$('.lay_conke').each(function(index,el){
		if(sT >= $(this).offset().top - 50){
			$(".coursefd ul li").eq(index).addClass('cur').siblings().removeClass('cur');
		}	
	})
})







































