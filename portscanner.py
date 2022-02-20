import socket

while True:

    portas = [20, 21, 22, 23, 25, 53, 67, 68, 80, 110, 123, 156, 143, 161, 179, 443, 1723, 1863, 3128, 3389, 8080]
    alvo = input('Digite o URL do alvo: ')
    opt = input('Deseja saber o código de retorno das portas? use sim/nao como resposta. ')

    if opt == 'sim':
         for porta in portas:
             cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
             cliente.settimeout(0.2)
             codigo = cliente.connect_ex((alvo, porta))
             print('porta:', porta, ' codigo:', codigo)

    if opt == 'nao':
        for porta in portas:
            cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cliente.settimeout(0.2)
            codigo = cliente.connect_ex((alvo, porta))
            if codigo == 0:
                print('porta:', porta, ' OPEN')
            else:
                print('porta:', porta, ' CLOSED')

    else:
        continue;
    