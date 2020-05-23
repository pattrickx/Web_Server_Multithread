import os


def process_post(file_path, message, command=''):
    if command == 'clr':
        with open(file_path, 'w') as f:
            pass
        return
    dados = read_file(file_path)
    structured = message.split('&')
    for data in structured:
        chave, valor = data.split('=')
        dados[chave] = valor
    save_file(file_path, dados)
    return


def read_file(file_path):
    dados = {}
    if not os.path.exists(file_path):
        return dados
    else:
        with open(file_path, 'r') as f:
            for line in f.readlines():
                chave, valor = line.split('=')
                dados[chave] = valor
        return dados


def save_file(file_path, dados):
    with open(file_path, 'w') as f:
        for key in dados.keys():
            f.write(key + '=' + dados[key] + '\n')
    return True
