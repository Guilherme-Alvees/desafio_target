luminarias = {
    'Lâmpada 1': False,  
    'Lâmpada 2': False,  
    'Lâmpada 3': False   
}

print("Ligando o Interruptor 1...")
luminarias['Lâmpada 1'] = True  

print("Esperando 10 minutos...")

print("Desligando o Interruptor 1...")
luminarias['Lâmpada 1'] = False  

print("Ligando o Interruptor 2...")
luminarias['Lâmpada 2'] = True  

print("Indo até a sala das lâmpadas...")

for lampada, estado in luminarias.items():
    if estado:
        print(f"{lampada} está ACESA (Controlada pelo Interruptor 2)")
    else:
        print(f"{lampada} está APAGADA (Pode ser controlada pelo Interruptor 1 ou 3)")

print("\nConclusões:")
print("Interruptor 1 controla a lâmpada que estava quente.")
print("Interruptor 2 controla a lâmpada que está acesa.")
print("Interruptor 3 controla a lâmpada que está fria.")

