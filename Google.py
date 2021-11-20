try:
   import os,sys,time,requests,bs4
   from bs4 import BeautifulSoup
   from time import sleep
   from os import system
except:
      system("pip install requests bs4")
def jalan():
    tampil = """
==================================================
 Author : MAS BAGAS
=================================================="""
    system("clear")
    sleep(1)
    system("figlet GOOGLE")
    sleep(1)
    print(tampil)
    # isi data
    file = input("Masukan Pencarian: ")
    ulr = f"https://www.google.com/search?&q={file}"
    r = requests.get(ulr)
    cari = BeautifulSoup(r.text,"html.parser")
    a = cari.find("div",class_="BNeawe").text
    # hasil pencarian
    print("Hasil => ",a)

jalan()
