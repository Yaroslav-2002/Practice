import http.client
import json
from tkinter import *

conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "0b612b1598msh3361048666861b6p1c298djsnc9e2607b64e9",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

conn.request("GET", "/api/npm-covid-data/europe", headers=headers)

res = conn.getresponse()
global data
data = res.read()
data = json.loads(data.decode("UTF-8"))
print(data[6]['id'])
def search_country(country):
    for index, item in enumerate(data): 
        if item['Country'] == country:
            return index
            
def output():
    country = entry.get()
    if search_country(country) == None:
        field.delete(0.0, END)
        field.insert(0.0, "There's no such country in Europe")
    else:
        TotalDeath = "Total death: "+str(data[search_country(country)]['TotalDeaths'])+'\n'
        Country = "Country: "+str(data[search_country(country)]['Country'])+'\n'
        NewDeaths = "New deaths: "+str(data[search_country(country)]['NewDeaths'])+'\n'
        field.delete(0.0, END)
        field.insert(0.0, TotalDeath)
        field.insert(0.0, NewDeaths)
        field.insert(0.0, Country) 

        
def output_countries(countries):
    countries.reverse()
    field2.delete(0.0, END)
    for country in countries:
        field2.insert(0.0, country) 
    field2.insert(0.0, "Countries list:")

def search_all_countries():
    countries=[]
    for item in data: 
        countries.append('\n')
        countries.append(item['Country'])
        
    return countries
def update():
    
    conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")

    headers = {
    'x-rapidapi-key': "0b612b1598msh3361048666861b6p1c298djsnc9e2607b64e9",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

    conn.request("GET", "/api/npm-covid-data/europe", headers=headers)

    res = conn.getresponse()
    data = res.read()
    data = json.loads(data.decode("UTF-8"))
    countries = search_all_countries()
    output_countries(countries)
    

# tkinter
root = Tk()
root['bg']='#fafafa'
root.title('Covid Statistics Pro')
root.wm_attributes('-alpha')
root.geometry('520x250')


entry = Entry(root, font=('Arial',15))
entry.grid(row=0, column=1, stick='we')
root.resizable(width=False, height=False)
for i in range(4):
    root.grid_columnconfigure(i, minsize=60)

for i in range(1,5):
    root.grid_rowconfigure(i, minsize=60)

global field
field = Text (root, width=33, height=10, wrap=WORD, relief='solid', font = 'Arial', bg='gray')
field.grid(row=1, column=0, stick='we',padx=5, pady=5, columnspan= 3)
field2 = Text (root, width=10, height=10, wrap=WORD, relief='solid', font = 'Arial', bg='gray')
field2.grid(row=1, column=3, stick='we',padx=5, pady=5, columnspan= 3)
update()
title = Label( text='Введіть країну:', font=40).grid(row=0, column=0)
Button(text='пошук', bd=5, font=('Arial', 13),  command=lambda : output()).grid(row=0, column=2, stick='wens', padx=5, pady=5)
Button(text='оновити', bd=5, font=('Arial', 13),  command=lambda : update()).grid(row=0, column=3, stick='wens', padx=5, pady=5)
root.mainloop()