m1 = [[9834, 2038,2321,31,44,341,143],
      [235,523,532,532,532,234,2354],
      [7341,41,421,21,1331,32,234]]
pares = int(0)
for linha in m1:
    for valor in linha:
        if (valor % 2 == 0):
            pares += 1
        
print(pares)