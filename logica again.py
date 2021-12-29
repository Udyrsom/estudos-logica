print("----------------------")
print('ESCOLA SANTA MONICA')
print("----------------------")
alunos = input("quantos alunos tem na turma?: ")
print(alunos)
aluno = 1
print('--------------------------------------------------')
while(aluno <= int(alunos)):
    print("--------------------------")
    print("ALUNO:",aluno)
    nota = input('NOTA:')
    print(nota)
    aluno = aluno + 1
    if int(nota) >= 8:
        print('continue assim')
    else:
        if int(nota) <= 6:
            print('dá para melhorar')
    if int(nota) > 8:
        print('excelente')
    
