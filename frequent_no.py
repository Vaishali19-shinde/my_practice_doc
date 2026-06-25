########################### most frequent number in a list
k=[1,1,1,2,2,3,4,5]
print(k)
for f_no in set(k):
    k_count=k.count(f_no)

    if k_count>1:
        print(f_no)



#numbers = [1, 2, 3, 2, 4, 2, 5]
#specific_count = numbers.count(2)
#print(specific_count)