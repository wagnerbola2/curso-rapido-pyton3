nota = float(input('Informe a nota do aluno: '))

if nota >= 9:
    print('Parabens!')
    print('Adicionado ao QUadro de Honra')
elif nota >= 7:
    print('Aprovado')
elif nota >= 5.5:
    print('Recuperação')
elif nota >= 3.5:
    print('Recuperação + Trabalho')
else:
    print('Reprovado')
print(nota)
