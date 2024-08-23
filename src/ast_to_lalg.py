from src.parser import (
    Exps,
    Exp,
    Vec,
    Matrix,
    Int,
    Var,
    Sum,
    Minus,
    Product,
    Elements,
    Element,
    Vectors,
    )

from src.utils import get_vector_elements, get_matrix_elements

"""Module consists of the conversion between the AST generated by the parser in `parser.py` into an intermediate language `lalg` that makes loops explicit.

Example usage:

       >>> ast = parser.parse('[3 4 5 6] * [2 3 4 5]')
       >>> ast_to_lalg(ast)
"""

def ast_to_lalg(ast):
    match ast:
        case Exp(exp):
            match exp:
                case Sum(Vec(elements), Vec(elements2)):
                    vec = ast_to_lalg(Exp(Vec(elements)))
                    vec2 = ast_to_lalg(Exp(Vec(elements2)))

                    n = LalgInt(len(vec))
                    i = LalgInt(0)

                    vec_node = LalgVec(vec)
                    vec2_ode = LalgVec(vec2)

                    op = LalgOp('+')
                    
                    exps = LalgExps([vec_node, vec_node])
                    return LalgForLoop(exps, n, i, op)

                case Minus(Vec(elements), Vec(elements2)):
                    vec = ast_to_lalg(Exp(Vec(elements)))
                    vec2 = ast_to_lalg(Exp(Vec(elements2)))

                    n = LalgInt(len(vec))
                    i = LalgInt(0)

                    vec_node = LalgVec(vec)
                    vec2_ode = LalgVec(vec2)

                    op = LalgOp('-')
                    
                    exps = LalgExps([vec_node, vec_node])
                    
                    return LalgForLoop(exps, n, i, op)

                case Sum(Matrix(elements), Matrix(elements2)):
                    matrix = ast_to_lalg(Exp(Matrix(elements)))
                    matrix2 = ast_to_lalg(Exp(Matrix(elements2)))

                    matrix_node = LalgMatrix(matrix)
                    matrix2_node = LalgMatrix(matrix2)

                    n = LalgInt(len(matrix))

                    inner_n = LalgInt(len(matrix[0]))
 
                    op = LalgOp('+')

                    i = LalgInt(0)
                    j = LalgInt(0)

                    exps = LalgExps([matrix_node, matrix2_node])
                    return LalgForLoop2D(exps, n, inner_n, i, j, op)

                case Minus(Matrix(elements), Matrix(elements2)):
                    matrix = ast_to_lalg(Exp(Matrix(elements)))
                    matrix2 = ast_to_lalg(Exp(Matrix(elements2)))

                    matrix_node = LalgMatrix(matrix)
                    matrix2_node = LalgMatrix(matrix2)

                    n = LalgInt(len(matrix))

                    inner_n = LalgInt(len(matrix[0]))
 
                    op = LalgOp('-')

                    i = LalgInt(0)
                    j = LalgInt(0)

                    exps = LalgExps([matrix_node, matrix2_node])
                    return LalgForLoop2D(exps, n, inner_n, i, j, op)

                case Vec(elements):
                    return get_vector_elements(elements)

                case Matrix(elements):
                    return get_matrix_elements(elements)

                case _:
                    raise ValueError("{} is not an Exp.".format(exp))
        case _:
            raise ValueError("{} is not valid AST.".format(ast))

class LalgInt:
    __match_args__  = ('num',)

    def __init__(self, num):
        self.num = num

    def __repr__(self):
        return f'(LalgInt {self.num})'

class LalgVec:
    __match_args__  = ('vec',)

    def __init__(self, vec):
        self.vec = vec

    def __repr__(self):
        return f'(LalgVec{self.vec})'


class LalgMatrix:
    __match_args__  = ('matrix',)

    def __init__(self, matrix):
        self.matrix = matrix

    def __repr__(self):
        return f'(LalgMatrix {self.matrix})'


class LalgOp:
    __match_args__  = ('op',)

    def __init__(self, op):
        self.op= op

    def __repr__(self):
        return f'(LalgOp {self.op})'

class LalgExps:
    __match_args__  = ('exps',)

    def __init__(self, exps):
        self.exps = exps

    def __repr__(self):
        return f'(LalgExps {self.exps})'

class LalgForLoop2D:
    __match_args__  = ('exps', 'n', 'inner_n', 'i', 'j', 'op')

    def __init__(self, exps, n, inner_n, i, j, op):
        self.exps = exps
        self.n = n
        self.inner_n = inner_n
        self.i = i
        self.j = j
        self.op = op

    def __repr__(self):
        return f'(LalgForLoop2D (exps: {self.exps}) (n: {self.n}) (inner_n: {self.inner_n}) (i: {self.i}) (j: {self.j}) (op:{self.op}))'

class LalgForLoop:
    __match_args__  = ('exps', 'n', 'i', 'op')

    def __init__(self, exps, n, i, op):
        self.exps = exps
        self.n = n
        self.i = i
        self.op = op

    def __repr__(self):
        return f'(LalgForLoop (exps: {self.exps}) (n: {self.n}) (i: {self.i}) (op:{self.op}))'

