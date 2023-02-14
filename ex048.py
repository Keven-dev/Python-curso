c_mult = 0
for c in range(1, 500):
    if c % 3 == 0:
        c_mult += 1
        print(c)
        
print(f'No intervalo de 1 a 500 existem {c_mult} números multiplos de três')        


