import pyperclip

rawString = pyperclip.paste()
rawString = rawString.replace("“", "「")
newString = rawString.replace("”", "」")


raw_list = newString.split("\n")

for i in range(len(raw_list)):
    if raw_list[i] == '':
        raw_list[i] = '  <br />'
    else:
        raw_list[i] = "  <p>"+raw_list[i]+"</p>"

output = '\n'.join(raw_list)
print(output)