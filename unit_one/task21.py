#todo: Задан словарь, его значения необходимо внести по соответвющим тегам и атрибутам вместо вопросов (?)
# заполненный шаблон записать в файл index.html
# template = """
# <!DOCTYPE HTML>
# <html>
#  <head>
#   <title> ? </title>
#   <meta charset=?>
#  </head>
#  <body onload="alert(?)">
#
#   <p>?</p>
#
#  </body>
# </html>
# """
template = """ 
<!DOCTYPE HTML>
<html>
 <head>
  <title> ? </title>
  <meta charset=?>
 </head>
 <body onload="alert(?)">
  <p>?</p>
 </body>
</html>
"""
page = {"title": "Тег BODY",
        "charset": "utf-8",
        "alert": "Документ загружен",
        "p": "Ut wisis enim ad minim veniam,  suscipit lobortis nisl ut aliquip ex ea commodo consequat."}

new_lines = []
for line in template.split('\n'):
    if '?' in line:
        for key, value in page.items():
            if key in line:
                line = line.replace('?', value)
                break
    new_lines.append(line + '\n')


fd = open('index.html', 'w+', encoding='utf-8')
fd.writelines(new_lines)
fd.close()

# temp.close()
# f.close()

