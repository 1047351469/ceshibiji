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

    
    //无缝滚动（banner）
    $('.slideBox .bd ul').append($('.slideBox .bd ul li:eq(0)').clone());
    
	var num_wf1 = 0;//全局变量初始值肯定是0 代表当前是第0个li被选中
	var num_wf2 = 0;
	function yfFn(){//自定义函数简化代码
        //1：ol的li切换 2：换ul的li图片
		num_wf1++;//让num自己加1
		if(num_wf1 > 6){
			num_wf1 = 0;
		}
		$('.slideBox .hd ul li').eq(num_wf1).addClass('on').siblings().removeClass('on');
		/*
		  0 * -800 = 0
		  1 * -800 = -800
		  2 * -800 = -1600
		  3 * -800 = -2400
		*/
		num_wf2++;
		if(num_wf2 > 7){
			num_wf2 = 1;
			$('.slideBox .bd ul').css('left','0');
		}
		
		
		var move = num_wf2 * -958;
		$('.slideBox .bd ul').stop().animate({'left':move + 'px'},500);
	}
	
	$('.next').click(function(e) {
		yfFn();
   });		
	$('.prev').click(function(e) {
       	num_wf1--;
		if(num_wf1 < 0){
			num_wf1 = 6;
		}
		//1：ol的li切换 2：换ul的li图片
		$('.slideBox .hd ul li').eq(num_wf1).addClass('on').siblings().removeClass('on');
		num_wf2--;
		if(num_wf2 < 0){
			num_wf2 = 6;
			$('.slideBox .bd ul').css('left','-6706px');
		}
		var move = num_wf2 * -958;
		$('.slideBox .bd ul').stop().animate({'left':move + 'px'},500);
    });
	
	//点击ol的li实现切换效果
	$('.slideBox .hd ul li').click(function(e) {
		//控制ol的li有特殊类样式
		$(this).addClass('on').siblings().removeClass('on');
		//控制ul移动到相应位置
		num_wf1 = $(this).index();//这句话就是为了改变num这个全局变量为当前点击的li的索引值
		num_wf2 = $(this).index();
		var move = num_wf1 * -958;
		$('.slideBox .bd ul').stop().animate({'left':move + 'px'},500);
    });
	
	//定时器控制移动
	var timer_yf = null;
	timer_yf = setInterval(function(){
		yfFn();
	},2000);
	
	//鼠标滑入con停止定时器 划出再开启
	$('.slideBox').hover(function(e) {
    	clearInterval(timer_yf);    
    },function(){
    	clearInterval(timer_yf);
		timer_yf = setInterval(function(){
			yfFn();
		},2000);
	});
})







































