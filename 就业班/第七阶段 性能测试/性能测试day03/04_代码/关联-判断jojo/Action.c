Action()
{	
	// ע��������붨�� �ڿ�ͷ
    int result;
	lr_start_transaction("��¼");

	// ���� session
	web_reg_save_param("Session",
		"LB=name=userSession value=",
		"RB=>",
		LAST);


	// ��URL
	
	web_submit_data("web_submit_data",
		"Action=http://127.0.0.1:1080/WebTours/",
		"Method=GET",
		"TargetFrame=",
		"Referer=",
		"Mode=HTML",
		ITEMDATA,
		LAST);

	// ��ȡ��¼����û���

	web_reg_save_param("username",
		"LB=Welcome, <b>",
		"RB=</b>,",
		LAST);

	// ��¼
	
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
		LAST);

	// �жϵ�¼�û��Ƿ�Ϊjojo 0:Ϊ���  ASCII��

	result = strcmp(lr_eval_string("{username}"),"jojo");

	if(result==0){
		lr_end_transaction("��¼", LR_PASS);
		lr_output_message("���Ϊ��%d,ͨ������",result);

	}else{
		
		lr_end_transaction("��¼", LR_FAIL);
		lr_output_message("���Ϊ��%d,��������",result);
		
	}

	return 0;
}
