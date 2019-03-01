Action()
{
	// 打开首页
	web_url("打开首页","URL=http://192.168.72.22/iwebshop/",LAST);

	// 点击登录-跳转到登录页面
	web_url("打开登录页面","URL=http://localhost/iwebshop/index.php?controller=simple&action=login",LAST);

	// 输入用户名和密码-登录

	web_submit_data("web_submit_data",
		"Action=http://localhost/iwebshop/index.php?controller=simple&action=login_act",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		"Mode=HTML",
		ITEMDATA,
		"Name=login_info", "Value=admin", ENDITEM,
		"Name=password", "Value=123456", ENDITEM,
		"Name=callback", "Value=", ENDITEM,
		LAST);
	// 退出
	web_url("退出登录","URL=http://localhost/iwebshop/index.php?controller=simple&action=logout",LAST);
	return 0;
}
