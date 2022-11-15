# Imports

import os
import shutil
import subprocess
import sys
import time
from tkinter import filedialog as fd

import keyboard
import runpy

# Set ANSI escape colors

RED = "\033[0;31m"
NC = "\033[0m"
P = "\033[0;35m"

# Set the CWD to the parent directory of the Python file

pydir = sys.argv[0].replace("\\", "/")
h = len(pydir)
stop = False
while True:
    h -= 1
    try:
        chars = pydir[h]
        if chars == "/":
            break
    except IndexError:  # If the script gets an IndexError, then it must already be in the correct directory
        stop = True
        break
if not stop:
    bounded = h
    h = -1
    direc = ""
    while True:
        h += 1
        if h == bounded:
            break
        chars = pydir[h]
        direc += chars
    os.chdir(direc)
jsonfile = ""
global corr


def error(text):  # Error prompt
    print(RED + "Error: " + text + NC)


def createdir(
    credir,
):  # Created this function because I was too lazy to type out "os.mkdir"
    os.mkdir(credir)


def getinput():  # Gets input from the user
    return str(keyboard.read_key())


def writetofile(
    file, towrite
):  # Write to a file. If it doesn't exist, then create it.
    if os.path.isfile(file):
        f = open(file, "r")
        fcontents = f.read()
        f = open(file, "w")
        f.write(fcontents + "\n" + towrite)
    else:
        f = open(file, "w")
        f.write(towrite)
        f.close()


def startpy(a1=""):  # Main menu.
    os.chdir("..")
    f = open("version", "r")
    ver = f.readline()  # Get ScratchLang's local version
    f.close()
    os.chdir("mainscripts")
    if not os.path.isfile("var/asked"):
        if not os.path.isfile("var/vc"):
            print(
                "Would you like ScratchLang to check its version every time you start it? [Y/N]"
            )
            ff = getinput()
            if "h" + ff.lower() == "hy":
                writetofile("var/vc", "Don't remove this file please.")
            writetofile("var/asked", "Don't remove this file please.")
    if os.path.isfile("var/vc"):
        if not a1 == "nope":
            print("Checking version...")  # Check your version
            if os.path.isfile("version"):
                os.remove("version")
            subprocess.run(
                "wget -q https://raw.githubusercontent.com/ScratchLang/ScratchLang/main/version",
                shell=False,
            )  # Get the up-to-date version file from the ScratchLang repo
            utd = "1"
            f = open("version", "r")
            gver = f.readline()
            if not ver == gver:
                utd = "0"
            if utd == "0":
                print(
                    "Your version of ScratchLang ("
                    + ver
                    + ") is outdated. The current version is "
                    + gver
                    + ". Would you like to update? [Y/N]"
                )
                hh = getinput()
                if "h" + hh.lower() == "hy":
                    subprocess.run("git pull origin main", shell=False)
                exit()
            f.close()
            os.remove("version")
    args = False
    global args2
    args2 = False
    try:
        if (
            sys.argv[1] == "--help"
        ):  # If --help is passed as an arguent, then print the help screen.
            print(
                "scratchlang (or 'python3 scratchlang.py' if you haven't created the scratchlang command)\n"
            )
            print("  -1                Create a project.")
            print("  -2                Remove a project.")
            print("  -3                Compile a project.")
            print("  -4                Decompile a project.")
            print("  -5                Export a project.")
            print("  -6                Import a project.")
            print(
                "  --debug [FILE]    Debug a ScratchScript file. Currently not available."
            )
            print("  --help            Display this help message.")
            exit()
        args = True  # If the script has at least 1 argument being passed to it, then set args to True
        try:
            if sys.argv[2] == "":
                pass
            args2 = True  # If the script has at least 2 arguments, then set args2 to True
        except IndexError:
            pass
    except IndexError:
        pass
    print(
        "\033[8;40;125t\033[3;250;60t"
    )  # Set the terminal size to 40x125, then put it in the middle of the screen
    subprocess.run("clear", shell=False)
    print(
        P
        + """\n      /$$$$$$                                 /$$               /$$       /$$                                    
     /$$__  $$                               | $$              | $$      | $$                                    
    | $$  \\__/  /$$$$$$$  /$$$$$$  /$$$$$$  /$$$$$$    /$$$$$$$| $$$$$$$ | $$        /$$$$$$  /$$$$$$$   /$$$$$$ 
    |  $$$$$$  /$$_____/ /$$__  $$|____  $$|_  $$_/   /$$_____/| $$__  $$| $$       |____  $$| $$__  $$ /$$__  $$
     \\____  $$| $$      | $$  \\__/ /$$$$$$$  | $$    | $$      | $$  \\ $$| $$        /$$$$$$$| $$  \\ $$| $$  \\ $$
     /$$  \\ $$| $$      | $$      /$$__  $$  | $$ /$$| $$      | $$  | $$| $$       /$$__  $$| $$  | $$| $$  | $$
    |  $$$$$$/|  $$$$$$$| $$     |  $$$$$$$  |  $$$$/|  $$$$$$$| $$  | $$| $$$$$$$$|  $$$$$$$| $$  | $$|  $$$$$$$
     \\______/  \\_______/|__/      \\_______/   \\___/   \\_______/|__/  |__/|________/ \\_______/|__/  |__/ \\____  $$
                                                                                                        /$$  \\ $$
                                                                                                       |  $$$$$$/
                                                                                                        \\______/ """
        + NC
    )  # logo
    print("")
    if not args or a1 == "nope":
        print(
            "Welcome to ScratchLang "
            + ver
            + ". (Name suggested by @MagicCrayon9342 on Scratch.)"
        )
        inputloop()
    else:
        inputloop(sys.argv[1])
    os.chdir("..")
    if os.path.isdir("projects"):
        os.chdir("projects")
        if len(os.listdir()) == 0:
            os.chdir("..")
            subprocess.run("rm -rf projects", shell=False)
            os.chdir("mainscripts")
    else:
        os.chdir("mainscripts")


