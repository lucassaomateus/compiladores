#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ply import lex
import re
import sys

reserved = {
    'se'        : 'KW_IF',
    'senao'     : 'KW_ELSE',
    'para'      : 'KW_FOR',
    'enquanto'  : 'KW_WHILE',
    'int'       : 'KW_INT',
    'real'      : 'KW_FLOAT',
    'texto'     : 'KW_STRING',
    'mostra'    : 'KW_PRINT',
    'leia'      : 'KW_INPUT',
    'verdadeiro': 'TRUE',
    'falso'     : 'FALSE',
    'mais'      : 't_OP_ADD',
    'menos'     : 't_OP_SUB',
    'vezes'     : 't_OP_MUL',
    'dividido_por'  : 't_OP_DIV',
    'maismais'   : 't_OP_INC',
    'decrementa' : 't_OP_DEC',
    'na'         : 't_OP_EXP',
    'e'          : 't_OP_LOG_AND',
    'ou'         : 't_OP_LOG_OR',
    'igual_a'    : 't_OP_LOG_EQUAL',
    'diferente'  : 't_OP_LOG_DIFF',
    'não'        : 't_OP_LOG_NOT',
    'menor_que'  : 't_OP_LOG_LT',
    'menor_igual':'t_OP_LOG_LT_E',
    'maior_que'  : 't_OP_LOG_BT',
    'maior_igual': 't_OP_LOG_BT_E',
    'como'       : 't_KW_FUNC_OPEN',
    'deu'        : 't_KW_FUNC_CLOSE',
    'então'      : 't_KW_IF_OPEN',
    'deu'        : 't_KW_IF_CLOSE',
    'faça'      : 't_KW_FOR_OPEN',
    'deu'       : 't_KW_FOR_CLOSE',
    'define'    : 't_KW_FUNCTION',
    'com'       : 't_KW_FUNC_OPEN_ARGS',
     'é'        : 't_OP_ATRIB',
     'agora_argumentos' : 't_PAR_OPEN',
     'deu_de_argumentos': 't_PAR_CLOSE',
     ','        : 't_KW_FUNC_ARGS_SEP',
     '.'        : 't_KW_FPUNC',

}



tokens = [
    'OP_ADD',
    'OP_SUB',
    'OP_MUL',
    'OP_DIV1',
    'OP_INC',
    'OP_DEC',
    'OP_EXP',
    'PAR_OPEN',
    'PAR_CLOSE',
    'OP_ATRIB',
    'IDENTIFIER',
    'INT_NUMBER',
    'FLOAT_NUMBER',
    'STRING',
    'OP_LOG_AND',
    'OP_LOG_OR',
    'OP_LOG_EQUAL',
    'OP_LOG_DIFF',
    'OP_LOG_NOT',
    'OP_LOG_LT',
    'OP_LOG_LT_E',
    'OP_LOG_BT',
    'OP_LOG_BT_E'
    'KW_FUNC_OPEN',
    'KW_FUNC_CLOSE',
    'KW_IF_OPEN',
    'KW_IF_CLOSE',
    'KW_FOR_OPEN',
    'KW_FOR_CLOSE',
    'KW_FUNCTION',
    'KW_FUNC_OPEN_ARGS',
    'KW_FUNC_ARGS_SEP',
    'KW_FPUNC',
    'ID',
]+ (list(reserved.values()))

t_ignore  = ' \t|\n'; #pula linhas e espaços do codigo fonte


def t_FLOAT_NUMBER(t) :
    r'\d+(\.)\d+'
    digito = '0,1,2,3,4,5,6,7,8,9'
    for x in digito:
        if t != x:
            t.value = float(t.value)
            return t

def t_INT_NUMBER(t) : # \d quer dizer que pode ser qual quer digito
    r'[0-9]+'
    t.value = int (t.value)
    return t

def t_ID (t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'STRING')    # Check for reserved words
    return t

def t_STRING (t):
    r'"[a-zA-Z_][a-zA-Z_0-9]*"'
    t.type = str ('STRING')
    return t

def t_error(t) :
    print ('Caractere ilegal : {} '.format(t.value[0]))
    t.lexer.skip(1)

def t_COMMENT(t):
    r'\#.*'
    pass


lexer = lex.lex()

# testando////////////////////testanto//////////////////////testanto/////////////////////////

arq = open('/home/lucas/Desktop/2018 /compiladores/programação.txt', 'r')
texto = arq.read()
lexer.input(texto)

while True :
    token = lexer.token()
    if not token:
        break
    print (token)
arq.close()
