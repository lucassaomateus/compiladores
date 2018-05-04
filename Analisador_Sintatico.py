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

def p_soma(p):
    'expressao  : expressao t_OP_ADD termo'
    p[0] = p[1] + p[3]

def p_subtracao(p):
    'expressao  : expressao t_OP_SUB termo'
    p[0] = p[1] - p[3]

def p_multiplicacao(p):
    'expressao  : expressao t_OP_MUL termo'
    p[0] = p[1] * p[3]

def p_divisao(p):
    'expressao  : expressao t_OP_DIV termo'
    p[0] = p[1] / p[3]

def p_atribuicao(p):
    'expressao  : termo'
    p[0] = p[1]

def p_termo(p):
    '''termo  : KW_FLOAT
              | KW_INT
              | t_PAR_OPEN expressao t_PAR_CLOSE
    '''

def p_error(p):
    print("Syntax error in input!")

#arvore = Node(p)
#arvore._pretty()
parser = yacc.yacc()

with open("Teste.txt", "r") as arquivo:
    for line in arquivo:
        result = parser.parse(line)

print(result)
