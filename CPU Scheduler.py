def sortSecond(val): 
    return val[1]
def sortThird(val): 
    return val[2] 
def disp(l):
    for i in range(len(l)):
        print('| ',l[i], end=' |')
    print()
##########################################################
def FCFS(pro):
    pro.sort(key=sortThird)
    arrivall=[0,0,0]
    wt=[0,0,0]
    ta=[0,0,0]
    brust=[0,0,0]
    process=['','','']
    j=1
    for i in range(len(pro)):
        process[i]=pro[i][0]
    for i in range(len(pro)):
        brust[i]=pro[i][1]
    for i in range(len(pro)):
        arrivall[i]=pro[i][2]
    s=arrivall[0]
    for i in range(len(wt)):
        s=s+brust[i]
        wt[j]=s-arrivall[j]
        j=j+1
        if j >=len(wt):
            break
    awt=sum(wt)/len(wt)
    for i in range(len(ta)):
        ta[i]=wt[i]+brust[i]
    ata=sum(ta)/len(ta)
    # print('The Order of Processes is : ',process)
    print('CPU Gantt')
    disp(process)
    print('The Average Waiting Time is = ',round(awt,2),' ms')
    print('The Turn Around Time is = ',round(ata,2),' ms')
    print()
##########################################################
def SJF(pro,ans):
    if ans=='y' or ans=='Y':
        pro.sort(key=sortThird)
    else:
        pro.sort(key=sortSecond)
    arriv=[0]*3
    brust=[0]*3
    process=[0]*3
    lis=[0]*3
    for i in range(len(pro)):
        arriv[i]=pro[i][2]
    for i in range(len(pro)):
        brust[i]=pro[i][1]
    s=arriv[0]
    e=arriv[0]+brust[0]
    lis[0]=[pro[0][0],s,e,pro[0][1],pro[0][2]]
    lis1=[0]*3
    lis2=[0]*3
    wt=[0]*3
    ta=[0]*3
    j=0
    awt=0
    ata=0
    if e>arriv[j+1]:
        while pro[j+1][2]==arriv[j+1]:
            lis1.append(pro[j+1])
            j=j+1
            if j>=len(arriv)-1:
                break
        while lis1.__contains__(0):
            lis1.remove(0)
        # lis1.sort(key=sortSecond)
        for i in range(len(lis1)):
            s=e
            e=e+lis1[i][1]
            lis[i+1]=[lis1[i][0],s,e,lis1[i][1],lis1[i][2]]
    else:
        while True:
            lis2.append(pro[j+1])
            j=j+1
            if j>=len(arriv)-1:
                break
        while lis2.__contains__(0):
            lis2.remove(0)
        for i in range(len(lis2)):
            s=e
            e=e+lis2[i][1]
            lis[i+1]=[lis2[i][0],s,e,lis2[i][1],lis2[i][2]]
    for i in range(len(lis)):
        process[i]=lis[i][0]
    for i in range(len(lis)):
        brust[i]=lis[i][3]
    for i in range(len(wt)):
        wt[i]=lis[i][1]-lis[i][4]
    awt=sum(wt)/len(wt)
    for i in range(len(ta)):
        ta[i]=wt[i]+brust[i]
    ata=sum(ta)/len(ta)
    # print('The Order of Processes is : ',process)
    print('CPU Gantt')
    disp(process)
    print('The Average Waiting Time is = ',round(awt,2),' ms')
    print('The Turn Around Time is = ',round(ata,2),' ms')
    print()
##########################################################
def Priority(pro):
    pro.sort(key=sortThird,reverse=True)
    wt=[0,0,0]
    ta=[0,0,0]
    brust=[0,0,0]
    process=['','','']
    s=0
    for i in range(len(pro)):
        process[i]=pro[i][0]
    for i in range(len(pro)):
        brust[i]=pro[i][1]
    for i in range(len(wt)):
        wt[i]=s
        s=s+brust[i]
    awt=sum(wt)/len(wt)
    for i in range(len(ta)):
        ta[i]=wt[i]+brust[i]
    ata=sum(ta)/len(ta)
    # print('The Order of Processes is : ',process)
    print('CPU Gantt')
    disp(process)
    print('The Average Waiting Time is = ',round(awt,2),' ms')
    print('The Turn Around Time is = ',round(ata,2),' ms')
    print()
