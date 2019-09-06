import os

p_name=input("Enter Person Name")
ft = int(input("What you Want diet or exercise \n Press 1 for Create diet \nPress 2 for Create exercise\n3 for Read Diet\n4 for Read exercise\n"))
f_diet = p_name + "_diet.txt"
f_exercise = p_name+"_exercise.txt"
if ft < 5:
    if ft == 1:
        f = open(f_diet,'x')
        f.write(p_name+"\nWelcome For Diet\n")
        f.close()
        f = open(f_diet,'a')
        data = input("\nhii..\nEnter Your Today Diet\n")
        f.write(data)
        f.close()
    if ft == 2:
        f = open(f_exercise, 'w')
        f.write(p_name + "\nWelcome For exercise\n")
        f.close()
        f.close()
        f = open(f_exercise,'a')
        data = input("\nhii..\nEnter Your Today exercise\n")
        f.write(data)
        f.close()
    if ft == 3:
        f = open(f_diet,'a')
        print(f.read())
        f.close()
    if ft == 4:
        f.close()
        f = open(f_diet,'a')
        print(f.read())
        f.close()
else:
    print("Invalid Input")