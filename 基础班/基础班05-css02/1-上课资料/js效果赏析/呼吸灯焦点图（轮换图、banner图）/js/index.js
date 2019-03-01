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
   	
   	
   	//无缝滚动
   	$('.fast_r ul').append($('.fast_r ul li:lt(4)').clone(true));
   	
		var timer01 = null;
		var num = 0;
		
		var myFn = function(){
			num-=3;//  '+num+'  num = num + -3
			if(num < -968){//3600才是一轮结束的位置 不能比这个3600大 所以我们要让ul再回复到0点
				num = 0;
			}
			$('.fast_r ul').css('left',''+num+'px');
		}
		
		timer01 = setInterval(myFn,30);
		
		$('.fast_r ul li').mouseover(function(e) {
            //鼠标进来之后 要停止定时器
			clearInterval(timer01);
			
        }).mouseout(function(){
			clearInterval(timer01);//记住在开启定时器之前 就要把之前的定时器都清除掉
			timer01 = setInterval(myFn,30);

		})
        
        //呼吸灯焦点图
	$('.slideBox .bd ul li').eq(0).show();
	var num_huxi = 0;//全局变量 是轮换图的灵魂 所有的人都可以随时随地的修改或者获取这个值
	
	$('.next').click(function(e) {
        $('.slideBox .bd ul li').eq(num_huxi).stop().fadeOut(500);//这里控制的是目前能看到的这张图 让它fadeOut
		num_huxi++;
		if(num_huxi > 6){//这里要加1之后 再去判断是否超出了范围
			num_huxi = 0;
		}
		//alert(num);
		$('.slideBox .bd ul li').eq(num_huxi).fadeIn().siblings().fadeOut();
		
		$('.slideBox .hd ul li').eq(num_huxi).addClass('on').siblings().removeClass('on');//要在加1之后 再控制ol的li变化
    });
	
	$('.prev').click(function(e) {
		$('.slideBox .bd ul li').eq(num_huxi).fadeOut('500');//这里控制的是目前能看到的这张图 让它fadeOut
        num_huxi--;
		if(num_huxi < 0){
			num_huxi = 6;
		}
		
		//alert(num);
		
		$('.slideBox .hd ul li').eq(num_huxi).addClass('on').siblings().removeClass('on');//要在加1之后 再控制ol的li变化
		$('.slideBox .bd ul li').eq(num_huxi).fadeIn('500');
    });
   	
})







































