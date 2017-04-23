import ply.yacc as yacc
from lexer import tokens,symbol_table
from collections import deque
start = 'start_state'
stack = []
n=0
label=0
tac=[]
temp=1
i=0
q = deque([])


class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
s= Stack()
#print(symbol_table)
def p_start_state(p):
	'start_state : INT ID OPBRAC  CLOSEBRAC stmts'
	global result
	result = 'Valid'	

def p_iter_stmt(p):
	'''iter_stmt : IF  OPBRAC cond_stmt CLOSEBRAC  stmts 
	| IF  OPBRAC cond_stmt CLOSEBRAC  stmts  ELSE  stmts  '''
	global n
	global s
	global q
	global label
	z= "L"+str(label)
	k=str(s.pop())
	if(p[1]=="if" and len(p)>5):
    		tac.append(["ifFalse "+k+" GOTO "+z])	
    		n+=1

def p_iter_stmt(p):
	'''iter_stmt : IF  OPBRAC cond_stmt  CLOSEBRAC X '''
	global n
	global s
	k=str(s.pop())
	if(p[1]=="if" and len(p)>5):
    		tac.append(["ifFalse "+k])	
    		n+=1

##	ifstmt: IF '(' expr ')' '{' 
##            statements 
##        '}' 
##            { ifcount++; }
##        |
##        IF '(' expr ')' '{'
##            statements
##        '}' ELSE '{'
##            statements
##        '}'
##            { ifcount++; }

def p_X(p):
     '''X : stmts Y'''

def p_Y(p):
     '''Y : ELSE stmts
           | '''

def p_newone(p):
	'''newone : ID ASSIGN ID PLUS NUMBER STATETER 
    	|  ID ASSIGN ID PLUS ID STATETER 
    	|  ID ASSIGN ID MINUS NUMBER STATETER 
    	|  ID ASSIGN ID MINUS ID STATETER 
    	'''
   	global temp
	global n
	m = "t"+str(temp)
  	if(p[4]=="+" and p[2]=="="):
		tac.append([m+"  =  "+p[1]+"  +  "+p[5]])
		tac.append([p[1]+"  =  "+m])
		temp+=1
		n+=2
	elif(p[4]=="-" and p[2]=="="):
		tac.append([m+"  =  "+p[1]+"  -  "+p[5]])
		tac.append([p[1]+"  =  "+m])
		temp+=1
		n+=2

def p_expr_stmt(p):
	'''expr_stmt : assignment_int
			| declare'''
def p_assignment_int(p):
	'''assignment_int : INT ID ASSIGN NUMBER followint
	'''
	lineno = p.lineno(1)
	stack.append([p[2],p[4],lineno])
	tac.append([p[2]+"  =  "+p[4]])
	global n
	n=n+1

	symbol_table[p[2]]=['ID','int',p[4], lineno]

def p_assignment_int1(p):
	'''assignment_int : INT ID  followint
	'''
	lineno = p.lineno(2)
	stack.append([p[2],'0',lineno])
	symbol_table[p[2]]=['ID','int','0', lineno]

def p_follow_int(p):
	'''followint : COMMA ID ASSIGN NUMBER followint'''
	lineno = p.lineno(2)
	stack.append([p[2],p[4],lineno])
	symbol_table[p[2]]=['ID','int',p[4], lineno]
	tac.append([p[2]+"  =  "+p[4]])
	global n
	n=n+1

def p_follow_int1(p):
	'''followint : COMMA ID  followint'''
	lineno = p.lineno(2)
	stack.append([p[2],'0',lineno])
	symbol_table[p[2]]=['ID','int','0', lineno]
def p_follow_int2(p):
	'''followint : '''



def p_assignment_float(p):
	'''assignment : FLOAT ID ASSIGN NUMBER followfloat
	'''
	lineno = p.lineno(1)
	stack.append([p[2],p[4],lineno])
	tac.append([p[2]+"  =  "+p[4]])
	global n
	n=n+1

	symbol_table[p[2]]=['ID','float',p[4], lineno]
def p_assignment_float1(p):
	'''assignment : FLOAT ID  followfloat
	'''
	lineno = p.lineno(2)
	stack.append([p[2],'0.0',lineno])
	symbol_table[p[2]]=['ID','float','0.0', lineno]
def p_follow_float(p):
	'''followfloat : COMMA ID ASSIGN NUMBER followfloat'''
	lineno = p.lineno(2)
	stack.append([p[2],p[4],lineno])
	symbol_table[p[2]]=['ID','float',p[4], lineno]
	tac.append([p[2]+"  =  "+p[4]])
	global n
	n=n+1
def p_follow_float1(p):
	'''followfloat : COMMA ID  followfloat'''
	lineno = p.lineno(2)
	stack.append([p[2],'0',lineno])
	symbol_table[p[2]]=['ID','float','0.0', lineno]
def p_follow_float2(p):
	'''followfloat : '''

	
def p_assignment_char(p):
	'''assignment : CHAR ID ASSIGN NUMBER follow
	'''
	lineno = symbol_table[p[2]]
	symbol_table[p[2]]=['ID','char',p[4], lineno[0]]
	tac.append([p[2]+"  =  "+p[4]])
	global n
	n=n+1


