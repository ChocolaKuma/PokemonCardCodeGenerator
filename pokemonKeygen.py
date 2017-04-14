
##Example codes
##HTG-V6YW-676-DZYXY     FATESCOLIDE DECK SKY GUARDIAN
##H9C-H5SP-3FK-QMR       XYBREAKTHROUGH
##KMK-LWJX-772-GGC       XYBREAKPOINT
##DDV-WGQG-ZZC-7WX       SUNANDMOON DECK FOREST SHADOW
##QQ6-RB74-J6B-RBJ       XYBREAKPOINT
##MDR-JPY4-TQA-FQP       XYBREAKTHROUGH
##
##3-4-3-3


import random as r
import string 
x = 0

while(x<10):
    Code = r.choice(string.ascii_uppercase)
    Code = Code + r.choice(string.ascii_uppercase)
    Code = Code + r.choice(string.ascii_uppercase)
    Code = Code + "-"
    Code = Code + r.choice(string.ascii_uppercase)
    Code = Code + r.choice(string.ascii_uppercase)
    Code = Code + r.choice(string.ascii_uppercase)
    Code = Code + r.choice(string.ascii_uppercase)
    Code = Code + "-"
    Code = Code + r.choice(string.ascii_uppercase)
    Code = Code + r.choice(string.ascii_uppercase)
    Code = Code + r.choice(string.ascii_uppercase)
    Code = Code + "-"
    Code = Code + r.choice(string.ascii_uppercase)
    Code = Code + r.choice(string.ascii_uppercase)
    Code = Code + r.choice(string.ascii_uppercase)
    print(Code)
    x=x+1
