# encoding=UTF-8
import codecs
from ply import lex
import re
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

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
    'naho'        : 't_OP_LOG_NOT',
    'menor_que'  : 't_OP_LOG_LT',
    'menor_igual':'t_OP_LOG_LT_E',
    'maior_que'  : 't_OP_LOG_BT',
    'maior_igual': 't_OP_LOG_BT_E',
    'como'       : 't_KW_FUNC_OPEN',
    'deu'        : 't_KW_FUNC_CLOSE',
    'entao'      : 't_KW_IF_OPEN',
    'deu'        : 't_KW_IF_CLOSE',
    'facha'      : 't_KW_FOR_OPEN',
    'deu'       : 't_KW_FOR_CLOSE',
    'define'    : 't_KW_FUNCTION',
    'com'       : 't_KW_FUNC_OPEN_ARGS',
     'eh'        : 't_OP_ATRIB',
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
    'ERRADO',
    'ID',
]+ (list(reserved.values()))


digit = [0-9]


t_ignore  = ' \t|\n'; #pula linhas e espaços do codigo fonte

#tokens de numero float,
def t_FLOAT_NUMBER(t) :
    r'[0-9]+[\.][0-9]+|[0-9]+[\.][0-9]*' # essa função capta 1.
    #t.type = reserved.get(t.value,'FLOAT_NUMBER')
    t.value = float (t.value)
    return t

#nessa função variaveis que comecem com numeral estão descatadas
#Esse erro será tratado na analise sintatica
def t_ERRADO(t):
    r'[0-9]+[a-zA-Z_]+'
    print ('Caractere ilegal : {} '.format(t.value))
    t.lexer.skip(1)

#nessa função temos os tokens numeral, inteiro
def t_INT_NUMBER(t) : # \d quer dizer que pode ser qual quer digito
    r'[0-9]+'
    #t.type = reserved.get(t.value,'INT_NUMBER')
    t.value = int (t.value) # convertendo o valor em inteiro
    return t

#tokens identificador, variavel
def t_ID (t):
    r'[a-zA-Z_][a-zA-Z_0-9]+'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

#nessa função, é necessário ter "" para que venha se considerada string
#além disso, somente nessa função o space não é desprezado
def t_STRING (t):
    r'\"[a-zA-Z_][a-zA-Z_0-9| \t]*\"'
    t.type = str ('STRING')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t) :
    print ('Caractere ilegal : {} '.format(t.value[0]))
    t.lexer.skip(1)

def t_COMMENT(t):
    r' \#.*'
    pass

lexer = lex.lex()

# testando////////////////////testanto//////////////////////testanto/////////////////////////

arq = codecs.open('/home/lucas/Desktop/2018 /compiladores/programação.txt', 'r', encoding='utf-8')
texto = arq.read().encode('utf-8')
lexer.input(texto)

while True :
    token = lexer.token()
    if not token:
        break
    print (token)
arq.close()
