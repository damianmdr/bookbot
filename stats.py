def wordcount(booktext):
    count = 0
    words = booktext.split()
    for i in words:
        count +=1
    return count

def charcount(booktext):
    chardict = {}
    low = booktext.lower()
    for i in low:
        if i not in chardict:
            chardict[i] = 1
        else:
            chardict[i] +=1
    return chardict

def getpriority(data):
    return data['num']

def sorting(chardict):
    initiallist = []
    for i in chardict:
        if i.isalpha() == True:
            b = {"char": i, "num": chardict[i]}
            initiallist.append(b)
        else:
            pass 

    
    newlist = sorted(initiallist, key=getpriority, reverse=True)
    return newlist

