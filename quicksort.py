
array=[434,1,12,4,2,8,2,1,35,45,-5,222,0,-8,212]
print(array)



def sort(a):
    if len(a)>1:
        pivot=len(a)//2
        left=[x for x in a if x<a[pivot] ]
        mid=[x for x in a if x==a[pivot]]
        right = [x for x in a if x > a[pivot]]
        if not left and not right:
            return left+mid+right
        left=sort(left)
        mid = sort(mid)
        right=sort(right)

        return left+mid+right
    else:
        return a



print(sort(array))


