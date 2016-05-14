import os
import time
#use string to define each single line of each single English letter

a1=' '*2+'#'+' '*2
a2=' '+'#'+' '+'#'+' '
a3='#'+' '*3+'#'
a4='#'*5
a5='#'+' '*3+'#'
b1='#'*4+' '
b2='#'+' '*3+'#'
b3='#'*4+' '
b4='#'+' '*3+'#'
b5='#'*4+' '
c1='#'*5
c2='#'+' '*4
c3='#'+' '*4
c4='#'+' '*4
c5='#'*5
d1='#'*4+' '
d2='#'+' '*3+'#'
d3='#'+' '*3+'#'
d4='#'+' '*3+'#'
d5='#'*4+' '
e1='#'*5
e2='#'+' '*4
e3='#'*5
e4='#'+' '*4
e5='#'*5
f1='#'*5
f2='#'+' '*4
f3='#'*5
f4='#'+' '*4
f5='#'+' '*4
g1='#'*5
g2='#'+' '*4
g3='#'+' '+'#'*3
g4='#'+' '*3+'#'
g5='#'*5
h1='#'+' '*3+'#'
h2='#'+' '*3+'#'
h3='#'*5
h4='#'+' '*3+'#'
h5='#'+' '*3+'#'
i1='#'*5
i2=' '*2+'#'+' '*2
i3=' '*2+'#'+' '*2
i4=' '*2+'#'+' '*2
i5='#'*5
j1='#'*5
j2=' '*2+'#'+' '*2
j3=' '*2+'#'+' '*2
j4='#'+' '+'#'+' '*2
j5=' '+'#'*2+' '*2
k1='#  ##'
k2='# #  '
k3='##   '
k4='# #  '
k5='#  ##'
l1='#    '
l2='#    '
l3='#    '
l4='#    '
l5='#####'
m1='#####'
m2='# # #'
m3='# # #'
m4='# # #'
m5='# # #'
n1='#   #'
n2='##  #'
n3='# # #'
n4='#  ##'
n5='#  ##'
o1=' ### '
o2='#   #'
o3='#   #'
o4='#   #'
o5=' ### '
p1='#### '
p2='#   #'
p3='#### '
p4='#    '
p5='#    '
q1='#### '
q2='#  # '
q3='# ## '
q4='#### '
q5='    #'
r1='#### '
r2='#   #'
r3='#### '
r4='# #  '
r5='#  ##'
s1='#####'
s2='#    '
s3='#####'
s4='    #'
s5='#####'
t1='#####'
t2='  #  '
t3='  #  '
t4='  #  '
t5='  #  '
u1='#   #'
u2='#   #'
u3='#   #'
u4='#   #'
u5='#####'
v1='#   #'
v2='#   #'
v3=' # # '
v4=' # # '
v5='  #  '
w1='# # #'
w2='# # #'
w3='# # #'
w4='# # #'
w5='#####'
x1='#   #'
x2=' # # '
x3='  #  '
x4=' # # '
x5='#   #'
y1='#   #'
y2=' # # '
y3='  #  '
y4='  #  '
y5='  #  '
z1='#####'
z2='   # '
z3='  #  '
z4=' #   '
z5='#####'
wu1='     '
wu2='     '
wu3='     '
wu4='     '
wu5='     '

#use list to define each single letter

aa=[a1,a2,a3,a4,a5]
bb=[b1,b2,b3,b4,b5]
cc=[c1,c2,c3,c4,c5]
dd=[d1,d2,d3,d4,d5]
ee=[e1,e2,e3,e4,e5]
ff=[f1,f2,f3,f4,f5]
gg=[g1,g2,g3,g4,g5]
hh=[h1,h2,h3,h4,h5]
ii=[i1,i2,i3,i4,i5]
jj=[j1,j2,j3,j4,j5]
kk=[k1,k2,k3,k4,k5]
ll=[l1,l2,l3,l4,l5]
mm=[m1,m2,m3,m4,m5]
nn=[n1,n2,n3,n4,n5]
oo=[o1,o2,o3,o4,o5]
pp=[p1,p2,p3,p4,p5]
qq=[q1,q2,q3,q4,q5]
rr=[r1,r2,r3,r4,r5]
ss=[s1,s2,s3,s4,s5]
tt=[t1,t2,t3,t4,t5]
uu=[u1,u2,u3,u4,u5]
vv=[v1,v2,v3,v4,v5]
ww=[w1,w2,w3,w4,w5]
xx=[x1,x2,x3,x4,x5]
yy=[y1,y2,y3,y4,y5]
zz=[z1,z2,z3,z4,z5]
wu=[wu1,wu2,wu3,wu4,wu5]

