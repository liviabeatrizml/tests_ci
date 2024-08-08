import logging

def fat(a):
    try:
        aux = 1
        for i in range(1, a+1):
            aux *= i
        return aux
    except AssertionError:
        print("Entrada de dados errada.")
        logging.error("Erro na entrada de dados do usuário.")
    except TypeError:
        print("Falha na solicitação.")
        logging.error("Falha no processamento por valores inválidos.")