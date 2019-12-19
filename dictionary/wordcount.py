lines="hello hai how are you hello hai"
words=lines.split(" ")
print(words)
dict={}
for word in words:
    if(word not in dict):
        dict[word]=1
    else:
        dict[word]+=1
print(dict)


# words="ABABA"
# dict={}
# for word in words:
#     if(word not in words):
#         dict[words]=1
#     else:
#         print("recursive character found is",word)
#         break
# #print(dict)

