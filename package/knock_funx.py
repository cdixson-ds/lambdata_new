#my_lambdata/knock_knock.py


if __name__ == "__main__":
    #only run the code below if this script is invoked from the command
    #not if it is imported from another
    print('Hello! I have a joke for you:')
a= input('Knock, knock!\n')
if (a=="Who's there" or a=="who's there" or a=="Who's there?" or a=="who's there?"):
   b=input('Scold\n')
else:
    a=input("Please print 'Who's there?'\n")
    if (a=="Who's there" or a=="who's there" or a=="Who's there?" or a=="who's there?"):
        b=input('Scold\n')
if (b=="Scold who?" or b=="scold who?" or b=="Scold who" or b=="scold who"):
    c='Scold outside let me in!'
    print(c)
else:
    b=input("Please print 'Scold who?'\n")
    if (b=="Scold who?" or b=="scold who?" or b=="Scold who" or b=="scold who"):
       c='Scold outside let me in!'
       print(c)

    

