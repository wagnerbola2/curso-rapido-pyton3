pessoas = ['Eu', 'Voce']
cores = ['branco', 'preto']

for p in pessoas:
    for c in cores:
        print(f'{p} é {c}')


for i in [1,2,3]:
   pass

for i in range(1, 11):
   if i % 2:
      continue
   print(i)

for i in range(1, 11):
    if i == 5:
        break
    print(i)
print('Fim')
