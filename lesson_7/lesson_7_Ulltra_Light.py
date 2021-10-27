import datetime

from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage

"""""
Работа с текстами
"""""


def get_context(company, result_sku_list):  # возвращает словарь аргуменов
    return {
        'retailer': company,
        'sku_list': result_sku_list,
    }


def from_template(company, result_sku_list, template, signature):
    template = DocxTemplate(template)
    context = get_context(company, result_sku_list)  # gets the context used to render the document

    img_size = Cm(15)  # sets the size of the image
    acc = InlineImage(template, signature, img_size)

    context['acc'] = acc  # adds the InlineImage object to the context
    template.render(context)

    template.save(company + '_' + str(datetime.datetime.now().date()) + '_report.docx')


def generate_report(company, result_sku_list):
    template = 'report.docx'
    signature = 'Major.png'
    from_template(company, result_sku_list, template, signature)


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


car_data = ("""
        brand  price  year
        Volvo  1.5  2017
        Lada  0.5  2018
        Audi  2.0  2018
        """)

with open('data_text', 'w') as f:
    f.write(car_data.strip())

# Считывание файла построчно
f = open('data_text')
data = ''
for line in f:
    data += line + '\n'
f.close()

generate_report('MAJOR', data)
