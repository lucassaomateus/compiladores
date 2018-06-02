# encoding=UTF-8
import codecs
from ply import lex
import re
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

reserved = {
    'fim'                   : 'EOF',
    'se'                    : 'KW_IF',
    'senao'                 : 'KW_ELSE',
    'para'                  : 'KW_FOR',
    'enquanto'              : 'KW_WHILE',
    'faca'                  : 'FACA'
    'em'                    : 'EM'
    'int'                   : 'KW_INT',
    'real'                  : 'KW_FLOAT',
    'texto'                 : 'KW_STRING',
    'mostra'                : 'KW_PRINT',
    'leia'                  : 'KW_INPUT',
    'verdadeiro'            : 'TRUE',
    'falso'                 : 'FALSE',
    'mais'                  : 'OP_ADD',
    'menos'                 : 'OP_SUB',
    'vezes'                 : 'OP_MUL',
    'dividido_por'          : 'OP_DIV',
    'maismais'              : 'OP_INC',
    'decrementa'            : 'OP_DEC',
    'na'                    : 'OP_EXP',
    'e'                     : 'OP_LOG_AND',
    'ou'                    : 'OP_LOG_OR',
    'igual_a'               : 'OP_LOG_EQUAL',
    'diferente'             : 'OP_LOG_DIFF',
    'nao'                   : 'OP_LOG_NOT',
    'menor_que'             : 'OP_LOG_LT',
    'menor_igual'           : 'OP_LOG_LT_E',
    'maior_que'             : 'OP_LOG_BT',
    'maior_igual'           : 'OP_LOG_BT_E',
    'como'                  : 'KW_FUNC_OPEN',
    'deu'                   : 'KW_FUNC_CLOSE',
    'entao'                 : 'KW_IF_OPEN',
    'deu'                   : 'KW_CLOSE',
    'fecha'                 : 'KW_FOR_CLOSE',
    'define'                : 'KW_FUNCTION',
    'com'                   : 'KW_FUNC_OPEN_ARGS',
    'eh'                    : 'OP_ATRIB',
    'agora_argumentos'      : 'PAR_OPEN',
    'deu_de_argumentos'     : 'PAR_CLOSE',
    ','                     : 'KW_FUNC_ARGS_SEP',
    ';'                     : 'KW_END_LINE'
}

tokens = [
    'OP_ADD',
    'OP_SUB',
    'OP_MUL',
    'OP_DIV',
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

t_ignore  = ' \t|\n';   #pula linhas e espaços do codigo fonte

#tokens de numero float,
def t_FLOAT_NUMBER(t):

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
def t_INT_NUMBER(t): # \d quer dizer que pode ser qual quer digito

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

def t_error(t):

    print ('Caractere ilegal : {} '.format(t.value[0]))
    t.lexer.skip(1)

def t_COMMENT(t):

    r' \#.*'
    pass

lexer = lex.lex()

arq = codecs.open('Teste.txt', 'r', encoding='utf-8')
texto = arq.read().encode('utf-8')
lexer.input(texto)

while True :
    token = lexer.token()
    if not token:
        break
    print (token)
arq.close()