def decomp():
    while True:
        dv2dt = "0"

        def dte(arg1):
            if dv2dt == "1":
                print(arg1)

        if os.path.isfile("var/devmode"):
            dv2dt = "1"
        print("")
        print(RED + "Decompiler Python Version 1.0" + NC)
        global dcd
        dcd = "Stage"
        if dv2dt == "1":
            print("")
            print(RED + "Todo list:" + NC)
            print("Higher Priorities go first.")
            print(
                "-------------------------------------------------------------------"
            )
            print(RED + "* " + NC + "Make custom blocks")
            print("")
            print("Order of items may change.")
            print(
                "-------------------------------------------------------------------"
            )
        print("")
        print(
            "Select the .sb3 you want to decompile. "
            + RED
            + "WARNING! THE NAME OF THE FILE CANNOT HAVE ANY SPACES OR IT WILL NOT UNZIP CORRECTLY!!!"
            + NC
        )
        print("")
        if not args2:
            time.sleep(2)
            filetypes = (("Scratch SB3", "*.sb3"), ("All files", "*.*"))
            sb3file = fd.askopenfilename(
                title="Choose a Scratch project",
                initialdir="/",
                filetypes=filetypes,
            )
            sb3file.replace("\\", "/")
        else:
            ppath = os.getcwd()
            sb3file = sys.argv[2].replace("\\", "/")
            if not os.path.isfile(sb3file):
                error("File doesn't exist.")
                exit()
            h = len(sb3file)
            while True:
                h -= 1
                chars = sb3file[h]
                if chars == "/":
                    break
            bounded = h
            h = -1
            direc = ""
            while True:
                h += 1
                if h == bounded:
                    break
                chars = sb3file[h]
                direc += chars
            os.chdir(direc)
            sb3pth = os.getcwd() + "/"
            h = bounded
            while True:
                h += 1
                try:
                    chars = sb3file[h]
                except IndexError:
                    break
                sb3pth += chars
            sb3file = sb3pth
            os.chdir(ppath)
        if sb3file == "":
            error("Empty path.")
            exit()
        name = input(
            "Name of project? "
            + RED
            + "Keep in mind that it cannot be empty or it will not be created."
            + NC
            + "\n"
        )
        print("")
        if name == "":
            error("Project name cannot be empty.")
            exit()
        os.chdir("..")
        if not os.path.isdir("projects"):
            createdir("projects")
        os.chdir("projects")
        if os.path.isdir(name):
            print("Project " + name + " already exists. Replace? [Y/N]")
            anss = getinput()
            if anss.lower() == "y":
                subprocess.run("rm -rf " + name, shell=False)
            else:
                exit()
            print("")
        print("Decompiling project...\n")
        time.sleep(1)
        createdir(name)
        os.chdir(name)
        with open(".maindir", "w") as f:
            f.write("Please don't remove this file.")
        print("Extracting .sb3...\n")
        print(sb3file)
        subprocess.run("unzip " + sb3file, shell=False)
        createdir("Stage")
        os.chdir("Stage")
        createdir("assets")
        os.chdir("..")
        file = open("project.json", "r")
        jsonfile = file.read()
        file.close()
        global i
        i = 55

        def extdata():
            b = "0"
            word = ""
            while True:
                ip()
                b = getchar('-"')
                if b:
                    break
                word += char
            return word

        def getchar(a1, a2=""):
            global b
            global char
            char = ""
            b = False
            if not "-" + a2 == "-++":
                char = jsonfile[i]
                if "-" + char == a1:
                    b = True
            elif not "-" + char == a1:
                char = jsonfile[i + 1]
                if "-" + char == a1:
                    b = True
                char = jsonfile[i]
            else:
                char = ""
            return b

        def ip(num=1):
            global i
            i = i + num

        def im(num=1):
            global i
            i = i - num

        def nq(num=1):
            for k in range(num):
                global b
                b = "0"
                while True:
                    ip()
                    b = getchar('-"')
                    if b:
                        break

        def start(a1=""):
            global nxt
            nq(2)
            ip(2)
            b = "0"
            b = getchar('-"')
            if not b:
                if "h" + a1 == "h":
                    nxt = "fin"
            else:
                b = "0"
                varname = ""
                while True:
                    ip()
                    b = getchar('-"')
                    if b:
                        break
                    varname += char
                if "h" + a1 == "h":
                    nxt = varname
                    dte("next: " + nxt + ", " + varname)
            nq(2)
            ip(2)
            b = "0"
            b = getchar('-"')
            if not b:
                if a1 == "":
                    writetofile(dcd + "/project.ss1", "\\nscript")
                    print("")
            else:
                b = "0"
                pname = ""
                while True:
                    ip()
                    b = getchar('-"')
                    if b:
                        break

                    pname += char
            dte(nxt)

        def addblock(a1, dcon=0):
            global i
            global nxt
            global con
            try:
                con += ""
            except NameError:
                con = ""
            cnext = ""
            start()
            if a1 == "looks_switchbackdropto":
                nq(5)
                word = extdata()
                i = jsonfile.find('"' + word + '":{"opcode":')
                nq(18)
                word = extdata()
                writetofile(
                    dcd + "/project.ss1", 'switch backdrop to ("' + word + '")'
                )
                print(
                    RED
                    + "Added block: "
                    + NC
                    + '"switch backdrop to ("'
                    + word
                    + '")"'
                )
            elif a1 == "looks_switchbackdroptoandwait":
                nq(5)
                word = extdata()
                i = jsonfile.find('"' + word + '":{"opcode":')
                nq(18)
                word = extdata()
                writetofile(
                    dcd + "/project.ss1",
                    'switch backdrop to ("' + word + '") and wait',
                )
                print(
                    RED
                    + "Added block: "
                    + NC
                    + '"switch backdrop to ("'
                    + word
                    + '") and wait"'
                )
            elif a1 == "looks_nextbackdrop":
                writetofile(dcd + "/project.ss1", "next backdrop")
                print(RED + "Added block: " + NC + '"next backdrop"')
            elif a1 == "looks_changeeffectby":
                nq(5)
                word = extdata()
                if not word == "fields":
                    amt = word
                    nq(2)
                else:
                    amt = ""
                nq(3)
                word = extdata()
                word = word.lower()
                writetofile(
                    dcd + "/project.ss1",
                    "change [" + word + '] effect by ("' + amt + '") # looks',
                )
                print(
                    RED
                    + "Added block: "
                    + NC
                    + '"change ['
                    + word
                    + '] effect by ("'
                    + amt
                    + '")"'
                )
            elif a1 == "looks_seteffectto":
                nq(5)
                word = extdata()
                if not word == "fields":
                    amt = word
                    nq(2)
                else:
                    amt = ""
                nq(3)
                word = extdata()
                word = word.lower()
                writetofile(
                    dcd + "/project.ss1",
                    "set [" + word + '] effect to ("' + amt + '") # looks',
                )
                print(
                    RED
                    + "Added block: "
                    + NC
                    + '"set ['
                    + word
                    + '] effect to ("'
                    + amt
                    + '")"'
                )
            elif a1 == "looks_graphiceffects":
                writetofile(dcd + "/project.ss1", "clear graphic effects")
                print(RED + "Added block: " + NC + '"clear graphic effects"')
            elif a1 == "looks_backdropnumbername":
                nq(7)
                word = extdata()
                con += "(backdrop [" + word + "])"
                if dcon == 1:
                    writetofile(dcd + "/project.ss1", con)
                    print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "sound_playuntildone":
                nq(5)
                word = extdata()
                i = jsonfile.find('"' + word + '":{"opcode":')
                nq(18)
                word = extdata()
                writetofile(
                    dcd + "/project.ss1",
                    'play sound ("' + word + '") until done',
                )
                print(
                    RED
                    + "Added block: "
                    + NC
                    + '"play sound ("'
                    + word
                    + '") until done"'
                )
            elif a1 == "sound_play":
                nq(5)
                word = extdata()
                i = jsonfile.find('"' + word + '":{"opcode":')
                nq(18)
                word = extdata()
                writetofile(
                    dcd + "/project.ss1", 'start sound ("' + word + '")'
                )
                print(
                    RED
                    + "Added block: "
                    + NC
                    + '"start sound ("'
                    + word
                    + '")"'
                )
            elif a1 == "sound_stopallsounds":
                writetofile(dcd + "/project.ss1", "stop all sounds")
                print(RED + "Added block: " + NC + '"stop all sounds"')
            elif a1 == "sound_changeeffectby":
                nq(5)
                word = extdata()
                if not word == "fields":
                    amt = word
                    nq(2)
                else:
                    amt = ""
                nq(3)
                word = extdata()
                word = word.lower()
                writetofile(
                    dcd + "/project.ss1",
                    "change [" + word + '] effect by ("' + amt + '") # sound',
                )
                print(
                    RED
                    + "Added block: "
                    + NC
                    + '"change ['
                    + word
                    + '] effect by ("'
                    + amt
                    + '")"'
                )
            elif a1 == "sound_seteffectto":
                nq(5)
                word = extdata()
                if not word == "fields":
                    amt = word
                    nq(2)
                else:
                    amt = ""
                nq(3)
                word = extdata()
                word = word.lower()
                writetofile(
                    dcd + "/project.ss1",
                    "set [" + word + '] effect to ("' + amt + '") # sound',
                )
                print(
                    RED
                    + "Added block: "
                    + NC
                    + '"set ['
                    + word
                    + '] effect to ("'
                    + amt
                    + '")"'
                )
            elif a1 == "sound_cleareffects":
                writetofile(dcd + "/project.ss1", "clear sound effects")
                print(RED + "Added block: " + NC + '"clear sound effects"')
            elif a1 == "sound_changevolumeby":
                nq(5)
                word = extdata()
                if word == "fields":
                    word = ""
                writetofile(
                    dcd + "/project.ss1", 'change volume by ("' + word + '")'
                )
                print(
                    RED
                    + "Added block: "
                    + NC
                    + '"change volume by ("'
                    + word
                    + '")"'
                )
            elif a1 == "sound_setvolumeto":
                nq(5)
                word = extdata()
                if word == "fields":
                    word = ""
                writetofile(
                    dcd + "/project.ss1", 'set volume to ("' + word + '") %'
                )
                print(
                    RED
                    + "Added block: "
                    + NC
                    + '"set volume to ("'
                    + word
                    + '") %"'
                )
            elif a1 == "sound_volume":
                con += "(volume)"
                if dcon == 1:
                    writetofile(dcd + "/project.ss1", con)
                    print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "event_whenflagclicked":
                writetofile(dcd + "/project.ss1", "when flag clicked")
                print(RED + "Added block: " + NC + '"when flag clicked"')
            elif a1 == "event_whenkeypressed":
                nq(7)
                word = extdata()
                writetofile(
                    dcd + "/project.ss1", "when [" + word + "] key pressed"
                )
                print(
                    RED
                    + "Added block: "
                    + NC
                    + '"when ['
                    + word
                    + '] key pressed"'
                )
            elif a1 == "event_whenstageclicked":
                writetofile(dcd + "/project.ss1", "when flag clicked")
                print(RED + "Added block: " + NC + '"when flag clicked"')
            elif a1 == "event_whenbackdropswitchesto":
                nq(7)
                word = extdata()
                writetofile(
                    dcd + "/project.ss1",
                    "when backdrop switches to [" + word + "]",
                )
                print(
                    RED
                    + "Added block: "
                    + NC
                    + '"when backdrop switches to ['
                    + word
                    + ']"'
                )
            elif a1 == "event_whengreaterthan":
                nq(5)
                word = extdata()
                if word == "fields":
                    word = ""
                else:
                    nq(2)
                amt = word
                nq(3)
                word = extdata()
                word = word.lower()
                writetofile(
                    dcd + "/project.ss1",
                    "when [" + word + '] > ("' + amt + '")',
                )
                print(
                    RED
                    + "Added block: "
                    + NC
                    + '"when ['
                    + word
                    + '] > ("'
                    + amt
                    + '")"'
                )
            elif a1 == "event_whenbroadcastreceived":
                nq(7)
                word = extdata()
                writetofile(
                    dcd + "/project.ss1", "when I receive [" + word + "]"
                )
                print(
                    RED
                    + "Added block: "
                    + NC
                    + '"when I receive ['
                    + word
                    + ']"'
                )
            elif a1 == "event_broadcast":
                nq(5)
                word = extdata()
                writetofile(dcd + "/project.ss1", "broadcast [" + word + "]")
                print(
                    RED + "Added block: " + NC + '"broadcast [' + word + ']"'
                )
            elif a1 == "event_broadcastandwait":
                nq(5)
                word = extdata()
                writetofile(
                    dcd + "/project.ss1", "broadcast [" + word + "] and wait"
                )
                print(
                    RED
                    + "Added block: "
                    + NC
                    + '"broadcast ['
                    + word
                    + '] and wait"'
                )
            elif a1 == "control_wait":
                nq(5)
                word = extdata()
                if word == "fields":
                    word = ""
                writetofile(
                    dcd + "/project.ss1", 'wait ("' + word + '") seconds'
                )
                print(
                    RED
                    + "Added block: "
                    + NC
                    + '"wait ("'
                    + word
                    + '") seconds"'
                )
            elif a1 == "control_repeat":
                cnext = nxt
                nq(5)
                word = extdata()
                if word == "SUBSTACK":
                    word = ""
                    writetofile(
                        dcd + "/project.ss1", 'repeat ("' + word + '") {'
                    )
                    print(
                        RED
                        + "Starting repeat |"
                        + NC
                        + ' repeat ("'
                        + word
                        + '") {'
                    )
                else:
                    nq()
                    writetofile(
                        dcd + "/project.ss1", "repeat (" + word + ") {"
                    )
                    print(
                        RED
                        + "Starting repeat |"
                        + NC
                        + ' repeat ("'
                        + word
                        + '") {'
                    )
                    word = extdata()
                if not word == "SUBSTACK":
                    writetofile(dcd + "/project.ss1", "}")
                    print("")
                    print(RED + "Ended repeat |" + NC + " }")
                else:
                    nq()
                    word = extdata()
                    if not word == "fields":
                        i = jsonfile.find('"' + word + '":{"opcode":')
                        nq(4)
                        word = extdata()
                        addblock(word)
                        writetofile(dcd + "/project.ss1", "}")
                        print(RED + "Ended repeat |" + NC + " }")
                    else:
                        writetofile(dcd + "/project.ss1", "}")
                        print(RED + "Ended repeat |" + NC + " }")
                    nxt = cnext
            elif a1 == "control_forever":
                cnext = nxt
                nq(3)
                word = extdata()
                if word == "SUBSTACK":
                    nq()
                    word = extdata()
                    if word == "fields":
                        word = ""
                else:
                    word = ""
                writetofile(dcd + "/project.ss1", "forever {")
                print(RED + "Starting forever |" + NC + " forever {")
                if not word == "":
                    i = jsonfile.find('"' + word + '":{"opcode":')
                    nq(4)
                    word = extdata()
                    addblock(word)
                    writetofile(dcd + "/project.ss1", "}")
                    print(RED + "Ended forever |" + NC + " }")
                else:
                    writetofile(dcd + "/project.ss1", "}")
                    print(RED + "Ended forever |" + NC + " }")
                nxt = cnext
            elif a1 == "control_if":
                con = ""
                cnext = nxt
                nq(2)
                j = i
                while True:
                    word = extdata()
                    if word == "CONDITION" or word == "fields":
                        break
                if word == "CONDITION":
                    k = i
                    b = "0"
                    while True:
                        ip()
                        b = getchar("-]")
                        if b:
                            break
                    im()
                    b = False
                    b = getchar('-"')
                    if b:
                        i = k
                        nq()
                        word = extdata()
                        i = jsonfile.find('"' + word + '":{"opcode":')
                        nq(4)
                        word = extdata()
                        addblock(word)
                        writetofile(dcd + "/project.ss1", "if " + con + " {")
                        print(RED + "Starting if |" + NC + " if " + con + " {")
                    else:
                        writetofile(dcd + "/project.ss1", "if <> {")
                        print(RED + "Starting if |" + NC + " if <> {")
                else:
                    writetofile(dcd + "/project.ss1", "if <> {")
                    print(RED + "Starting if |" + NC + " if <> {")
                i = j
                while True:
                    word = extdata()
                    if word == "SUBSTACK" or word == "fields":
                        break
                if word == "SUBSTACK":
                    k = i
                    b = "0"
                    while True:
                        ip()
                        b = getchar("-]")
                        if b:
                            break
                    im()
                    b = False
                    b = getchar('-"')
                    if b:
                        i = k
                        nq()
                        word = extdata()
                        i = jsonfile.find('"' + word + '":{"opcode":')
                        nq(4)
                        word = extdata()
                        addblock(word)
                    writetofile(dcd + "/project.ss1", "}")
                    print(RED + "Ended if |" + NC + " }")
                else:
                    writetofile(dcd + "/project.ss1", "}")
                    print(RED + "Ended if |" + NC + " }")
                nxt = cnext
            elif a1 == "control_if_else":
                con = ""
                cnext = nxt
                nq(2)
                j = i
                while True:
                    word = extdata()
                    if word == "CONDITION" or word == "fields":
                        break
                if word == "CONDITION":
                    k = i
                    b = "0"
                    while True:
                        ip()
                        b = getchar("-]")
                        if b:
                            break
                    im()
                    b = False
                    b = getchar('-"')
                    if b:
                        i = k
                        nq()
                        word = extdata()
                        i = jsonfile.find('"' + word + '":{"opcode":')
                        nq(4)
                        word = extdata()
                        addblock(word)
                        writetofile(dcd + "/project.ss1", "if " + con + " {")
                        print(
                            RED
                            + "Starting if/else |"
                            + NC
                            + " if "
                            + con
                            + " {"
                        )
                    else:
                        writetofile(dcd + "/project.ss1", "if <> {")
                        print(RED + "Starting if/else |" + NC + " if <> {")
                else:
                    writetofile(dcd + "/project.ss1", "if <> {")
                    print(RED + "Starting if/else |" + NC + " if <> {")
                i = j
                while True:
                    word = extdata()
                    if word == "SUBSTACK" or word == "fields":
                        break
                if word == "SUBSTACK":
                    k = i
                    b = "0"
                    while True:
                        ip()
                        b = getchar("-]")
                        if b:
                            break
                    im()
                    b = False
                    b = getchar('-"')
                    if b:
                        i = k
                        nq()
                        word = extdata()
                        i = jsonfile.find('"' + word + '":{"opcode":')
                        nq(4)
                        word = extdata()
                        addblock(word)
                    writetofile(dcd + "/project.ss1", "} else {")
                    print(RED + "else |" + NC + " } else {")
                else:
                    writetofile(dcd + "/project.ss1", "} else {")
                    print(RED + "else |" + NC + " } else {")
                i = j
                while True:
                    word = extdata()
                    if word == "SUBSTACK2" or word == "fields":
                        break
                if word == "SUBSTACK2":
                    k = i
                    b = "0"
                    while True:
                        ip()
                        b = getchar("-]")
                        if b:
                            break
                    im()
                    b = False
                    b = getchar('-"')
                    if b:
                        i = k
                        nq()
                        word = extdata()
                        i = jsonfile.find('"' + word + '":{"opcode":')
                        nq(4)
                        word = extdata()
                        addblock(word)
                    writetofile(dcd + "/project.ss1", "}")
                    print(RED + "Ended if/else |" + NC + " }")
                else:
                    writetofile(dcd + "/project.ss1", "}")
                    print(RED + "Ended if/else |" + NC + " }")
                nxt = cnext
            elif a1 == "control_wait_until":
                con = ""
                cnext = nxt
                nq(2)
                j = i
                while True:
                    word = extdata()
                    if word == "CONDITION" or word == "fields":
                        break
                if word == "CONDITION":
                    k = i
                    b = "0"
                    while True:
                        ip()
                        b = getchar("-]")
                        if b:
                            break
                    im()
                    b = False
                    b = getchar('-"')
                    if b:
                        i = k
                        nq()
                        word = extdata()
                        i = jsonfile.find('"' + word + '":{"opcode":')
                        nq(4)
                        word = extdata()
                        addblock(word)
                        writetofile(dcd + "/project.ss1", "wait until " + con)
                        print(
                            RED
                            + "Added block: "
                            + NC
                            + '"wait until '
                            + con
                            + '"'
                        )
                    else:
                        writetofile(dcd + "/project.ss1", "wait until <>")
                        print(RED + "Added block: " + NC + '"wait until <>')
                else:
                    writetofile(dcd + "/project.ss1", "wait until " + con)
                    print(
                        RED + "Added block: " + NC + '"wait until ' + con + '"'
                    )
                i = j
            elif a1 == "control_repeat_until":
                con = ""
                cnext = nxt
                nq(2)
                j = i
                while True:
                    word = extdata()
                    if word == "CONDITION" or word == "fields":
                        break
                if word == "CONDITION":
                    k = i
                    b = "0"
                    while True:
                        ip()
                        b = getchar("-]")
                        if b:
                            break
                    im()
                    b = False
                    b = getchar('-"')
                    if b:
                        i = k
                        nq()
                        word = extdata()
                        i = jsonfile.find('"' + word + '":{"opcode":')
                        nq(4)
                        word = extdata()
                        addblock(word)
                        writetofile(
                            dcd + "/project.ss1", "repeat until " + con + " {"
                        )
                        print(
                            RED
                            + "Starting repeat until |"
                            + NC
                            + " repeat until "
                            + con
                            + " {"
                        )
                    else:
                        writetofile(dcd + "/project.ss1", "repeat until <> {")
                        print(
                            RED
                            + "Starting repeat until |"
                            + NC
                            + " repeat until <> {"
                        )
                else:
                    writetofile(dcd + "/project.ss1", "repeat until <> {")
                    print(
                        RED
                        + "Starting repeat until |"
                        + NC
                        + " repeat until <> {"
                    )
                i = j
                while True:
                    word = extdata()
                    if word == "SUBSTACK" or word == "fields":
                        break
                if word == "SUBSTACK":
                    k = i
                    b = "0"
                    while True:
                        ip()
                        b = getchar("-]")
                        if b:
                            break
                    im()
                    b = False
                    b = getchar('-"')
                    if b:
                        i = k
                        nq()
                        word = extdata()
                        i = jsonfile.find('"' + word + '":{"opcode":')
                        nq(4)
                        word = extdata()
                        addblock(word)
                    writetofile(dcd + "/project.ss1", "}")
                    print(RED + "Ended repeat until |" + NC + " }")
                else:
                    writetofile(dcd + "/project.ss1", "}")
                    print(RED + "Ended repeat until |" + NC + " }")
                nxt = cnext
            elif a1 == "control_while":
                con = ""
                cnext = nxt
                nq(2)
                j = i
                while True:
                    word = extdata()
                    if word == "CONDITION" or word == "fields":
                        break
                if word == "CONDITION":
                    k = i
                    b = "0"
                    while True:
                        ip()
                        b = getchar("-]")
                        if b:
                            break
                    im()
                    b = False
                    b = getchar('-"')
                    if b:
                        i = k
                        nq()
                        word = extdata()
                        i = jsonfile.find('"' + word + '":{"opcode":')
                        nq(4)
                        word = extdata()
                        addblock(word)
                        writetofile(
                            dcd + "/project.ss1", "while " + con + " {"
                        )
                        print(
                            RED
                            + "Starting while |"
                            + NC
                            + " while "
                            + con
                            + " {"
                        )
                    else:
                        writetofile(dcd + "/project.ss1", "while <> {")
                        print(RED + "while |" + NC + " while <> {")
                else:
                    writetofile(dcd + "/project.ss1", "while <> {")
                    print(RED + "Starting while |" + NC + " while <> {")
                i = j
                while True:
                    word = extdata()
                    if word == "SUBSTACK" or word == "fields":
                        break
                if word == "SUBSTACK":
                    k = i
                    b = "0"
                    while True:
                        ip()
                        b = getchar("-]")
                        if b:
                            break
                    im()
                    b = False
                    b = getchar('-"')
                    if b:
                        i = k
                        nq()
                        word = extdata()
                        i = jsonfile.find('"' + word + '":{"opcode":')
                        nq(4)
                        word = extdata()
                        addblock(word)
                    writetofile(dcd + "/project.ss1", "}")
                    print(RED + "Ended while |" + NC + " }")
                else:
                    writetofile(dcd + "/project.ss1", "}")
                    print(RED + "Ended while |" + NC + " }")
                nxt = cnext
            elif a1 == "control_create_clone_of":
                nq(5)
                word = extdata()
                i = jsonfile.find('"' + word + '":{"opcode":')
                nq(18)
                word = extdata()
                writetofile(
                    dcd + "/project.ss1", 'create a clone of ("' + word + '")'
                )
                print(
                    RED
                    + "Added block: "
                    + NC
                    + '"create a clone of ("'
                    + word
                    + '")"'
                )
            elif a1 == "sensing_askandwait":
                nq(5)
                word = extdata()
                writetofile(
                    dcd + "/project.ss1", 'ask ("' + word + '") and wait'
                )
                print(
                    RED
                    + "Added block: "
                    + NC
                    + '"ask ("'
                    + word
                    + '") and wait"'
                )
            elif a1 == "sensing_answer":
                con += "(anwser)"
                if dcon == 1:
                    writetofile(dcd + "/project.ss1", con)
                    print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "sensing_keypressed":
                nq(5)
                word = extdata()
                i = jsonfile.find('"' + word + '":{"opcode":')
                nq(18)
                word = extdata()
                con += '<key ("' + word + '") pressed?>'
                if dcon == 1:
                    writetofile(dcd + "/project.ss1", con)
                    print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "sensing_mousedown":
                con += "<mouse down?>"
                if dcon == 1:
                    writetofile(dcd + "/project.ss1", con)
                    print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "sensing_mousex":
                con += "(mouse x)"
                if dcon == 1:
                    writetofile(dcd + "/project.ss1", con)
                    print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "sensing_mousey":
                con += "(mouse y)"
                if dcon == 1:
                    writetofile(dcd + "/project.ss1", con)
                    print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "sensing_loudness":
                con += "(loudness)"
                if dcon == 1:
                    writetofile(dcd + "/project.ss1", con)
                    print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "sensing_timer":
                con += "(timer)"
                if dcon == 1:
                    writetofile(dcd + "/project.ss1", con)
                    print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "sensing_resettimer":
                writetofile(dcd + "/project.ss1", "reset timer")
                print(RED + "Added block: " + NC + '"reset timer"')
            elif a1 == "sensing_of":
                nq(2)
                j = i
                while True:
                    word = extdata()
                    if word == "PROPERTY" or word == "shadow":
                        break
                if word == "PROPERTY":
                    nq()
                    word = extdata()
                    sofprop = word
                else:
                    sofprop = ""
                i = j
                while True:
                    word = extdata()
                    if word == "OBJECT" or word == "shadow":
                        break
                if word == "OBJECT":
                    nq()
                    word = extdata()
                    i = jsonfile.find('"' + word + '":{"opcode":')
                    nq(18)
                    word = extdata()
                    if word == "_stage_":
                        word = "Stage"
                else:
                    word = ""
                con += "([" + sofprop + '] of ("' + word + '"))'
                if dcon == 1:
                    writetofile(dcd + "/project.ss1", con)
                    print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "sensing_current":
                nq(7)
                word = extdata()
                word = word.lower()
                con += "(current [" + word + "])"
                if dcon == 1:
                    writetofile(dcd + "/project.ss1", con)
                    print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "sensing_dayssince2000":
                con += "(days since 2000)"
                if dcon == 1:
                    writetofile(dcd + "/project.ss1", con)
                    print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "sensing_username":
                con += "(username)"
                if dcon == 1:
                    writetofile(dcd + "/project.ss1", con)
                    print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "operator_add":
                nq(2)
                j = i
                while True:
                    word = extdata()
                    if word == "NUM1" or word == "fields":
                        break
                if word == "NUM1":
                    nq()
                    op1 = extdata()
                else:
                    op1 = ""
                i = j
                while True:
                    word = extdata()
                    if word == "NUM2" or word == "fields":
                        break
                if word == "NUM2":
                    nq()
                    op2 = extdata()
                else:
                    op2 = ""
                con += '(("' + op1 + '") + ("' + op2 + '"))'
                if dcon == 1:
                    writetofile(dcd + "/project.ss1", con)
                    print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "operator_subtract":
                nq(2)
                j = i
                while True:
                    word = extdata()
                    if word == "NUM1" or word == "fields":
                        break
                if word == "NUM1":
                    nq()
                    op1 = extdata()
                else:
                    op1 = ""
                i = j
                while True:
                    word = extdata()
                    if word == "NUM2" or word == "fields":
                        break
                if word == "NUM2":
                    nq()
                    op2 = extdata()
                else:
                    op2 = ""
                con += '(("' + op1 + '") - ("' + op2 + '"))'
                if dcon == 1:
                    writetofile(dcd + "/project.ss1", con)
                    print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "operator_multiply":
                nq(2)
                j = i
                while True:
                    word = extdata()
                    if word == "NUM1" or word == "fields":
                        break
                if word == "NUM1":
                    nq()
                    op1 = extdata()
                else:
                    op1 = ""
                i = j
                while True:
                    word = extdata()
                    if word == "NUM2" or word == "fields":
                        break
                if word == "NUM2":
                    nq()
                    op2 = extdata()
                else:
                    op2 = ""
                con += '(("' + op1 + '") * ("' + op2 + '"))'
                if dcon == 1:
                    writetofile(dcd + "/project.ss1", con)
                    print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "operator_divide":
                nq(2)
                j = i
                while True:
                    word = extdata()
                    if word == "NUM1" or word == "fields":
                        break
                if word == "NUM1":
                    nq()
                    op1 = extdata()
                else:
                    op1 = ""
                i = j
                while True:
                    word = extdata()
                    if word == "NUM2" or word == "fields":
                        break
                if word == "NUM2":
                    nq()
                    op2 = extdata()
                else:
                    op2 = ""
                con += '(("' + op1 + '") / ("' + op2 + '"))'
                if dcon == 1:
                    writetofile(dcd + "/project.ss1", con)
                    print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "operator_random":
                nq(2)
                j = i
                while True:
                    word = extdata()
                    if word == "FROM" or word == "fields":
                        break
                if word == "FROM":
                    nq()
                    op1 = extdata()
                else:
                    op1 = ""
                i = j
                while True:
                    word = extdata()
                    if word == "TO" or word == "fields":
                        break
                if word == "TO":
                    nq()
                    op2 = extdata()
                else:
                    op2 = ""
                con += '(pick random ("' + op1 + '") to ("' + op2 + '"))'
                if dcon == 1:
                    writetofile(dcd + "/project.ss1", con)
                    print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "operator_equals":
                nq(2)
                j = i
                while True:
                    word = extdata()
                    if word == "OPERAND1" or word == "fields":
                        break
                if word == "OPERAND1":
                    k = i
                    b = "0"
                    while True:
                        ip()
                        b = getchar("-,")
                        if b:
                            break
                    ip()
                    b = "0"
                    b = getchar('-"')
                    if b:
                        word = extdata()
                        i = jsonfile.find('"' + word + '":{"opcode":')
                        nq(4)
                        word = extdata()
                        con += "<"
                        addblock(word)
                        con += " = "
                    else:
                        b = "0"
                        while True:
                            ip()
                            b = getchar("-]")
                            if b:
                                break
                        im()
                        b = False
                        b = getchar('-"')
                        if b:
                            i = k
                            nq()
                            op1 = extdata()
                        else:
                            op1 = ""
                        con += '<("' + op1 + '") = ("'
                else:
                    op1 = ""
                i = j
                while True:
                    word = extdata()
                    if word == "OPERAND2" or word == "fields":
                        break
                if word == "OPERAND2":
                    k = i
                    b = "0"
                    while True:
                        ip()
                        b = getchar("-,")
                        if b:
                            break
                    ip()
                    b = "0"
                    b = getchar('-"')
                    if b:
                        word = extdata()
                        i = jsonfile.find('"' + word + '":{"opcode":')
                        nq(4)
                        word = extdata()
                        addblock(word)
                        con += ">"
                    else:
                        b = "0"
                        while True:
                            ip()
                            b = getchar("-]")
                            if b:
                                break
                        im()
                        b = False
                        b = getchar('-"')
                        if b:
                            i = k
                            nq()
                            op2 = extdata()
                        else:
                            op2 = ""
                        con += op2 + '")>'
                else:
                    op2 = ""
                    con += op2 + '")>'
                if dcon == 1:
                    writetofile(dcd + "/project.ss1", con)
                    print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "operator_gt":
                nq(2)
                j = i
                while True:
                    word = extdata()
                    if word == "OPERAND1" or word == "fields":
                        break
                if word == "OPERAND1":
                    k = i
                    b = "0"
                    while True:
                        ip()
                        b = getchar("-,")
                        if b:
                            break
                    ip()
                    b = "0"
                    b = getchar('-"')
                    if b:
                        word = extdata()
                        i = jsonfile.find('"' + word + '":{"opcode":')
                        nq(4)
                        word = extdata()
                        con += "<"
                        addblock(word)
                        con += " > "
                    else:
                        b = "0"
                        while True:
                            ip()
                            b = getchar("-]")
                            if b:
                                break
                        im()
                        b = False
                        b = getchar('-"')
                        if b:
                            i = k
                            nq()
                            op1 = extdata()
                        else:
                            op1 = ""
                        con += '<("' + op1 + '") > ("'
                else:
                    op1 = ""
                i = j
                while True:
                    word = extdata()
                    if word == "OPERAND2" or word == "fields":
                        break
                if word == "OPERAND2":
                    k = i
                    b = "0"
                    while True:
                        ip()
                        b = getchar("-,")
                        if b:
                            break
                    ip()
                    b = "0"
                    b = getchar('-"')
                    if b:
                        word = extdata()
                        i = jsonfile.find('"' + word + '":{"opcode":')
                        nq(4)
                        word = extdata()
                        addblock(word)
                        con += ">"
                    else:
                        b = "0"
                        while True:
                            ip()
                            b = getchar("-]")
                            if b:
                                break
                        im()
                        b = False
                        b = getchar('-"')
                        if b:
                            i = k
                            nq()
                            op2 = extdata()
                        else:
                            op2 = ""
                        con += op2 + '")>'
                else:
                    op2 = ""
                    con += op2 + '")>'
                if dcon == 1:
                    writetofile(dcd + "/project.ss1", con)
                    print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "operator_lt":
                nq(2)
                j = i
                while True:
                    word = extdata()
                    if word == "OPERAND1" or word == "fields":
                        break
                if word == "OPERAND1":
                    k = i
                    b = "0"
                    while True:
                        ip()
                        b = getchar("-,")
                        if b:
                            break
                    ip()
                    b = "0"
                    b = getchar('-"')
                    if b:
                        word = extdata()
                        i = jsonfile.find('"' + word + '":{"opcode":')
                        nq(4)
                        word = extdata()
                        con += "<"
                        addblock(word)
                        con += " <"
                    else:
                        b = "0"
                        while True:
                            ip()
                            b = getchar("-]")
                            if b:
                                break
                        im()
                        b = False
                        b = getchar('-"')
                        if b:
                            i = k
                            nq()
                            op1 = extdata()
                        else:
                            op1 = ""
                        con += '<("' + op1 + '") < ("'
                else:
                    op1 = ""
                i = j
                while True:
                    word = extdata()
                    if word == "OPERAND2" or word == "fields":
                        break
                if word == "OPERAND2":
                    k = i
                    b = "0"
                    while True:
                        ip()
                        b = getchar("-,")
                        if b:
                            break
                    ip()
                    b = "0"
                    b = getchar('-"')
                    if b:
                        word = extdata()
                        i = jsonfile.find('"' + word + '":{"opcode":')
                        nq(4)
                        word = extdata()
                        addblock(word)
                        con += ">"
                    else:
                        b = "0"
                        while True:
                            ip()
                            b = getchar("-]")
                            if b:
                                break
                        im()
                        b = False
                        b = getchar('-"')
                        if b:
                            i = k
                            nq()
                            op2 = extdata()
                        else:
                            op2 = ""
                        con += op2 + '")>'
                else:
                    op2 = ""
                    con += op2 + '")>'
                if dcon == 1:
                    writetofile(dcd + "/project.ss1", con)
                    print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "operator_and":
                nq(2)
                j = i
                while True:
                    word = extdata()
                    if word == "OPERAND1" or word == "fields":
                        break
                if word == "OPERAND1":
                    nq()
                    word = extdata()
                    if not word == "fields" and not word == "OPERAND2":
                        i = jsonfile.find('"' + word + '":{"opcode":')
                        con += "<"
                        nq(4)
                        word = extdata()
                        addblock(word)
                        con += " and "
                    else:
                        con += "<<> and "
                else:
                    con += "<<> and "
                i = j
                while True:
                    word = extdata()
                    if word == "OPERAND2" or word == "fields":
                        break
                if word == "OPERAND2":
                    nq()
                    word = extdata()
                    if not word == "fields" and not word == "OPERAND1":
                        i = jsonfile.find('"' + word + '":{"opcode":')
                        nq(4)
                        word = extdata()
                        addblock(word)
                        con += ">"
                    else:
                        con += "<>>"
                else:
                    con += "<>>"
                if dcon == 1:
                    writetofile(dcd + "/project.ss1", con)
                    print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "operator_or":
                nq(2)
                j = i
                while True:
                    word = extdata()
                    if word == "OPERAND1" or word == "fields":
                        break
                if word == "OPERAND1":
                    nq()
                    word = extdata()
                    if not word == "fields" and not word == "OPERAND2":
                        i = jsonfile.find('"' + word + '":{"opcode":')
                        con += "<"
                        nq(4)
                        word = extdata()
                        addblock(word)
                        con += " or "
                    else:
                        con += "<<> or "
                else:
                    con += "<<> or "
                i = j
                while True:
                    word = extdata()
                    if word == "OPERAND2" or word == "fields":
                        break
                if word == "OPERAND2":
                    nq()
                    word = extdata()
                    if not word == "fields" and not word == "OPERAND1":
                        i = jsonfile.find('"' + word + '":{"opcode":')
                        nq(4)
                        word = extdata()
                        addblock(word)
                        con += ">"
                    else:
                        con += "<>>"
                else:
                    con += "<>>"
                if dcon == 1:
                    writetofile(dcd + "/project.ss1", con)
                    print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "operator_not":
                nq(2)
                j = i
                while True:
                    word = extdata()
                    if word == "OPERAND" or word == "fields":
                        break
                if word == "OPERAND":
                    nq()
                    word = extdata()
                    if not word == "fields":
                        i = jsonfile.find('"' + word + '":{"opcode":')
                        con += "<not "
                        nq(4)
                        word = extdata()
                        addblock(word)
                        con += ">"
                    else:
                        con += "<not <>>"
                else:
                    con += "<not <>>"
                if dcon == 1:
                    writetofile(dcd + "/project.ss1", con)
                    print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "operator_join":
                nq(2)
                j = i
                while True:
                    word = extdata()
                    if word == "STRING1":
                        break
                b = "0"
                k = i
                while True:
                    ip()
                    b = getchar("-,")
                    if b:
                        break
                ip()
                b = "0"
                b = getchar('-"')
                if b:
                    word = extdata()
                    i = jsonfile.find('"' + word + '":{"opcode":')
                    con += "(join "
                    nq(4)
                    word = extdata()
                    addblock(word)
                else:
                    i = k
                    nq()
                    word = extdata()
                    con += '(join ("' + word + '")'
                i = j
                while True:
                    word = extdata()
                    if word == "STRING2":
                        break
                b = "0"
                k = i
                while True:
                    ip()
                    b = getchar("-,")
                    if b:
                        break
                ip()
                b = "0"
                b = getchar('-"')
                if b:
                    word = extdata()
                    i = jsonfile.find('"' + word + '":{"opcode":')
                    nq(4)
                    word = extdata()
                    addblock(word)
                    con += ")"
                else:
                    i = k
                    nq()
                    word = extdata()
                    con += '("' + word + '"))'
                if dcon == 1:
                    writetofile(dcd + "/project.ss1", con)
                    print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "operator_letter_of":
                nq(2)
                j = i
                while True:
                    word = extdata()
                    if word == "LETTER":
                        break
                b = "0"
                k = i
                while True:
                    ip()
                    b = getchar("-,")
                    if b:
                        break
                ip()
                b = "0"
                b = getchar('-"')
                if b:
                    word = extdata()
                    i = jsonfile.find('"' + word + '":{"opcode":')
                    con += "(letter "
                    nq(4)
                    word = extdata()
                    addblock(word)
                    con += " of "
                else:
                    i = k
                    nq()
                    word = extdata()
                    con += '(letter ("' + word + '") of '
                i = j
                while True:
                    word = extdata()
                    if word == "STRING":
                        break
                b = "0"
                k = i
                while True:
                    ip()
                    b = getchar("-,")
                    if b:
                        break
                ip()
                b = "0"
                b = getchar('-"')
                if b:
                    word = extdata()
                    i = jsonfile.find('"' + word + '":{"opcode":')
                    nq(4)
                    word = extdata()
                    addblock(word)
                    con += ")"
                else:
                    i = k
                    nq()
                    word = extdata()
                    con += '("' + word + '"))'
                if dcon == 1:
                    writetofile(dcd + "/project.ss1", con)
                    print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "operator_length":
                nq(2)
                j = i
                while True:
                    word = extdata()
                    if word == "STRING":
                        break
                b = "0"
                k = i
                while True:
                    ip()
                    b = getchar("-,")
                    if b:
                        break
                ip()
                b = "0"
                b = getchar('-"')
                if b:
                    word = extdata()
                    i = jsonfile.find('"' + word + '":{"opcode":')
                    con += "(length of "
                    nq(4)
                    word = extdata()
                    addblock(word)
                    con += ")"
                else:
                    i = k
                    nq()
                    word = extdata()
                    con += '(length of ("' + word + '"))'
                if dcon == 1:
                    writetofile(dcd + "/project.ss1", con)
                    print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "operator_contains":
                nq(2)
                j = i
                while True:
                    word = extdata()
                    if word == "STRING1":
                        break
                b = "0"
                k = i
                while True:
                    ip()
                    b = getchar("-,")
                    if b:
                        break
                ip()
                b = "0"
                b = getchar('-"')
                if b:
                    word = extdata()
                    i = jsonfile.find('"' + word + '":{"opcode":')
                    con += "<"
                    nq(4)
                    word = extdata()
                    addblock(word)
                    con += " contains "
                else:
                    i = k
                    nq()
                    word = extdata()
                    con += '<("' + word + '") contains '
                i = j
                while True:
                    word = extdata()
                    if word == "STRING2":
                        break
                b = "0"
                k = i
                while True:
                    ip()
                    b = getchar("-,")
                    if b:
                        break
                ip()
                b = "0"
                b = getchar('-"')
                if b:
                    word = extdata()
                    i = jsonfile.find('"' + word + '":{"opcode":')
                    nq(4)
                    word = extdata()
                    addblock(word)
                    con += "?>"
                else:
                    i = k
                    nq()
                    word = extdata()
                    con += '("' + word + '")?>'
                if dcon == 1:
                    writetofile(dcd + "/project.ss1", con)
                    print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "operator_mod":
                nq(2)
                j = i
                while True:
                    word = extdata()
                    if word == "NUM1":
                        break
                b = "0"
                k = i
                while True:
                    ip()
                    b = getchar("-,")
                    if b:
                        break
                ip()
                b = "0"
                b = getchar('-"')
                if b:
                    word = extdata()
                    i = jsonfile.find('"' + word + '":{"opcode":')
                    con += "("
                    nq(4)
                    word = extdata()
                    addblock(word)
                    con += " mod "
                else:
                    i = k
                    nq()
                    word = extdata()
                    con += '(("' + word + '") mod '
                i = j
                while True:
                    word = extdata()
                    if word == "NUM2":
                        break
                b = "0"
                k = i
                while True:
                    ip()
                    b = getchar("-,")
                    if b:
                        break
                ip()
                b = "0"
                b = getchar('-"')
                if b:
                    word = extdata()
                    i = jsonfile.find('"' + word + '":{"opcode":')
                    nq(4)
                    word = extdata()
                    addblock(word)
                    con += ")"
                else:
                    i = k
                    nq()
                    word = extdata()
                    con += '("' + word + '"))'
                if dcon == 1:
                    writetofile(dcd + "/project.ss1", con)
                    print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "operator_round":
                nq(2)
                j = i
                while True:
                    word = extdata()
                    if word == "NUM":
                        break
                b = "0"
                k = i
                while True:
                    ip()
                    b = getchar("-,")
                    if b:
                        break
                ip()
                b = "0"
                b = getchar('-"')
                if b:
                    word = extdata()
                    i = jsonfile.find('"' + word + '":{"opcode":')
                    con += "(round "
                    nq(4)
                    word = extdata()
                    addblock(word)
                    con += ")"
                else:
                    i = k
                    nq()
                    word = extdata()
                    con += '(round ("' + word + '"))'
                if dcon == 1:
                    writetofile(dcd + "/project.ss1", con)
                    print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "operator_mathop":
                nq(2)
                j = i
                while True:
                    word = extdata()
                    if word == "OPERATOR":
                        break
                nq()
                word = extdata()
                con += "([" + word + "] of "
                i = j
                while True:
                    word = extdata()
                    if word == "NUM":
                        break
                b = "0"
                k = i
                while True:
                    ip()
                    b = getchar("-,")
                    if b:
                        break
                ip()
                b = "0"
                b = getchar('-"')
                if b:
                    word = extdata()
                    i = jsonfile.find('"' + word + '":{"opcode":')
                    nq(4)
                    word = extdata()
                    addblock(word)
                    con += ")"
                else:
                    i = k
                    nq()
                    word = extdata()
                    con += '("' + word + '"))'
                if dcon == 1:
                    writetofile(dcd + "/project.ss1", con)
                    print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "data_setvariableto":
                con = ""
                nq(2)
                j = i
                while True:
                    word = extdata()
                    if word == "VARIABLE":
                        break
                nq()
                word = extdata()
                con += "set [" + word + "] to "
                i = j
                while True:
                    word = extdata()
                    if word == "VALUE":
                        break
                b = "0"
                k = i
                while True:
                    ip()
                    b = getchar("-,")
                    if b:
                        break
                ip()
                b = "0"
                b = getchar('-"')
                if b:
                    word = extdata()
                    i = jsonfile.find('"' + word + '":{"opcode":')
                    nq(4)
                    word = extdata()
                    addblock(word)
                else:
                    i = k
                    nq()
                    word = extdata()
                    con += '("' + word + '")'
                writetofile(dcd + "/project.ss1", con)
                print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "data_changevariableby":
                con = ""
                nq(2)
                j = i
                while True:
                    word = extdata()
                    if word == "VARIABLE":
                        break
                nq()
                word = extdata()
                con += "change [" + word + "] by "
                i = j
                while True:
                    word = extdata()
                    if word == "VALUE":
                        break
                b = "0"
                k = i
                while True:
                    ip()
                    b = getchar("-,")
                    if b:
                        break
                ip()
                b = "0"
                b = getchar('-"')
                if b:
                    word = extdata()
                    i = jsonfile.find('"' + word + '":{"opcode":')
                    nq(4)
                    word = extdata()
                    addblock(word)
                else:
                    i = k
                    nq()
                    word = extdata()
                    con += '("' + word + '")'
                writetofile(dcd + "/project.ss1", con)
                print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "data_showvariable":
                nq(7)
                word = extdata()
                writetofile(
                    dcd + "/project.ss1", "show variable [" + word + "]"
                )
                print(
                    RED
                    + "Added block: "
                    + NC
                    + '"'
                    + "show variable ["
                    + word
                    + "]"
                    + '"'
                )
            elif a1 == "data_hidevariable":
                nq(7)
                word = extdata()
                writetofile(
                    dcd + "/project.ss1", "hide variable [" + word + "]"
                )
                print(
                    RED
                    + "Added block: "
                    + NC
                    + '"'
                    + "hide variable ["
                    + word
                    + "]"
                    + '"'
                )
            elif a1 == "data_addtolist":
                con = ""
                nq(2)
                j = i
                while True:
                    word = extdata()
                    if word == "ITEM":
                        break
                b = "0"
                k = i
                while True:
                    ip()
                    b = getchar("-,")
                    if b:
                        break
                ip()
                b = "0"
                b = getchar('-"')
                if b:
                    word = extdata()
                    i = jsonfile.find('"' + word + '":{"opcode":')
                    con += "add "
                    nq(4)
                    word = extdata()
                    addblock(word)
                    con += " to "
                else:
                    i = k
                    nq()
                    word = extdata()
                    con += 'add ("' + word + '") to '
                i = j
                while True:
                    word = extdata()
                    if word == "LIST":
                        break
                nq()
                word = extdata()
                con += "[" + word + "]"
                writetofile(dcd + "/project.ss1", con)
                print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "data_deleteoflist":
                con = ""
                nq(2)
                j = i
                while True:
                    word = extdata()
                    if word == "INDEX":
                        break
                b = "0"
                k = i
                while True:
                    ip()
                    b = getchar("-,")
                    if b:
                        break
                ip()
                b = "0"
                b = getchar('-"')
                if b:
                    word = extdata()
                    i = jsonfile.find('"' + word + '":{"opcode":')
                    con += "delete "
                    nq(4)
                    word = extdata()
                    addblock(word)
                    con += " of "
                else:
                    i = k
                    nq()
                    word = extdata()
                    con += 'delete ("' + word + '") of '
                i = j
                while True:
                    word = extdata()
                    if word == "LIST":
                        break
                nq()
                word = extdata()
                con += "[" + word + "]"
                writetofile(dcd + "/project.ss1", con)
                print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "data_deletealloflist":
                nq(7)
                word = extdata()
                writetofile(
                    dcd + "/project.ss1", "delete all of [" + word + "]"
                )
                print(
                    RED
                    + "Added block: "
                    + NC
                    + '"delete all of ['
                    + word
                    + ']"'
                )
            elif a1 == "data_insertatlist":
                con = ""
                nq(2)
                j = i
                while True:
                    word = extdata()
                    if word == "ITEM":
                        break
                b = "0"
                k = i
                while True:
                    ip()
                    b = getchar("-,")
                    if b:
                        break
                ip()
                b = "0"
                b = getchar('-"')
                if b:
                    word = extdata()
                    i = jsonfile.find('"' + word + '":{"opcode":')
                    con += "insert "
                    nq(4)
                    word = extdata()
                    addblock(word)
                    con += " at "
                else:
                    i = k
                    nq()
                    word = extdata()
                    con += 'insert ("' + word + '") at '
                i = j
                while True:
                    word = extdata()
                    if word == "INDEX":
                        break
                b = "0"
                k = i
                while True:
                    ip()
                    b = getchar("-,")
                    if b:
                        break
                ip()
                b = "0"
                b = getchar('-"')
                if b:
                    word = extdata()
                    i = jsonfile.find('"' + word + '":{"opcode":')
                    nq(4)
                    word = extdata()
                    addblock(word)
                    con += " of "
                else:
                    i = k
                    nq()
                    word = extdata()
                    con += ' ("' + word + '") of '
                i = j
                while True:
                    word = extdata()
                    if word == "LIST":
                        break
                nq()
                word = extdata()
                con += "[" + word + "]"
                writetofile(dcd + "/project.ss1", con)
                print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "data_replaceitemoflist":
                con = ""
                nq(2)
                j = i
                while True:
                    word = extdata()
                    if word == "INDEX":
                        break
                b = "0"
                k = i
                while True:
                    ip()
                    b = getchar("-,")
                    if b:
                        break
                ip()
                b = "0"
                b = getchar('-"')
                if b:
                    word = extdata()
                    i = jsonfile.find('"' + word + '":{"opcode":')
                    con += "replace item "
                    nq(4)
                    word = extdata()
                    addblock(word)
                    con += " of "
                else:
                    i = k
                    nq()
                    word = extdata()
                    con += 'replace item ("' + word + '") of '
                i = j
                while True:
                    word = extdata()
                    if word == "LIST":
                        break
                nq()
                word = extdata()
                con += "[" + word + "] with "
                i = j
                while True:
                    word = extdata()
                    if word == "ITEM":
                        break
                b = "0"
                k = i
                while True:
                    ip()
                    b = getchar("-,")
                    if b:
                        break
                ip()
                b = "0"
                b = getchar('-"')
                if b:
                    word = extdata()
                    i = jsonfile.find('"' + word + '":{"opcode":')
                    nq(4)
                    word = extdata()
                    addblock(word)
                    con += " of "
                else:
                    i = k
                    nq()
                    word = extdata()
                    con += '("' + word + '")'
                writetofile(dcd + "/project.ss1", con)
                print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "data_itemoflist":
                con = ""
                nq(2)
                j = i
                while True:
                    word = extdata()
                    if word == "INDEX":
                        break
                b = "0"
                k = i
                while True:
                    ip()
                    b = getchar("-,")
                    if b:
                        break
                ip()
                b = "0"
                b = getchar('-"')
                if b:
                    word = extdata()
                    i = jsonfile.find('"' + word + '":{"opcode":')
                    con += "(item "
                    nq(4)
                    word = extdata()
                    addblock(word)
                    con += " of "
                else:
                    i = k
                    nq()
                    word = extdata()
                    con += '(item ("' + word + '") of '
                i = j
                while True:
                    word = extdata()
                    if word == "LIST":
                        break
                nq()
                word = extdata()
                con += "[" + word + "])"
                writetofile(dcd + "/project.ss1", con)
                print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "data_itemnumoflist":
                con = ""
                nq(2)
                j = i
                while True:
                    word = extdata()
                    if word == "ITEM":
                        break
                b = "0"
                k = i
                while True:
                    ip()
                    b = getchar("-,")
                    if b:
                        break
                ip()
                b = "0"
                b = getchar('-"')
                if b:
                    word = extdata()
                    i = jsonfile.find('"' + word + '":{"opcode":')
                    con += "(item # of "
                    nq(4)
                    word = extdata()
                    addblock(word)
                    con += " in "
                else:
                    i = k
                    nq()
                    word = extdata()
                    con += '(item # of ("' + word + '") in '
                i = j
                while True:
                    word = extdata()
                    if word == "LIST":
                        break
                nq()
                word = extdata()
                con += "[" + word + "])"
                writetofile(dcd + "/project.ss1", con)
                print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "data_lengthoflist":
                con = ""
                nq(2)
                while True:
                    word = extdata()
                    if word == "LIST":
                        break
                nq()
                word = extdata()
                con += "(length of [" + word + "])"
                writetofile(dcd + "/project.ss1", con)
                print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "data_listcontainsitem":
                con = ""
                nq(2)
                j = i
                while True:
                    word = extdata()
                    if word == "LIST":
                        break
                nq()
                word = extdata()
                con += "<[" + word + "] contains "
                i = j
                while True:
                    word = extdata()
                    if word == "ITEM":
                        break
                b = "0"
                k = i
                while True:
                    ip()
                    b = getchar("-,")
                    if b:
                        break
                ip()
                b = "0"
                b = getchar('-"')
                if b:
                    word = extdata()
                    i = jsonfile.find('"' + word + '":{"opcode":')
                    nq(4)
                    word = extdata()
                    addblock(word)
                    con += "?>"
                else:
                    i = k
                    nq()
                    word = extdata()
                    con += '("' + word + '")?>'
                writetofile(dcd + "/project.ss1", con)
                print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "data_showlist":
                con = ""
                nq(2)
                while True:
                    word = extdata()
                    if word == "LIST":
                        break
                nq()
                word = extdata()
                con += "show list [" + word + "]"
                writetofile(dcd + "/project.ss1", con)
                print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "data_hidelist":
                con = ""
                nq(2)
                while True:
                    word = extdata()
                    if word == "LIST":
                        break
                nq()
                word = extdata()
                con += "hide list [" + word + "]"
                writetofile(dcd + "/project.ss1", con)
                print(RED + "Added block: " + NC + '"' + con + '"')
            elif a1 == "procedures_definition":
                nq(5)
                word = extdata()
                i = jsonfile.find('"' + word + '":{"opcode":')
                print(
                    RED
                    + "What the hell are custom blocks? They're going to be so hard to program into the decompiler..."
                    + NC
                )
                print(RED + 'Unknown block: "' + a1 + '" Skipping.' + NC)
                writetofile(
                    dcd + "/project.ss1",
                    'DECOMPERR: Unknown block:  "' + "a1" + '"',
                )
            else:
                print(RED + 'Unknown block: "' + a1 + '" Skipping.' + NC)
                writetofile(
                    dcd + "/project.ss1",
                    'DECOMPERR: Unknown block:  "' + a1 + '"',
                )
            if not nxt == "fin":
                i = jsonfile.find('"' + nxt + '":{"opcode":')
                nq(4)
                word = extdata()
                addblock(word, 1)

        print("Defining variables...\n")
        while True:
            nq()
            ip()
            nq()
            b = False
            novars = "0"
            while True:
                ip()
                b = getchar("-[")
                if b:
                    break
                b = getchar("-}")
                if b:
                    novars = "1"
                    break
            if novars == "0":
                ip()
                b = "0"
                varname = ""
                while True:
                    ip()
                    b = getchar('-"', "++")
                    varname += char
                    if b:
                        break
                ip(2)
                b = "0"
                varvalue = ""
                while True:
                    ip()
                    b = getchar("-]", "++")
                    varvalue += char
                    if b:
                        break
                if not os.path.isfile("Stage/project.ss1"):
                    writetofile(
                        "Stage/project.ss1",
                        "#There should be no empty lines.\nss1\n\\prep",
                    )
                writetofile(
                    "Stage/project.ss1", "var: " + varname + "=" + varvalue
                )
                print(RED + "Added variable: " + NC + '"' + varname + '".')
                print(RED + "Value: " + NC + varvalue)
                print("")
                b = "0"
                varname = ""
                ip(2)
                b = getchar("-}")
                if b:
                    break
                im(2)
            if novars == "1":
                writetofile(
                    "Stage/project.ss1",
                    "#There should be no empty lines.\nss1\n\\prep",
                )
                break
        print("Building lists...")
        print("")
        ip(9)
        while True:
            ip(2)
            b = "0"
            b = getchar("-}")
            if b:
                novars = "1"
                im(2)
            else:
                im(2)
                nq()
                ip()
                nq()
                b = "0"
                novars = "0"
                while True:
                    ip()
                    b = getchar("-[")
                    if b:
                        break
                    b = getchar("-}")
                    if b:
                        novars = "1"
                        break
            if novars == "0":
                ip()
                b = "0"
                listname = ""
                while True:
                    ip()
                    b = getchar('-"', "++")
                    listname += char
                    if b:
                        break
                ip(4)
                b = "0"
                b = getchar("-]")
                if not b:
                    if char == '"':
                        b = False
                        while True:
                            b = False
                            varname = ""
                            while True:
                                ip()
                                b = getchar('-"')
                                if b:
                                    break
                                varname += char
                            ip()
                            b = False
                            b = getchar("-]")
                            if not b:
                                writetofile("st", varname + ",")
                                ip()
                            else:
                                writetofile("st", varname)
                                break
                    else:
                        im()
                        b = "0"
                        while True:
                            b = "0"
                            varname = ""
                            while True:
                                ip()
                                b = getchar("-,")
                                if b:
                                    break
                                b = getchar("-]")
                                if b:
                                    break
                                varname += char
                            b = "0"
                            b = getchar("-]")
                            if not b:
                                writetofile("st", varname + ",")
                            else:
                                writetofile("st", varname)
                                break
                    f = open("st", "r")
                    list = ""
                    for k in f:
                        list += f.readline().replace("\n", "")
                    f.close()
                    writetofile(
                        "Stage/project.ss1", "list: " + listname + "=" + list
                    )
                    print(RED + "Added list: " + NC + '"' + listname + '".')
                    print(RED + "Contents: " + NC + list)
                    print("")
                else:
                    writetofile(
                        "Stage/project.ss1", "list: " + listname + "=,"
                    )
                    print(RED + "Added list: " + NC + '"' + listname + '".')
                    print(RED + "Contents: " + NC + "Nothing.")
                    print("")
                    if novars == "1":
                        break
            if novars == "1":
                break
            ip(2)
            b = "0"
            b = getchar("-}")
            if b:
                break
        print("Loading broadcasts...")
        print("")
        while True:
            b = "0"
            word = ""
            while True:
                ip()
                b = getchar('-"')
                if b:
                    break
                word += char
            if word == "broadcasts":
                break
        b = "0"
        novars = "0"
        ip(3)
        b = "0"
        b = getchar("-}")
        if b:
            novars = "1"
            im(2)
        else:
            im(2)
            while True:
                ip()
                b = getchar('-"')
                if b:
                    break
                b = getchar("-}")
                if b:
                    novars = "1"
                    break
            nq()
        if novars == "0":
            while True:
                ip()
                nq()
                b = "0"
                varname = ""
                while True:
                    ip()
                    b = getchar('-"')
                    if b:
                        break
                    varname += char
                writetofile("Stage/project.ss1", "broadcast: " + varname)
                print(RED + "Loaded broadcast: " + NC + '"' + varname + '"')
                print("")
                ip()
                b = "0"
                b = getchar("-}")
                if b:
                    break
                ip(2)
                nq()
        global rep
        rep = 0
        print("Making blocks...")
        print("")
        dcd = "Stage"
        k = -1
        done = "0"
        global con
        while True:
            i = k
            while True:
                word = extdata()
                if word == "parent":
                    k = i
                    ip(2)
                    b = "0"
                    b = getchar('-"')
                    if not b:
                        break
                if word == "comments":
                    done = "1"
                    break
            if done == "0":
                b = "0"
                while True:
                    im()
                    b = getchar("-{")
                    if b:
                        break
                ip()
                nq(2)
                word = extdata()
                con = ""
                addblock(word, 1)
            if done == "1":
                break
        print("\nAdding assets...")
        while True:
            word = extdata()
            if word == "costumes":
                break
        while True:
            nq(15)
            asset_file = extdata()
            try:
                shutil.move("./" + asset_file, "Stage/assets/" + asset_file)
                print(asset_file + " >> Stage/assets/" + asset_file)
            except FileNotFoundError:
                pass
            nq(4)
            b = "0"
            while True:
                ip()
                b = getchar("-}")
                if b:
                    break
            ip()
            b = "0"
            b = getchar("-]")
            if b:
                break
            nq(2)
        print("\nFormatting code to make it easier to read (Please wait)...")
        print("")
        f = open(dcd + "/project.ss1", "r")
        spaces = ""
        i = 0
        q = 0
        flen = len(f.readlines())
        f.close()
        f = open(dcd + "/project.ss1", "r")
        proglen = 55
        for line in f.readlines():
            q = q + 1
            per = q / flen
            print(
                "\033[A["
                + round(proglen * per) * "#"
                + (proglen - round(proglen * per)) * " "
                + "] "
                + str(round(per * 100))
                + "%"
            )
            line = line.strip("\n")
            if "}" in line and "{" in line:
                i -= 1
                spaces = i * "  "
                i += 1
            elif "{" in line:
                spaces = i * "  "
                i += 1
            elif "}" in line:
                i -= 1
                spaces = i * "  "
            else:
                spaces = i * "  "
            writetofile(dcd + "/a.txt", spaces + line)
        f.close()
        os.remove(dcd + "/project.ss1")
        os.rename(dcd + "/a.txt", dcd + "/project.ss1")
        os.chdir("..")
        dir = os.getcwd().replace("\\", "/")
        print("")
        print(
            RED + "Your project can be found in " + dir + "/" + name + "." + NC
        )
        break
    exit()


