import pyperclip
import sys
#------------------------------------------------------------------#
def add_img(imgName):
    img_format = '''  <br />\n  <img alt="{name}" src="../Images/{name}.jpg"/>\n  <br />'''
    output = img_format.format(name = imgName)
    return output


def add_para_from_clipboard():
    lineformat = "  <p>{content}</p>"
    output = ''
    rawString = pyperclip.paste()
    rawString = rawString.replace("“", "「")
    newString = rawString.replace("”", "」")

    raw_list = newString.split("\r\n")
    
    for i in range(len(raw_list)):
        if raw_list[i] == '':
            raw_list[i] = '  <br />'

        else:
            raw_list[i] = lineformat.format(content = raw_list[i])
        
    output = '\n'.join(raw_list)
    
    return output
    

def toRawTXT():
    raw_dir = r"C:\Users\user\Desktop\PROJECT EPUB\{Project_title}\Raw\{Chapter}.html"
    
    projectTitle = input("project file name(full name): ")
    title = input("chapter title: ")
    
    file = open(raw_dir.format(Project_title = projectTitle, Chapter = title))
    file.write(pyperclip.paste())

def html_template_generation(ID, title, content):
    template_1 = '''<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE html>\n\n<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">'''
    template_2 = '''\n<head>\n  <link href="../Styles/main_style.css" rel="stylesheet" type="text/css"/>\n  <title>{chapterID}</title>\n</head>'''
    template_3 = '''\n\n<body>\n  <h2>{title}</h2>\n  <br />\n{Content}\n</body>\n</html>'''
    # template_3 = '''\n\n<body>\n    <h2>{title}</h2>\n    <br />\n</body>\n</html>'''
    
    output = template_1 + template_2.format(chapterID = ID) + template_3.format(title = title, Content = content)
    
    return output


def main():
    print("Welcome!")
    print("pls copy the first part of the content first! press any key to continue.")
    input()
    moreExtraContent = True
    content = add_para_from_clipboard()


    projectTitle = input("project file name(full name): ")
    if projectTitle == "":
        sys.exit("ERROR: NO_CONTENT")

    ChapterID = input("chapterID: ")
    ChapterName = input("Chapter Name: ")
    directory = r"C:\Users\user\Desktop\PROJECT EPUB\{Project_title}\processed\{Chapter}.html"

    template = open(directory.format(Project_title = projectTitle, Chapter = ChapterID),"w", encoding="utf-8")
    pyperclip.copy(html_template_generation(ChapterID, ChapterName, content))

    template.write(pyperclip.paste())
    template.close()

    print("template generated!")

    while moreExtraContent == True:

        DLC = ""
        string_bool = input("Is there any extra content?(Y/N): ")

        if string_bool == "N":
            moreExtraContent = False
            break

        DLC_type = input("Image or Text: ")

        if DLC_type == "Image":
            DLC = add_img(input("image name: "))
        else:
            print("pls copy the extra text first, press any key to continue")
            input()
            DLC = add_para_from_clipboard()

        content = content + "\n" + DLC

        New_template = open(directory.format(Project_title = projectTitle, Chapter = ChapterID),"w", encoding="utf-8")
        pyperclip.copy(html_template_generation(ChapterID, ChapterName, content))
        New_template.write(pyperclip.paste())
        New_template.close()
    
    print("File generation is finished, press any key to exit!")
    input()
    return 1

main()

    
