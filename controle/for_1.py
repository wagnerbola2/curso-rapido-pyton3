

for i in range(10):
    print(i)

for i in range(1, 11):
  print(i)

for i in range(1, 100, 7):
    print(i)

for i in range(20, 0, -3):
    print(i)

nums = [2,4,6,8]

for n in nums:
    print(n, end=', ')

texto = 'zzz'

for l in texto:
    print(l, end='Z')

for i in {1, 2, 3, 4, 5, 5, 5, 5}:
    print(i, end=' ')

produto = {
    'nome': 'Faca',
    'preco': 500.00,
    'desconto': 0.25 
}

for p in produto:
    print(p, produto[p])

for p, v in produto.items():
    print(p, v)

for v in produto.values():
    print(v, end=' ')

