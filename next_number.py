def logic_a(lista):
    result = lista[-1] + 2 
    return result

def logic_b(lista):
    result = lista[-1] * 2  
    return result

def logic_c(lista):
    result = (len(lista)) ** 2  
    return result

def logic_d(lista):
    result = ((len(lista) + 1) * 2) ** 2 
    return result

def logic_e(lista):
    result = lista[-1] + lista[-2]  
    return result

def logic_f(lista):
    result = lista[-1] + 1 
    return result

list_a = [1, 3, 5, 7]
list_b = [2, 4, 8, 16, 32, 64]
list_c = [0, 1, 4, 9, 16, 25, 36]
list_d = [4, 16, 36, 64]
list_e = [1, 1, 2, 3, 5, 8]
list_f = [2, 10, 12, 16, 17, 18, 19]

next_a = logic_a(list_a)
next_b = logic_b(list_b)
next_c = logic_c(list_c)
next_d = logic_d(list_d)
next_e = logic_e(list_e)
next_f = logic_f(list_f)

print(next_a, next_b, next_c, next_d, next_e, next_f)
