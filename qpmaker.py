from tkinter import *
t=Tk()
def user():
    print("Welcome to the question maker :)")
    print("Hello User")
    print("Types of questions available:- \n"
          "1)Short Answer Type\n"
          "2)Long Answer Type\n")
    print("To confirm selections type ok")
    choice = []
    y = input("Enter choice type:-")
    choice.append(y)
    while y!="ok":
        y=input("Enter choice type:-")
        choice.append(y)
    if choice==["1","ok"]:
        import random
        import ast as ast
        file = open("C:/Users/DELL/Documents/qpmaker.txt", "r")
        contents = file.read()
        ques = ast.literal_eval(contents)
        file.close()
        x = int(input("Enter number of SATQs:"))
        print("Short Anwer Type:-")
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
                    print("Q.", index, ")", use, "?")
        print("Done ;)")
    elif choice==["2","ok"]:
        import random
        import ast as ast
        file = open("C:/Users/DELL/Documents/qpmaker2.txt", "r")
        contents = file.read()
        ques = ast.literal_eval(contents)
        file.close()
        z = int(input("Enter number of LATQs:"))
        print("Long Anwer Type:-")
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
                    print("Q.", index, ")", use, "?")
        print("Done ;)")
    else:
        import random
        import ast as ast
        file = open("C:/Users/DELL/Documents/qpmaker.txt", "r")
        contents = file.read()
        ques = ast.literal_eval(contents)
        file.close()
        x = int(input("Enter number of SATQs:"))
        z = int(input("Enter number of LATQs:"))
        print("Short Anwer Type:-")
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
                    print("Q.", index, ")", use, "?")
        import random
        import ast as ast
        file = open("C:/Users/DELL/Documents/qpmaker2.txt", "r")
        contents = file.read()
        ques = ast.literal_eval(contents)
        file.close()
        print("Long Anwer Type:-")
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
                    print("Q.", index, ")", use, "?")
        print("Done ;)")
x=Button(t,text="Enter",command=user,fg="White",bg="Red",activeforeground="White"
         ,activebackground="Red",font="Algerian")
x.pack()
t.mainloop()


