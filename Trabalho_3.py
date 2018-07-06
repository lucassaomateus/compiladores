import numpy as np


class tac:

    def __init__(self, res, arg1, op, arg2):
        self.res = str(res)
        self.arg1 = str(arg1)
        self.op = str(op)
        self.arg2 = str(arg2)

    def print_tac(self, arquivo):
        print (self.res + " " + self.arg1 + " " + self.op + " " + self.arg2 + " " + "\n")
        arquivo.write(self.res + " " + self.arg1 + " " + self.op + " " + self.arg2 + " " + "\n")

'''
 Esse trecho de código acima corresponde as funções do arquivo lista.h
disponibilizado pelo professor, a ideia e usar uma lista de classes, sendo
assim desnecessário implementar algumas funções que estão la naquele arquivo
'''

class entry_t:

    def __init__(self, name, type, size, desloc):
        self.name = name
        self.type = type
        self.size = size
        self.desloc = desloc

    def print_entry(self):
        return self.name + str(self.type) + str(self.size) + str(self.desloc) + str(self.extra)

    def print_declaracao(self, arquivo):
        print (self.name + " " + self.type + " " + self.size + " " + self.desloc + " " + "\n")
        arquivo.write(self.name + " " + self.type + " " + self.size + " " + "\n")

def hash_221(name):
    result = hash(name) % 221
    print (result)
    return result

def init_table():
    lista_tabela = np.zeros(221)
    return lista_tabela

def lookup_table(lista_tabela, name):
    return lista_tabela.where(name)

def insert_table(lista_tabela, entrada):
    indice = hash_221(entrada.res)
    if lista_tabela[indice] is not None:
        return False
    else:
        lista.tabela[indice] = entrada
        '''
        não vou trabalhar com sublistas, porque com o numpy eu posso colocar
        vários elementos em um índice e depois quebrar eles
        '''
        return True

#def print_table(lista_tabela, arquivo):
    #for name in lista_tabela.name

def free_table(lista_tabela):
    aux_lista_tabela = np.zeros(len(lista_tabela))
    del lista_tabela
    return aux_lista_tabela
