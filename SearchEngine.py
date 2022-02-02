"""Make a search engine 
list of strings is already given to you
take input from user what word or sentence they are searching for
diplay user their desired result in decreasing order of relevence

eg. lists= ['mayank is a very good boy', 'this is a very good work and good result', 'this is all about python']
search query = good
output = 
2 search result in 0.009 second 
this is a very good work and good result
mayank is a very good boy
"""

sentences=['Python is used in Progaraming', 'Python is not Python snake',"python python python this is good", 'Computer is a machine on which we code', 'mayank is a very good boy', 'good is good and bad is bad']

c=list()
relevance=0
b=list()
j=1

if __name__ == "__main__":
    text=input('Enter your query string: ')
    result=0

    for i in sentences:
        c=i.split()
        for t in c:
            if t.lower() == text.lower():
                if relevance >=2:
                    b.insert(0, i)
                    result += 1
                    break
                else:
                    b.insert(j, i)
                    j+=1
                result+=1
                relevance+=1
            else:
                exit
if relevance >=2:
    b.pop(len(b)-1)
    print(f'{result -1} results found: ')
    print(b)
else:
    print(f'{result} results found: ')
    print(b)
