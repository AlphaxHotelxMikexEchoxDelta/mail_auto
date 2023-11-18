import pyautogui as pia
import pyperclip as pyp
from time import sleep

mails = open("mail.txt","r")
lines = ips.readlines()
for line in lines:
    mail = line.replace("\n","")
    
    sleep(5)
    # nouveau mail
    pia.click(1778,361)

    sleep(0.5)
    # destinataire
    pia.click(1953,587)
    pyp.copy(mail)
    pia.hotkey("ctrl", "v")

    sleep(0.5)
    # objet
    pia.click(1822,789)
    pyp.copy("[Candidature spontanée][Génie informatique]")
    pia.hotkey("ctrl", "v")

    sleep(0.5)
    # message
    pia.click(1908,888)
    pyp.copy("""
MAILS MAILS MAILS MAILS MAILS MAILS MAILS MAILS MAILS MAILS 
MAILS MAILS MAILS MAILS MAILS MAILS MAILS MAILS MAILS MAILS 
MAILS MAILS MAILS MAILS MAILS MAILS MAILS MAILS MAILS MAILS 
MAILS MAILS MAILS MAILS MAILS MAILS MAILS MAILS MAILS MAILS 
MAILS MAILS MAILS MAILS MAILS MAILS MAILS MAILS MAILS MAILS 
MAILS MAILS MAILS MAILS MAILS MAILS MAILS MAILS MAILS MAILS 
    """)
    pia.hotkey("ctrl", "v")

    sleep(0.5)
    # CV calendrier
    pia.click(2656,362)
    pia.click(2486,825)
    pia.click(1967,1277)
    pia.click(2656,362)
    pia.click(2486,825)
    pia.click(1768,1372)

    sleep(5)
    # envoi
    pia.click(1702,471)
