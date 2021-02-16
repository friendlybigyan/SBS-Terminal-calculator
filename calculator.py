import sys
import os
import math
import re
from decimal import *
from requisites import *
# easeof acces
asc_colors = {
    'default': '\u001b[m',
    'black': '\u001b[30m',
    'red': '\u001b[31m',
    'green': '\u001b[32m',
    'yellow': '\u001b[33m',
    'cyan': '\u001b[34m',
    'magenta': '\u001b[35m',
    'cyan': '\u001b[36m',
    'white': '\u001b[37m',
}
logo = f'''{asc_colors['cyan']}
 ▄██████▄           █ █         {asc_colors['white']}           ██          ███                    {asc_colors['cyan']}
████  ████          █ █         {asc_colors['white']}           ██          ███                    {asc_colors['cyan']}
█ █    ███          █ █         {asc_colors['white']}          ██           ██                     {asc_colors['cyan']}
█ █         ████▄▄  ███  ▄▄████▄{asc_colors['white']}  ██   ██ ██   ████▄▄   █ ███ ▄▄██▄▄  ███▄███ {asc_colors['cyan']}
██             ▀█ ▄ ██  ▄ █▀▀   {asc_colors['white']} ███   ██ ███     ▀█ ▄  ██   ▄██▀▀██▄ ███▀▀   {asc_colors['cyan']}
███    ███ ▄▄█ ██ █ ██  █ █     {asc_colors['white']} ██    ██ ███ ▄▄████ █  ███  █ █    █ ███     {asc_colors['cyan']}
████  ███  ███  ███ ███ ▀██▄▄   {asc_colors['white']} ▀██▄  ██  ██ ███  ███ ▀██▄▄ ▀██▄▄██▀ ██      {asc_colors['cyan']}
 ▀████ █▀  ▀▀████ █  ██  ▀▀████▀{asc_colors['white']}  ▀▀████    █ ▀▀█████   ▀▀███ ▀▀██▀▀  ██      {asc_colors['cyan']}

{asc_colors['yellow']}▄▄▄▀▄▄▄▄▀█▄▄██▄▄▄▄▄▄▄▄▄▄▄█▄▄▄█▄▄▄█▀███▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▀▀▀█▄▄▄█▄▄▀█▄▄▄▄▄▄▄▀█▄
{asc_colors['yellow']}▀▀█▄▄██▄▄███████▄▄▄██▄▄▀▀▄▄▄██████▄▄▄▄████▄▄███▀▀▀▀██████▄▄▄███████▄▄█████▀▀▀
'''
set_of_signs = ("+", "-", "*", "/", "^", "!")
os.system('cls' if os.name == 'nt' else 'clear')
# global definitions of variables
executable = True
continuable = False
prev = ""
print(logo + f'''                     

{asc_colors['green']}Enter h for help.
{asc_colors['cyan']}(Steps enabled){asc_colors['white']}
\n''')
steps = True
prev_ans = None
cardin = -1
brackets = [["(", ")"], ["{", "}"], ["[", "]"], ["|", "|"]]
# >-> >-> >-> >-> >-> >-> >-> >-> >-> >-> >-> >-> >-> >-> >-> >-> >-> >->
while executable:
    # try:
    continue_index = 0
    if not continuable:
        user_input = input(f'''{asc_colors['red']}:{asc_colors['white']}> ''')
        is_users_input = True
        prev_input = []

    signs_unavailable = 0
    br_1 = 0
    br_2 = 0

    # features
    if user_input == "":
        continue
    if user_input.lower() == "r":
        os.execl(sys.executable, sys.executable, *sys.argv)
    if user_input.lower() == "cls" or user_input == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo+f'''                                                        
{asc_colors['green']}Enter h for help.{asc_colors['cyan']} (Steps enabled){asc_colors['white']}
\n                                                                    ''')
        continue
    if user_input.lower() == "s":
        if steps:
            steps = False
            print(
                f'''{asc_colors['red']}Steps disabled{asc_colors['white']}''')
        else:
            steps = True
            print(f"{asc_colors['green']}Steps enabled{asc_colors['white']}")
        continue
    if user_input.lower() == "h":
        print(f'''
{asc_colors['magenta']}Enter:
{asc_colors['red']}h{asc_colors['cyan']} - to open this help dialoge
{asc_colors['red']}x{asc_colors['cyan']} - to exit
{asc_colors['red']}r{asc_colors['cyan']} - to restart
{asc_colors['red']}s{asc_colors['cyan']} - toggle the availability of steps
{asc_colors['red']}c{asc_colors['cyan']} - to toggle cardinality
{asc_colors['red']}cls/clear{asc_colors['cyan']} - to clear the screen
{asc_colors['red']}q{asc_colors['cyan']} - to solve quadratic equations

{asc_colors['magenta']}
M a i n  F e a t u r e s :
{asc_colors['white']}
    Quadratic equations' solutions can be performed by entering "q" in the input.
    Absolute values are {asc_colors['green']} added{asc_colors['white']}. Use "|" symbol.
        |-> {asc_colors['green']}use {asc_colors['red']}|{asc_colors['magenta']}x{asc_colors['red']}|{asc_colors['green']} to denote the absolute value of {asc_colors['cyan']}x{asc_colors['white']}
    Complex numbers are {asc_colors['green']} compatible{asc_colors['white']}.
        |-> {asc_colors['green']}use {asc_colors['magenta']}x{asc_colors['red']}i{asc_colors['green']} to denote the imaginary number{asc_colors['white']}

    Addition: {asc_colors['cyan']}+{asc_colors['white']}     Subtraction: {asc_colors['cyan']}-{asc_colors['white']}
    Multiplication: {asc_colors['cyan']}*{asc_colors['white']}   Division: {asc_colors['cyan']}/{asc_colors['white']}
    Exponential: ^

    Factorial solution vls: {asc_colors['cyan']}(integer)!{asc_colors['white']}
    Infinity: {asc_colors['cyan']}infinity or ∞{asc_colors['white']}
    Indeterminant: {asc_colors['cyan']}indeterminant or (0/0)){asc_colors['white']}
    Constants: {asc_colors['yellow']}pi, e, c, g{asc_colors['white']}
    {asc_colors['cyan']}For obtaining the previous answer, use {asc_colors['white']}"{asc_colors['red']}..{asc_colors['white']}"
    {asc_colors['red']} |-> {asc_colors['cyan']}If the previous answer is a combination of answers, {asc_colors['white']}"{asc_colors['red']}..{asc_colors['white']}"{asc_colors['cyan']} gives the first answer, {asc_colors['white']}"{asc_colors['red']}...{asc_colors['white']}"{asc_colors['cyan']} gives the second one and so on.

    {asc_colors['cyan']}
    Trigonometry:
    {asc_colors['green']}
        {asc_colors['white']}Sine {asc_colors['red']}=>{asc_colors['green']} sin{asc_colors['magenta']}x{asc_colors['green']} {asc_colors['white']}or {asc_colors['green']}sin({asc_colors['magenta']}x{asc_colors['green']})
        {asc_colors['white']}Cosine {asc_colors['red']}=>{asc_colors['green']} cos{asc_colors['magenta']}x{asc_colors['green']} {asc_colors['white']}or {asc_colors['green']}cos({asc_colors['magenta']}x{asc_colors['green']})
        {asc_colors['white']}Tangent {asc_colors['red']}=>{asc_colors['green']} tan{asc_colors['magenta']}x{asc_colors['green']} {asc_colors['white']}or {asc_colors['green']}tan({asc_colors['magenta']}x{asc_colors['green']})
        {asc_colors['white']}Cosecant {asc_colors['red']}=>{asc_colors['green']} cosec{asc_colors['magenta']}x{asc_colors['green']} {asc_colors['white']}or {asc_colors['green']}cosec({asc_colors['magenta']}x{asc_colors['green']})
        {asc_colors['white']}Secant {asc_colors['red']}=>{asc_colors['green']} sec{asc_colors['magenta']}x{asc_colors['green']} {asc_colors['white']}or {asc_colors['green']}sec({asc_colors['magenta']}x{asc_colors['green']})
        {asc_colors['white']}Cotangent {asc_colors['red']}=>{asc_colors['green']} cot{asc_colors['magenta']}x{asc_colors['green']} {asc_colors['white']}or {asc_colors['green']}cot({asc_colors['magenta']}x{asc_colors['green']})
{asc_colors['yellow']}
A C C E S S I B I L I T Y  F E A T U R E S :
{asc_colors['cyan']}
    Brackets Autocomplete:
{asc_colors['green']}
    {asc_colors['red']}*{asc_colors['white']} {asc_colors['yellow']}All{asc_colors['white']} combinations of  brackets get autocompleted.{asc_colors['white']}
    {asc_colors['red']}*{asc_colors['white']} Brackets priority: {asc_colors['magenta']}Small brackets (paranthesis){asc_colors['green']} > {asc_colors['red']}Curly brackets{asc_colors['green']} > {asc_colors['yellow']}Square Brackets{asc_colors['green']}
{asc_colors['cyan']}
    Multi-statement solution:
{asc_colors['white']}
    Multiple statements can be solved by separating each statements with ':'
    {asc_colors['red']}For example:{asc_colors['white']} 5/2{asc_colors['red']}:{asc_colors['white']}3+2{asc_colors['green']} that simplifies to:{asc_colors['white']} 2.5{asc_colors['red']}:{asc_colors['white']}5 {asc_colors['white']}
{asc_colors['cyan']}
    Small details:
{asc_colors['cyan']}
    ~ {asc_colors['white']}12g{asc_colors['yellow']} = {asc_colors['white']}12{asc_colors['red']}*{asc_colors['white']}g{asc_colors['yellow']}, so {asc_colors['white']}12e/12{asc_colors['yellow']} = {asc_colors['white']}12{asc_colors['red']}*{asc_colors['white']}e/12{asc_colors['yellow']}, ie {asc_colors['white']}e/12{asc_colors['yellow']} will be done first. If you want {asc_colors['white']}12{asc_colors['red']}*{asc_colors['white']}e{asc_colors['yellow']} to be done first, try {asc_colors['white']}(12e)/12{asc_colors['yellow']} = {asc_colors['white']}(12{asc_colors['red']}*{asc_colors['white']}e)/12{asc_colors['yellow']}
    ~ {asc_colors['white']}12(5){asc_colors['yellow']} = {asc_colors['white']}12{asc_colors['red']}*{asc_colors['white']}5{asc_colors['yellow']}
    ~ {asc_colors['white']}(12-5)(5-12){asc_colors['yellow']} = {asc_colors['white']}(12-5){asc_colors['red']}*{asc_colors['white']}(5-12){asc_colors['yellow']}

{asc_colors['magenta']}
Example: {asc_colors['white']}pi*20^-1+(5*2)/12-28
{asc_colors['cyan']}
If you encounter any bugs, contact me at "friendlybigyan@gmail.com".{asc_colors['white']}

''')

        continue
    if user_input.lower() == "x":
        print(f"{asc_colors['cyan']}Exiting..")
        print(f"{asc_colors['cyan']}Exited{asc_colors['white']}")
        break
    if user_input.lower() == "q":
        print(
            f"{asc_colors['cyan']}a {asc_colors['red']}x² {asc_colors['cyan']}+ {asc_colors['cyan']}b {asc_colors['red']}x {asc_colors['cyan']}+ {asc_colors['cyan']}c{asc_colors['white']}")
        a = input(
            f"{asc_colors['cyan']}(a) {asc_colors['cyan']}Coeficient of {asc_colors['red']}x²:{asc_colors['white']} ")
        b = input(
            f"{asc_colors['cyan']}(b) {asc_colors['cyan']}Coeficient of {asc_colors['red']}x:{asc_colors['white']} ")
        c = input(
            f"{asc_colors['cyan']}(c) {asc_colors['cyan']}Constant:{asc_colors['white']} ")

        user_input = f"(-{b}+({b}^2-4*{a}*{c})^(1/2))/(2*{a}):(-{b}-({b}^2-4*{a}*{c})^(1/2))/(2*{a})"
    if user_input.lower() == "c":
        cardin *= -1
        if cardin < 0:
            print(
                f"{asc_colors['yellow']}Cardinality {asc_colors['red']}Disabled.{asc_colors['white']}")
        else:
            print(
                f"{asc_colors['yellow']}Cardinality {asc_colors['green']}Enabled{asc_colors['white']}")
        continue

    def float_toInt(num):
        # remove the trailing zeroes and convert it into a number
        if float(num) == int(float(num)):
            num = int(float(num))
        else:
            num = float(num)
        return num

    def has_exp(entry):
        if re.search(r"\de(-)?\d", entry):
            return True
        return False

    def makePrecise(entry):
        testVal = entry.replace(":", " ")
        for sign in set_of_signs:
            testVal = testVal.replace(f" {sign} ", " ")
            for bracket in brackets:
                for i in [0, 1]:
                    testVal = testVal.replace(bracket[i], " ")
        newArray = []
        testArray = testVal.split(" ")
        for n, num in enumerate(testArray):
            if testArray[n] != "" and ("j" in testArray[n] or "i" in testArray[n]):
                # make a clone of tesetArray
                testArray[n] = testArray[n].replace("j", "").replace(
                    "i", "").replace("e", "")
                tempArrayVal = []
                tempArrayVal.extend(testArray)
                # get rid of signs
                for sign in set_of_signs:
                    tempArrayVal[n] = tempArrayVal[n].replace(f"{sign}", " ")
                if tempArrayVal[n] != testArray[n]:
                    newArray.extend(tempArrayVal[n].split(" "))
        if newArray == []:
            return entry
        # print(newArray)
        for n, num in enumerate(newArray):
            if num != "" and (float(num)*(10 ** 10)) > 0.0 and "." in num[0:11]:
                roundNumber = 10
                entry = entry.replace(
                    num, f"{float_toInt(round(float_toInt(num), roundNumber))}")

        return entry

    def deg_to_rad(deg):
        rad = deg * (math.pi/180)
        return rad

    def is_smaller_than(brac1, brac2, i):
        brac1Ind = 0
        brac2Ind = 0
        for bInd, bracket in enumerate(brackets[0:-1]):
            if brac1 == bracket[i]:
                brac1Ind = bInd
            if brac2 == bracket[i]:
                brac2Ind = bInd
        smaller = min(brac1Ind, brac2Ind)
        if smaller != brac2Ind:
            return True
        return False

    def is_larger_than(brac1, brac2, i):
        if (not is_smaller_than(brac1, brac2, i)) and brac1 != brac2:
            return True
        return False

    def is_alpha(stuff):
        test = stuff
        pattern = r"^[a-zA-Z]+$"
        if re.search(pattern, test):
            return True
        return False

    def update_brac(us_r):
        leftBrac.clear()
        rightBrac.clear()
        leftInd.clear()
        rightInd.clear()
        for index, alpha in enumerate(us_r):
            for bracket in brackets[0:-1]:
                if alpha == bracket[0]:
                    leftBrac.append(alpha)
                    leftInd.append(index)
                elif alpha == bracket[1]:
                    rightBrac.append(alpha)
                    rightInd.append(index)

    def listifyCB(entry, lb, rb):
        hCS = False
        # if there are bits of both sided brackets
        # eliminate the completed brackets
        update_brac(entry)
        for a, brac in enumerate(rb):
            for bracket in brackets[0:-1]:
                if brac == bracket[1]:
                    # match it with the leftmost parenthesis in lb
                    for b, brac2 in enumerate(lb):
                        # find the left most parenthesis
                        if brac2 == bracket[0]:
                            # print(permaBracleft)
                            # print(permaBracRight)
                            hCS = True
                            if (rightInd[a] > leftInd[b]) and not isinstance(rb[a], list) and not isinstance(lb[b], list):
                                rb[a] = [
                                    rightInd[a], rb[a]]
                                lb[b] = [
                                    leftInd[b], lb[b]]
        return lb, rb, hCS
    # AUTOCOMPLTETION OF BRACKETS
    usA = []
    wrong_order = False
    for usr in user_input.split(":"):
        allBracketsCompleted = False
        loopCount = 0
        oop = 0
        # if they require autocomplete
        while not allBracketsCompleted:
            leftBrac = []
            rightBrac = []
            leftInd = []
            rightInd = []
            update_brac(usr)
            # create a constant to store the first brackets
            if loopCount == 0:
                permaBracleft = leftBrac
                permaBracRight = rightBrac
            HasCompletedStuff = False
            leftBrac, rightBrac, HasCompletedStuff = listifyCB(
                usr, leftBrac, rightBrac)

            def somecompleted_bracAC(usr, leftBrac, rightBrac):
                update_brac(usr)
                if ("{" in leftBrac and "[" in leftBrac) or ("}" in rightBrac and "]" in rightBrac) or (")" in rightBrac and "}" in rightBrac) or ("(" in leftBrac and "{" in leftBrac) or (")" in rightBrac and "]" in rightBrac) or ("(" in leftBrac and "[" in leftBrac) or ("{" in leftBrac and "]" in rightBrac) or ("}" in rightBrac and "[" in leftBrac) or (")" in rightBrac and "{" in leftBrac) or ("(" in leftBrac and "}" in rightBrac) or (")" in rightBrac and "[" in leftBrac) or ("(" in leftBrac and "]" in rightBrac):
                    if (len(leftBrac) != 0 and len(rightBrac) != 0):
                        leftBrac, rightBrac, HasCompletedStuff = listifyCB(
                            usr, leftBrac, rightBrac)
                        if HasCompletedStuff:
                            for a, brac in enumerate(rightBrac):
                                # check if there is complete bracket "in its left and right"
                                # is brac completed, i.e a list?
                                if not isinstance(brac, list):
                                    # if it is not completed
                                    #
                                    for j in [1, -1]:
                                        if (a-j) >= 0 and (a-j) < (len(rightBrac)):
                                            if isinstance(rightBrac[a-j], list):
                                                # i.e if it is already completed
                                                # check for each bracket if the found bracket iis its pair
                                                for bracket in brackets:
                                                    loopControl = 0
                                                    if bracket[1] == rightBrac[a-j][1]:
                                                        # find the bracket which is the pair of leftBrac[a-j][1] in rightBrac:
                                                        for brac2 in leftBrac:
                                                            while loopControl == 0:
                                                                if isinstance(brac2, list):
                                                                    # check if it has the pair
                                                                    if brac2[1] == bracket[0]:
                                                                        # get the pair of the incomplete bracket
                                                                        for bracket1 in brackets:
                                                                            if bracket1[1] == brac:
                                                                                # bracket[0] is the helper bracket
                                                                                # brac is the main left bracket
                                                                                # if indexes are wrong due to brackets being pushed due to addition of more brackets
                                                                                # inde = 0
                                                                                inde = brac2[0]

                                                                                if j == 1:
                                                                                    affectRange = inde
                                                                                    usr = f"{usr[0:inde]}{bracket1[0]}{usr[inde:]}"

                                                                                    if not is_smaller_than(bracket[1], brac, 1):
                                                                                        print(
                                                                                            f"{asc_colors['red']}Please use right order of nesting brackets{asc_colors['white']}")
                                                                                elif j == -1:
                                                                                    affectRange = inde+1
                                                                                    # if indexes are wrong due to brackets being pushed due to adding more
                                                                                    usr = f"{usr[0:inde+1].rstrip()}{bracket1[0]}{usr[inde+1:]}"
                                                                                    if is_smaller_than(bracket[1], brac, 1):
                                                                                        print(
                                                                                            f"{asc_colors['red']}Please use right order of nesting brackets{asc_colors['white']}")
                                                                                for r, brack in enumerate(leftBrac):
                                                                                    if leftInd[r] >= affectRange:
                                                                                        leftInd[r] = leftInd[r] + 1
                                                                                        # if it also has a list with its index
                                                                                        if isinstance(leftBrac[r], list):
                                                                                            leftBrac[r][0] += 1
                                                                                for r2, brack in enumerate(rightBrac):
                                                                                    if rightInd[r2] >= inde:
                                                                                        rightInd[r2] = rightInd[r2] + 1
                                                                                        # if it also has a list with its index
                                                                                        if isinstance(rightBrac[r2], list):
                                                                                            rightBrac[r2][0] += 1
                                                                loopControl += 1
                            for a, brac in enumerate(leftBrac):

                                # check if there is complete bracket "in its left and right"
                                # is brac completed, i.e a list?
                                if not isinstance(brac, list):
                                    # if it is not completed
                                    #
                                    for j in [1, -1]:
                                        if (a-j) >= 0 and (a-j) < (len(leftBrac)):
                                            if isinstance(leftBrac[a-j], list):
                                                # i.e if it is already completed
                                                # check for each bracket if the found bracket iis its pair
                                                for bracket in brackets:
                                                    loopControl = 0
                                                    if bracket[0] == leftBrac[a-j][1]:
                                                        # find the bracket which is the pair of leftBrac[a-j][1] in rightBrac:
                                                        for brac2 in rightBrac:
                                                            while loopControl == 0:
                                                                if isinstance(brac2, list):
                                                                    # check if it has the pair
                                                                    if brac2[1] == bracket[1]:
                                                                        # get the pair of the incomplete bracket
                                                                        for bracket1 in brackets:
                                                                            if bracket1[0] == brac:

                                                                                # bracket[0] is the helper bracket
                                                                                # brac is the main left bracket
                                                                                # if indexes are wrong due to brackets being pushed due to addition of more brackets
                                                                                # inde = 0
                                                                                inde = brac2[0]
                                                                                if j == 1:
                                                                                    affectRange = inde
                                                                                    usr = f"{usr[0:inde]}{bracket1[1]}{usr[inde:]}"
                                                                                elif j == -1:
                                                                                    affectRange = inde+1
                                                                                    # if indexes are wrong due to brackets being pushed due to adding more
                                                                                    usr = f"{usr[0:inde+1].rstrip()}{bracket1[1]}{usr[inde+1:]}"

                                                                                for r, brack in enumerate(leftBrac):
                                                                                    if leftInd[r] >= affectRange:
                                                                                        leftInd[r] = leftInd[r] + 1
                                                                                        # if it also has a list with its index
                                                                                        if isinstance(leftBrac[r], list):
                                                                                            leftBrac[r][0] += 1
                                                                                for r2, brack in enumerate(rightBrac):
                                                                                    if rightInd[r2] >= inde:
                                                                                        rightInd[r2] = rightInd[r2] + 1
                                                                                        # if it also has a list with its index
                                                                                        if isinstance(rightBrac[r2], list):
                                                                                            rightBrac[r2][0] += 1
                                                                                leftBrac, rightBrac, HasCompletedStuff = listifyCB(
                                                                                    usr, leftBrac, rightBrac)
                                                                loopControl += 1
                        else:   # doesnt have completedStuff
                            non = 0
                            for brac in rightBrac:
                                for brac2 in leftBrac:
                                    for bracket in brackets[0:-1]:
                                        # if there are lists, i.e they are matched:
                                        if isinstance(brac, list) or isinstance(brac2, list):
                                            non = non+1
                            # if none are matched
                            if non == 0:
                                count = 0
                                for a, brac in enumerate(rightBrac):
                                    for b, brac2 in enumerate(leftBrac):
                                        for bracket in brackets:
                                            if brac == bracket[1] and count == 0:
                                                # left is smaller
                                                thereisanotherbracketafterthefirstone = False
                                                if is_smaller_than(brac2, bracket[0], 0):
                                                    # ie bracket[0] can be infront of brac2(left)
                                                    usr = f"{usr[0:leftInd[b]]}{bracket[0]}{usr[leftInd[b]:]}"
                                                    update_brac(usr)

                                                    count = count+1
                                                # right is smaller
                                                elif not is_smaller_than(brac2, bracket[0], 0):
                                                    # if there is another bracket after the first one
                                                    for checkbrac in usr[leftInd[b]+1:rightInd[a]]:
                                                        for brackettt in brackets:
                                                            # which brac is checkbrac
                                                            if checkbrac == brackettt[0] and brackettt[1] != brac:
                                                                if is_smaller_than(brackettt[1], brac, 1):
                                                                    insertInd = usr.index(
                                                                        checkbrac)
                                                                    update_brac(
                                                                        usr)
                                                                    count = count+1
                                                                elif not is_smaller_than(brackettt[1], brac, 1):
                                                                    insertInd = usr.index(
                                                                        checkbrac)+1
                                                                    update_brac(
                                                                        usr)
                                                                    count = count+1
                                                                usr = f"{usr[:insertInd]}{bracket[0]}{usr[insertInd:]}"
                                                                thereisanotherbracketafterthefirstone = True

                                                    if not thereisanotherbracketafterthefirstone:
                                                        if not (("(" in usr and ")" in usr) or ("{" in usr and "}" in usr) or ("[" in usr and "]" in usr)):
                                                            usr = f"{usr[0:leftInd[b]+1]}{bracket[0]}{usr[leftInd[b]+1:]}"
                                                            update_brac(usr)
                                                            count = count+1

                        # usr = somecompleted_bracAC(usr, leftBrac, rightBrac)
                        # leftBrac, rightBrac, HasCompletedStuff = listifyCB(usr,
                        #                                                    leftBrac, rightBrac)
                    # print(leftBrac, rightBrac)
                    elif len(rightBrac) != 0 and len(leftBrac) == 0:
                        insertInd = 0
                        for brac in (rightBrac):
                            for bracket in brackets:
                                if bracket[1] == brac:
                                    usr = usr[:insertInd] + \
                                        bracket[0] + usr[insertInd:]
                    elif len(leftBrac) != 0 and len(rightBrac) == 0:
                        insertInd = len(usr)
                        # -1 because there is a space in the end
                        for brac in (leftBrac):
                            for bracket in brackets:
                                if bracket[0] == brac:
                                    usr = usr[0:insertInd] + \
                                        bracket[1] + usr[insertInd:]

                else:
                    # if they have only parenthesis
                    for bracket in brackets[0:-1]:
                        if bracket[0] in leftBrac or bracket[1] in rightBrac and not (("(" in usr and "{" in usr) or ("(" in usr and "[" in usr) or ("{" in usr and "[" in usr) or (")" in usr and "}" in usr) or (")" in usr and "]" in usr) or ("}" in usr and "]" in usr)):
                            while len(leftBrac) != len(rightBrac):
                                if len(leftBrac) < len(rightBrac):
                                    usr = f"{bracket[0]}{usr.lstrip()}"
                                    leftBrac.append(bracket[0])
                                elif len(leftBrac) > len(rightBrac):
                                    usr = f"{usr.rstrip()}{bracket[1]}"
                                    rightBrac.append(bracket[1])

                # are the brackets already matched?
                leftPara = []
                rightPara = []
                leftCurly = []
                rightCurly = []
                leftSquare = []
                rightSquare = []
                allBracketsCompleted = False
                for i, a in enumerate(usr):
                    if a == brackets[0][0]:
                        leftPara.append(a)
                    elif a == brackets[0][1]:
                        rightPara.append(a)
                    elif a == brackets[1][0]:
                        leftCurly.append(a)
                    elif a == brackets[1][1]:
                        rightCurly.append(a)
                    elif a == brackets[2][0]:
                        leftSquare.append(a)
                    elif a == brackets[2][1]:
                        rightSquare.append(a)
                    if (len(leftPara) == len(rightPara)) and (len(leftCurly) == len(rightCurly)) and (len(leftSquare) == len(rightSquare)):
                        allBracketsCompleted = True
                    else:
                        allBracketsCompleted = False
                return usr, allBracketsCompleted
            # section division
            for l, lbr in enumerate(leftBrac, start=0):
                # print(l, leftBrac, lbr, leftInd)
                for r, rbr in enumerate(rightBrac):
                    # for starting with L E F T sided brackets
                    finalind = None
                    if (leftInd[l] > rightInd[r]) and not isinstance(lbr, list):
                        search_domain = usr[leftInd[l]+1:]
                        finalind = len(usr)
                        # find the final point of the section
                        for alInd, alpha in enumerate(search_domain):
                            # for ending at left sided brackets in the searchIndex
                            # since the leftBrac might have lists too,
                            # ----------------------------
                            bracListInd = 0
                            while bracListInd < len(leftBrac):
                                smallLBrac = leftBrac[bracListInd]
                                if isinstance(smallLBrac, list):
                                    if alpha in smallLBrac:
                                        insmallLBrac = True
                                        break
                                    else:
                                        insmallLBrac = False
                                else:
                                    insmallLBrac = False
                                bracListInd += 1
                            # ----------------------------
                            bracListInd = 0
                            while bracListInd < len(rightBrac):
                                smallRBrac = rightBrac[bracListInd]
                                if isinstance(smallRBrac, list):
                                    if alpha in smallRBrac:
                                        insmallRBrac = True
                                        break
                                    else:
                                        insmallRBrac = False
                                else:
                                    insmallRBrac = False
                                bracListInd += 1
                            # ---------------------
                            if alpha in leftBrac or insmallLBrac:
                                if lbr == alpha:
                                    finalind = alInd - len(
                                        search_domain)
                                elif is_smaller_than(lbr, alpha, 0):
                                    finalind = alInd - \
                                        len(search_domain)
                            # for ending right sided brackets in the searchIndex
                            elif alpha in rightBrac or insmallRBrac:
                                # get the rightside of lbr
                                for bracket in brackets:
                                    if lbr == bracket[0]:
                                        if is_smaller_than(bracket[1], alpha, 1):
                                            finalind = alInd - len(
                                                search_domain)
                        section = usr[leftInd[l]: finalind]
                        section2, allBracketsCompleted = somecompleted_bracAC(
                            section, leftBrac, rightBrac)
                        leftBrac, rightBrac, HasCompletedStuff = listifyCB(
                            usr, leftBrac, rightBrac)
                        # print("be1", usr)
                        usr = usr[:(leftInd[l])] + \
                            section2 + usr[finalind:]
                        # print("1", usr)
                        leftBrac, rightBrac, HasCompletedStuff = listifyCB(
                            usr, leftBrac, rightBrac)
                    # for starting with R I G H T sided brackets
                    if rightInd[r] < leftInd[l] and not isinstance(rbr, list):
                        search_domain = usr[: rightInd[r]]
                        finalind = 0
                        # find the final point of the section (right to left)
                        alInd = len(search_domain)-1
                        while alInd >= 0:
                            alpha = search_domain[alInd]
                            # ----------------------------
                            bracListInd = 0
                            while bracListInd < len(leftBrac):
                                smallLBrac = leftBrac[bracListInd]
                                if isinstance(smallLBrac, list):
                                    if alpha in smallLBrac:
                                        insmallLBrac = True
                                        break
                                    else:
                                        insmallLBrac = False
                                else:
                                    insmallLBrac = False
                                bracListInd += 1
                            # ----------------------------
                            bracListInd = 0
                            while bracListInd < len(rightBrac):
                                smallRBrac = rightBrac[bracListInd]
                                if isinstance(smallRBrac, list):
                                    if alpha in smallRBrac:
                                        insmallRBrac = True
                                        break
                                    else:
                                        insmallRBrac = False
                                else:
                                    insmallRBrac = False
                                bracListInd += 1
                            # ---------------------
                            # for ending at right sided brackets in the searchIndex
                            if alpha in rightBrac or insmallRBrac:
                                if rbr == alpha:
                                    finalind = alInd + 1
                                elif is_smaller_than(rbr, alpha, 1):
                                    finalind = alInd + 1
                            # for ending left sided brackets in the searchIndex
                            elif alpha in leftBrac or insmallLBrac:
                                # get the left side of rbr
                                for bracket in brackets:
                                    if rbr == bracket[1]:
                                        if is_smaller_than(bracket[0], alpha, 0):
                                            finalind = alInd + 1
                            alInd -= 1

                        section = usr[finalind: rightInd[r]+1]
                        section2, allBracketsCompleted = somecompleted_bracAC(
                            section, leftBrac, rightBrac)
                        # print("be2", usr)
                        usr = usr[:finalind] + \
                            section2 + usr[rightInd[r]+2:]
                        # print("2", usr)
                        leftBrac, rightBrac, HasCompletedStuff = listifyCB(
                            usr, leftBrac, rightBrac)
            usr, allBracketsCompleted = somecompleted_bracAC(
                usr, leftBrac, rightBrac)
            # warn for unordered brackets
            wrong_order = False
            for l, brac in enumerate(leftBrac):
                if l + 1 < len(leftBrac):
                    if is_larger_than(leftBrac[l+1], brac, 0):
                        # get brac's (1st one's) partner
                        for bracket in brackets:
                            if bracket[0] == brac:
                                brac_mate = bracket[1]
                                if brac_mate not in usr[leftInd[l]:leftInd[l+1]]:
                                    print(f"{asc_colors['yellow']}{usr[:leftInd[l]]}{asc_colors['red']}{usr[leftInd[l]:leftInd[l]+1]}{asc_colors['yellow']}{usr[leftInd[l]+1:leftInd[l+1]]}{asc_colors['red']}{usr[leftInd[l+1]:leftInd[l+1]+1]}{asc_colors['yellow']}{usr[leftInd[l+1]+1:]}{asc_colors['white']}",
                                          f"\n{asc_colors['red']}Please type the right order of brackets!{asc_colors['white']}")
                                    wrong_order = True

            loopCount += 1
        usA.append(usr)
    user_input = ":".join(usA)
    if wrong_order:
        continue

    # add multiplication sign near brackets if there are no signs
    # print("a", user_input)
    usA = []
    for usr in user_input.split(":"):
        for bracket in brackets:
            allowBracketsToHaveStarLeft = True
            allowBracketsToHaveStarRight = True
            center_of_br = CenterOf_bracket_from_in(
                bracket, 0, len(usr), usr)
            if center_of_br:
                for i, a in enumerate(usr, start=0):
                    if a == bracket[0] and i < center_of_br[0]:
                        allowBracketsToHaveStarLeft = True
                        if a == bracket[0] and i >= 1 and (usr[i - 1].isdigit() or usr[i-1] == "!" or usr[i-1] == ")" or is_alpha(usr[i-1]) or usr[i-1] == "}" or usr[i-1] == "]") and allowBracketsToHaveStarLeft:
                            usr = f"{usr[0:i]}*{usr[i:len(usr)]}"
                    else:
                        allowBracketsToHaveStarLeft = False
                # for right brackets
                for i, a in reversed(list(enumerate(usr, start=0))):
                    if a == bracket[1] and i >= center_of_br[1]:
                        allowBracketsToHaveStarRight = True
                        if a == bracket[1] and i != len(usr)-1 and (usr[i + 1].isdigit()) and allowBracketsToHaveStarRight:
                            usr = f"{usr[0:i+1]}*{usr[i+1:]}"
                    else:
                        allowBracketsToHaveStarRight = False
        usA.append(usr)
    user_input = ":".join(usA)
    # print("b", user_input)