def p_declare(p):
	'''declare : ID ASSIGN NUMBER followint'''
	lineno = p.lineno(1)
	stack.append([p[1],p[3],lineno])
	tac.append([p[1]+"  =  "+p[3]])
	global n
	n=n+1
def p_declareint(p):
	'''declareint : ID ASSIGN NUMBER '''
	print("-------------",p[1])
	lineno = symbol_table[p[1]]
	stack.append([p[1],p[3],lineno])
	tac.append([p[1]+"  =  "+p[3]])
	global n
	n=n+1
def p_declarefloat(p):
	'''decfloat : ID ASSIGN NUMBER '''
	print("-------------",p[1])
	lineno = p.lineno(1)
	stack.append([p[1],p[3],lineno])
	tac.append([p[1]+"  =  "+p[3]])
	global n
	n=n+1
def p_cond_stmt(p):
	'''cond_stmt : ID RELOP ID
			| ID RELOP NUMBER
			| NUMBER RELOP ID
			| NUMBER RELOP NUMBER
			| cond_stmt LOGOP cond_stmt
			|'''
	global temp
	global n
	m = "t"+str(temp)
	if(p[2]=="||" or p[2]=="&&" or p[2]=="!=" ):
		z=s.pop()
		k=s.pop()
		tac.append([m+" = "+k+" "+str(p[2])+" "+z])
		s.push(m)
	else:
		tac.append([m+" = "+str(p[1])+str(p[2])+str(p[3])])
		s.push(m)

	n=n+1
	temp+=1


def p_math(p):

	'''math : ID PLUS ASSIGN NUMBER STATETER
			| ID PLUS ASSIGN ID STATETER 
			| ID MINUS ASSIGN NUMBER STATETER
			| ID MINUS ASSIGN ID STATETER
			| ID AOP ASSIGN NUMBER STATETER
			| ID AOP ASSIGN ID STATETER
			| PLUS PLUS ID STATETER
			| ID PLUS PLUS STATETER
			| MINUS MINUS ID STATETER
			| ID MINUS MINUS STATETER
			'''
	global temp
	global n
	m = "t"+str(temp)
	if(p[2]=="+" and p[3]=="="):
		tac.append([m+"  =  "+p[1]+"  +  "+p[4]])
		tac.append([p[1]+"  =  "+m])
		temp+=1
		n+=2
	elif(p[2]=="-" and p[3]=="="):
		tac.append([m+"  =  "+p[1]+"  -  "+p[4]])
		tac.append([p[1]+"  =  "+m])
		temp+=1
		n+=2
	elif(p[2]=="/" and p[3]=="="):
		tac.append([m+"  =  "+p[1]+"  /  "+p[4]])
		tac.append([p[1]+"  =  "+m])
		temp+=1
		n+=2
	elif(p[2]=="*" and p[3]=="="):
		tac.append([m+"  =  "+p[1]+"  *  "+p[4]])
		tac.append([p[1]+"  =  "+m])
		temp+=1
		n+=2		
	elif(p[2]=="%" and p[3]=="="):
		tac.append([m+"  =  "+p[1]+"  %  "+p[4]])
		tac.append([p[1]+"  =  "+m])
		temp+=1
		n+=2
	elif((p[1]=="+" and p[2]=="+" ) or (p[2]=="+" and p[3]=="+")):
		tac.append([m+"  =  "+p[1]+"  +  "+"1"])
		tac.append([p[1]+"  =  "+m])
		temp+=1
		n+=2
	elif((p[1]=="-" and p[2]=="-" ) or (p[2]=="-" and p[3]=="-")):
		tac.append([m+"  =  "+p[1]+"  -  "+"1"])
		tac.append([p[1]+"  =  "+m])
		temp+=1
		n+=2


def p_printing(p):
	'''printing : PRINT 
		| PRINTF OPBRAC STRLIT follow CLOSEBRAC
			 '''
	#print("---------------------------",p[1],'---------------------------------------------')

def p_follow (p):
	''' follow : COMMA ID follow
			|'''


def p_error(p):
	print("\n")
	print("Syntax error in input: %s line number:%s" % (p,str(p.lineno)))
	print("\n")

        #pass
	#sys.exit()

result = 'Invalid'
parser = yacc.yacc()
program= open("test.c",'r').read()

def parse(program):
	global parser
	global result
	res = parser.parse(program,tracking=True)
	return (result,symbol_table,stack)
parse(program)
for key in symbol_table.keys():
	print(key, ':',  symbol_table[key])
print("------SEMANTIC PHASE ----------------------------------------")
#for x in stack :
#	if x[0] in symbol_table.keys():
#		value = symbol_table[x[0]]
#		if value[1]=='int' and ('.' in x[1]):
#			print("Error: ID",x[0]," |lineno : ",x[2],"| expected value type : int | found : float")


print(result)	
print ("\n")	
print(stack)
print ("\n\n\n3 ADDRESS CODE")
for i in range(n):
	print(tac[i])