#use dic to show the connection between letter and pattern

engdic={'a':aa,'b':bb,'c':cc,'d':dd,'e':ee,'f':ff,'g':gg,'h':hh,
        'i':ii,'j':jj,'k':kk,'l':ll,'m':mm,'n':nn,'o':oo,'p':pp,'q':qq,
        'r':rr,'s':ss,'t':tt,'u':uu,'v':vv,'w':ww,'x':xx,'y':yy,'z':zz,' ':wu}

#define the output of each line

def line0(x,s):
    li=list(s)
    length=len(li)
    line_0=''
    for i in li:
        line_0=line_0+' '+engdic[i][0]
    return '|'+(x[0]-1)*' ' + line_0 + (61-x[0]-length)*' '+'|'

def line1(x,s):
    li=list(s)
    length=len(li)
    line_1=''
    for i in li:
        line_1=line_1+' '+engdic[i][1]
    return '|'+(x[0]-1)*' ' + line_1 + (61-x[0]-length)*' '+'|'

def line2(x,s):
    li=list(s)
    length=len(li)
    line_2=''
    for i in li:
        line_2=line_2+' '+engdic[i][2]
    return '|'+(x[0]-1)*' ' + line_2 + (61-x[0]-length)*' '+'|'

def line3(x,s):
    li=list(s)
    length=len(li)
    line_3=''
    for i in li:
        line_3=line_3+' '+engdic[i][3]
    return '|'+(x[0]-1)*' ' + line_3 + (61-x[0]-length)*' '+'|'

def line4(x,s):
    li=list(s)
    length=len(li)
    line_4=''
    for i in li:
        line_4=line_4+' '+engdic[i][4]
    return '|'+(x[0]-1)*' ' + line_4 + (61-x[0]-length)*' '+'|'

#define the function to draw a single picture

def draw(x,y,s):
    for i in range(3):
        print
    print 40*' '+'-'*len(line0(x,s))
    for up in range(y[0]-1):
        print 
    print 40*' '+line0(x,s)
    print 40*' '+line1(x,s)
    print 40*' '+line2(x,s)
    print 40*' '+line3(x,s)
    print 40*' '+line4(x,s)
    for down in range(26-y[0]):
        print 
    print 40*' '+'-'*len(line0(x,s))

#functions to make block move

def move_ul():
    x[0]=x[0]-1
    y[0]=y[0]-1

def move_ur():
    x[0]=x[0]+1
    y[0]=y[0]-1

def move_dl():
    x[0]=x[0]-1
    y[0]=y[0]+1

def move_dr():
    x[0]=x[0]+1
    y[0]=y[0]+1

#define the way to change direction 

def change(x,y,count):

    if (x[0],y[0]) == (1,1) and count[0] == 0:
        count[0]=3

    if (x[0],y[0]) == (61-len(s),1) and count[0] == 1:
        count[0]=2

    if (x[0],y[0]) == (1,26) and count[0] == 2:
        count[0]=1

    if (x[0],y[0]) == (61-len(s),26) and count[0] == 3:
        count[0]=0

    if y[0] == 1:
        if count[0] == 1:
            count[0] = 3
        if count[0] == 0:
            count[0] = 2

    if y[0] == 26:
        if count[0] == 3:
            count[0] = 1
        if count[0] == 2:
            count[0] = 0

    if x[0] == 1:
        if count[0] == 2:
            count[0] = 3
        if count[0] == 0:
            count[0] = 1

    if x[0] == 61-len(s):
        if count[0] == 1:
            count[0] = 0
        if count[0] == 3:
            count[0] = 2           
            

#define the way to run
def run():
    while True:
        draw(x,y,s)
        change(x,y,count)
        if count[0] == 0:
            move_ul()
        elif count[0] == 1:
            move_ur()
        elif count[0] == 2:
            move_dl()
        elif count[0] == 3:
            move_dr()
        time.sleep(0.1)
        
        

x = [1]
y = [1]
count = [0]
s=raw_input('What do you want to show? ')
run()
