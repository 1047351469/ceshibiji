Action()
{
	/*
	web_reg_save_param("Session",
		"LB=name=userSession value=",
		"RB=>",
		LAST);

	
	// 打开WebTours首页
	web_url("首页","URL=http://127.0.0.1:1080/WebTours/",LAST);

	// 登录操作
	
	web_submit_data("登录",
		"Action=http://127.0.0.1:1080/WebTours/login.pl",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		"Mode=HTML",
		ITEMDATA,
		"Name=userSession", "Value={Session}", ENDITEM,
		"Name=username", "Value=jojo", ENDITEM,
		"Name=password", "Value=bean", ENDITEM,
		"Name=login.x", "Value=40", ENDITEM,
		"Name=login.y", "Value=9", ENDITEM,
		"Name=login", "Value=Login", ENDITEM,
		"Name=JSFormSubmit", "Value=off", ENDITEM,
		LAST);
*/


	// 使用 另一种方法来实现

	// 打开首页
	web_custom_request("首页_web_custom_request",
		"URL=http://127.0.0.1:1080/WebTours/",
		"Method=GET",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"Mode=HTML",
		"Body=",
		LAST);

	// 登录
	
	return 0;
}
