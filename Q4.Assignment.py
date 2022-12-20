import re
from pdfminer.high_level import extract_pages, extract_text

# for page_layout in extract_pages("assig.pdf"):
# 	for element in page_layout:
# 		print(element)

text = extract_text("assig.pdf")
modified = []

new_vend_re = re.compile(r'[Q]\d{1}.+\s*[a-zA-Z0-9].+?\s[a-zA-Z0-9]')
for line in text.split('\n'):
	# for i in sorted(line, key=len, reverse=False):
	words =  new_vend_re.match(line)
	if words:
		modified.append(line.strip())
modified.sort()
print(modified)

with open('output.pdf', "w") as writefile:
	for line in modified:
		writefile.write(line + '\n')

		