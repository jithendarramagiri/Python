# import re
# text = "Email: jithenda@1810.com!"
# matches = re.findall(r'[^a-zA-Z0-9]', text)
# print("Special characters:", matches)


import re
text = "123 4567 89"
pattern = r'\d{2,4}'
result = re.findall(pattern, text)

