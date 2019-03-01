Action()
{
	/*

	注意：注册函数位置【必须】放到被关联的【数据函数（数据存在那个函数里边，放到那个函数之前）】之前
    */
	// 插入关联函数
	web_reg_save_param("Welcome",
		"LB=Tours</b></H1>\n",
		"RB=\n"
		"<br>",
		LAST);

	// 打开首页
	web_url("首页","URL=http://127.0.0.1:1080/WebTours/",LAST);



	// 调用
	lr_output_message("获取出的值为：%s",lr_eval_string("{Welcome}"));

	return 0;
}
