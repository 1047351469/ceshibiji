Action()
{

	web_set_max_html_param_len("1024");

	lr_start_transaction("����ҳ");

	web_url("WebTours", 
		"URL=http://127.0.0.1:1080/WebTours/", 
		"TargetFrame=", 
		"Resource=0", 
		"RecContentType=text/html", 
		"Referer=", 
		"Snapshot=t1.inf", 
		"Mode=HTML", 
		LAST);

	lr_end_transaction("����ҳ", LR_AUTO);

	lr_think_time(12);

    // ���뼯�ϵ�
	lr_rendezvous("���ϵ�-��¼");

	lr_start_transaction("��¼");
	web_submit_data("login.pl", 
		"Action=http://127.0.0.1:1080/WebTours/login.pl", 
		"Method=POST", 
		"TargetFrame=body", 
		"RecContentType=text/html", 
		"Referer=http://127.0.0.1:1080/WebTours/nav.pl?in=home", 
		"Snapshot=t2.inf", 
		"Mode=HTML", 
		ITEMDATA, 
		"Name=userSession", "Value=123886.107735925zDHcDQVpzzzzzzzHDicDtpDf", ENDITEM, 
		"Name=username", "Value=jojo", ENDITEM, 
		"Name=password", "Value=bean", ENDITEM, 
		"Name=JSFormSubmit", "Value=off", ENDITEM, 
		"Name=login.x", "Value=63", ENDITEM, 
		"Name=login.y", "Value=3", ENDITEM, 
		LAST);

	lr_end_transaction("��¼", LR_AUTO);

	web_find("web_find",
		"What=jojo",
		LAST);

	lr_think_time(26);

	lr_start_transaction("�˳�");

	web_url("SignOff Button", 
		"URL=http://127.0.0.1:1080/WebTours/welcome.pl?signOff=1", 
		"TargetFrame=body", 
		"Resource=0", 
		"RecContentType=text/html", 
		"Referer=http://127.0.0.1:1080/WebTours/nav.pl?page=menu&in=home", 
		"Snapshot=t3.inf", 
		"Mode=HTML", 
		LAST);

	lr_end_transaction("�˳�", LR_AUTO);

	return 0;
}
