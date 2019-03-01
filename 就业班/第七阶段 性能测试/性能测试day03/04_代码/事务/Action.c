Action()
{
	// 定义变量 
	int result;
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

	// 插入开始 事务

	lr_start_transaction("登录");

    // 获取登录后的用户名
	web_reg_save_param("username",
		"LB=Welcome, <b>",
		"RB=</b>,",
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
		"Name=username", "Value=login1", ENDITEM, 
		"Name=password", "Value=123456", ENDITEM, 
		"Name=JSFormSubmit", "Value=off", ENDITEM, 
		"Name=login.x", "Value=38", ENDITEM, 
		"Name=login.y", "Value=9", ENDITEM, 
		LAST);
    
    // 输出 username
    lr_output_message("username值为：%s",lr_eval_string("{username}"));

	// 判断 是否为jojo

	result=strcmp(lr_eval_string("{username}"),"jojo");

	/*

	注意：输出变量直接读取，不用lr_eval_string()读取；
    */
	lr_output_message("判断的结果值为：%d",result);


	// 判断是否相等，相等插入 LR_PASS事务状态
	if(result==0){
		lr_output_message("登录的用户为:%s 通过！",lr_eval_string("{username}"));
		// 插入事务状态为通过
		lr_end_transaction("登录", LR_PASS);
	}else{
		lr_output_message("登录的用户为:%s 不通过！",lr_eval_string("{username}"));
		// 插入事务状态为通过
		lr_end_transaction("登录", LR_FAIL);
	}



	return 0;
}
