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
})







































