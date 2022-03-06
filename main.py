from pyautogui import *
from time import *
import pyautogui as pt
from random import *
from pyperclip import *
import pyperclip as pc

#just to rectify the text because some character doesnt'n write like I want .
def _workaround_write(text):
    pc.copy(text)
    pt.hotkey('ctrl', 'v')
    pc.copy('')



# more precise position of the image 'confidence=.8' .
def nav_to_imgage_more_precise(image, clicks, off_x=0, off_y=0):
    position = pt.locateCenterOnScreen(image, confidence=.8)
    if position is None:
        print(f"{image} not found ...")
        return 0
    else:
        pt.moveTo(position, duration=.1)
        pt.moveRel(off_x, off_y, duration=.1)
        pt.click(clicks=clicks, interval=.3)


def main():
    phrase0 = ("(0) Entrez une phrase : ")
    phrase1 = ("(1) Entrez une phrase : ")
    phrase2 = ("(2) Entrez une phrase : ")
    phrase3 = ("(3) Entrez une phrase : ")
    phrase4 = ("(4) Entrez une phrase : ")
    phrase5 = ("(5) Entrez une phrase : ")
    phrase6 = ("(6) Entrez une phrase : ")
    phrase7 = ("(7) Entrez une phrase : ")
    phrase8 = ("(8) Entrez une phrase : ")
    phrase9 = ("(9) Entrez une phrase : ")
    phrase10 = ("(10) Entrez une phrase : ")
    phrase11 = ("(11) Entrez une phrase : ")
    phrase12 = ("(12) Entrez une phrase : ")
    phrase13 = ("(13) Entrez une phrase : ")
    phrase14 = ("(14) Entrez une phrase : ")
    phrase15 = ("(15) Entrez une phrase : ")
    phrase16 = ("(16) Entrez une phrase : ")
    phrase17 = ("(17) Entrez une phrase : ")
    phrase18 = ("(18) Entrez une phrase : ")
    phrase19 = ("(19) Entrez une phrase : ")
    phrase20 = ("!rank")
  

    sleep(2)
    
    verify_search_ma_bar = nav_to_imgage_more_precise(
        "images/ma-barre.png", 1)
    verify_search_bar = nav_to_imgage_more_precise("images/barre.png", 1)
    sleep(2)
    #loop to verify if u can see the scearch bar of discord , I have my own discord theme so its why there is 2 verify_scearch_bar ^^ .
    while verify_search_ma_bar == 0 or verify_search_bar == 0:
        print("we are in the loop")
        _workaround_write(phrase0)
        pt.press('enter')
        sleep(1)
        _workaround_write(
            phrase1)
        pt.press('enter')
        sleep(1.5)
        _workaround_write(phrase2)
        pt.press('enter')
        sleep(1)
        _workaround_write(
            phrase3)
        pt.press('enter')
        sleep(1.5)
        _workaround_write(
            phrase4)
        pt.press('enter')
        sleep(1)

        _workaround_write(
            phrase5)
        pt.press('enter')
        sleep(1.5)
        _workaround_write(
            phrase6)
        pt.press('enter')
        sleep(1)
        _workaround_write(
            phrase7)
        pt.press('enter')
        sleep(1.5)
        _workaround_write(
            phrase8)
        pt.press('enter')
        sleep(1)
        _workaround_write(
            phrase9)
        pt.press('enter')
        sleep(1.5)
        _workaround_write(
            phrase10)
        pt.press('enter')
        sleep(1)
        _workaround_write(
            phrase11)
        pt.press('enter')
        sleep(1.5)
        _workaround_write(phrase12)
        pt.press('enter')
        sleep(1.5)
        _workaround_write(phrase13)
        pt.press('enter')
        sleep(1)
        _workaround_write(phrase14)
        pt.press('enter')
        sleep(1.5)
        _workaround_write(phrase15)
        pt.press('enter')
        sleep(1)
        _workaround_write(phrase16)
        pt.press('enter')
        sleep(1.5)
        _workaround_write(phrase17)
        pt.press('enter')
        sleep(1)
        _workaround_write(phrase18)
        pt.press('enter')
        sleep(1.5)
        _workaround_write(phrase19)
        pt.press('enter')
        sleep(1)
        _workaround_write(phrase20)
        pt.press('enter')
        if verify_search_ma_bar == 1 or verify_search_bar == 1:
            print("stoping ....!")
            exit(main())

    else:
        return "Not working"

    # main() end here


if __name__ == '__main__':
    main()