##########################################################
def RR(pro,q):
    pro.sort(key=sortThird)
    cop=[['p1',pro[0][1]],['p2',pro[1][1]],['p3',pro[2][1]]]
    listp1=[0]*100
    listp2=[0]*100
    listp3=[0]*100
    wt=[0]*3
    ta=[0]*3
    brust=[0]*3
    awt=0
    ata=0
    lis=[0]*100
    i=0
    while len(pro) != 0:
        for j in range(len(pro)):
            if(pro[j][1]>q):
                if lis[0] == 0:
                    lis.insert(i,[pro[j][0],0,q])
                    pro[j][1]=pro[j][1]-q
                else:
                    s=lis[i-1][2]
                    e=lis[i-1][2]+q
                    lis.insert(i,[pro[j][0],s,e])
                    pro[j][1]=pro[j][1]-q
            else:
                if lis[0] == 0:
                    lis.insert(i,[pro[j][0],0,pro[j][1]])
                    pro[j][1]=0
                else:
                    s=lis[i-1][2]
                    e=lis[i-1][2]+pro[j][1]
                    lis.insert(i,[pro[j][0],s,e])
                    pro[j][1]=0
            i=i+1
        for k in range(len(pro)):
            if pro[k][1] == 0:
                pro.remove(pro[k])
                break
    while lis.__contains__(0):
        lis.pop()
    process=['']*len(lis)
    for i in range(len(lis)):
        process[i]=lis[i][0]
    for i in range(len(lis)):
        if(lis[i][0]=='p1'):
            listp1.insert(i,lis[i])
        elif (lis[i][0]=='p2'):
            listp2.insert(i,lis[i])
        else:
            listp3.insert(i,lis[i])
    while listp1.__contains__(0):
        listp1.remove(0)
    while listp2.__contains__(0):
        listp2.remove(0)
    while listp3.__contains__(0):
        listp3.remove(0)
    s1=listp1[0][1]
    s2=listp2[0][1]
    s3=listp3[0][1]
    for i in range(len(listp1)-1):
        s1=s1+(listp1[i+1][1]-listp1[i][2])
    for i in range(len(listp2)-1):
        s2=s2+(listp2[i+1][1]-listp2[i][2])
    for i in range(len(listp3)-1):
        s3=s3+(listp3[i+1][1]-listp3[i][2])
    wt[0]=s1
    wt[1]=s2
    wt[2]=s3
    awt=sum(wt)/len(wt)
    for i in range(len(cop)):
        brust[i]=cop[i][1]
    for i in range(len(ta)):
        ta[i]=wt[i]+brust[i]
    ata=sum(ta)/len(ta)
    # print('The Order of Processes is : ',process)
    print('CPU Gantt')
    disp(process)
    print('The Average Waiting Time is = ',round(awt,2),' ms')
    print('The Turn Around Time is = ',round(ata,2),' ms')
##########################################################
#GUI
print()
print('Welcome in CPU Scheduler Calculator...')
print('Please, Enter the values of Brust Time...')
p1=int(input('Enter the burst time of p1 : '))
p2=int(input('Enter the burst time of p2 : '))
p3=int(input('Enter the burst time of p3 : '))
print()
print('Do you want to add arrival time ?!')
ans=input('(Enter y/n) : ')
print()
if(ans=='Y' or ans=='y'):
    print('Please, Enter the values of Arrival Time...')
    pa1=int(input('Enter the arrival time of p1 : '))
    pa2=int(input('Enter the arrival time of p2 : '))
    pa3=int(input('Enter the arrival time of p3 : '))
else:
    pa1=0
    pa2=0
    pa3=0
print()
answer='y'
while answer=='y' or answer=='Y':
    print('Please, Choose the algorithm which you want to use...')
    print('(1) FCFS (NoN Preemptive)')
    print('(2) SJF (NoN Preemptive)')
    print('(3) SRTF (Preemptive)')
    print('(4) RR (Preemptive)')
    print('(5) Priority (NoN Preemptive || Don\'t use Arrival Time)')
    print()
    ans1=int(input('Enter your choice : '))
    print()
    while ans1<=0 or ans1>5:
        print('Worng choice, Try again')
        ans1=int(input('Enter your choice : '))
    if ans1==1:
        pro=[['p1',p1,pa1],['p2',p2,pa2],['p3',p3,pa3]]
        FCFS(pro)
    elif ans1==2:
        pro=[['p1',p1,pa1],['p2',p2,pa2],['p3',p3,pa3]]
        SJF(pro,ans)
    elif ans1==3 and (ans!='y' or ans!='Y'):
        pro=[['p1',p1,pa1],['p2',p2,pa2],['p3',p3,pa3]]
        SJF(pro,ans)
    elif ans1==4 and (ans!='y' or ans!='Y'):
        q=int(input('Enter Quantum Time : '))
        pro=[['p1',p1,pa1],['p2',p2,pa2],['p3',p3,pa3]]
        RR(pro,q)
    else:
        print('Please, Enter the Priority of processes...')
        pa1=int(input('Enter the Priority time of p1 : '))
        pa2=int(input('Enter the Priority time of p2 : '))
        pa3=int(input('Enter the Priority time of p3 : '))
        pro=[['p1',p1,pa1],['p2',p2,pa2],['p3',p3,pa3]]
        Priority(pro)
    print('Do you want to try anther algorithm with the same values of brust and arrival time ?!')
    answer=input('( Enter y/n ) : ')
    print()