def inputloop(ia1: str = ""):
    inp = ""
    if not ia1 == "":
        ia1 = ia1.replace("-", "")
        a1 = int(ia1)
    else:
        a1 = ""
    print("")
    if a1 == "":
        print("1. Create a project.")
        print("2. Remove a project.")
        print("3. Compile a project.")
        print("4. Decompile a .sb3 file.")
        print("5. Export project.")
        print("6. Import project.")
        print(
            "7. Are options 3 and 4 not working? Input 7 to install dependencies."
        )
        print("8. Create scratchlang command.")
        print("9. Remove scratchlang command.")
        if not os.path.isfile("var/devmode"):
            print("A. Enable Developer Mode.")
            print("B. Exit.")
        else:
            print("A. Disable Developer Mode.")
            print("B. Delete all variables.")
            print("C. Prepare for commit and push.")
            print("D. Change decompiler script.")
            print("E. Exit.")
        inp = getinput()
    else:
        if a1 > 0 and a1 < 7:
            inp = str(a1)
        else:
            error(ia1 + " is not an argument.")
            time.sleep(2)
            startpy("nope")
    if inp == "1":
        pdir = os.getcwd()
        print("")
        name = input(
            "Name your project. Keep in mind that it cannot be empty or it will not be created properly.\n"
        )
        os.chdir("..")
        if name == "":
            error("Project name empty.")
            exit()
        elif os.path.isdir("projects/" + name):
            print("Project " + name + " already exists. Replace? [Y/N]")
            yessor = getinput()
            if yessor.lower() == "y":
                subprocess.run("rm -rf projects/" + name, shell=False)
            elif yessor.lower() == "n":
                exit()
            else:
                error(yessor + " is not an input.")
                exit()
        print(
            "You named your project "
            + name
            + ". If you want to rename it, use the File Explorer."
        )
        if not os.path.isdir("projects"):
            os.mkdir("projects")
        os.chdir("projects")
        os.mkdir(name)
        os.chdir(name)
        writetofile(".maindir", "Please don't remove this file.")
        os.mkdir("Stage")
        os.chdir("Stage")
        os.mkdir("assets")
        os.chdir("../../..")
        subprocess.run(
            "cp resources/cd21514d0531fdffb22204e0ec5ed84a.svg projects/"
            + name
            + "/Stage/assets",
            shell=False,
        )
        os.chdir("projects/" + name + "/Stage")
        writetofile("project.ss1", "# There should be no empty lines")
        writetofile("project.ss1", "ss1")
        os.chdir("..")
        os.mkdir("Sprite1")
        os.chdir("Sprite1")
        writetofile("project.ss1", "# There should be no empty lines.")
        writetofile("project.ss1", "ss1")
        os.mkdir("assets")
        os.chdir("../../..")
        subprocess.run(
            "cp resources/341ff8639e74404142c11ad52929b021.svg projects/"
            + name
            + "/Sprite1/assets",
            shell=False,
        )
        subprocess.run(
            "cp resources/c9466893cdbdda41de3ec986256e5a47.svg projects/"
            + name
            + "/Sprite1/assets",
            shell=False,
        )
        os.chdir("mainscripts")
        sys.argv = ["editor.py", "../projects/" + name]
        runpy.run_path("editor.py")
        exit()
    elif inp == "2":
        os.chdir("..")
        if not os.path.isdir("projects"):
            error("there are no projects to delete.")
            exit()
        os.chdir("projects")
        print("")
        subprocess.run("ls -1", shell=False)
        print("")
        pgrd = input(
            "Choose a project to get rid of, or input nothing to cancel.\n"
        )
        if not pgrd == "":
            if os.path.isdir(pgrd):
                subprocess.run("rm -rf " + pgrd)
            else:
                error("directory " + pgrd + " does not exist.")
        exit()
    elif inp == "3":
        comp()
        exit()
    elif inp == "4":
        if os.path.isfile("var/ds"):
            f = open("var/ds", "r")
            line = f.readline().strip()
            f.close()
            if line == "py":
                decomp()
            else:
                subprocess.run("chmod 755 " + line)
                subprocess.run("bash " + line)
        else:
            subprocess.run("chmod 755 decompiler.v2.ss1.sh")
            subprocess.run("bash decompiler.v2.ss1.sh")
        exit()
    elif inp == "5":
        os.chdir("..")
        if not os.path.isdir("projects"):
            error("there are no projects to export.")
            exit()
        os.chdir("projects")
        print("")
        subprocess.run("ls -1", shell=False)
        print("")
        pgrd = input(
            "Choose a project to export, or input nothing to cancel.\n"
        )
        if not pgrd == "":
            if os.path.isdir(pgrd):
                subprocess.run("tar -cf " + pgrd + ".ssa " + pgrd)
                os.chdir("..")
                subprocess.run("cp projects/" + pgrd + ".ssa exports")
                os.remove("projects/" + pgrd + ".ssa")
                print(
                    "Your project "
                    + pgrd
                    + ".ssa can be found in the exports folder."
                )
            else:
                error("directory " + pgrd + " does not exist.")
        os.chdir("mainscripts")
        exit()
    elif inp == "6":
        filetypes = (("ScratchScript Archive", "*.ssa"), ("All files", "*.*"))
        ssi = fd.askopenfilename(
            title="Choose a ScratchScript Archive",
            initialdir="/",
            filetypes=filetypes,
        )
        ssi.replace("\\", "/")
        os.chdir("..")
        if not os.path.isdir("projects"):
            os.mkdir("projects")
        os.chdir("projects")
        subprocess.run("tar -xf " + ssi, shell=False)
        print("Remove .ssa file? [Y/N]")
        f = getinput()
        if f.lower() == "y":
            subprocess.run("rm " + ssi, shell=False)
        exit()
    elif inp == "7":
        print("This only works for MSYS2/MINGW. Continue? [Y/N]")
        con = getinput()
        if con.lower() == "y":
            print("")
            subprocess.run("pacman -S --noconfirm unzip git bc", shell=False)
            startpy("nope")
        exit()
    elif inp == "8":
        pdir = os.getcwd().replace("\\", "/")
        if not os.path.isfile("var/alias"):
            subprocess.run("chmod 755 shcommand.sh", shell=False)
            subprocess.run(
                "bash -c './shcommand.sh 1 " + pdir + "'", shell=False
            )
            writetofile(
                "var/alias",
                "This file tells the program that the command is already created. Please don't touch this.",
            )
        else:
            print("scratchlang command has already been created.")
        exit()
    elif inp == "9":
        while True:
            print("")
            if not os.path.isfile("var/alias"):
                error(
                    "scratchlang command has not been created or var/alias file has been deleted."
                )
                exit()
            print(
                RED
                + "WARNING:"
                + NC
                + " This will remove the scratchlang command.\nContinue? [Y/N]"
            )
            inp2 = getinput()
            print("")
            if inp2.lower() == "y":
                subprocess.run(
                    "bash -c './shcommand.sh 1 HHHHFFFFFFSDFSHDFSKDFGDSILGFSDIIMPOSSIBLEPATHOTESFEE'",
                    shell=False,
                )
                os.remove("var/alias")
                break
            elif inp2.lower() == "n":
                print("")
                break
            else:
                error(inp2 + " is not an option.")
        exit()
    elif inp.lower() == "a":
        if not os.path.isfile("var/devmode"):
            writetofile(
                "var/devmode",
                "This is a devmode file. You can manually remove it to disable dev mode if you don't want to use the "
                "program to disable it for some reason.",
            )
        else:
            os.remove("var/devmode")
        startpy("nope")
        exit()
    elif inp.lower() == "b":
        if not os.path.isfile("var/devmode"):
            exit()
        else:
            varlists = [
                "var/devmode",
                "var/zenity",
                "var/ds",
                "var/asked",
                "var/vc",
                "var/pe",
            ]
            for remove in varlists:
                os.remove(remove)
            writetofile("var/ds", "py")
            if os.path.isfile("var/alias"):
                print("Get rid of the scratchlang command? [Y/N]")
                yn = getinput()
                if yn.lower() == "y":
                    while True:
                        print("")
                        if not os.path.isfile("var/alias"):
                            error(
                                "scratchlang command has not been created or var/alias file has been deleted."
                            )
                            exit()
                        print(
                            RED
                            + "WARNING:"
                            + NC
                            + " This will remove the scratchlang command.\nContinue? [Y/N]"
                        )
                        inp2 = getinput()
                        print("")
                        if inp2.lower() == "y":
                            subprocess.run(
                                "bash -c './shcommand.sh 1 HHHHFFFFFFSDFSHDFSKDFGDSILGFSDIIMPOSSIBLEPATHOTESFEE'",
                                shell=False,
                            )
                            os.remove("var/alias")
                            break
                        elif inp2.lower() == "n":
                            print("")
                            break
                        else:
                            error(inp2 + " is not an option.")
                elif yn.lower() == "n":
                    if os.path.isfile("var/alias"):
                        os.remove("var/alias")
                else:
                    error(yn + " is not an input.")
                    print(
                        "If you want to remove the command now, get rid of the command in your /usr/bin directory."
                    )
                    exit()
        exit()
    if os.path.isfile("var/devmode"):
        if inp.lower() == "c":
            varlists = [
                "var/devmode",
                "var/zenity",
                "var/ds",
                "var/asked",
                "var/vc",
                "var/pe",
            ]
            for remove in varlists:
                if os.path.isfile(remove):
                    os.remove(remove)
            writetofile("var/ds", "py")
            os.chdir("..")
            if os.path.isdir("projects"):
                subprocess.run("rm -rf projects", shell=False)
                subprocess.run("rm -rf exports")
                os.mkdir("exports")
                writetofile("exports/.temp", "")
                os.chdir("mainscripts")
            if os.path.isfile("var/alias"):
                print("Get rid of the scratchlang command? [Y/N]")
                yn = getinput()
                if yn.lower() == "y":
                    while True:
                        print("")
                        if not os.path.isfile("var/alias"):
                            error(
                                "scratchlang command has not been created or var/alias file has been deleted."
                            )
                            exit()
                        print(
                            RED
                            + "WARNING:"
                            + NC
                            + " This will remove the scratchlang command.\nContinue? [Y/N]"
                        )
                        inp2 = getinput()
                        print("")
                        if inp2.lower() == "y":
                            subprocess.run(
                                "bash -c 'shcommand.sh 1 HHHHFFFFFFSDFSHDFSKDFGDSILGFSDIIMPOSSIBLEPATHOTESFEE'",
                                shell=False,
                            )
                            os.remove("var/alias")
                            break
                        elif inp2.lower() == "n":
                            print("")
                            break
                        else:
                            error(inp2 + " is not an option.")
                elif yn.lower() == "n":
                    if os.path.isfile("var/alias"):
                        os.remove("var/alias")
                else:
                    error(yn + " is not an input.")
                    print(
                        "If you want to remove the command now, get rid of the command in your /usr/bin directory."
                    )
                    exit()
        elif inp.lower() == "d":
            print("")
            print("1. Pick one of the included decompilers.")
            print("2. Choose your own decompiler.")
            print("3. Reset to default. (decompilerpy.v1.ss1.py)")
            inf = getinput()
            corr = "0"
            if inf == "1":
                corr = "1"
                print("")
                print(
                    "1. decompiler.v1.ss1.sh - First version of the decompiler. No longer being programmed. "
                    "ScratchScript1 language. "
                )
                print("")
                print(
                    "2. decompiler.v2.ss1.sh - Most up-to-date version of the decompiler. ScratchScript1 language."
                )
                print("")
                print(
                    "3. decompilerpy.v1.ss1.py - Decompiler V2 remade in Python for speed and more capabilities. "
                    "ScratchScript 1 language. "
                )
                nfi = getinput()
                corr = "0"
                if nfi == "1":
                    corr = "1"
                    if os.path.isfile("var/ds"):
                        os.remove("var/ds")
                    writetofile("var/ds", "decompiler.v1.ss1.sh")
                elif nfi == "2":
                    corr = "1"
                    if os.path.isfile("var/ds"):
                        os.remove("var/ds")
                elif nfi == "3":
                    corr = "1"
                    if os.path.isfile("var/ds"):
                        os.remove("var/ds")
                    writetofile("var/ds", "py")
                if corr == "0":
                    error(nfi + " is not an input.")
            elif inf == "2":
                corr = "1"
                if os.path.isfile("var/ds"):
                    os.remove("var/ds")
                decom = fd.askopenfilename(
                    title="Choose a Custom Decompiler", initialdir="."
                )
                writetofile("var/ds", decom.replace("\\", "/"))
            elif inf == "3":
                corr = "1"
                if os.path.isfile("var/ds"):
                    os.remove("var/ds")
                writetofile("var/ds", "py")
            if corr == "0":
                error(inf + " is not an input.")
        elif inp.lower() == "e":
            exit()
        else:
            error(inp + " is not an input.")
            inputloop()
    else:
        error(inp + " is not an input.")
        inputloop()


def comp():
    print("")
    print(RED + "Compiler 1.0" + NC)
    print("")
    print("Remember, the compiler doesn't work yet.")
    print("")
    print("Select your project folder.")
    print("")
    time.sleep(2)
    fold = fd.askdirectory(title="Choose a project.", initialdir="../projects")
    fold = fold.replace("\\", "/")
    print(fold)


startpy()
