Action()
{
	// ����ҳ
	web_url("����ҳ","URL=http://192.168.72.22/iwebshop/",LAST);

	// �����¼-��ת����¼ҳ��
	web_url("�򿪵�¼ҳ��","URL=http://localhost/iwebshop/index.php?controller=simple&action=login",LAST);

	// �����û���������-��¼

	web_submit_data("web_submit_data",
		"Action=http://localhost/iwebshop/index.php?controller=simple&action=login_act",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		"Mode=HTML",
		ITEMDATA,
		"Name=login_info", "Value=admin", ENDITEM,
		"Name=password", "Value=123456", ENDITEM,
		"Name=callback", "Value=", ENDITEM,
		LAST);
	// �˳�
	web_url("�˳���¼","URL=http://localhost/iwebshop/index.php?controller=simple&action=logout",LAST);
	return 0;
}
