#anagrams.py

def anagrams(a,b) :
    a_count,b_count=0,0
    for i in a :
        a_count=a_count+ord(i)
    for j in b :
        b_count=b_count+ord(j)
    if(a_count==b_count):
        print('both are anagrams')

anagrams('python','thnoyp')
