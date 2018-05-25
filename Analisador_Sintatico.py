import ply.yacc as yacc
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

def p_operacoes_aritmeticas(p):

    '''
    expressao : declaracao ID atrib ID numero

    atrib : t_OP_ATRIB
          | empty

    declaracao : KW_INT
               | KW_FLOAT

    numero : INT_NUMBER
           | FLOAT_NUMBER
           | ID

    op : t_OP_ADD
       | t_OP_SUB
       | t_OP_DIV
       | t_OP_MUL

    exp : numero
        | numero op exp
        | empty
    '''

    if p[2] == 't_OP_ADD':
        p[0] = p[1] + p[3]
    elif p[2] == 't_OP_SUB':
        p[0] = p[1] - p[3]
    elif p[2] == 't_OP_MUL':
        p[0] = p[1] * p[3]
    elif p[2] == 't_OP_DIV':
        p[0] = p[1] / p[3]

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()

with open("Teste.txt", "r") as arquivo:
    for line in arquivo:
        result = parser.parse(line)

print(result)
