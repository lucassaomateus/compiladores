from ply import yacc
from Analisador_Lexico import tokens

class BinOp:
    def __init__(self, op, left, right):
        self.type = 'bin_op'
        self.left = left
        self.right = right
        self.op = op

    def __str__(self):
        return '({} {} {})'.format(self.left, self.op, self.right)

class Node:
    def __init__(self, type, children=None, leaf=None):
        self.type = type
        if children:
            if not isinstance(children, (list, tuple)):
                children = [children]
            self.children = children
        else:
            self.children = []
        self.leaf = leaf

    def _pretty(self, prefix='| '):
        string = []
        if self.leaf:
            root += ' ({})'.format(self.leaf)
            root = '{}'.format(str(self.type))
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
    ('left','t_OP_ADD','t_OP_SUB'),
    ('left','t_OP_MUL','t_OP_DIV')
)


def p_programa (p):
	'''expressao : EOF
	             | programa
	 '''


def p_statement_list(p):
    '''expressao     : empty
                     | statement
                     | statement_list ignore
                     | statement_list ignore statement
                     | statement_list
                     | statement_list  statement
    '''


def p_statement (p):
	'''statement	: expressao
		            | KW_STRING
		            | Return PAR_OPEN return_expression PAR_CLOSE
		            | KW_FOR_OPEN PAR_OPEN expressao relational_expression expressao PAR_CLOSE KW_FOR_CLOSE statement
		            | KW_IF PAR_OPEN relational_expression PAR_CLOSE statement
		            | KW_WHILE PAR_OPEN relational_expression PAR_CLOSE statement
'''


def p_function(p) :
    '''expressao : KW_FUNCTION VAR PAR_OPEN opt_parameter_list PAR_CLOSE ignore opt_auto_define_list statement_list

    '''


def p_opt_parameter_list(p):
    '''expressao : parameter_list
    '''


def p_parameter_list(p):
    '''expressao : return_expresao
                 | define_list KW_FUNC_ARGS_SEP VAR
    '''


def p_opt_auto_define_list(p) :
    '''expressao : define_list ignore
                 | define_list
    '''


def p_define_list(p):
    '''expressao : term
                 | define_list KW_FUNC_ARGS_SEP term'''
    ''' term     : VAR
                 | KW_FUNC_ARGS_SEP'''


def p_opt_argument_list(p):
    '''expressao : argument_list
    '''

def p_argument_list(p):
    '''expressao : named_expressao
                 | VAR KW_FUNC_ARGS_SEP argument_list
    '''
def p_relational_expression(p) :
    '''expressao : expressao
                 | OP_LOG_EQUAL expressao
                 | OP_LOG_DIFF expressao
                 | OP_LOG_LT expressao
                 | OP_LOG_GE expressao
                 | OP_LOG_GT expressao
                 | OP_LOG_LE expressao
    '''

    if p[2]== OP_LOG_EQUAL :
        p[0]= p[2]



def p_return_expresao(p) :
    '''expressao : VAR
    '''

def p_expresao (p) :
    '''expressao : p_named_expressao
                 | INT_NUMBER
                 | INT_NUMBER expressao
                 | FLOAT_NUMBER expressao
                 | FLOAT_NUMBER
                 | PAR_OPEN expressao PAR_CLOSE
                 | OP_LOG_NOT expressao
                 | expressao OP_ADD expressao
                 | expressao OP_SUB expressao
                 | expressao OP_MUL expressao
                 | expressao OP_LOG_AND expressao
                 | named_expressao OP_INC
                 | named_expressao OP_DEC
                 | named_expressao OP_EXP expressao
                 | PAR_CLOSE

    '''
    if p[1] == INT_NUMBER and p[2]== expressao:
        p[0] = p[1]

def p_named_expressao (p) :
    '''expressao : VAR expressao
                 | factor
    '''
    ''' factor   : VAR
    '''


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()

while True:
    try:
        s = input('calc> ')
    except EOFError:
        break
    if not s:
        continue
    resultado = parser.parse(s)
    print(resultado)
