Action()
{
    
	lr_start_transaction("����ҳ");

	web_url("����ҳ","URL=http://127.0.0.1:1080/WebTours/",LAST);
    
	lr_end_transaction("����ҳ", LR_AUTO);

	return 0;
}
