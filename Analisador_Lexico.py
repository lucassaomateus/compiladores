import sys
from ply import lex

reserved = {
    'fim'                   : 'EOF',
    'se'                    : 'KW_IF',
    'senao'                 : 'KW_ELSE',
    'para'                  : 'KW_FOR_OPEN',
    'enquanto'              : 'KW_WHILE',
    'faca'                  : 'FACA',
    'em'                    : 'EM',
    'retorna'               : 'KW_RETURN',
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
    'ou'                    : 'OP_LOG_OR',
    'igual_a'               : 'OP_LOG_EQUAL',
    'diferente'             : 'OP_LOG_DIFF',
    'nao'                   : 'OP_LOG_NOT',
    'menor_que'             : 'OP_LOG_LT',
    'menor_igual'           : 'OP_LOG_LT_E',
    'maior_que'             : 'OP_LOG_BT',
    'maior_igual'           : 'OP_LOG_BT_E',
    'como'                  : 'KW_FUNC_OPEN',
    'entao'                 : 'KW_IF_OPEN',
    'deu'                   : 'KW_CLOSE',
    'fecha'                 : 'KW_FOR_CLOSE',
    'define'                : 'KW_FUNCTION',
    'com'                   : 'KW_FUNC_OPEN_ARGS',
    'eh'                    : 'OP_ATRIB',
    'agora_argumentos'      : 'PAR_OPEN',
    'deu_de_argumentos'     : 'PAR_CLOSE',
}

tokens = [
    'VIRGULA',
    'OP_LOG_AND',
    'INT_NUMBER',
    'FLOAT_NUMBER',
    'STRING',
    'ERROR',
    'ID',
]+ (list(reserved.values()))

digit = [0-9]
t_VIRGULA = r','
t_OP_LOG_AND = r'e'
t_ignore  = ' \t|\n';   #pula linhas e espaços do codigo fonte

#tokens de tipo float
def t_FLOAT_NUMBER(t):

    r'[0-9]+[\.][0-9]+|[0-9]+[\.][0-9]*'
    t.value = float (t.value)
    return t

#tokens de tipo int
def t_INT_NUMBER(t):

    r'[0-9]+'
    t.value = int (t.value)
    return t

#tokens de variáveis
def t_ID (t):

    r'[a-zA-Z_]+[a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')
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

codigo = open(sys.argv[1]).read()
lexer.input(codigo)

token = lexer.token()
while token:
    print(token)
    token = lexer.token()
