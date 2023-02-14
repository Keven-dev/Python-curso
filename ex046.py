from time import sleep

print('===== CONTAGEM REGRESSIVA =====')
for c in range(10, -1, -1):
    sleep(1)
    print(c)
print('\033[1;30;43mFELIZ ANO NOVO!\033[m')