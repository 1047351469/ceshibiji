Action()
{
	
	lr_start_transaction("注册-注册业务");

	web_url("打开首页","URL=http://127.0.0.1:1080/WebTours/",LAST);

    web_url("打开注册页面","URL=http://127.0.0.1:1080/WebTours/login.pl?username=&password=&getInfo=true",LAST);

	lr_rendezvous("集合点-注册");

	web_submit_data("web_submit_data",
		"Action=http://127.0.0.1:1080/WebTours/login.pl",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		"Mode=HTML",
		ITEMDATA,
		"Name=username", "Value={username}", ENDITEM,
		"Name=password", "Value=123456", ENDITEM,
		"Name=passwordConfirm", "Value=123456", ENDITEM,
		"Name=register.x", "Value=47", ENDITEM,
		"Name=register.y", "Value=7", ENDITEM,
		LAST);

	lr_end_transaction("注册-注册业务", LR_AUTO);

	return 0;
}
