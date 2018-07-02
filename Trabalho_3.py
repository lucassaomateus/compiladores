import numpy as np

class tac:

    def __init__(res, arg1, op, arg2):
        self.res = res
        self.arg1 = arg1
        self.op = op
        self.arg2 = arg2

    def print_tac(self):
        return self.res + self.arg1 + self.op + self.arg2

def print_inst_tac(arquivo, tac):
    arquivo.write(print_tac(tac))

'''
 Esse trecho de código acima corresponde as funções do arquivo lista.h
disponibilizado pelo professor, a ideia e usar uma lista de classes, sendo
assim desnecessário implementar algumas funções que estão la naquele arquivo
'''

class entry_t:

    def __init__(name, type, size, desloc, extra):
        self.name = name
        self.type = type
        self.size = size
        self.desloc = desloc
        self.extra = extra

    def print_entry(self):
        return self.name + str(self.type) + str(self.size) + str(self.desloc) + str(self.extra)

def hash(name):
    '''
    Perguntar ao professor se eu preciso usar aquela função hash dos arquivos
    disponibilizados, ou se posso usar uma tipo md5
    '''

def init_table():
    lista_tabela = np.zeros(221)
    return lista_tabela

def lookup_table(lista_tabela, name):
    return lista_tabela.where(lista_tabela.name = name)

def insert_table(lista_tabela, entrada):
    #Avisar professor que tem erro no codigo original nessa parte
    indice = hash(entrada.nome)
    if lista_tabela[indice] is not None:
        return False
    else:
        lista.tabela[indice] = entrada
        '''
        não vou trabalhar com sublistas, porque com o numpy eu posso colocar
        vários elementos em um índice e depois quebrar eles
        '''
        return True

def print_table(lista_tabela, arquivo):
    for name in lista_tabela.name

def free_table(lista_tabela):
    aux_lista_tabela = np.zeros(len(lista_tabela))
    del lista_tabela
    return aux_lista_tabela
