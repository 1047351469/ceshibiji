Action()
{
    
	lr_start_transaction("注册-打开首页");

	web_url("注册-打开首页","URL=http://127.0.0.1:1080/WebTours/",LAST);

	lr_end_transaction("注册-打开首页", LR_AUTO);

	lr_start_transaction("注册-注册页面");

	web_url("注册-打开注册页面","URL=http://127.0.0.1:1080/WebTours/login.pl?username=&password=&getInfo=true",LAST);

	lr_end_transaction("注册-注册页面", LR_AUTO);

	lr_start_transaction("注册-注册业务");

	lr_rendezvous("集合点-注册");

	web_submit_data("注册页面",
		"Action=http://127.0.0.1:1080/WebTours/login.pl",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		"Mode=HTML",
		ITEMDATA,
		"Name=username", "Value={username}", ENDITEM,
		"Name=password", "Value=123456", ENDITEM,
		"Name=passwordConfirm", "Value=123456", ENDITEM,
		"Name=register.x", "Value=31", ENDITEM,
		"Name=register.y", "Value=13", ENDITEM,
		LAST);

	lr_end_transaction("注册-注册业务", LR_AUTO);

	return 0;
}