# i to j
    pattern1 = r"(\d|\-|\+|\*|\/|\^|\!|\|| |^)i( |\-|\+|\*|\/|\^|\!|\)|\}|\||\]|$)"
    while re.search(pattern1, user_input):
        for match in re.finditer(pattern1, user_input):
            user_input = user_input[:match.span(
                0)[0]]+user_input[match.span(0)[0]:match.span(0)[1]].replace("i", "j") + user_input[match.span(0)[1]:]

    # replace all the constants
    replacements = {"c": "299792458",
                    "e": "2.7182818284",
                    "g": "9.8",
                    "pi": "3.1415926535",
                    "infinity": f"{math.inf}",
                    }
    user_input = f" {user_input} "
    # multiplication in constants
    if not continuable:
        pattern1 = r"(\d|\))(e|c|pi|g)(\d| |\/|\*|\+|\-|\)|\}|\])"
        pattern2 = r"(\d| |\/|\*|\+|\-|\(|\{|\[)(e|c|pi|g)\d"
        for match in re.finditer(pattern1, user_input):
            mid = match.span(0)[0]+1
            user_input = f"{user_input[:mid]}*{user_input[mid:]}"
        for match in re.finditer(pattern2, user_input):
            mid = match.span(0)[0]+2
            # mid = int((match.span(0)[0] + match.span(0)[1])/2)
            user_input = f"{user_input[:mid]}*{user_input[mid:]}"
        for key, val in replacements.items():
            if not has_exp(user_input):
                pattern1 = r"(\d|\-|\+|\*|\/|\^|\!|\(|\{|\[|\|| |^)" + \
                    key+r"( |\-|\+|\*|\/|\^|\!|\)|\}|\]|$|\|)"
                while re.search(pattern1, user_input):
                    for match in re.finditer(pattern1, user_input):
                        user_input = user_input[:match.span(
                            0)[0]]+user_input[match.span(0)[0]:match.span(0)[1]].replace(f"{key}", f"{val}") + user_input[match.span(0)[1]:]
    # convert .. to previous answer
    if prev_ans:
        prev = prev_ans.split(":")
        for pIn, p in enumerate(prev):
            BpIn = len(prev) - 1 - pIn
            # print(prev, user_input)
            user_input = user_input.lower().replace(
                "."*(BpIn+2), str(prev[BpIn]))
    else:
        user_input = user_input.lower().replace("..", "")
    # convert ∞ to infinity
    user_input = user_input.lower().replace("∞", f'{math.inf}')

    if re.search(r"[a-zA-Z]+", user_input) and "indeterminant" not in user_input and "inf" not in user_input and ":" not in user_input and "e" not in user_input and "j" not in user_input and "sin" not in user_input and "cos" not in user_input and "tan" not in user_input and "cosec" not in user_input and "sec" not in user_input and "cot" not in user_input:
        print(
            f"{asc_colors['red']}Please enter numbers with operators for calculations.{asc_colors['green']} Enter 'h' for help.{asc_colors['white']}")
        continue
    user_input = " " + user_input.replace(" ", "") + " "

    # does user_input contain signs?
    for sign in set_of_signs:
        if not user_input.isdigit() and not continuable:
            if sign not in user_input:
                signs_unavailable += 1
    if signs_unavailable == len(set_of_signs) and ":" not in user_input and "|" not in user_input and "sin" not in user_input and "cos" not in user_input and "tan" not in user_input and "cosec" not in user_input and "sec" not in user_input and "cot" not in user_input:
        # reset
        print(f'''{asc_colors['red']}Please enter operations with operators.
        {asc_colors['green']}Or enter "x" to exit{asc_colors['white']}''')
        continue

    # remove unnecessary lead signs
    usA = []
    for usr in user_input.split(":"):
        if re.search(r"(^| \()( +)?(\*|\+|\/|\^|!)\d+", usr):
            # ie if there are any signs except "-" in lead
            signIndex = re.search(r"(\*|\+|\/|\^|!)", usr).span()[0]
            usr = usr[0:signIndex] + \
                usr[signIndex+1:len(usr)]
        usA.append(usr)
    user_input = ":".join(usA)
    # deal with spaces
    for sign in set_of_signs:
        if sign != "!":
            user_input = user_input.replace(f'{sign}', f" {sign} ")
    for bracket in brackets:
        user_input_without_brackets = user_input.replace(bracket[0], "").replace(
            bracket[1], "")
    # big numbers e
    bgPatt = r"\de (\+|\-) \d"
    while re.search(bgPatt, user_input):
        for it in re.finditer(bgPatt, user_input):
            for sign in ["+", "-"]:
                user_input = user_input.replace(
                    it.group(0), it.group(0).replace(f" {sign} ", sign))
    user_input = plus_minus_combo_check(user_input)
    # make negatives negatives
    whLoopI = 0
    if re.search(r"(\(|\||\{|\[|e|^|\*|\/|:|( ))( )(\-)( )\d+", user_input):
        itterable = re.finditer(
            r"(\(|\||\{|\[|e|^|\*|\/|:|( ))( )(\-)( )\d+", user_input)
        # print(list(itterable))
        for it in itterable:
            val = it.group(0)
            # position
            user_input = user_input.replace(val, val.replace(" - ", "-"))
    # make complex numbers complex:
    for sign in set_of_signs:
        if sign != "/" and sign != "*" and sign != "^":
            i = 0
            while i < len(user_input):
                alpha = user_input[i]
                if alpha == sign and alpha != "!":
                    chars = prev_next_chars(user_input, i)
                    if "j" in chars[1] and "j" not in chars[0]:
                        user_input = f"{user_input[:i].rstrip()}{sign}{user_input[i+1:].lstrip()}"
                    # if "j" in chars[1] and "j" in chars[0]:
                    #     user_input = f"{user_input[:i].rstrip()}{sign}{user_input[i+1:].lstrip()}"

                i += 1
    trigs = ["sin", "cosec", "cos", "tan", "sec", "cot"]

    def trigo(entry):
        # adding multiplication before the trig symbols
        pattern1 = r"\d(sin|cos|tan|cosec|sec|cot)(\d| |\/|\*|\+|\-|\)|\}|\])"
        for match in re.finditer(pattern1, entry):
            mid = match.span(0)[0]+1
            entry = f"{entry[:mid]} * {entry[mid:]}"

        # when there is bracket
        # it gets solved in the bracketWorks sectionl
        # L   O   L
        # when there is no bracket

        for trig in trigs:
            while trig in entry:
                trigInd = entry.lower().find(trig)
                # value corrections:
                entry = entry.replace("tan90", f"{math.inf}")
                entry = entry.replace("cot90", f"{0}")
                spaceAt = trigInd+3
                rightspacefound = False
                while not rightspacefound:
                    if entry[spaceAt] == " ":
                        rightspacefound = True
                    elif spaceAt == len(entry):
                        rightspacefound = True
                    else:
                        spaceAt += 1

                try:

                    if trig == "sin":
                        entry = entry.replace(entry[trigInd:spaceAt], str(round(math.sin(
                            deg_to_rad(float(entry[trigInd+3:spaceAt]))), 15)))
                    elif trig == "cosec":
                        entry = entry.replace(entry[trigInd:spaceAt], str(1/round(math.sin(
                            deg_to_rad(float(entry[trigInd+5:spaceAt]))), 15)))
                    elif trig == "cos":
                        entry = entry.replace(entry[trigInd:spaceAt], str(round(math.cos(
                            deg_to_rad(float(entry[trigInd+3:spaceAt]))), 15)))
                    elif trig == "sec":
                        entry = entry.replace(entry[trigInd:spaceAt], str(1/round(math.cos(
                            deg_to_rad(float(entry[trigInd+3:spaceAt]))), 15)))
                    elif trig == "tan":
                        entry = entry.replace(entry[trigInd:spaceAt], str(round(math.tan(
                            deg_to_rad(float(entry[trigInd+3:spaceAt]))), 15)))
                    elif trig == "cot":
                        entry = entry.replace(entry[trigInd:spaceAt], str(1/round(math.tan(
                            deg_to_rad(float(entry[trigInd+3:spaceAt]))), 15)))
                except Exception as e:
                    if str(e) == "float division by zero":
                        entry = entry.replace(
                            entry[trigInd:spaceAt], f"{math.inf}")

        return entry

    def factorial(entry):
        while "!" in entry:
            spaceFound = False

            fact_ind = entry.index("!")
            spc_ind = fact_ind
            #
            while not spaceFound:
                spc_ind -= 1
                for bracket in brackets:
                    if entry[spc_ind] == " " or entry[spc_ind] == bracket[0]:
                        spaceFound = True
            extracted = (entry[spc_ind+1:fact_ind])
            if extracted == "indeterminant":
                fact = "indeterminant"
            elif extracted == "inf":
                fact = math.inf
            elif float(extracted) < 0:
                fact = math.inf
            # solution
            elif extracted.isdigit() or re.search(r"\d+\.0$", extracted):  # ie is integer
                fac = extracted.replace(".0", "")
                fact = math.factorial(int(fac))
            else:
                print(
                    f"{asc_colors['red']}Cannot take factorials of non integers!{asc_colors['white']}")
                return
            entry = entry.replace(f'{extracted}!', f"{fact}")
        return entry

    def exp(entry):
        while " ^ " in entry:
            div_index = entry.index("^")
            chars = prev_next_chars(entry, div_index)
            # print("entry", entry)
            # print(chars)
            # for complexes
            charsC = [chars[0], chars[1]]
            if "j" in chars[0] and "j" in chars[1]:
                charsC[0] = complex(charsC[0])
                charsC[1] = complex(charsC[1])
                charsC[0] = complex(makePrecise(str(chars[0])))
                charsC[1] = complex(makePrecise(str(chars[1])))
            elif "j" in chars[0]:
                charsC[0] = complex(charsC[0])
                charsC[1] = float(chars[1])
                charsC[1] = complex(makePrecise(str(chars[1])))
            elif "j" in chars[1]:
                charsC[0] = float(chars[0])
                charsC[0] = complex(makePrecise(str(chars[0])))
                charsC[1] = complex(charsC[1])
            if (isinstance(charsC[0], complex) or isinstance(charsC[1], complex)):
                # if complex
                pro = charsC[0] ** charsC[1]
            else:
                # if not complex
                # pro = math.pow(Decimal(charsC[0]), Decimal(charsC[1]))
                # print(chars, "\n", charsC)
                pro = float(charsC[0]) ** float(charsC[1])

            entry = entry.replace(f'{chars[0]} ^ {chars[1]}', f'{pro}')
        return entry

    def divide(entry):
        while " / " in entry:
            div_index = entry.index("/")
            chars = prev_next_chars(entry, div_index)
            charsC = [chars[0], chars[1]]
            # print(charsC)
            if "j" in chars[0] and "j" in chars[1]:
                charsC[0] = complex(charsC[0])
                charsC[1] = complex(charsC[1])
                charsC[0] = complex(makePrecise(str(chars[0])))
                charsC[1] = complex(makePrecise(str(chars[1])))
            elif "j" in chars[0]:
                charsC[0] = complex(charsC[0])
                charsC[1] = float(chars[1])
                charsC[1] = complex(makePrecise(str(chars[1])))
            elif "j" in chars[1]:
                charsC[0] = float(chars[0])
                charsC[0] = complex(makePrecise(str(chars[0])))
                charsC[1] = complex(charsC[1])
            # indeterminant/indeterminant
            if chars[0] == "indeterminant" or chars[1] == "indeterminant":
                pro = "indeterminant"
            # infinity/infinity
            elif chars[0] == "inf" and chars[1] == "inf":
                pro = "indeterminant"
            # 0/0
            elif (chars[1] == "0" and chars[0] == "0") or (chars[1] == "0.0" and chars[0] == "0.0"):
                pro = "indeterminant"
            # x/0
            elif chars[1] == "0" or chars[1] == "0.0":
                pro = math.inf
            # for complexes
            elif (isinstance(charsC[0], complex) or isinstance(charsC[1], complex)):
                # if complex
                pro = charsC[0] / charsC[1]
            else:
                # if not complex
                pro = Decimal(charsC[0]) / Decimal(charsC[1])
            entry = entry.replace(
                f'{chars[0]} / {chars[1]}', f'{pro}')
            # print("div", entry)
        return entry

    def multiply(entry):
        if " * " in entry:
            while " * " in entry:
                mul_index = entry.index("*")
                chars = prev_next_chars(entry, mul_index)
                charsC = [chars[0], chars[1]]
                if "j" in chars[0] and "j" in chars[1]:
                    charsC[0] = complex(charsC[0])
                    charsC[1] = complex(charsC[1])
                    charsC[0] = complex(makePrecise(str(chars[0])))
                    charsC[1] = complex(makePrecise(str(chars[1])))
                elif "j" in chars[0]:
                    charsC[0] = complex(charsC[0])
                    charsC[1] = float(chars[1])
                    charsC[1] = complex(makePrecise(str(chars[1])))
                elif "j" in chars[1]:
                    charsC[0] = float(chars[0])
                    charsC[0] = complex(makePrecise(str(chars[0])))
                    charsC[1] = complex(charsC[1])
                # print(chars, "\n", charsC)
                # print(chars)
                if chars[0] == "indeterminant" or chars[1] == "indeterminant":
                    pro = "indeterminant"
                    # for complexes
                elif (isinstance(charsC[0], complex) or isinstance(charsC[1], complex)):
                    # if complex
                    pro = charsC[0] * charsC[1]
                else:
                    # print(charsC)
                    # if not complex
                    pro = Decimal(charsC[0]) * Decimal(charsC[1])

                entry = entry.replace(
                    f'{chars[0]} * {chars[1]}', f'{pro}')
                # print("mul", entry)
        return entry

    def subtract(entry):
        if " - " in entry:
            while " - " in entry:
                entry = plus_minus_combo_check(entry)
                sub_index = entry.index(" - ")
                sub_index = entry.index("-", sub_index)
                chars = prev_next_chars(entry, sub_index)
                # for complexes
                charsC = [chars[0], chars[1]]
                if "j" in chars[0] and "j" in chars[1]:
                    charsC[0] = complex(charsC[0])
                    charsC[1] = complex(charsC[1])
                    charsC[0] = complex(makePrecise(str(charsC[0])))
                    charsC[1] = complex(makePrecise(str(charsC[1])))
                    # print(charsC)
                elif "j" in chars[0]:
                    charsC[0] = complex(charsC[0])
                    charsC[1] = float(chars[1])
                    charsC[1] = complex(makePrecise(str(charsC[1])))
                elif "j" in chars[1]:
                    charsC[0] = float(chars[0])
                    charsC[0] = complex(makePrecise(str(charsC[0])))
                    charsC[1] = complex(charsC[1])
                if chars[0] == "indeterminant" or chars[1] == "indeterminant":
                    pro = "indeterminant"
                elif chars[0] == "inf" and chars[1] == "inf":
                    pro = "indeterminant"
                elif (isinstance(charsC[0], complex) or isinstance(charsC[1], complex)):
                    # if complex
                    pro = charsC[0] - charsC[1]
                else:
                    # if not complex
                    pro = Decimal(charsC[0]) - Decimal(charsC[1])

                entry = entry.replace(
                    f'{chars[0]} - {chars[1]}', f'{pro}')
                # print("sub", entry)
        return entry

    def add(entry):
        if " + " in entry:
            while " + " in entry:
                add_index = entry.index("+")
                chars = prev_next_chars(entry, add_index)
                # for complexes
                charsC = [chars[0], chars[1]]

                if "j" in chars[0] and "j" in chars[1]:
                    charsC[0] = complex(charsC[0])
                    charsC[1] = complex(charsC[1])
                    charsC[0] = complex(makePrecise(str(chars[0])))
                    charsC[1] = complex(makePrecise(str(chars[1])))
                elif "j" in chars[0]:
                    charsC[0] = complex(charsC[0])
                    charsC[1] = float(charsC[1])
                    charsC[1] = complex(makePrecise(str(chars[1])))
                elif "j" in chars[1]:
                    charsC[0] = float(charsC[0])
                    charsC[0] = complex(makePrecise(str(chars[0])))
                    charsC[1] = complex(charsC[1])

                # print(charsC, "\n", chars)
                if chars[0] == "indeterminant" or chars[1] == "indeterminant":
                    pro = "indeterminant"
                elif (isinstance(charsC[0], complex) or isinstance(charsC[1], complex)):
                    # if complex
                    pro = charsC[0] + charsC[1]
                else:
                    # if not complex
                    pro = Decimal(charsC[0]) + Decimal(charsC[1])

                entry = entry.replace(f'{chars[0]} + {chars[1]}', f'{pro}')
                # print("add", entry)
        return entry

    # work splitting section
    def BracketWork(entry, lOut, rOut):
        if ("(" in entry and ")" in entry) or ("{" in entry and "}" in entry) or ("[" in entry and "]" in entry) or ("|" in entry):
            if "|" in entry:
                lb = "|"
                rb = "|"
            elif "(" in entry:
                lb = brackets[0][0]
                rb = brackets[0][1]
            elif "{" in entry:
                lb = brackets[1][0]
                rb = brackets[1][1]
            elif "[" in entry:
                lb = brackets[2][0]
                rb = brackets[2][1]
            while (lb in entry and rb in entry):
                if lb == "|":
                    brac_init_index = entry.index(lb)
                    brac_end_index = entry.index(
                        rb, brac_init_index+1)
                else:
                    brac_init_index = findLastIndex(entry, lb)
                    brac_end_index = entry.index(rb, brac_init_index)
                process_unit = " " + \
                    entry[brac_init_index +
                          1:brac_end_index] + " "
                if lb == "|":
                    # for nesting
                    process_unit = BracketWork(process_unit, "|", "|")
                # print("pu1", ":"+prev_input[-1]+":")
                entry = plus_minus_combo_check(entry)
                process_unit = makePrecise(process_unit)
                process_unit = str(trigo(process_unit))
                process_unit = makePrecise(process_unit)
                # print("pu2", ":"+prev_input[-1]+":")
                appendable = entry[:brac_init_index + 1] + \
                    entry[brac_init_index + 1:brac_end_index] + \
                    entry[brac_end_index:]
                prev_input.append(appendable)

                process_unit = str(factorial(process_unit))
                process_unit = makePrecise(process_unit)
                appendable = entry[:brac_init_index + 1] + \
                    entry[brac_init_index + 1:brac_end_index] + \
                    entry[brac_end_index:]
                prev_input.append(appendable)
                # print("pu3", ":"+prev_input[-1]+":")

                process_unit = str(exp(process_unit))
                process_unit = makePrecise(process_unit)
                appendable = entry[:brac_init_index + 1] + \
                    entry[brac_init_index + 1:brac_end_index] + \
                    entry[brac_end_index:]
                prev_input.append(appendable)

                # print("pu4", ":"+prev_input[-1]+":")
                process_unit = str(divide(process_unit))
                process_unit = makePrecise(process_unit)
                appendable = entry[:brac_init_index + 1] + \
                    entry[brac_init_index + 1:brac_end_index] + \
                    entry[brac_end_index:]
                prev_input.append(appendable)

                # print("pu5", ":"+prev_input[-1]+":")
                process_unit = str(multiply(process_unit))
                process_unit = makePrecise(process_unit)
                appendable = entry[:brac_init_index + 1] + \
                    entry[brac_init_index + 1:brac_end_index] + \
                    entry[brac_end_index:]
                prev_input.append(appendable)

                # print("pu6", ":"+prev_input[-1]+":")
                process_unit = str(subtract(process_unit))
                process_unit = makePrecise(process_unit)
                appendable = entry[:brac_init_index + 1] + \
                    entry[brac_init_index + 1:brac_end_index] + \
                    entry[brac_end_index:]
                prev_input.append(appendable)

                # print("pu7", ":"+prev_input[-1]+":")
                process_unit = str(add(process_unit))
                process_unit = makePrecise(process_unit)
                appendable = entry[:brac_init_index + 1] + \
                    entry[brac_init_index + 1:brac_end_index] + \
                    entry[brac_end_index:]
                prev_input.append(appendable)

                # space management
                process_unit = process_unit.replace(" ", "")
                if lb == "|":
                    if "j" not in process_unit:
                        process_unit = math.fabs(float(process_unit))
                    else:
                        process_unit2 = process_unit
                        for s in ["+", "-"]:
                            sign = s
                            if sign in process_unit2 and "j" in process_unit2:
                                process_unit2 = " "+process_unit2.replace(" ", "").replace(
                                    sign, f" {sign} ").replace("(", "").replace(")", "") + " "
                                snInd = process_unit2.find(sign)
                                phars = prev_next_chars(process_unit2, snInd)
                                process_unit2 = f"({float(phars[0])}^2 - {phars[1].replace('j', '')}^2) ^0.5"
                        process_unit = process_unit2
                entry = entry.replace(
                    f'{lb}{entry[brac_init_index + 1:brac_end_index]}{rb}', str(process_unit))
                # print(entry)
        return entry
    trigInUserInput = "sin" in user_input or "cos" in user_input or "tan" in user_input or "cosec" in user_input or "sec" in user_input or "cot" in user_input
    # ie if signs are available

    if signs_unavailable != len(set_of_signs) or trigInUserInput:
        prev_input.append(user_input)
        if ("(" in user_input and ")" in user_input) or ("{" in user_input and "}" in user_input) or ("[" in user_input and "]" in user_input) or ("|" in user_input):
            user_input = BracketWork(user_input, "", "")
            continuable = True
            continue
        else:
            for sign in set_of_signs:
                user_input = str(factorial(user_input))

                user_input = str(trigo(user_input))
                while f" {sign} " in user_input:
                    user_input = plus_minus_combo_check(user_input)
                    # print("process1:>", user_input)

                    user_input = makePrecise(user_input)
                    user_input = str(trigo(user_input))

                    prev_input.append(user_input)

                    user_input = makePrecise(user_input)
                    user_input = str(exp(user_input))

                    prev_input.append(user_input)

                    user_input = makePrecise(user_input)
                    user_input = str(divide(user_input))
                    # print("process2:>", user_input)

                    prev_input.append(user_input)

                    user_input = makePrecise(user_input)
                    user_input = str(multiply(user_input))
                    # print("process3:>", user_input)

                    prev_input.append(user_input)

                    user_input = makePrecise(user_input)
                    user_input = str(subtract(user_input))

                    # print("process4:>", user_input)
                    prev_input.append(user_input)

                    user_input = makePrecise(user_input)
                    user_input = str(add(user_input))

                    # print("process5:>", user_input)
                    prev_input.append(user_input)
                    user_input = makePrecise(user_input)

    # remove unnecessary brackets before answers
    for i in range(0, len(prev_input) - 1):
        for bracket in brackets:
            if prev_input[i].replace(bracket[0], "").replace(bracket[1], "") == user_input:
                prev_input[i] = prev_input[i].replace(
                    bracket[0], "").replace(bracket[1], "")

            for j in range(0, len(prev_input) - 1):
                if prev_input[i].replace(bracket[0], "").replace(bracket[1], "").replace(" ", "") == prev_input[j].replace(" ", ""):
                    prev_input[i] = prev_input[j]
                    # remove duplicates
    prev_input = list(dict.fromkeys(prev_input))
    for i in range(0, len(prev_input) - 1):
        # to remove the .0 decimals
        # print(prev_input[i])

        prev_input[i] = prev_input[i].replace(":", " : ")
        prev_input[i] = prev_input[i].replace(" .0 ", " 0 ")
        prev_input[i] = prev_input[i].replace(".0 ", " ")
        prev_input[i] = prev_input[i].replace("E+", "*10^")
        prev_input[i] = prev_input[i].replace("E-", "*10^-")
        prev_input[i] = prev_input[i].replace("e+", "*10^")
        prev_input[i] = prev_input[i].replace("e-", "*10^-")
        # brackets colors
        brackets_withColor = [[f"{asc_colors['magenta']}{'('}{asc_colors['white']}", f"{asc_colors['magenta']}{')'}{asc_colors['white']}"], [
            f"{asc_colors['red']}{'{'}{asc_colors['white']}", f"{asc_colors['red']}{'}'}{asc_colors['white']}"], [f"{asc_colors['yellow']}{'['}{asc_colors['white']}", f"{asc_colors['yellow']}{']'}{asc_colors['white']}"]]
        prev_input[i] = prev_input[i].replace(
            "[", f'''{asc_colors['yellow']}{"["}{asc_colors['white']}''').replace(
            "]", f'''{asc_colors['yellow']}{"]"}{asc_colors['white']}''').replace(
            "(", f'''{asc_colors['magenta']}{"("}{asc_colors['white']}''').replace(
            ")", f'''{asc_colors['magenta']}{")"}{asc_colors['white']}''').replace(
            "{", f'''{asc_colors['red']}{"{"}{asc_colors['white']}''').replace(
            "}", f'''{asc_colors['red']}{"}"}{asc_colors['white']}''')
        # signs colors
        for sign in set_of_signs:
            prev_input[i] = prev_input[i].replace(
                sign, f"{asc_colors['cyan']}{sign}{asc_colors['white']}")
        # re-replacement of constants
        prev_input[i] = prev_input[i].replace(
            "j", "{asc_colors['yellow']}i{asc_colors['white']}")
        for bracket in brackets_withColor:
            for key, val in replacements.items():
                if key != "infinity":
                    prev_input[i] = prev_input[i].lower().replace(
                        f' {val} ', f"{asc_colors['yellow']} {key} {asc_colors['white']}")
                    prev_input[i] = prev_input[i].lower().replace(
                        f'{bracket[0]}{val} ', f"{asc_colors['yellow']}{bracket[0]}{key} {asc_colors['white']}")
                    prev_input[i] = prev_input[i].lower().replace(
                        f'{val}{bracket[1]} ', f"{asc_colors['yellow']}{key}{bracket[1]} {asc_colors['white']}")
                    # print(bracket[0]+str(val), prev_input[i])
                elif key == "infinity":
                    prev_input[i] = prev_input[i].lower().replace(
                        f'inf', f"{asc_colors['yellow']}∞{asc_colors['white']}")
        # decimal colors
        if re.search(r"\.\d+", prev_input[i]):
            itter = re.finditer(r"\.\d+", prev_input[i])
            for j in itter:
                prev_input[i] = prev_input[i].replace(
                    f"{j.group(0)}", f"{asc_colors['green']}{j.group(0)}{asc_colors['white']}")
        # colon color
        prev_input[i] = prev_input[i].replace(
            ":", f"{asc_colors['red']} : {asc_colors['white']} = ")
        if steps:
            # print steps
            print(
                f"{asc_colors['yellow']}={asc_colors['white']}", prev_input[i])
    # print(prev_input)
    user_Array = user_input.replace(" ", "").split(":")
    usrArray = []
    # Answer formatting
    for i, usr in enumerate(user_Array):
        if usr.replace(" ", "") != "indeterminant":
            if "j" not in usr and "e" not in usr.lower():
                if float(usr) != math.inf:
                    if usr != math.inf:
                        usr = float_toInt(usr)
        usr = str(usr)
        usr = usr.replace("inf", "∞")
        usrArray.append(usr)
        # print(usrArray)
    usrStr = str(usrArray).replace(
        "[", "").replace("]", "").replace("'", "")
    # e formatting
    usrStr = str(usrStr).replace("E+", "*10^")
    usrStr = str(usrStr).replace("E-", "*10^-")
    usrStr = str(usrStr).replace("e+", "*10^")
    usrStr = str(usrStr).replace("e-", "*10^-")
    # signs colors
    for sign in set_of_signs:
        usrStr = usrStr.replace(
            sign, f"{asc_colors['green']}{sign}{asc_colors['magenta']}")
    # re-replacement of constants
    usrStr = usrStr.replace(
        "j", "f{asc_colors['yellow']}i{asc_colors['magenta']}")
    for key, val in replacements.items():
        if key != "infinity":
            usrStr = usrStr.lower().replace(
                f" {val} ", f"{asc_colors['yellow']} {key} {asc_colors['magenta']}")
        elif key == "infinity":
            usrStr = usrStr.lower().replace(
                f'infinity', f"{asc_colors['yellow']}∞{asc_colors['magenta']}")
    # decimal colors
    if re.search(r"\.\d+", usrStr):
        itter = re.finditer(r"\.\d+", usrStr)
        for j in itter:
            usrStr = usrStr.replace(
                f'{j.group(0)}', f"{asc_colors['cyan']}{j.group(0)}{asc_colors['magenta']}")
    # commas
    usrStr = usrStr.replace(
        ",", f"{asc_colors['white']},{asc_colors['magenta']}")
    print(f"{asc_colors['cyan']}Answer:{asc_colors['magenta']}>",
          f"{asc_colors['magenta']}{usrStr}{asc_colors['white']}")
    length = 0
    usA = []
    for usr in user_input.split(":"):
        if "j" in user_input:
            usr = str(makePrecise(usr))
        elif float(usr) != math.inf:
            usr = str(float_toInt(usr))
        usA.append(usr)
    user_input = ":".join(usA)
    # count number of digits in the output
    if user_input.replace(" ", "").replace(".", "").replace("-", "").isdigit() and cardin > 0:
        indOfDeci = user_input.find(".")
        if indOfDeci != -1:
            for i, l in enumerate(user_input):
                if i < indOfDeci:
                    length = length+1
        else:
            length = len(user_input.replace(" ", "").replace("-", ""))
        print(
            f"{asc_colors['yellow']}Cardinality:{asc_colors['green']}> {length}{asc_colors['red']}.{asc_colors['green']}{len(user_input.replace(' ', '').replace('.', '').replace('-','')) - length}")
    # to check if the userinput is actually an answer
    user_input_without_decimal = str(
        user_input).replace(".", "")
    user_input_without_neg = user_input_without_decimal
    if re.search(r"^-(\d)+$", user_input_without_neg.replace(" ", "")):
        user_input_without_neg = user_input_without_neg.replace("-", "")

    for sign in set_of_signs:
        if sign not in user_input_without_neg:
            continue_index += 1
    # if continue_index == len(set_of_signs):
    continuable = False
    prev_ans = user_input.replace("e+", "*10^").replace("e-", "*10^-")
    prev_ans = user_input.replace("E+", "*10^").replace("E-", "*10^-")

#     except Exception as e:
#         continuable = False
#         print(f'''{asc_colors['red']}Something went wrong, please check you input.
# {asc_colors['green']}Enter h for help.{asc_colors['white']}''')
