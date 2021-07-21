L1=[None,None,None]
L1[0]=str(input('Protein 1 name: '))
L1[1]=float(input('First weighing of protein 1 in gr:'))
L1[2]=float(input('Second weighing of protein 1 in gr:'))
L2=[None,None,None]
L2[0]=str(input('Protein 2 name: '))
L2[1]=float(input('First weighing of protein 2 in gr:'))
L2[2]=float(input('Second weighing of protein 2 in gr:'))
L3=L1+L2
a=[]
for i in L3:
    if i == 10:
        a.append(1)
if any(a)==True:
    print('Weighing of 10gr has been found in L3')
else:
    print('Weighing of 10gr has not been found in L3')
L4=[None,None,None]
L4[0]=str(input('Protein 3 name: '))
L4[1]=float(input('First weighing of protein 3 in gr:'))
L4[2]=float(input('Second weighing of protein 3 in gr:'))
L3=L1+L2+L4
del L3[0:3]
print('Reversed L3 now is',list(reversed(L3)))
        
