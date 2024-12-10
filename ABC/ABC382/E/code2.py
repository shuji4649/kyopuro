N,Q=map(int,input().split())
S=input()
count1=[0]*(N+1)
count2=[0]*(N+1)
slashes=[]
for i in range(N):
    count1[i+1]=count1[i]+(S[i]=="1")
    count2[i+1]=count2[i]+(S[i]=="2")
    if(S[i]=="/"):
        slashes.append(i)
import bisect
for q in range(Q):
    l,r=map(int,input().split())
    l,r=l-1,r-1
    ans=0
    b_l=bisect.bisect_left(slashes,l)
    b_r=bisect.bisect_right(slashes,r)
    if(b_r==b_l):
        print(0)
        continue
    left=b_l
    right=b_r
    middle=(left+right)//2
    while right-left>0:
        #print(left,right,middle)
        left1Count=count1[slashes[middle]+1]-count1[l]
        right2Count=count2[r+1]-count2[slashes[middle]+1]
        if(right2Count> left1Count):
            ans=max(ans,left1Count)
            left=middle+1
        else:
            ans=max(ans,right2Count)
            right=middle-1
        middle=(left+right)//2
        #ans=max(ans,min(count2[r+1]-count2[slashes[j]+1],count1[slashes[j]+1]-count1[l]))
    if 0<=left<len(slashes):
        left1Count=count1[slashes[left]+1]-count1[l]
        right2Count=count2[r+1]-count2[slashes[left]+1]
        ans=max(ans,min(left1Count,right2Count))
    if 0<=right<len(slashes):
        left1Count=count1[slashes[right]+1]-count1[l]
        right2Count=count2[r+1]-count2[slashes[right]+1]
        ans=max(ans,min(left1Count,right2Count))


    print(ans*2+1)
