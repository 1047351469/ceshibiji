Action()
{

	lr_start_transaction("��Ʊ-��Ʊ��");

    
	lr_start_transaction("��Ʊ-����ҳ");

    // ʹ�ù������� ����Session
	web_reg_save_param("Session",
		"LB=ssion value=",
		"RB=>",
		LAST);


    web_url("����ҳ","URL=http://127.0.0.1:1080/WebTours/",LAST);

	lr_end_transaction("��Ʊ-����ҳ", LR_AUTO);

	lr_start_transaction("��Ʊ-��¼");


	web_submit_data("��¼",
		"Action=http://127.0.0.1:1080/WebTours/login.pl",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		"Mode=HTML",
		ITEMDATA,
		"Name=userSession", "Value={Session}", ENDITEM,
		"Name=username", "Value={username}", ENDITEM,
		"Name=password", "Value=123456", ENDITEM,
		LAST);

	lr_end_transaction("��Ʊ-��¼", LR_AUTO);
    
	lr_start_transaction("��Ʊ-��Ʊҵ��");


	lr_rendezvous("��Ʊ-���ϵ�");

	web_url("��Ʊ-�򿪺�����ҳ","URL=http://127.0.0.1:1080/WebTours/welcome.pl?page=search",LAST);


	web_submit_data("���ǵ���",
		"Action=http://127.0.0.1:1080/WebTours/reservations.pl",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		"Mode=HTML",
		ITEMDATA,
		"Name=advanceDiscount", "Value=0", ENDITEM,
		"Name=depart", "Value=Denver", ENDITEM,
		"Name=departDate", "Value=06/23/2018", ENDITEM,
		"Name=arrive", "Value=Denver", ENDITEM,
		"Name=returnDate", "Value=06/24/2018", ENDITEM,
		"Name=numPassengers", "Value=1", ENDITEM,
		"Name=seatPref", "Value=None", ENDITEM,
		"Name=seatType", "Value=Coach", ENDITEM,
		"Name=findFlights.x", "Value=22", ENDITEM,
		"Name=findFlights.y", "Value=9", ENDITEM,
		"Name=.cgifields", "Value=roundtrip", ENDITEM,
		"Name=.cgifields", "Value=seatType", ENDITEM,
		"Name=.cgifields", "Value=seatPref", ENDITEM,
		LAST);

	web_submit_data("���๫˾",
		"Action=http://127.0.0.1:1080/WebTours/reservations.pl",
		"Method=POST",
		"EncodeAtSign=YES",
		"TargetFrame=",
		"Referer=",
		"Mode=HTML",
		ITEMDATA,
		"Name=outboundFlight", "Value=000;0;06/23/2018", ENDITEM,
		"Name=numPassengers", "Value=1", ENDITEM,
		"Name=advanceDiscount", "Value=0", ENDITEM,
		"Name=seatType", "Value=Coach", ENDITEM,
		"Name=seatPref", "Value=None", ENDITEM,
		"Name=reserveFlights.x", "Value=38", ENDITEM,
		"Name=reserveFlights.y", "Value=5", ENDITEM,
		LAST);

	web_submit_data("web_submit_data",
		"Action=http://127.0.0.1:1080/WebTours/reservations.pl",
		"Method=POST",
		"EncodeAtSign=YES",
		"TargetFrame=",
		"Referer=",
		"Mode=HTML",
		ITEMDATA,
		"Name=firstName", "Value=Joseph", ENDITEM,
		"Name=lastName", "Value=Marshall", ENDITEM,
		"Name=address1", "Value=234 Willow Drive", ENDITEM,
		"Name=address2", "Value=San Jose/CA/94085", ENDITEM,
		"Name=pass1", "Value=Joseph Marshall", ENDITEM,
		"Name=creditCard", "Value=", ENDITEM,
		"Name=expDate", "Value=", ENDITEM,
		"Name=oldCCOption", "Value=", ENDITEM,
		"Name=numPassengers", "Value=1", ENDITEM,
		"Name=seatType", "Value=Coach", ENDITEM,
		"Name=seatPref", "Value=None", ENDITEM,
		"Name=outboundFlight", "Value=200;338;06/22/2018", ENDITEM,
		"Name=advanceDiscount", "Value=0", ENDITEM,
		"Name=returnFlight", "Value=", ENDITEM,
		"Name=JSFormSubmit", "Value=off", ENDITEM,
		"Name=buyFlights.x", "Value=40", ENDITEM,
		"Name=buyFlights.y", "Value=9", ENDITEM,
		"Name=.cgifields", "Value=saveCC", ENDITEM,
		LAST);

	lr_end_transaction("��Ʊ-��Ʊҵ��", LR_AUTO);

		web_url("�˳���¼",
		"URL=http://127.0.0.1:1080/WebTours/welcome.pl?signOff=1",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		LAST);

	lr_end_transaction("��Ʊ-��Ʊ��", LR_AUTO);

	return 0;
}
