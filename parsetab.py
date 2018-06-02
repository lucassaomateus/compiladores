
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftt_OP_ADDt_OP_SUBleftt_OP_MULt_OP_DIVEOF ERRADO FALSE FLOAT_NUMBER ID IDENTIFIER INT_NUMBER KW_ELSE KW_FLOAT KW_FOR KW_FOR_CLOSE KW_FOR_OPEN KW_FPUNC KW_FUNCTION KW_FUNC_ARGS_SEP KW_FUNC_CLOSE KW_FUNC_OPEN_ARGS KW_IF KW_IF_CLOSE KW_IF_OPEN KW_INPUT KW_INT KW_PRINT KW_STRING KW_WHILE OP_ADD OP_ATRIB OP_DEC OP_DIV1 OP_EXP OP_INC OP_LOG_AND OP_LOG_BT OP_LOG_BT_EKW_FUNC_OPEN OP_LOG_DIFF OP_LOG_EQUAL OP_LOG_LT OP_LOG_LT_E OP_LOG_NOT OP_LOG_OR OP_MUL OP_SUB PAR_CLOSE PAR_OPEN STRING TRUE t_KW_FOR_CLOSE t_KW_FOR_OPEN t_KW_FPUNC t_KW_FUNCTION t_KW_FUNC_ARGS_SEP t_KW_FUNC_OPEN t_KW_FUNC_OPEN_ARGS t_KW_IF_OPEN t_OP_ADD t_OP_ATRIB t_OP_DEC t_OP_DIV t_OP_EXP t_OP_INC t_OP_LOG_AND t_OP_LOG_BT t_OP_LOG_BT_E t_OP_LOG_DIFF t_OP_LOG_EQUAL t_OP_LOG_LT t_OP_LOG_LT_E t_OP_LOG_NOT t_OP_LOG_OR t_OP_MUL t_OP_SUB t_PAR_CLOSE t_PAR_OPEN\n    expressao : declaracao ID atrib ID numero\n\n    atrib : t_OP_ATRIB\n          | empty\n\n    declaracao : KW_INT\n               | KW_FLOAT\n\n    numero : INT_NUMBER\n           | FLOAT_NUMBER\n           | ID\n\n    op : t_OP_ADD\n       | t_OP_SUB\n       | t_OP_DIV\n       | t_OP_MUL\n\n    exp : numero\n        | numero op exp\n        | empty\n    empty :'
    
_lr_action_items = {'KW_INT':([0,],[2,]),'t_OP_ATRIB':([5,],[7,]),'FLOAT_NUMBER':([9,],[11,]),'INT_NUMBER':([9,],[12,]),'KW_FLOAT':([0,],[3,]),'ID':([2,3,4,5,6,7,8,9,],[-4,-5,5,-16,9,-2,-3,13,]),'$end':([1,10,11,12,13,],[0,-1,-7,-6,-8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'atrib':([5,],[6,]),'expressao':([0,],[1,]),'declaracao':([0,],[4,]),'numero':([9,],[10,]),'empty':([5,],[8,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expressao","S'",1,None,None,None),
  ('expressao -> declaracao ID atrib ID numero','expressao',5,'p_operacoes_aritmeticas','Analisador_Sintatico.py',54),
  ('atrib -> t_OP_ATRIB','atrib',1,'p_operacoes_aritmeticas','Analisador_Sintatico.py',56),
  ('atrib -> empty','atrib',1,'p_operacoes_aritmeticas','Analisador_Sintatico.py',57),
  ('declaracao -> KW_INT','declaracao',1,'p_operacoes_aritmeticas','Analisador_Sintatico.py',59),
  ('declaracao -> KW_FLOAT','declaracao',1,'p_operacoes_aritmeticas','Analisador_Sintatico.py',60),
  ('numero -> INT_NUMBER','numero',1,'p_operacoes_aritmeticas','Analisador_Sintatico.py',62),
  ('numero -> FLOAT_NUMBER','numero',1,'p_operacoes_aritmeticas','Analisador_Sintatico.py',63),
  ('numero -> ID','numero',1,'p_operacoes_aritmeticas','Analisador_Sintatico.py',64),
  ('op -> t_OP_ADD','op',1,'p_operacoes_aritmeticas','Analisador_Sintatico.py',66),
  ('op -> t_OP_SUB','op',1,'p_operacoes_aritmeticas','Analisador_Sintatico.py',67),
  ('op -> t_OP_DIV','op',1,'p_operacoes_aritmeticas','Analisador_Sintatico.py',68),
  ('op -> t_OP_MUL','op',1,'p_operacoes_aritmeticas','Analisador_Sintatico.py',69),
  ('exp -> numero','exp',1,'p_operacoes_aritmeticas','Analisador_Sintatico.py',71),
  ('exp -> numero op exp','exp',3,'p_operacoes_aritmeticas','Analisador_Sintatico.py',72),
  ('exp -> empty','exp',1,'p_operacoes_aritmeticas','Analisador_Sintatico.py',73),
  ('empty -> <empty>','empty',0,'p_empty','Analisador_Sintatico.py',87),
]