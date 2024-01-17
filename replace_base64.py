string = "https://bcca65a9a395227f1a54fee96dec6c37.ctf.hacker101.com/?post=duXbzT!-FHd!YbxlzkUYasxaXvZgSYYmc8rXWoeWC!NVZtm9XGymMrX-UgAl4M-nQ0c5Ke67DtfCqdvpM13w83hQ0AT7GQeh0T2wtMS0Eiv1HkiHuRBTNwqtCdSWum94piT9BZpm4yzI!3PZzYYwhjcqYX6oIBUx3vV7EU9LHod4EAjE4!6HOtWN87FhE9oIs-MsO98Wa6kmN5FQyFLLcA~~"
 
# replace the following characters and then print the new string
new_string = string.replace("~", "=" ).replace("!", "/").replace("-", "+")
 
print(string)
print(new_string)