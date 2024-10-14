txt = input("Digite um texto: ")

def verificar(texto):
    a_min = texto.count('a')
    a_max = texto.count('A')
    
    resultado = []
    
    if a_min > 0:
        resultado.append(f"A letra 'a' minúscula aparece {a_min} vez(es) na string.")
    if a_max > 0:
        resultado.append(f"A letra 'A' maiúscula aparece {a_max} vez(es) na string.")
    if not resultado:
        return "A letra 'a' não aparece na string."
    
    return '\n'.join(resultado)

resultado = verificar(txt)
print(resultado)
