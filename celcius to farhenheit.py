from tkinter import Tk, Button, Entry

def converter():
      fah=int(e.get())*9/5+32
      print(fah)
      
r=Tk()
b=Button(r, text = " Enter Temperature In Celcius ")
b.pack()
e=Entry(r)
e.pack()
l=Button(r, text = " Convert to Fehrenheit ", command=converter)
l.pack()
r.mainloop()
