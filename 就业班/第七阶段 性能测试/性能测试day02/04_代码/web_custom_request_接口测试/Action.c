Action()
{

// 查询
	web_custom_request("web_custom_request",
		"URL=http://127.0.0.1:8000/api/departments/",
		"Method=GET",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"Mode=HTTP",
		"Body=",
		LAST);



// 新增学院
	web_custom_request("web_custom_request",
		"URL=http://127.0.0.1:8000/api/departments/",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"Mode=HTTP",
		"EncType=application/json",
		"Body={\"data\": [{\"dep_id\":\"TT004\",\"dep_name\":\"Test学院\",\"master_name\":\"Test-Master\",\"slogan\":\"Here is Slogan\"}]}",
		LAST);

	// 更新
	web_custom_request("web_custom_request",
		"URL=http://127.0.0.1:8000/api/departments/TT004/",
		"Method=PUT",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"Mode=HTTP",
		"EncType=application/json",
		"Body={\"data\": [{\"dep_id\":\"TT004\",\"dep_name\":\"Test学院2222222\",\"master_name\":\"Test-Master\",\"slogan\":\"Here is Slogan\"}]}",
		LAST);



// 删除学院
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
