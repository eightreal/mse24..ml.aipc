import json
import requests

url = "https://app-stores.p.rapidapi.com/search"
keyfile = "key.txt"

def resquest_google(input:str, writeable:bool=False) :

	query_string = {"language":"zh","store":"google","term":input}
	key = ""
	with open(keyfile,"r") as kf:
		key = kf.read()
		key.strip()
	headers = {
		"x-rapidapi-key": "82e7be9f73mshd050f89fe9d4377p1ba1bdjsn99cafbd0e1f9",
		"x-rapidapi-host": "app-stores.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=query_string)
	#请求结果转json
	res = response.json()
	print(json.dumps(res[0], ensure_ascii=False, indent=4))
	#筛选结果项目
	# app_list = [{k: item[k] for k in ('id', 'name', 'description', 'screenshots', "category", "developer") if k in item} for item in res]
	app_list = [{k: item[k] for k in ('name', 'description', "category", "developer", "ratings") if k in item} for item in res]
		
 #结果转字符串
	json_str = json.dumps(app_list, ensure_ascii=False, indent=4)

	if writeable:
		with open(input+'.json', 'w', encoding='utf-8') as file:
			file.write(json_str)

		print("文件写入完成")
	return app_list

# resquest_google("网易开发的游戏",  True)
