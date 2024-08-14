
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'INTEGER LBRACKET MINUS MUL NAME PLUS RBRACKETexpressions : expression expressionsexpressions : expressionexpression : INTEGERexpression : NAMEexpression : vectorexpression : matrixexpression : expression PLUS expressionexpression : expression MINUS expressionexpression : expression MUL expressionvector : LBRACKET elements RBRACKETmatrix : LBRACKET vectors RBRACKETvectors : vector vectorsvectors : vectorelements : INTEGER elementselements : INTEGER'
    
_lr_action_items = {'INTEGER':([0,2,3,4,5,6,7,9,10,11,12,15,17,18,19,20,21,],[3,3,-3,-4,-5,-6,15,3,3,3,15,15,-7,-8,-9,-10,-11,]),'NAME':([0,2,3,4,5,6,9,10,11,17,18,19,20,21,],[4,4,-3,-4,-5,-6,4,4,4,-7,-8,-9,-10,-11,]),'LBRACKET':([0,2,3,4,5,6,7,9,10,11,16,17,18,19,20,21,],[7,7,-3,-4,-5,-6,12,7,7,7,12,-7,-8,-9,-10,-11,]),'$end':([1,2,3,4,5,6,8,17,18,19,20,21,],[0,-2,-3,-4,-5,-6,-1,-7,-8,-9,-10,-11,]),'PLUS':([2,3,4,5,6,17,18,19,20,21,],[9,-3,-4,-5,-6,9,9,9,-10,-11,]),'MINUS':([2,3,4,5,6,17,18,19,20,21,],[10,-3,-4,-5,-6,10,10,10,-10,-11,]),'MUL':([2,3,4,5,6,17,18,19,20,21,],[11,-3,-4,-5,-6,11,11,11,-10,-11,]),'RBRACKET':([13,14,15,16,20,22,23,],[20,21,-15,-13,-10,-14,-12,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expressions':([0,2,],[1,8,]),'expression':([0,2,9,10,11,],[2,2,17,18,19,]),'vector':([0,2,7,9,10,11,16,],[5,5,16,5,5,5,16,]),'matrix':([0,2,9,10,11,],[6,6,6,6,6,]),'elements':([7,12,15,],[13,13,22,]),'vectors':([7,16,],[14,23,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expressions","S'",1,None,None,None),
  ('expressions -> expression expressions','expressions',2,'p_program','parser.py',47),
  ('expressions -> expression','expressions',1,'p_program_empty','parser.py',51),
  ('expression -> INTEGER','expression',1,'p_expression_int','parser.py',55),
  ('expression -> NAME','expression',1,'p_expression_var','parser.py',59),
  ('expression -> vector','expression',1,'p_expression_vector','parser.py',63),
  ('expression -> matrix','expression',1,'p_expression_matrix','parser.py',67),
  ('expression -> expression PLUS expression','expression',3,'p_expression_sum','parser.py',72),
  ('expression -> expression MINUS expression','expression',3,'p_expression_minus','parser.py',76),
  ('expression -> expression MUL expression','expression',3,'p_expression_mul','parser.py',80),
  ('vector -> LBRACKET elements RBRACKET','vector',3,'p_vector','parser.py',84),
  ('matrix -> LBRACKET vectors RBRACKET','matrix',3,'p_matrix','parser.py',88),
  ('vectors -> vector vectors','vectors',2,'p_vectors','parser.py',92),
  ('vectors -> vector','vectors',1,'p_vectors_one','parser.py',96),
  ('elements -> INTEGER elements','elements',2,'p_elements','parser.py',100),
  ('elements -> INTEGER','elements',1,'p_elements_int','parser.py',104),
]