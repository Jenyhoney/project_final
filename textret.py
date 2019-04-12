import docxpy

file = 'C:/Users/user/Documents/malayalam.docx'

# extract text
text = docxpy.process(file)

# extract text and write images in /tmp/img_dir
#text = docxpy.process(file, "/tmp/img_dir")
print(text)
