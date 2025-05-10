usuario_bd = 'User123'
senha_bd = 'Senha123'

usuario = str(input('Usuário: '))
senha = str(input('Senha: '))

if usuario == usuario_bd and senha == senha_bd:
    print('Usuário e senha corretos. Seguindo para o login.')
else:
    print('Usuário ou senha incorretos.')