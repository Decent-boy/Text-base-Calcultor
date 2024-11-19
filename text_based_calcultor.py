from sty import fg,ef, rs
import time
try:

    name=input(f"{fg.black}{ef.b}{ef.u}Enter your Name{ef.rs}: {rs.all}")
    if len(name)<3:
        print(f"{fg.green}{ef.i}Loding...{rs.all}")
        time.sleep(3)
        print(f"{fg.red}{ef.i}Sorry{rs.all}")
        quit()
    elif len(name)>40:
        print(f"{fg.green}{ef.i}Loding...{rs.all}")
        time.sleep(3)
        print(f"{fg.red}{ef.i}Sorry{rs.all}")
        quit()
            
    else:
        print(f"{fg.cyan}{ef.i}WellCome to {name} in Calcultor {rs.all}")
except ValueError:
    print(f"{fg.red}{ef.i}{ef.u}Invalid statement{rs.all}")

# start from here
try:
    while True:
        user=input(f"{fg.black}{ef.b}do you want to do mathmatic type (y) for yes\ntype here (Q) for quit: {rs.all}")
        if user.lower()=="q":
            print(f"{fg.green}{ef.i}Loding...{rs.all}")
            time.sleep(3)
            print(f"{fg.cyan}Done!{rs.all}")
            quit()
            
        try:
            operand=input(f"{fg.black}{ef.b}Enter value: {rs.all}")
            operand=float(operand)
        except ValueError:
            print(f"{fg.red}{ef.i}Invalid{rs.all}")
        sign=input(f"{fg.black}{ef.b}Enter sign: {rs.all}")
        try:
            operand2=input(f"{fg.black}{ef.b}Enter value: {rs.all}")
            operand2=float(operand2)
        except ValueError:
            print(f"{fg.red}{ef.i}Invalid{rs.all}")
        def sum():
            sum=operand + operand2
            print(f"{fg.cyan}{ef.i}Ans: {sum}{rs.all}")
        # sum()
        def substract():
            sub=operand - operand2
            print(f"{fg.cyan}{ef.i}Ans: {sub}{rs.all}")
        # substract()
        def multiplay():
            mul=operand * operand2
            print(f"{fg.cyan}{ef.i}Ans: {mul}{rs.all}")
        # multiplay()
        def power():
            powr=operand * operand2
            print(f"{fg.cyan}{ef.i}Ans: {powr}{rs.all}")
        # power()
        def devision():
            divi= operand / operand2
            print(f"{fg.cyan}{ef.i}Ans: {divi}{rs.all}")
        # devision()

        if sign.lower()=="sum" or sign=="+":
            print(f"{fg.green}{ef.i}Loding...{rs.all}")
            time.sleep(3)
            sum()
        elif sign.lower()=="substract" or sign=="-":
            print(f"{fg.green}{ef.i}Loding...{rs.all}")
            time.sleep(3)
            substract()
        elif sign.lower()=="multiplay" or sign=="*":
            print(f"{fg.green}{ef.i}Loding...{rs.all}")
            time.sleep(3)
            multiplay()
        elif sign.lower()=="division" or sign=="/":
            print(f"{fg.green}{ef.i}Loding...{rs.all}")
            time.sleep(3)
            devision()
        elif sign.lower()=="power" or sign=="**":
            print(f"{fg.green}{ef.i}Loding...{rs.all}")
            time.sleep(3)
            power()
        else:
            print(f"{fg.red}{ef.i}Sorry!{rs.all}")
except ValueError:
    print(f"{fg.red}{ef.i}Invalid!{rs.all}")