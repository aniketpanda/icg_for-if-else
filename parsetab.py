
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'start_statePRINT PRINTF CHAR INT FLOAT PLUS MINUS NUMBER AOP RELOP ID ASSIGN LOGOP OPBRAC CLOSEBRAC STRLIT STATETER COMMA OPENFLR CLOSEFLR ELSE IFstart_state : INT ID OPBRAC  CLOSEBRAC stmtsiter_stmt : X Y Z X : IF  OPBRAC cond_stmt  CLOSEBRAC Y : stmts Z : ELSE stmts stmts\n           | stmts : OPENFLR stmts CLOSEFLR\n\t\t\t| iter_stmt\n\t\t\t| expr_stmt STATETER stmts\n\t\t\t| printing  STATETER stmts\n\t\t\t| assignment STATETER stmts\n\t\t\t| decfloat STATETER stmts\n\t\t\t| declareint STATETER stmts\n\t\t\t| math stmts\n\t\t\t| newone stmts\n\t\t\t| newone : ID ASSIGN ID PLUS NUMBER STATETER stmts\n                   | ID ASSIGN ID PLUS ID STATETER stmts\n                   |  ID ASSIGN ID MINUS NUMBER STATETER stmts\n                   |  ID ASSIGN ID MINUS ID STATETER stmtsexpr_stmt : assignment_int\n\t\t\t| declareassignment_int : INT ID ASSIGN NUMBER followint\n\tassignment_int : INT ID  followint\n\tfollowint : COMMA ID ASSIGN NUMBER followintfollowint : COMMA ID  followintfollowint : assignment : FLOAT ID ASSIGN NUMBER followfloat\n\tassignment : FLOAT ID  followfloat\n\tfollowfloat : COMMA ID ASSIGN NUMBER followfloatfollowfloat : COMMA ID  followfloatfollowfloat : assignment : CHAR ID ASSIGN NUMBER follow\n\tdeclare : ID ASSIGN NUMBER followintdeclareint : ID ASSIGN NUMBER decfloat : ID ASSIGN NUMBER cond_stmt : ID RELOP ID\n\t\t\t| ID RELOP NUMBER\n\t\t\t| NUMBER RELOP ID\n\t\t\t| NUMBER RELOP NUMBER\n\t\t\t| cond_stmt LOGOP cond_stmt\n\t\t\t|math : ID PLUS ASSIGN NUMBER STATETER\n\t\t\t| ID PLUS ASSIGN ID STATETER \n\t\t\t| ID MINUS ASSIGN NUMBER STATETER\n\t\t\t| ID MINUS ASSIGN ID STATETER\n\t\t\t| ID AOP ASSIGN NUMBER STATETER\n\t\t\t| ID AOP ASSIGN ID STATETER\n\t\t\t| PLUS PLUS ID STATETER\n\t\t\t| ID PLUS PLUS STATETER\n\t\t\t| MINUS MINUS ID STATETER\n\t\t\t| ID MINUS MINUS STATETER\n\t\t\tprinting : PRINT \n\t\t| PRINTF OPBRAC STRLIT follow CLOSEBRAC\n\t\t\t  follow : COMMA ID follow\n\t\t\t|'
    
