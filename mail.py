import pyautogui as pia
import pyperclip as pyp
from time import sleep

try:
    mails = open("mail.txt","r")
    lines = mails.readlines()

    cc = len(lines)

    for line in lines:

        cc = cc - 1
        print("--- {}mails restant ---".format(cc))

        mail = line.replace("\n","")
        print("{} [en cours...]".format(mail))

        sleep(1)
        # nouveau mail
        pia.click(1778,361)

        sleep(1)
        # destinataire
        pia.click(1953,587)
        pyp.copy(mail)
        pia.hotkey("ctrl", "v")

        sleep(1)
        # objet
        pia.click(1822,789)
        pyp.copy("[Candidature spontanée][Génie informatique]")
        pia.hotkey("ctrl", "v")

        sleep(1)
        # message
        pia.click(1908,888)
        pyp.copy("""
MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL
MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL
MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL
MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL
MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL
MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL
MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL MAIL
        """)
        pia.hotkey("ctrl", "v")

        sleep(1)
        # CV calendrier
        pia.click(2656,362)
        pia.click(2486,825)
        sleep(0.5)
        pia.click(1768,1372)

        sleep(4)
        # envoi
        pia.click(1702,471)
        print("{} [Envoye]\n".format(mail))
except IOError as e:
    print("Oopsiii, fichier introuvable ! (~_~)")
