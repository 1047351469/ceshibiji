Action()
{
	/*

	ע�⣺ע�ắ��λ�á����롿�ŵ��������ġ����ݺ��������ݴ����Ǹ�������ߣ��ŵ��Ǹ�����֮ǰ����֮ǰ
    */
	// �����������
	web_reg_save_param("Welcome",
		"LB=Tours</b></H1>\n",
		"RB=\n"
		"<br>",
		LAST);

	// ����ҳ
	web_url("��ҳ","URL=http://127.0.0.1:1080/WebTours/",LAST);



	// ����
	lr_output_message("��ȡ����ֵΪ��%s",lr_eval_string("{Welcome}"));

	return 0;
}
