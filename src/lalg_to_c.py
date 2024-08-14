from src.ast_to_lalg import (
    LalgInt,
    LalgVec,
    LalgOp,
    LalgExps,
    LalgForLoop,
    LalgForLoop2D,
    LalgMatrix,
)

def lalg_to_c(lalg_ast):
    match lalg_ast:
        case LalgForLoop(LalgExps(exps), LalgInt(n), LalgInt(i), LalgOp(op)):
            if all(isinstance(x, LalgVec) for x in exps):
                vec = exps[0].vec
                vec2 = exps[1].vec
                
                c_vec = allocate_vector("v1", vec, n, 1)
                c_vec2 = allocate_vector("v2", vec2, n, 2)
                
                loop = f"""    for (int i = 0; i < {n}; i++) {{
        result->data[i] = v1->data[i] {op} v2->data[i];
    }}"""

                c_code = f"""#include <stdio.h>
#include <stdlib.h>

typedef struct {{
    int length;
    int *data;
}} vector;

vector* allocate_vector(int n) {{
    vector *v = calloc(1, sizeof(*v));
    v->length = n;
    v->data = calloc(n, sizeof(*v->data));
    return v;
}}

vector* compute_vector(vector *v1, vector *v2) {{
    vector *result = allocate_vector(v1->length);
{loop}
    return result;
}}

int main() {{
    {c_vec}
    {c_vec2}

    vector *result = compute_vector(v1, v2);

    printf("Result: ");
    for (int i = 0; i < result->length; i++) {{
        printf("%d ", result->data[i]);
    }}
    printf("\\n");

    free(v1->data);
    free(v1);
    free(v2->data);
    free(v2);
    free(result->data);
    free(result);

    return 0;
}}
"""
                return c_code

        case LalgForLoop2D(LalgExps(exps), LalgInt(n), LalgInt(inner_n), LalgInt(i), LalgInt(j), LalgOp(op)):
            if all(isinstance(x, LalgMatrix) for x in exps):
                mat1 = exps[0].matrix
                mat2 = exps[1].matrix
                
                c_mat1 = allocate_matrix("m1", mat1, n, inner_n, 1)
                c_mat2 = allocate_matrix("m2", mat2, n, inner_n, 2)
                
                loop = f"""    for (int i = 0; i < {n}; i++) {{
        for (int j = 0; j < {inner_n}; j++) {{
            result->data[i][j] = m1->data[i][j] {op} m2->data[i][j];
        }}
    }}"""

                c_code = f"""#include <stdio.h>
#include <stdlib.h>

typedef struct {{
    int rows;
    int cols;
    int **data;
}} matrix;

matrix* allocate_matrix(int rows, int cols) {{
    matrix *m = calloc(1, sizeof(*m));
    m->rows = rows;
    m->cols = cols;
    m->data = calloc(rows, sizeof(*m->data));
    for (int i = 0; i < rows; i++) {{
        m->data[i] = calloc(cols, sizeof(**m->data));
    }}
    return m;
}}

matrix* compute_matrix(matrix *m1, matrix *m2) {{
    matrix *result = allocate_matrix(m1->rows, m1->cols);
{loop}
    return result;
}}

int main() {{
    {c_mat1}
    {c_mat2}

    matrix *result = compute_matrix(m1, m2);

    printf("Result:\\n");
    for (int i = 0; i < result->rows; i++) {{
        for (int j = 0; j < result->cols; j++) {{
            printf("%d ", result->data[i][j]);
        }}
        printf("\\n");
    }}

    for (int i = 0; i < m1->rows; i++) {{
        free(m1->data[i]);
        free(m2->data[i]);
        free(result->data[i]);
    }}
    free(m1->data);
    free(m1);
    free(m2->data);
    free(m2);
    free(result->data);
    free(result);

    return 0;
}}
"""
                return c_code

            else:
                raise ValueError(f'{lalg_ast} is not a valid 2D for loop expression.')

        case _:
            raise ValueError(f'{lalg_ast} is not valid LALG AST.')

def allocate_vector(name, vec, n, i):
    c_exp = f"""vector *{name} = allocate_vector({n});
    int data{i}[] = {{{generate_c_for_vector(vec)}}};
    for (int i = 0; i < {n}; i++) {{
        {name}->data[i] = data{i}[i];
    }}"""
    return c_exp

def allocate_matrix(name, mat, rows, cols, i):
    c_exp = f"""matrix *{name} = allocate_matrix({rows}, {cols});
    int data{i}[{rows}][{cols}] = {{{generate_c_for_matrix(mat)}}};
    for (int i = 0; i < {rows}; i++) {{
        for (int j = 0; j < {cols}; j++) {{
            {name}->data[i][j] = data{i}[i][j];
        }}
    }}"""
    return c_exp

def generate_c_for_vector(vec):
    return ', '.join(map(str, vec))

def generate_c_for_matrix(mat):
    return ', '.join(['{' + ', '.join(map(str, row)) + '}' for row in mat])
