Action()
{

// ��ѯ
	web_custom_request("web_custom_request",
		"URL=http://127.0.0.1:8000/api/departments/",
		"Method=GET",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"Mode=HTTP",
		"Body=",
		LAST);



// ����ѧԺ
	web_custom_request("web_custom_request",
		"URL=http://127.0.0.1:8000/api/departments/",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"Mode=HTTP",
		"EncType=application/json",
		"Body={\"data\": [{\"dep_id\":\"TT004\",\"dep_name\":\"TestѧԺ\",\"master_name\":\"Test-Master\",\"slogan\":\"Here is Slogan\"}]}",
		LAST);

	// ����
	web_custom_request("web_custom_request",
		"URL=http://127.0.0.1:8000/api/departments/TT004/",
		"Method=PUT",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"Mode=HTTP",
		"EncType=application/json",
		"Body={\"data\": [{\"dep_id\":\"TT004\",\"dep_name\":\"TestѧԺ2222222\",\"master_name\":\"Test-Master\",\"slogan\":\"Here is Slogan\"}]}",
		LAST);



// ɾ��ѧԺ
	web_custom_request("web_custom_request",
		"URL=http://127.0.0.1:8000/api/departments/TT004/",
		"Method=DELETE",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"Mode=HTTP",
		"EncType=application/json",
		"Body=",
		LAST);

	return 0;
}
