Action()
{
	/*
	web_reg_save_param("Session",
		"LB=name=userSession value=",
		"RB=>",
		LAST);

	
	// ��WebTours��ҳ
	web_url("��ҳ","URL=http://127.0.0.1:1080/WebTours/",LAST);

	// ��¼����
	
	web_submit_data("��¼",
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


	// ʹ�� ��һ�ַ�����ʵ��

	// ����ҳ
	web_custom_request("��ҳ_web_custom_request",
		"URL=http://127.0.0.1:1080/WebTours/",
		"Method=GET",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"Mode=HTML",
		"Body=",
		LAST);

	// ��¼
	
	return 0;
}
