from ply import yacc
from Analisador_Lexico import tokens
import sys

class Node:
    def __init__(self, type, children=None, leaf=None, line=None):
        self.type = type
        self.line = line
        if children:
            if not isinstance(children, (list, tuple)):
                children = [children]
            self.children = children
        else:
            self.children = []
        self.leaf = leaf

    def _pretty(self, prefix='| '):
        string = []
        root = '{}'.format(str(self.type))
        if self.leaf is not None:
            root += ' ({})'.format(self.leaf)
        string.append(root)
        for child in self.children:
            if isinstance(child, Node):
                for child_string in child._pretty():
                    string.append('{}{}'.format(prefix, child_string))
            else:
                string.append('{}{}'.format(prefix, child))
        return string

    def pretty(self):
        return '\n'.join(self._pretty())

    def __str__(self):
        children_string = ', '.join([str(c) for c in self.children]) if self.children else ''
        leaf_string = '{} '.format(self.leaf) if self.leaf is not None else ''
        return '({} {}[{}])'.format(self.type, leaf_string, children_string)

precedence = (
    ('left', 'OP_ATRIB'),
    ('left', 'OP_LOG_BT', 'OP_LOG_LT', 'OP_LOG_BT_E', 'OP_LOG_LT_E', 'OP_LOG_DIFF'),
    ('left', 'OP_ADD', 'OP_SUB'),
    ('left','OP_MUL','OP_DIV'),
    ('left','PAR_OPEN', 'PAR_CLOSE'),
    ('left','OP_EXP')
)

def p_programa(p):      #Ponto inicial da derivação do codigo
                        #Deriva em uma lista de declarações
    '''
        programa : lista_declaracoes
    '''

    p[0] = Node('programa', children = p[1], leaf = '')

def p_lista(p):     #Pega a lista de declarações, e vai abrindo em uma ou mais declarações

    '''
    lista_declaracoes : declaracao lista_declaracoes
                      | declaracao
    '''

    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = Node('lista_declaracoes', children = [p[1],p[2]], leaf = ' ')

def p_declaracao(p):    #Transforma as declarações nos tipos de funções da nossa linguagem
                        #Exemplo: for, if, while
    '''
    declaracao : expressao KW_END_LINE
               | declaracao KW_END_LINE
               | declaracao_if KW_END_LINE
               | declaracao_for KW_END_LINE
               | declaracao_while KW_END_LINE
               | declaracao_print
               | declaracao_ler KW_END_LINE
               | atribuicao KW_END_LINE
               | declaracao_variavel_sem_valores KW_END_LINE
               | expressao_booleana KW_END_LINE
               | declaracao_funcao KW_END_LINE
               | retorna KW_END_LINE
    '''

    p[0] = p[1]

def p_operacoes_binarias(p):

    '''
    expressao : expressao OP_ADD expressao
              | expressao OP_SUB expressao
              | expressao OP_MUL expressao
              | expressao OP_DIV expressao
              | expressao OP_EXP expressao
              | OP_INC ID
              | OP_DEC ID
              | KW_INT
              | KW_FLOAT
              | KW_STRING
              | boolean
              | expressao_booleana
              | ID
    '''

    if p.slice[1].type == 'ID':
        p[0] = Node('valor', children = p[1], leaf = 'id', line = p.lineno(1))
    elif p.slice[1].type == 'expressao_booleana':
        p[0] = Node('value', children = p[1], leaf = 'exp_bool', line = p.lineno(1))
    elif p.slice[1].type == 'KW_INT':
        p[0] = Node('valor', children = p[1], leaf = 'int', line = p.lineno(1))
    elif p.slice[1].type == 'KW_FLOAT':
        p[0] = Node('valor', children = p[1], leaf = 'float', line = p.lineno(1))
    elif p.slice[1].type == 'KW_STRING':
        p[0] = Node('valor', children = p[1], leaf = 'string', line = p.lineno(1))
    elif p.slice[1].type == 'OP_INC':
        p[0] = Node('valor', children = p[2], leaf = '++', line = p.lineno(2))
    elif p.slice[1].type == 'OP_DEC':
        p[0] = Node('valor', children = p[2], leaf = '--', line = p.lineno(2))
    elif p.slice[1].type == 'boolean':
        p[0] = Node('value', children=p[1], leaf='boolean', line=p.lineno(1))
    elif p.slice[1].type == 'expressao':
        p[0] = Node('operacao_binaria', children = [p[1], p[3]], leaf = p[2], line = p.lineno(2))

def p_expressao_booleana(p):

    #menor_que = OP_LOG_LT
    #menor_igual = OP_LOG_LT_E
    #maior_que = OP_LOG_BT
    #maior_igual = OP_LOG_BT_E

    '''
    expressao_booleana : expressao OP_LOG_BT_E expressao
                       | expressao OP_LOG_LT_E expressao
                       | expressao OP_LOG_EQUAL expressao
                       | expressao OP_LOG_DIFF expressao
                       | expressao OP_LOG_LT expressao
                       | expressao OP_LOG_BT expressao
                       | expressao OP_LOG_OR expressao
    '''

    if p.slice[2].type == 'OP_LOG_BT_E':
        p[0] = Node('exp_boolean', children = [p[1],p[3]], leaf = 'maior ou igual a', line = p.lineno(1))
    elif p.slice[2].type == 'OP_LOG_LT_E':
        p[0] = Node('exp_boolean', children = [p[1],p[3]], leaf = 'menor ou igual a', line = p.lineno(1))
    elif p.slice[2].type == 'OP_LOG_EQUAL':
        p[0] = Node('exp_boolean', children = [p[1],p[3]], leaf = 'igual a', line = p.lineno(1))
    elif p.slice[2].type == 'OP_LOG_DIFF':
        p[0] = Node('exp_boolean', children = [p[1],p[3]], leaf = 'diferente de', line = p.lineno(1))
    elif p.slice[2].type == 'OP_LOG_LT':
        p[0] = Node('exp_boolean', children = [p[1],p[3]], leaf = 'menor que', line = p.lineno(1))
    elif p.slice[2].type == 'OP_LOG_BT':
        p[0] = Node('exp_boolean', children = [p[1],p[3]], leaf = 'maior que', line = p.lineno(1))
    elif p.slice[2].type == 'OP_LOG_OR':
        p[0] = Node('boolean_exp', children=[p[1],p[3]], leaf='ou',line=p.lineno(1))

