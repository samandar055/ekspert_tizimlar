# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qfIhXjH4sGwLhSXrBwQus6NZ04EgZ66_
"""

def dori_tavsiya(kasallik):
    if kasallik.lower() == "gripp":
        return " Parasetamol"
    elif kasallik.lower() == "spazma":
        return "No-spa"
    elif kasallik.lower() == "bosh og'rig'i":
        return " Aspirin"
    elif kasallik.lower() == "tomoq og'rig'i":
        return "Strepsils"
    elif kasallik.lower() == "tumov":
        return "Nazivin"
    elif kasallik.lower() == "allergiya":
        return "Suprastin"
    elif kasallik.lower() == "yo'tal":
        return " Ambroxol, ACC"
    elif kasallik.lower() == "oshqozon og'rig'i":
        return "Rennie"
    elif kasallik.lower() == "uyqusizlik":
        return "Melatonin"
    elif kasallik.lower() == "stress":
        return " Sedafiton"
    else:
        return "Shifokorga murojaat qiling"

kasallik = input("Kasallik nomini kiriting: ")
natija = dori_tavsiya(kasallik)
print(natija)





