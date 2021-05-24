import requests
import tkinter
from bs4 import BeautifulSoup


root = tkinter.Tk()
canvas1 = tkinter.Canvas(root, width=450, height=275)
canvas1.pack()

string_arr = []


def scrap_page(country_code):
    url = 'https://www.worldometers.info/coronavirus/country/' + country_code
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all(id='maincounter-wrap')
    country_name = soup.find(class_='content-inner')

    name = country_name.find('h1')
    string_arr.append(name.text[3:])

    for result in results:
        case_elem = result.find('h1')
        number_elem = result.find('span')
        if None in (case_elem, number_elem):
            continue
        string_arr.append(case_elem.text)
        string_arr.append(number_elem.text)

    def apply_to_label():
        n = len(string_arr)
        element = ''
        for i in range(n):
            element = element + string_arr[i] + '\n' + '\n'
        return element

    label_case = tkinter.Label(root, text=apply_to_label())
    label_case.config(font=('helvetica', 10))
    canvas1.create_window(325, 150, window=label_case)
    string_arr.clear()


label1 = tkinter.Label(root, text='Enter country name:')
label1.config(font=('helvetica', 10))
canvas1.create_window(100, 75, window=label1)

code_entry = tkinter.Entry(root)
canvas1.create_window(100, 100, window=code_entry)

button1 = tkinter.Button(text='Scrap Page', command=lambda: scrap_page(code_entry.get()))
canvas1.create_window(100, 150, window=button1)


root.mainloop()

