import random
import js
from js import document
from js import console
import string
import pandas as pd
from js import navigator


document.getElementById('len').value = 8
def genrt(*args, **kwargs):
    btn = document.getElementById('btn-form')
    #btn.style.backgroundColor = "red"
    upper = document.getElementById("upper").checked
    digits = document.getElementById("digits").checked
    ponct = document.getElementById("ponct").checked

    inp = document.getElementById("password-generated")
    len = int(document.getElementById('len').value)
    letters = string.ascii_lowercase
    if upper == True:
        letters += string.ascii_uppercase
    if digits == True:
        letters += string.digits
    if ponct == True:
        letters += string.punctuation

    pw=''
    for i in range(len):
        l = random.choice(letters)
        pw+=l
    
    inp.value = pw


genrt()
