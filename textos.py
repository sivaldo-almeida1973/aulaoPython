

# faturamento = 1000
# custo = 700

# lucro = faturamento - custo

# print('Faturamento: ' , faturamento)
# print('Custo: ' , custo)
# print('Lucro: ' , lucro)

# # print(f'O faturamento foi R$: {faturamento} o Custo R$:{ custo} e o lucro R$: {lucro}')


# # email = 'E-mail_falso@sivaldo.com'
# email = 'sivaldo@gmail.com'

# #deixar tudo minuscula
# print(email.lower())

# #cahar a posicao(indice) do elemento indicado
# print(email.find('@'))


# posicao = email.find('@')
# servidor = email[posicao:]

# print(servidor)
# nome_email = email[:posicao]
# print(nome_email)

# #tamanho de texto
# tamanho = len(email)
# print(tamanho)

# #trocar parte do elemento
# email_trocado = email.replace('sivaldo', 'lucas')
# print(email_trocado)

# nome = 'sivaldo vieira almeida'
# #primeira letra maiuscula do primeiro nome
# print(nome.capitalize())

#primeira letra de cada palavra nomes
# print(nome.title())



# margem_lucro = lucro / faturamento

#formatar numeros
# print(f'O faturamento: R$:{faturamento:.2f}')
# print(f'O custo: R$:{custo:.2f}')
# print(f'O Lucro: R$:{lucro:.2f}')

# print(f'O faturamneto R${faturamento:.2f}\n o Custo R$ {custo:.2f}\n o lucro R$:{lucro:.2f}')

# print(f'A matgem: R${margem_lucro:.1%}')


nome = 'sivaldo vieira'
email = 'email_falso@gmail.com'

#descobrir o servidor
posicao = email.find('@')
print(posicao)
servidor = email[posicao:]
print(servidor)

#pegar o primeiro nome
posicao = nome.find(' ')

primeiro_nome = nome[:posicao]
print(primeiro_nome)


#mensagem 
mensagem = f'Usuario {primeiro_nome} cadastrado com sucesso com o email:{email}'
print(mensagem)


#enviar uma mensagem tipo a***email.com
primeira_letra = email[0]
mensagem2 = f'Enviamos um link de confirmacao para o email {primeira_letra}*** {servidor}'
print(mensagem2)