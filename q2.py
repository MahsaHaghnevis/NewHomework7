#
##
### created by yseeva
##  word counter
#    aug 14th
def wordCount(string):
    word_count = len(string.split())
    print("Number of words:", word_count)
    

print("enter desired sentence you have : ")
str=input()
wordCount(str)


