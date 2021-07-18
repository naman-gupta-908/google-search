from googlesearch import search
query=input("Let's search something : ")
for i in search(query,lang='en',num=10,start=0,stop=10,pause=2):
    print(i)