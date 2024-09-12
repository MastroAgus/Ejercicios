def restar1(a:int, b:int)->int:
    return a - b

def restar2()->int:
    a = 40
    b = 10
    return a - b

def restar3(a= int, b = int):
    print (f"resultado de resta 3 /{a} - {b}/ es {a - b}")

def restar4():
    a = 100
    b = 50 
    print (f"resultado de resta 3 /{a} - {b}/ es {a - b}")





resultado1 = restar1 (20,10)
print (f"resultado resta 1 es {resultado1}")

resultado2 = restar2()
print (f"resultado resta 2 es {resultado2}")

resultado3 = restar3 (9,6)

restar4() 