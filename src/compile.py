from src.parser import parser
from src.ast_to_lalg import ast_to_lalg
from src.lalg_to_c import lalg_to_c

def compile_exp(lalg_exp):
    return lalg_to_c(ast_to_lalg(parser.parse(lalg_exp)))

def create_c_file(exp, file_name):
    c_code = compile_exp(exp)
    with open(file_name, "w") as f:
        f.write(c_code)
        
