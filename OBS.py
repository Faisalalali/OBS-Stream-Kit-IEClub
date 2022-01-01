import os.path as p
import PySimpleGUI as sg

VERSION = "0.1/GUI"
title = str("IE CLUB EDITION " + VERSION)
# windowSize = (150, 300)
windowSize = (0, 0)  # Make it fit
sg.ChangeLookAndFeel("DarkBrown5")

layout_name1 = [
    [sg.Input(key="-name1-", size=(30, 1))],
    [
        sg.Text("Score"),
        sg.Button(
            key="-left_score_m-",
            pad=(0, 0),
            button_text="-",
            tooltip="Decrease Score",
            size=(2, 1),
        ),
        sg.InputText(0, size=(10, 1), pad=(0, 0)),
        sg.Button(
            key="-left_score_p-",
            pad=(0, 0),
            button_text="+",
            tooltip="Increase Score",
            size=(2, 1),
        ),
    ],
]
layout_name2 = [
    [sg.Input(key="-name2-", size=(30, 1))],
    [
        sg.Text("Score"),
        sg.Spin([i for i in range(0, 100)], initial_value=0, size=(10, 1)),
    ],
]
layout_names = [
    [
        sg.Frame(
            "Left Player", layout_name1, element_justification="left", border_width=0
        ),
        sg.Button(key="-Swap-", button_text="<->", tooltip="Swap the names"),
        sg.Frame(
            "Right Player", layout_name2, element_justification="left", border_width=0
        ),
    ],
    [],
]
layout = [
    [sg.Frame("Names", layout_names, title_location="n", font=("", 15))],
    [],
    # [sg.Button("Close")],
    [sg.B("Start A Thread"), sg.B("Dummy"), sg.Button("Exit2")],
    [sg.OK(), sg.Cancel(), sg.B("Apply")],
]
window = sg.Window(
    title=title,
    layout=layout,
    margins=windowSize,
    icon=r"icon/ie logo only ( dark ).ico",
)


def save_names(values):
    print(
        "Saving in", f'({p.abspath("")})'
    )  # hehe, clever right? although still useless but wtvr...
    # Actully save stuff
    with open("Name1.txt", "w+") as n1, open("Name2.txt", "w+") as n2:
        print(f"{values=}")
        n1.write(values["-name1-"])
        n2.write(values["-name2-"])


# initilize
def initialize_text_fields():
    with open("Name1.txt", "r") as n1, open("Name2.txt", "r") as n2:
        window["-name1-"].update(n1.read())
        window["-name2-"].update(n2.read())


event, values = window.read(timeout=100)
initialize_text_fields()
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the Exit button
    if event == "-Swap-":
        # Swap names
        tmp = values["-name1-"]
        values["-name1-"] = values["-name2-"]
        values["-name2-"] = tmp
        save_names(values)
        initialize_text_fields()
        print("Updated")

    # TODO edit apply functionality to only apply when there are changes.
    # + "OK" functions as Cancel if no changes
    if event in ("OK", "Apply"):
        save_names(values)
        print("Saved!")

    if event in ("Cancel", "OK", sg.WIN_CLOSED):
        if event != "OK":
            print("why? what a pain...")
        break


window.close()
exit()


def split(word):
    return [char for char in word]


userInput = ""
print(
    "Program Started!\nIE CLUB EDITION\ns -->  Set Scores\nc --> Set Contestants\nf --> Flip Names and Scores\nb --> Set Current Bracket\ne --> Exit\nh --> help"
)
while userInput.lower() != "e":
    print("__________________________")
    userInput = input()
    if userInput.lower() == "s":
        # ------------Scores-----------------
        scoreInput = input("Enter Score:\n")
        score = open("Score.txt", "w")
        score.write(scoreInput)
        score.close()
    # elif userInput.lower() == "ss":
    #     s1Input = input("Enter Score 1:\n")
    #     score = open("Score1.txt", "w")
    #     score.write(s1Input)
    #     score.close()
    #     s2Input = input("Enter Score 2:\n")
    #     score = open("Score2.txt", "w")
    #     score.write(s2Input)
    #     score.close()
    elif userInput.lower() == "c":
        # ------------Name 1-----------------
        nameInput = input("Enter Contestant 1's Name:\n")
        a = nameInput.find(" ")
        if nameInput[a] == " ":
            nameInput = nameInput[0:a] + "   " + nameInput[a : (len(nameInput))]
        name1 = open("Name1.txt", "w")
        name1.write(nameInput)
        name1.close()
        # ------------Name 2-----------------
        nameInput = input("Enter Contestant 2's Name:\n")
        a = nameInput.find(" ")
        if nameInput[a] == " ":
            nameInput = nameInput[0:a] + "   " + nameInput[a : (len(nameInput))]
        name2 = open("Name2.txt", "w")
        name2.write(nameInput)
        name2.close()
    elif userInput.lower() == "h":
        # ------------Help-----------------
        print(
            "s -->  Set Scores\nc --> Set Contestants\nf --> Flip Names and Scores\nb --> Set Current Bracket\ne --> Exit"
        )
    elif userInput.lower() == "b":
        # -----------Bracket---------------
        bracket = open("bracket.txt", "w")
        bracketInput = input("Enter current bracket: \n")
        a = bracketInput.find(" ")
        if bracketInput[a] == " ":
            bracketInput = (
                bracketInput[0:a] + "   " + bracketInput[a : (len(bracketInput))]
            )
        bracket.write(bracketInput)
        bracket.close()
    elif userInput.lower() == "f":
        # --------------flip---------------
        if (
            (os.path.isfile("Name1.txt"))
            and (os.path.isfile("Name2.txt"))
            and (os.path.isfile("Score.txt"))
        ):
            name1 = open("Name1.txt", "r")
            temp1 = name1.readline()
            name1.close()
            name2 = open("Name2.txt", "r")
            temp2 = name2.readline()
            name2.close()
            name1 = open("Name1.txt", "w")
            name1.write(temp2)
            name1.close()
            name2 = open("Name2.txt", "w")
            name2.write(temp1)
            name2.close()
            score = open("Score.txt", "r")
            temp3 = score.readline()
            score.close()
            temp4 = split(temp3)
            temp5 = temp4[2] + "-" + temp4[0]
            score1 = open("Score.txt", "w")
            score1.write(temp5)
            score1.close()
        else:
            print("files missing")
    else:
        print("Invalid choice")