def p_boolean(p):

    '''
    boolean : TRUE
            | FALSE
    '''

    p[0] = p[1]

def p_atribuicao(p):

    '''
    atribuicao : ID OP_ATRIB expressao
               | atribuicao VIRGULA atribuicao
    '''

    if p.slice[1].type == 'ID':
        p[0] = Node('atribuicao', children = [p[1], p[3]], leaf = '=',line = p.lineno(1))
    else:
        p[0] = Node('atribuicao', children = [p[1], p[3]], leaf = ',', line = p.lineno(1))

def p_declaracao_sem_valores(p):

    '''
    declaracao_variavel_sem_valores : tipo ID
    '''

    p[0] = Node('declaracao_sem_valor', children = p[2], leaf = p[1], line = p.lineno(2))

def p_criacao_variavel(p):

    '''
    criacao_variavel : tipo ID OP_ATRIB expressao
    '''

    p[0] = Node('declaracao', children = [p[2],p[4]], leaf = p[1], line = p.lineno(2))

def p_criacao_variaveis(p):

    '''
    criacao_variaveis : tipo ID OP_ATRIB expressao VIRGULA atribuicao
    '''

    p[0] = Node('declaracao', children = [p[2],p[4],p[6]], leaf = p[1], line = p.lineno(2))

def p_parenteses(p):

    '''
    expressao : PAR_OPEN expressao PAR_CLOSE
    '''

    p[0] = p[2]

def p_tipos(p):

    '''
    tipo : KW_INT
         | KW_BOOLEAN
         | KW_FLOAT
         | KW_STRING

    '''

    p[0] = p[1]

def p_if(p):

    '''
    declaracao_if : KW_IF expressao_booleana KW_IF_OPEN lista_declaracoes KW_CLOSE
    '''

    p[0] = Node('declaracao_if', children = [p[2],p[4]], leaf = 'if', line = p.lineno(1))

def p_if_else(p):

    '''
    declaracao_if : KW_IF expressao_booleana KW_IF_OPEN lista_declaracoes KW_ELSE lista_declaracoes KW_CLOSE
    '''

    p[0] = Node('if_statement', children=[p[2], p[4], p[7]], leaf='if/else', line = p.lineno(1))

def p_printa(p):

    '''
    declaracao_print : KW_PRINT parametros KW_END_LINE
    '''

    p[0] = Node('print', children = p[2], leaf = p[1], line = p.lineno(1))

def p_ler(p):

    '''
    declaracao_ler : KW_INPUT ID
    '''

    p[0] = Node('read', children = p[2], leaf = p[1], line = p.lineno(1))

def p_for(p):

    '''
    declaracao_for : KW_FOR_OPEN ID EM expressao FACA lista_declaracoes KW_CLOSE
    '''

    p[0] = Node('for', children = [p[2],p[4],p[6]], leaf = 'for', line = p.lineno(2))

def p_while(p):

    '''
    declaracao_while : KW_WHILE expressao_booleana FACA lista_declaracoes KW_CLOSE
    '''

    p[0] = Node('while', children = [p[2],p[4]], leaf = 'while', line = p.lineno(1))

def p_funcao(p):

    '''
    declaracao_funcao : KW_FUNCTION ID KW_FUNC_OPEN lista_declaracoes KW_CLOSE
    '''

    p[0] = Node('declaracao_funcao', children = p[4],leaf = p[2], line = p.lineno(1))

def p_funcao_argumentos(p):

    '''
    declaracao_funcao : KW_FUNCTION ID KW_FUNC_OPEN_ARGS lista_declaracoes KW_CLOSE
    '''

    p[0] = Node('declaracao_funcao', children = [p[4],p[6]], leaf = p[2], line = p.lineno(1))

def p_function_call(p):

    '''
    expressao : ID KW_FUNC_OPEN_ARGS parametros
    '''

    p[0] = Node('chamada_funcao', children = p[3], leaf = p[1], line = p.lineno(1))

def p_return(p):

    '''
    retorna : KW_RETURN expressao
    '''

    p[0] = Node('return', children = p[2], leaf = p[1], line = p.lineno(1))

def p_parametros(p):

    '''
    parametros : expressao
               | parametros VIRGULA parametros
    '''

    if len(p) == 2:
        p[0] = Node('parametro', children = p[1], leaf ='parametros')
    else:
        p[0] = Node('parametros', children = [p[1], p[3]], leaf='parametros')

#Se passou por todas as regras e não casou com nenhuma, então está errado
def p_error(p):
    print("Erro de sintaxe!")

parser = yacc.yacc()

codigo = open(sys.argv[1]).read()
ast = parser.parse(codigo)
print(ast.pretty())
