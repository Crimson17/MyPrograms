import sys, time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


allKeysList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a',
               's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
sharpKeyboardKeys = ['1', '2', '4', '5', '6', '8', '9', 'q', 'w', 'e', 't', 'y', 'i', 'o', 'p', 's', 'd', 'g', 'h', 'j',
                     'l', 'z', 'c', 'v', 'b']

pianoNotesList = ['C2', 'D2', 'E2', 'F2', 'G2', 'A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4',
                  'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6', 'D6', 'E6', 'F6', 'G6', 'A6',
                  'B6', 'C7']
sharpKeys = ['C2#', 'D2#', 'F2#', 'G2#', 'A2#', 'C3#', 'D3#', 'F3#', 'G3#', 'A3#', 'C4#', 'D4#', 'F4#', 'G4#', 'A4#',
             'C5#', 'D5#', 'F5#', 'G5#', 'A5#', 'C6#', 'D6#', 'F6#', 'G6#', 'A6#']


notesInput = open("Notes.txt", "r")
notesList = notesInput.read().upper().splitlines()
noteNumber = 1
i = 2

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

tempoInput = int(input("Tempo(BMP): "))
timeBetweenClicks = 60 / tempoInput

print(notesList)

"""
while "q" not in notesInput:
    notesInput = (input("%d. note: " % noteNumber)).lower()
    if "a" in notesInput or "b" in notesInput or "c" in notesInput or "d" in notesInput or "e" in notesInput\
            or "f" in notesInput or "g" in notesInput or "q" in notesInput:
        if notesInput.lower() != "q":
            notesList.append(notesInput.upper())
            noteNumber = noteNumber + 1
    else:
        sys.exit("The inputted note is not right!")
"""

browser = webdriver.Chrome(r"C:\Users\Ivan\Documents\GitHub\MyPrograms\ChromeVersions\76.exe", options=options)
browser.get(r"https://recursivearts.com/virtual-piano/")
time.sleep(5)

for x in notesList:
    if "#" not in x:
        if x in pianoNotesList:
            action = ActionChains(browser)
            action.key_down(allKeysList[pianoNotesList.index(x)])
            action.key_up(allKeysList[pianoNotesList.index(x)])
            action.perform()
    else:
        if x in sharpKeys:
            action = ActionChains(browser)
            action.key_down(Keys.LEFT_SHIFT)

            action.key_down(sharpKeyboardKeys[sharpKeys.index(x)])
            action.key_up(sharpKeyboardKeys[sharpKeys.index(x)])

            action.key_up(Keys.LEFT_SHIFT)
            action.perform()

    time.sleep(timeBetweenClicks)
