Action()
{
	// ������� 
	int result;
		// ���� session

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

	// ���뿪ʼ ����

	lr_start_transaction("��¼");

    // ��ȡ��¼����û���
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
    
    // ��� username
    lr_output_message("usernameֵΪ��%s",lr_eval_string("{username}"));

	// �ж� �Ƿ�Ϊjojo

	result=strcmp(lr_eval_string("{username}"),"jojo");

	/*

	ע�⣺�������ֱ�Ӷ�ȡ������lr_eval_string()��ȡ��
    */
	lr_output_message("�жϵĽ��ֵΪ��%d",result);


	// �ж��Ƿ���ȣ���Ȳ��� LR_PASS����״̬
	if(result==0){
		lr_output_message("��¼���û�Ϊ:%s ͨ����",lr_eval_string("{username}"));
		// ��������״̬Ϊͨ��
		lr_end_transaction("��¼", LR_PASS);
	}else{
		lr_output_message("��¼���û�Ϊ:%s ��ͨ����",lr_eval_string("{username}"));
		// ��������״̬Ϊͨ��
		lr_end_transaction("��¼", LR_FAIL);
	}



	return 0;
}
