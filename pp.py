print("Калькулятор операторов Python\n")

while True:
    print("\n1.Арифм 2.Сравн 3.Лог 4.Бит 5.Принадл 6.Тожд 0.Выход")
    c = input("Выбор: ")
    
    if c == '0': break
    
    if c == '1':
        a,b = float(input("a=")), float(input("b="))
        op = input("+ - * / // % **: ")
        if op == '+': print(f"{a}+{b}={a+b}")
        elif op == '-': print(f"{a}-{b}={a-b}")
        elif op == '*': print(f"{a}*{b}={a*b}")
        elif op == '/': print(f"{a}/{b}={a/b}" if b else "На 0 нельзя")
        elif op == '//': print(f"{a}//{b}={a//b}" if b else "На 0 нельзя")
        elif op == '%': print(f"{a}%{b}={a%b}" if b else "На 0 нельзя")
        elif op == '**': print(f"{a}**{b}={a**b}")
    
    elif c == '2':
        a,b = float(input("a=")), float(input("b="))
        op = input("== != > < >= <=: ")
        if op == '==': print(f"{a}=={b}={a==b}")
        elif op == '!=': print(f"{a}!={b}={a!=b}")
        elif op == '>': print(f"{a}>{b}={a>b}")
        elif op == '<': print(f"{a}<{b}={a<b}")
        elif op == '>=': print(f"{a}>={b}={a>=b}")
        elif op == '<=': print(f"{a}<={b}={a<=b}")
    
    elif c == '3':
        op = input("and or not: ")
        if op == 'not':
            a = input("True/False? ")[0].lower() == 't'
            print(f"not {a}={not a}")
        else:
            a = input("1(True/False)? ")[0].lower() == 't'
            b = input("2(True/False)? ")[0].lower() == 't'
            if op == 'and': print(f"{a} and {b}={a and b}")
            elif op == 'or': print(f"{a} or {b}={a or b}")
    
    elif c == '4':
        a,b = int(input("a=")), int(input("b="))
        op = input("& | ^ ~ << >>: ")
        if op == '&': print(f"{a}&{b}={a&b}")
        elif op == '|': print(f"{a}|{b}={a|b}")
        elif op == '^': print(f"{a}^{b}={a^b}")
        elif op == '~': print(f"~{a}={~a}")
        elif op == '<<': print(f"{a}<<{b}={a<<b}")
        elif op == '>>': print(f"{a}>>{b}={a>>b}")
    
    elif c == '5':
        lst = input("Список (через пробел): ").split()
        item = input("Элемент: ")
        op = input("in not in: ")
        if op == 'in': print(f"{item} in {lst} = {item in lst}")
        elif op == 'not in': print(f"{item} not in {lst} = {item not in lst}")
    
    elif c == '6':
        print("Пример: list1=[1], list2=[1], list3=list1")
        list1, list2, list3 = [1], [1], list1
        print(f"list1 is list2: {list1 is list2}")
        print(f"list1 is list3: {list1 is list3}")
        print(f"list1 is not list2: {list1 is not list2}")
    
    input("Далее...")