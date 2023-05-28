import tkinter
import requests

def gett():
    data = requests.get("https://api.kanye.rest").json()["quote"]
    # if data=="2024":
    #     gett()
    if len(data)>100:
        Label.config(width=len(data))
    Label.config(text=data)

window=tkinter.Tk()
Label=tkinter.Label(text="",width=100)
Label.grid(column=0,row=0)
Baton=tkinter.Button(text="Get",command=gett)
Baton.grid(column=0,row=1)



window.mainloop()

