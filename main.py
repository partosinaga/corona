from details import *
import requests
import json
from tkinter import *
from datetime import datetime


now = datetime.now()
current_time = now.strftime('%d-%m-%Y')

# get data indonesia global
r = requests.get('https://api.kawalcorona.com/indonesia')
data = r.text
data = data.replace('[', '')  # remove [ from string
data = data.replace(']', '')  # remove ] from string
dataJson = json.loads(data)  # format into json data
country = dataJson['name']
positive = dataJson['positif']
recovered = dataJson['sembuh']
died = dataJson['meninggal']

# start GUI
app = Tk()
app.title('Covid - 19 | ' + country + ' Statistic')
app.geometry('860x200')

# positive
partLabel = Label(app, text='POSITIF', font=('bold', 12))
partLabel.grid(row=0, column=0, padx=100, pady=5)
partContent = Label(app, text=positive, font=('bold', 14))
partContent.grid(row=1, column=0, padx=100)

# recovered
partLabel = Label(app, text='SEMBUH', font=('bold', 12))
partLabel.grid(row=0, column=1, padx=100, pady=5)
partContent = Label(app, text=recovered, font=('bold', 14))
partContent.grid(row=1, column=1, padx=100)

# died
partLabel = Label(app, text='MENINGGAL', font=('bold', 12))
partLabel.grid(row=0, column=2, padx=100, pady=5)
partContent = Label(app, text=died, font=('bold', 14))
partContent.grid(row=1, column=2, padx=100)

partNotif = Label(app, text=' ')
partNotif.grid(row=2, column=0, columnspan=3)

partNotif = Label(app, text=country + ' | ' + current_time)
partNotif.grid(row=3, column=0, columnspan=3)

btnDetail = Button(app, text='Details', width=30, command=showDetails)
btnDetail.grid(row=4, column=0, columnspan=3)

# execute program
app.mainloop()
