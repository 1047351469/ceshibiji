Action()
{
    
	lr_start_transaction("ע��-����ҳ");

	web_url("ע��-����ҳ","URL=http://127.0.0.1:1080/WebTours/",LAST);

	lr_end_transaction("ע��-����ҳ", LR_AUTO);

	lr_start_transaction("ע��-ע��ҳ��");

	web_url("ע��-��ע��ҳ��","URL=http://127.0.0.1:1080/WebTours/login.pl?username=&password=&getInfo=true",LAST);

	lr_end_transaction("ע��-ע��ҳ��", LR_AUTO);

	lr_start_transaction("ע��-ע��ҵ��");

	lr_rendezvous("���ϵ�-ע��");

	web_submit_data("ע��ҳ��",
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

	lr_end_transaction("ע��-ע��ҵ��", LR_AUTO);

	return 0;
}
