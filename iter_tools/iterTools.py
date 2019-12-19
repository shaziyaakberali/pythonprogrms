import itertools
#count
# counter=itertools.count(start=5,step=2.2)
# print(next(counter))
# print(next(counter))

#zip
lst=[100,200,300,400,500,600]
dailydata=list(zip(itertools.count(),lst))
print(dailydata)

#repeat
# counter=itertools.repeat(2,times=3)
# print(next(counter))
# print(next(counter))

#starmap
sq=itertools.starmap(pow,[(0,2),(1,2),(2,3)])
print(list(sq))

#combination
# lst=['a','b','c','d']
# result=itertools.combinations(lst,3)
# for item in result:
#     print(item)

#permutation
# lst=['a','b','c','d']
# result=itertools.permutations(lst,2)
# for item in result:
#     print(item)

#product with repeat
# number=[1,2,3,4,5]
# result=itertools.product(number,repeat=3)
# for item in result:
#     print(item)

#chain to combine
# letters=['a','b','c']
# numbers=[1,2,3,4,5]
# names=['aaa','bbb','ccc']
# combined=itertools.chain(letters,numbers,names)
# for item in combined:
#     print(item)

#slice
# result=itertools.islice(range(10),1,5)
# result=itertools.islice(range(10),1,5,2) #step=2
# for item in result:
#     print(item)
#
#compress
lst=['a','b','c','d']
val=[1,1,0,1]
result=itertools.compress(lst,val)
for item in result:
    print(item)
