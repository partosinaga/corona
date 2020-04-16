from tkinter import *
import json
import requests


def showDetails():
    root = Tk()
    root.geometry('400x800')

    prov = StringVar()
    prov = Label(root, text='PROVINSI')
    prov.grid(row=0, column=0, padx=5, sticky=W)

    pos = StringVar()
    pos = Label(root, text='POSITIF')
    pos.grid(row=0, column=1, padx=5)

    pos = StringVar()
    pos = Label(root, text='SEMBUH')
    pos.grid(row=0, column=2, padx=5)

    pos = StringVar()
    pos = Label(root, text='MENINGGAL')
    pos.grid(row=0, column=3, padx=5)

    api = requests.get('https://api.kawalcorona.com/indonesia/provinsi')
    response = api.json()

    i = 0
    rows = 1

    for row in response:
        provData = Label(root, text=response[i]['attributes']['Provinsi'])
        provData.grid(row=rows, column=0, padx=5, sticky=W)

        posData = Label(root, text=response[i]['attributes']['Kasus_Posi'])
        posData.grid(row=rows, column=1, padx=5)

        recovData = Label(root, text=response[i]['attributes']['Kasus_Semb'])
        recovData.grid(row=rows, column=2, padx=5)

        dieData = Label(root, text=response[i]['attributes']['Kasus_Meni'])
        dieData.grid(row=rows, column=3, padx=5)

        i += 1
        rows += 1