_lr_action_items = {'LOGOP':([42,66,95,116,117,118,119,120,],[-42,95,-42,95,-39,-40,-38,-37,]),'NUMBER':([38,42,50,61,64,65,71,74,84,85,95,96,97,123,126,],[59,67,77,86,90,92,98,100,106,108,67,118,119,132,133,]),'CHAR':([5,16,18,20,21,25,28,31,33,34,36,37,43,47,48,49,52,54,55,57,58,69,76,78,79,82,88,89,94,105,110,111,112,113,114,115,128,129,130,131,134,135,136,137,],[7,7,-8,7,7,7,7,7,7,7,-4,-6,-15,7,-14,-13,-9,-12,-11,-2,7,-7,-10,-51,-49,7,-52,-50,-3,-5,-45,-46,-43,-44,-47,-48,7,7,7,7,-17,-18,-19,-20,]),'CLOSEFLR':([16,18,20,21,25,28,31,33,34,36,37,43,44,47,48,49,52,54,55,57,58,69,76,78,79,82,88,89,94,105,110,111,112,113,114,115,128,129,130,131,134,135,136,137,],[-16,-8,-16,-16,-16,-16,-16,-16,-16,-4,-6,-15,69,-16,-14,-13,-9,-12,-11,-2,-16,-7,-10,-51,-49,-16,-52,-50,-3,-5,-45,-46,-43,-44,-47,-48,-16,-16,-16,-16,-17,-18,-19,-20,]),'PRINT':([5,16,18,20,21,25,28,31,33,34,36,37,43,47,48,49,52,54,55,57,58,69,76,78,79,82,88,89,94,105,110,111,112,113,114,115,128,129,130,131,134,135,136,137,],[8,8,-8,8,8,8,8,8,8,8,-4,-6,-15,8,-14,-13,-9,-12,-11,-2,8,-7,-10,-51,-49,8,-52,-50,-3,-5,-45,-46,-43,-44,-47,-48,8,8,8,8,-17,-18,-19,-20,]),'MINUS':([5,9,16,17,18,20,21,25,28,31,33,34,36,37,39,43,47,48,49,52,54,55,57,58,60,69,76,78,79,82,88,89,94,105,110,111,112,113,114,115,128,129,130,131,134,135,136,137,],[9,30,9,39,-8,9,9,9,9,9,9,9,-4,-6,62,-15,9,-14,-13,-9,-12,-11,-2,9,85,-7,-10,-51,-49,9,-52,-50,-3,-5,-45,-46,-43,-44,-47,-48,9,9,9,9,-17,-18,-19,-20,]),'STRLIT':([35,],[56,]),'PLUS':([5,12,16,17,18,20,21,25,28,31,33,34,36,37,40,43,47,48,49,52,54,55,57,58,60,69,76,78,79,82,88,89,94,105,110,111,112,113,114,115,128,129,130,131,134,135,136,137,],[12,32,12,40,-8,12,12,12,12,12,12,12,-4,-6,63,-15,12,-14,-13,-9,-12,-11,-2,12,84,-7,-10,-51,-49,12,-52,-50,-3,-5,-45,-46,-43,-44,-47,-48,12,12,12,12,-17,-18,-19,-20,]),'AOP':([17,],[41,]),'COMMA':([45,46,56,59,77,98,99,100,101,103,132,133,],[72,75,80,72,80,72,72,75,75,80,72,75,]),'ASSIGN':([17,29,39,40,41,45,46,99,101,],[38,50,61,64,65,71,74,123,126,]),'$end':([1,5,11,16,18,20,25,28,31,33,34,36,37,43,47,48,49,52,54,55,57,58,69,76,78,79,82,88,89,94,105,110,111,112,113,114,115,128,129,130,131,134,135,136,137,],[0,-16,-1,-16,-8,-16,-16,-16,-16,-16,-16,-4,-6,-15,-16,-14,-13,-9,-12,-11,-2,-16,-7,-10,-51,-49,-16,-52,-50,-3,-5,-45,-46,-43,-44,-47,-48,-16,-16,-16,-16,-17,-18,-19,-20,]),'RELOP':([67,68,],[96,97,]),'ELSE':([16,18,20,25,28,31,33,34,36,37,43,47,48,49,52,54,55,57,58,69,76,78,79,82,88,89,94,105,110,111,112,113,114,115,128,129,130,131,134,135,136,137,],[-16,-8,-16,-16,-16,-16,-16,-16,-4,58,-15,-16,-14,-13,-9,-12,-11,-2,-16,-7,-10,-51,-49,-16,-52,-50,-3,-5,-45,-46,-43,-44,-47,-48,-16,-16,-16,-16,-17,-18,-19,-20,]),'PRINTF':([5,16,18,20,21,25,28,31,33,34,36,37,43,47,48,49,52,54,55,57,58,69,76,78,79,82,88,89,94,105,110,111,112,113,114,115,128,129,130,131,134,135,136,137,],[15,15,-8,15,15,15,15,15,15,15,-4,-6,-15,15,-14,-13,-9,-12,-11,-2,15,-7,-10,-51,-49,15,-52,-50,-3,-5,-45,-46,-43,-44,-47,-48,15,15,15,15,-17,-18,-19,-20,]),'ID':([2,5,7,16,18,20,21,22,23,25,28,30,31,32,33,34,36,37,38,42,43,47,48,49,52,54,55,57,58,61,64,65,69,72,75,76,78,79,80,82,84,85,88,89,94,95,96,97,105,110,111,112,113,114,115,128,129,130,131,134,135,136,137,],[3,17,29,17,-8,17,17,45,46,17,17,51,17,53,17,17,-4,-6,60,68,-15,17,-14,-13,-9,-12,-11,-2,17,87,91,93,-7,99,101,-10,-51,-49,103,17,107,109,-52,-50,-3,68,117,120,-5,-45,-46,-43,-44,-47,-48,17,17,17,17,-17,-18,-19,-20,]),'IF':([5,16,18,20,21,25,28,31,33,34,36,37,43,47,48,49,52,54,55,57,58,69,76,78,79,82,88,89,94,105,110,111,112,113,114,115,128,129,130,131,134,135,136,137,],[19,19,-8,19,19,19,19,19,19,19,-4,-6,-15,19,-14,-13,-9,-12,-11,-2,19,-7,-10,-51,-49,19,-52,-50,-3,-5,-45,-46,-43,-44,-47,-48,19,19,19,19,-17,-18,-19,-20,]),'OPENFLR':([5,16,18,20,21,25,28,31,33,34,36,37,43,47,48,49,52,54,55,57,58,69,76,78,79,82,88,89,94,105,110,111,112,113,114,115,128,129,130,131,134,135,136,137,],[21,21,-8,21,21,21,21,21,21,21,-4,-6,-15,21,-14,-13,-9,-12,-11,-2,21,-7,-10,-51,-49,21,-52,-50,-3,-5,-45,-46,-43,-44,-47,-48,21,21,21,21,-17,-18,-19,-20,]),'INT':([0,5,16,18,20,21,25,28,31,33,34,36,37,43,47,48,49,52,54,55,57,58,69,76,78,79,82,88,89,94,105,110,111,112,113,114,115,128,129,130,131,134,135,136,137,],[2,22,22,-8,22,22,22,22,22,22,22,-4,-6,-15,22,-14,-13,-9,-12,-11,-2,22,-7,-10,-51,-49,22,-52,-50,-3,-5,-45,-46,-43,-44,-47,-48,22,22,22,22,-17,-18,-19,-20,]),'FLOAT':([5,16,18,20,21,25,28,31,33,34,36,37,43,47,48,49,52,54,55,57,58,69,76,78,79,82,88,89,94,105,110,111,112,113,114,115,128,129,130,131,134,135,136,137,],[23,23,-8,23,23,23,23,23,23,23,-4,-6,-15,23,-14,-13,-9,-12,-11,-2,23,-7,-10,-51,-49,23,-52,-50,-3,-5,-45,-46,-43,-44,-47,-48,23,23,23,23,-17,-18,-19,-20,]),'OPBRAC':([3,15,19,],[4,35,42,]),'STATETER':([6,8,10,13,14,24,26,27,45,46,51,53,59,62,63,70,73,77,83,86,87,90,91,92,93,98,99,100,101,102,103,104,106,107,108,109,121,122,124,125,127,132,133,138,139,],[28,-53,31,33,34,47,-21,-22,-27,-32,78,79,-27,88,89,-24,-29,-56,-34,110,111,112,113,114,115,-27,-27,-32,-32,-33,-56,-54,128,129,130,131,-23,-26,-28,-31,-55,-27,-32,-25,-30,]),'CLOSEBRAC':([4,42,56,66,81,95,103,116,117,118,119,120,127,],[5,-42,-56,94,104,-42,-56,-41,-39,-40,-38,-37,-55,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Z':([37,],[57,]),'newone':([5,16,20,21,25,28,31,33,34,47,58,82,128,129,130,131,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'start_state':([0,],[1,]),'stmts':([5,16,20,21,25,28,31,33,34,47,58,82,128,129,130,131,],[11,36,43,44,48,49,52,54,55,76,82,105,134,135,136,137,]),'assignment':([5,16,20,21,25,28,31,33,34,47,58,82,128,129,130,131,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'followint':([45,59,98,99,132,],[70,83,121,122,138,]),'declareint':([5,16,20,21,25,28,31,33,34,47,58,82,128,129,130,131,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'cond_stmt':([42,95,],[66,116,]),'printing':([5,16,20,21,25,28,31,33,34,47,58,82,128,129,130,131,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'follow':([56,77,103,],[81,102,127,]),'iter_stmt':([5,16,20,21,25,28,31,33,34,47,58,82,128,129,130,131,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'assignment_int':([5,16,20,21,25,28,31,33,34,47,58,82,128,129,130,131,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'Y':([16,],[37,]),'X':([5,16,20,21,25,28,31,33,34,47,58,82,128,129,130,131,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'followfloat':([46,100,101,133,],[73,124,125,139,]),'expr_stmt':([5,16,20,21,25,28,31,33,34,47,58,82,128,129,130,131,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'declare':([5,16,20,21,25,28,31,33,34,47,58,82,128,129,130,131,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'decfloat':([5,16,20,21,25,28,31,33,34,47,58,82,128,129,130,131,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'math':([5,16,20,21,25,28,31,33,34,47,58,82,128,129,130,131,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start_state","S'",1,None,None,None),
  ('start_state -> INT ID OPBRAC CLOSEBRAC stmts','start_state',5,'p_start_state','syntax_phase.py',38),
  ('iter_stmt -> X Y Z','iter_stmt',3,'p_iter_stmt','syntax_phase.py',43),
  ('X -> IF OPBRAC cond_stmt CLOSEBRAC','X',4,'p_X','syntax_phase.py',48),
  ('Y -> stmts','Y',1,'p_Y','syntax_phase.py',74),
  ('Z -> ELSE stmts stmts','Z',3,'p_Z','syntax_phase.py',88),
  ('Z -> <empty>','Z',0,'p_Z','syntax_phase.py',89),
  ('stmts -> OPENFLR stmts CLOSEFLR','stmts',3,'p_stmts','syntax_phase.py',97),
  ('stmts -> iter_stmt','stmts',1,'p_stmts','syntax_phase.py',98),
  ('stmts -> expr_stmt STATETER stmts','stmts',3,'p_stmts','syntax_phase.py',99),
  ('stmts -> printing STATETER stmts','stmts',3,'p_stmts','syntax_phase.py',100),
  ('stmts -> assignment STATETER stmts','stmts',3,'p_stmts','syntax_phase.py',101),
  ('stmts -> decfloat STATETER stmts','stmts',3,'p_stmts','syntax_phase.py',102),
  ('stmts -> declareint STATETER stmts','stmts',3,'p_stmts','syntax_phase.py',103),
  ('stmts -> math stmts','stmts',2,'p_stmts','syntax_phase.py',104),
  ('stmts -> newone stmts','stmts',2,'p_stmts','syntax_phase.py',105),
  ('stmts -> <empty>','stmts',0,'p_stmts','syntax_phase.py',106),
  ('newone -> ID ASSIGN ID PLUS NUMBER STATETER stmts','newone',7,'p_newone','syntax_phase.py',109),
  ('newone -> ID ASSIGN ID PLUS ID STATETER stmts','newone',7,'p_newone','syntax_phase.py',110),
  ('newone -> ID ASSIGN ID MINUS NUMBER STATETER stmts','newone',7,'p_newone','syntax_phase.py',111),
  ('newone -> ID ASSIGN ID MINUS ID STATETER stmts','newone',7,'p_newone','syntax_phase.py',112),
  ('expr_stmt -> assignment_int','expr_stmt',1,'p_expr_stmt','syntax_phase.py',128),
  ('expr_stmt -> declare','expr_stmt',1,'p_expr_stmt','syntax_phase.py',129),
  ('assignment_int -> INT ID ASSIGN NUMBER followint','assignment_int',5,'p_assignment_int','syntax_phase.py',131),
  ('assignment_int -> INT ID followint','assignment_int',3,'p_assignment_int1','syntax_phase.py',142),
  ('followint -> COMMA ID ASSIGN NUMBER followint','followint',5,'p_follow_int','syntax_phase.py',149),
  ('followint -> COMMA ID followint','followint',3,'p_follow_int1','syntax_phase.py',158),
  ('followint -> <empty>','followint',0,'p_follow_int2','syntax_phase.py',163),
  ('assignment -> FLOAT ID ASSIGN NUMBER followfloat','assignment',5,'p_assignment_float','syntax_phase.py',168),
  ('assignment -> FLOAT ID followfloat','assignment',3,'p_assignment_float1','syntax_phase.py',178),
  ('followfloat -> COMMA ID ASSIGN NUMBER followfloat','followfloat',5,'p_follow_float','syntax_phase.py',184),
  ('followfloat -> COMMA ID followfloat','followfloat',3,'p_follow_float1','syntax_phase.py',192),
  ('followfloat -> <empty>','followfloat',0,'p_follow_float2','syntax_phase.py',197),
  ('assignment -> CHAR ID ASSIGN NUMBER follow','assignment',5,'p_assignment_char','syntax_phase.py',201),
  ('declare -> ID ASSIGN NUMBER followint','declare',4,'p_declare','syntax_phase.py',211),
  ('declareint -> ID ASSIGN NUMBER','declareint',3,'p_declareint','syntax_phase.py',218),
  ('decfloat -> ID ASSIGN NUMBER','decfloat',3,'p_declarefloat','syntax_phase.py',226),
  ('cond_stmt -> ID RELOP ID','cond_stmt',3,'p_cond_stmt','syntax_phase.py',234),
  ('cond_stmt -> ID RELOP NUMBER','cond_stmt',3,'p_cond_stmt','syntax_phase.py',235),
  ('cond_stmt -> NUMBER RELOP ID','cond_stmt',3,'p_cond_stmt','syntax_phase.py',236),
  ('cond_stmt -> NUMBER RELOP NUMBER','cond_stmt',3,'p_cond_stmt','syntax_phase.py',237),
  ('cond_stmt -> cond_stmt LOGOP cond_stmt','cond_stmt',3,'p_cond_stmt','syntax_phase.py',238),
  ('cond_stmt -> <empty>','cond_stmt',0,'p_cond_stmt','syntax_phase.py',239),
  ('math -> ID PLUS ASSIGN NUMBER STATETER','math',5,'p_math','syntax_phase.py',262),
  ('math -> ID PLUS ASSIGN ID STATETER','math',5,'p_math','syntax_phase.py',263),
  ('math -> ID MINUS ASSIGN NUMBER STATETER','math',5,'p_math','syntax_phase.py',264),
  ('math -> ID MINUS ASSIGN ID STATETER','math',5,'p_math','syntax_phase.py',265),
  ('math -> ID AOP ASSIGN NUMBER STATETER','math',5,'p_math','syntax_phase.py',266),
  ('math -> ID AOP ASSIGN ID STATETER','math',5,'p_math','syntax_phase.py',267),
  ('math -> PLUS PLUS ID STATETER','math',4,'p_math','syntax_phase.py',268),
  ('math -> ID PLUS PLUS STATETER','math',4,'p_math','syntax_phase.py',269),
  ('math -> MINUS MINUS ID STATETER','math',4,'p_math','syntax_phase.py',270),
  ('math -> ID MINUS MINUS STATETER','math',4,'p_math','syntax_phase.py',271),
  ('printing -> PRINT','printing',1,'p_printing','syntax_phase.py',315),
  ('printing -> PRINTF OPBRAC STRLIT follow CLOSEBRAC','printing',5,'p_printing','syntax_phase.py',316),
  ('follow -> COMMA ID follow','follow',3,'p_follow','syntax_phase.py',324),
  ('follow -> <empty>','follow',0,'p_follow','syntax_phase.py',325),
]