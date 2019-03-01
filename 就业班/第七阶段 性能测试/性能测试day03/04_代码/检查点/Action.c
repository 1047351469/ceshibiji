Action()
{
	// 关联 session

	web_reg_save_param("Session",
		"LB=name=userSession value=",
		"RB=>",
		LAST);

	
	web_url("WebTours", 
		"URL=http://127.0.0.1:1080/WebTours/", 
		"TargetFrame=", 
		"Resource=0", 
		"RecContentType=text/html", 
		"Referer=", 
		"Snapshot=t1.inf", 
		"Mode=HTML", 
		LAST);

	// 插入 注册检查函数 web_reg_find()
	
	web_reg_find("Fail=NotFound",
		"Search=Body",
		"SaveCount=num",
		"Text=jojo",
		LAST);

	web_submit_data("login.pl", 
		"Action=http://127.0.0.1:1080/WebTours/login.pl", 
		"Method=POST", 
		"TargetFrame=body", 
		"RecContentType=text/html", 
		"Referer=http://127.0.0.1:1080/WebTours/nav.pl?in=home", 
		"Snapshot=t2.inf", 
		"Mode=HTML", 
		ITEMDATA, 
		"Name=userSession", "Value={Session}", ENDITEM, 
		"Name=username", "Value=jojo", ENDITEM, 
		"Name=password", "Value=bean", ENDITEM, 
		"Name=JSFormSubmit", "Value=off", ENDITEM, 
		"Name=login.x", "Value=38", ENDITEM, 
		"Name=login.y", "Value=9", ENDITEM, 
		LAST);

	// 使用传统普通检查文本函数
	web_find("web_find",
		"What=jojo",
		LAST);

	// 使用检查图片
	web_image_check("web_image_check",
		"Src=images/hp_logo.png",
		LAST);

	return 0;
}
