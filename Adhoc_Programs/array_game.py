def array_game(A):
    start, end=0, len(A)-1
    while start<=end:
        max=0
        val=0
        counter=A[start] if A[start]<end-start else end-start
        for i in range(counter):
            if A[start+i+1]>max:
                max=A[start+i+1]
                val=i+1
        start=start+val
        if max==0:
            break
    if start==end:
        print('True')
    else:
        print('False')

def array_game2(A):
    furthest_reach_so_far, last_index=0,len(A)-1
    i=0
    while i<=furthest_reach_so_far and furthest_reach_so_far<last_index:
        furthest_reach_so_far=max(furthest_reach_so_far, A[i]+1)
        i+=1
    return furthest_reach_so_far>=last_index
