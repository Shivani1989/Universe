def parity(num):
     num1=str(num)
     count=0
     for i in num1:
        if i=='1':
            count+=1
     if count%2==0:
             return True
     else:
             return False

def even_odd(A):
    next_even, next_odd=0, len(A)-1
    while next_even<next_odd:
        if A[next_even]%2==0:
            next_even+=1
        else:
            A[next_even], A[next_odd]=A[next_odd], A[next_even]
            next_odd-=1

def dutch_flag_problem(A,a):
    lower, higher=0, len(A)-1
    pivot=A[a]
    for x in range(len(A)):
        for y in range(x+1, len(A)):
            if A[y]<pivot:
                A[x],A[y]=A[y], A[x]
                break
    for i in reversed(range(len(A))):
        if A[i]<pivot:
            break
        for j in reversed(range(i)):
            if A[j]>pivot:
                A[i],A[j]=A[j],A[i]
                break

def dutch_flag_problem_opt(A,a):
    lower, higher=0, len(A)-1
    pivot=A[a]
    for x in range(len(A)):
        if A[x]<pivot:
            A[x],A[lower]=A[lower], A[x]
            lower+=1
    print(A)
    for i in reversed(range(len(A))):
        print('i='+str(i))
        if A[i]<pivot:
            break
        elif A[i]>pivot:
            print(A)
            print('higher='+str(higher))
            print(A[i])
            print(A[higher])
            A[i],A[higher]=A[higher],A[i]
            higher-=1

def Dutch_problem(A,a):
    lower, equal, higher=0,0,len(A)
    pivot=A[a]
    while equal<higher:
        if A[equal]<pivot:
            A[lower],A[equal]=A[equal], A[lower]
            equal, lower=equal+1, lower+1
            print(A)
            print('lower=' +str(lower) + ', equal =' + str(equal)+ ', higher=' + str(higher))
        elif A[equal]==pivot:
            equal+=1
            print(A)
            print('lower=' +str(lower) + ', equal =' + str(equal)+ ', higher=' + str(higher))
        else:
            higher-=1
            A[higher], A[equal]=A[equal], A[higher]
            print(A)
            print('lower=' +str(lower) + ', equal =' + str(equal)+ ', higher=' + str(higher))

def add_one(A):
    for i in reversed(range(len(A))):
        if A[i]==9:
            A[i]=0
        else:
            A[i]+=1
            break
    if A[0]==0:
        A.insert(0,1)

def mult(A,B):
    x=abs(int(''.join(str(i) for i in A)))
    y=abs(int(''.join(str(i) for i in B)))
    sum=0
    if x<y:
        for i in range(x):
            sum=sum+y
    else:
        for i in range(y):
            sum=sum+x
    L= map(int, str(sum))
    if A[0]<0:
        if B[0]>0:
            L[0]=-L[0]
    else:
        if B[0]<0:
            L[0]=-L[0]
    return L
