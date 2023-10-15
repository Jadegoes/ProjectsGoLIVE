from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
import ast as ast
import colorama
from colorama import Fore

LATQ=[]
SATQ=[]
def cursormoves1(canvas, loca, data):
    for line in data:
        textobject = canvas.beginText()
        textobject.setTextOrigin(40, loca)
        textobject.setFont("Helvetica", 14)

        textobject.textLine(line)
        loca = loca - 28
        used.append(line)
        canvas.drawText(textobject)

        if (loca <= 40):
            loca = 792
            canvas.showPage()
            for i in data:
                if (i in used):
                    data.remove(i)
                    break
            continue
        else:
            continue
    global loc
    loc = loca
def user():
    print(Fore.GREEN +
          '''
          Types of questions available:-
          1)Short Answer Type
          2)Long Answer Type
          ''')
    print(Fore.CYAN + "To confirm selections, Enter 'ok' ")
    choice = []
    y = input(Fore.CYAN + "Enter choice type : ")
    choice.append(y)
    while y!="ok":
        y=input(Fore.CYAN + "Enter choice type : ")
        choice.append(y)
    if choice==["1","ok"]:
        import random
        import ast as ast
        file = open(r"C:\Users\DELL\Documents\qpmaker.txt", "r")
        contents = file.read()
        ques = ast.literal_eval(contents)
        file.close()
        x = int(input(Fore.CYAN + "Enter number of SATQs:"))
        print(Fore.MAGENTA + "Short Anwer Type:-")
        used = []
        while len(used) < x:
            index = len(used) + 1
            q = random.sample(ques, 1)
            for i in q:
                use = i
                if use in used:
                    continue
                else:
                    used.append(use)
                    print(Fore.MAGENTA + use)
                    SATQ.append(use)
        print(Fore.RED + "Done ;)")
    elif choice==["2","ok"]:
        import random
        import ast as ast
        file = open(r"C:\Users\DELL\Documents\qpmaker2.txt", "r")
        contents = file.read()
        ques = ast.literal_eval(contents)
        file.close()
        z = int(input(Fore.CYAN + "Enter number of LATQs:"))
        print(Fore.MAGENTA + "Long Anwer Type:-")
        used = []
        while len(used) < z:
            index = len(used) + 1
            q = random.sample(ques, 1)
            for i in q:
                use = i
                if use in used:
                    continue
                else:
                    used.append(use)
                    print(Fore.MAGENTA + use)
                    LATQ.append(use)
        print(Fore.RED + "Done ;)")
    else:
        import random
        import ast as ast
        file = open(r"C:\Users\DELL\Documents\qpmaker.txt", "r")
        contents = file.read()
        ques = ast.literal_eval(contents)
        file.close()
        x = int(input(Fore.CYAN + "Enter number of SATQs:"))
        z = int(input(Fore.CYAN + "Enter number of LATQs:"))
        print(Fore.MAGENTA + "Short Anwer Type:-")
        used = []
        while len(used) < x:
            index = len(used) + 1
            q = random.sample(ques, 1)
            for i in q:
                use = i
                if use in used:
                    continue
                else:
                    used.append(use)
                    print(Fore.MAGENTA + use)
                    SATQ.append(use)

        import random
        import ast as ast
        file = open(r"C:\Users\DELL\Documents\qpmaker2.txt", "r")
        contents = file.read()
        ques = ast.literal_eval(contents)
        file.close()
        print(Fore.MAGENTA + "Long Anwer Type:-")
        used = []
        while len(used) < z:
            index = len(used) + 1
            q = random.sample(ques, 1)
            for i in q:
                use = i
                if use in used:
                    continue
                else:
                    used.append(use)
                    print(Fore.MAGENTA + use)
                    LATQ.append(use)
        print(Fore.RED + "Done ;)")

print(Fore.GREEN + "WELCOME TO THE PDF MAKER")

print(Fore.CYAN + "Enter the name fo the file : ")
filename = input().rstrip().upper() + ".pdf"

print(Fore.CYAN + "Enter the Title : ")
title = input().rstrip().upper()

print(Fore.CYAN + "Paste the the file path of the logo here ( without inverted commas ): ")
pathimage = input()

print(Fore.CYAN + "Enter the Subheading : ")
subtitle = input().rstrip().upper()

print(Fore.CYAN + "Enter maximum marks : ")
marks = str(input())
marks = 'Maximum marks : ' + marks

print(Fore.CYAN + "Enter time alloted ( min ) : ")
time = str(input())
time = 'Maximum time : ' + time

print(Fore.CYAN + "Enter the subject : ")
subject = input().rstrip().upper()
subject = 'Subject : ' + subject

ques = {"Short answer type":SATQ,"Long answer type":LATQ}
secname=["Short answer type","Long answer type"]

print(Fore.GREEN + "Initials Acquired Succesfully")
print(Fore.GREEN + "Now Acquiring Question Data")

pdf = Canvas(filename)

pdfmetrics.registerFont(
    TTFont("Mainfont" , r"C:\Users\DELL\Documents\fonts.ttf format\CutiveMono-Regular.ttf")
)
pdfmetrics.registerFont(
    TTFont("Mainfont1" , r"C:\Users\DELL\Documents\fonts.ttf format\FrontPageNeue.otf")
)

pdf.setFont('Mainfont1', 50)
pdf.drawCentredString(313, 770, title)

pdf.drawInlineImage(pathimage, 20, 752, 80, 80, showBoundary=True)

pdf.setFillColor(colors.black)
pdf.setFont("Mainfont", 24)
pdf.drawCentredString(297.5, 730, subtitle)

pdf.setFillColor(colors.black)
pdf.setFont("Courier-Bold", 14)
pdf.drawString(40, 700, time)

pdf.setFillColor(colors.black)
pdf.setFont("Courier-Bold", 14)
pdf.drawRightString(555, 700, marks)

pdf.setFillColor(colors.black)
pdf.setFont("Courier-Bold", 14)
pdf.drawString(40, 680, subject)

pdf.line(30, 670, 565, 670)

loc = 650
used = []

user()
# Data print
for i in secname:
    pdf.setFillColor(colors.black)
    pdf.setFont("Mainfont", 16)
    pdf.drawCentredString(297.5, loc, i)
    loc = loc - 30

    cursormoves1(pdf, loc, ques[i])
    loc = int(loc)
    loc = loc - 30

pdf.save()
