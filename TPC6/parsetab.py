
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftMULTIPLYDIVIDEDIVIDE MINUS MULTIPLY NUMBER PLUSexpression : expression PLUS expression\n| expression MINUS expression\n| expression MULTIPLY expression\n| expression DIVIDE expressionexpression : NUMBER'
    
_lr_action_items = {'NUMBER':([0,3,4,5,6,],[2,2,2,2,2,]),'$end':([1,2,7,8,9,10,],[0,-5,-1,-2,-3,-4,]),'PLUS':([1,2,7,8,9,10,],[3,-5,-1,-2,-3,-4,]),'MINUS':([1,2,7,8,9,10,],[4,-5,-1,-2,-3,-4,]),'MULTIPLY':([1,2,7,8,9,10,],[5,-5,5,5,-3,-4,]),'DIVIDE':([1,2,7,8,9,10,],[6,-5,6,6,-3,-4,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,3,4,5,6,],[1,7,8,9,10,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','exp_sin.py',12),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','exp_sin.py',13),
  ('expression -> expression MULTIPLY expression','expression',3,'p_expression_binop','exp_sin.py',14),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','exp_sin.py',15),
  ('expression -> NUMBER','expression',1,'p_expression_number','exp_sin.py',28),
]
