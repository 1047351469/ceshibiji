Action()
{
    
	lr_start_transaction("打开首页");

	web_url("打开首页","URL=http://127.0.0.1:1080/WebTours/",LAST);
    
	lr_end_transaction("打开首页", LR_AUTO);

	return 0;
}
