"""
La librairie calc permet de faire les opérations basiques de calcul entre deux entiers.
"""
#fonction addition
def add(arg1,arg2):
    try:
        return int(arg1)+int(arg2)
    except ValueError: 
        print("Un des arguments n'est pas un entier.") 
#fonction soustraction
def sous(arg1,arg2):
    try:
        return int(arg1)-int(arg2)
    except ValueError: 
        print("Un des arguments n'est pas un entier.") 

#fonction multiplication
def mult(arg1,arg2):
    try:
        return int(arg1)*int(arg2)
    except ValueError: 
        print("Un des arguments n'est pas un entier.") 
#fonction division
def div(arg1,arg2):
    try:
        return int(arg1)/int(arg2)
    except ValueError: 
        print("Un des arguments n'est pas un entier.") 
    except ZeroDivisionError:
        print("Vous divisez par 0.")
#fonction modulo
def modulo(arg1,arg2):
    try:
        return int(arg1)%int(arg2)
    except ValueError:
        print("Un des arguments n'est pas un entier")    
#fonction operation
def ope(operateur,arg1,arg2):   
    if operateur=='+':
        return add(arg1,arg2)        
    elif operateur=="%":
        return modulo(arg1,arg2)
    elif operateur=="-":
        return sous(arg1,arg2)
    elif operateur=="x":
        return mult(arg1,arg2)
    elif operateur=="/":
        return div(arg1,arg2)
    else:
        print("L'opérateur {} n'est pas reconnu.".format(operateur))