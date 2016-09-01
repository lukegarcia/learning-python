# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 18:52:55 2016

@author: lugarcia
"""

##use dictionary to store information, i.e. assign values
mydict = dict()
mydict["dogs"] =14
mydict["fish"] ="slumberland"
mydict["dogs"]+=3
##print mydict

##condensed, e.g., ** refers to x*10^2

##print dict([(x, x**2) for x in (2, 4, 6)])

##using 'for' to replace character in string

str ="UP and down went the seesaw. Up it went. Down it went."
##print str

## for "y" can be any value, it's just something to refer to
for y in ["."]:
    str = str.replace(y, ":-*")
##print str
str = str.upper()
##print str
##print set(str.upper().split())

## a simple function

def square(x):
    ##return x*x

## a function that counts the number of unique letters in a word

##def uniquelet(w):
    d = dict()
    for char in w:
        d[char]=1
        return len(d.keys())
##print uniquelet("dog")

##API application pgramming interface
##ways to interface with an app through a program, think how yelp can embed google maps rather than linking to it

##Procedures; map inputs to outputs

##def <name> any string that starts with the letter 'anything used a s variables'

##def <name> (<parameters/inputs>):

def restofstring(s):
    return s[1:]
    
##print restofstring('audacity')

import twitter

#Authorizing access to twitter api

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

## test authentication
print twitter_api

## test with yahoo where on earth ID, entire world = 1, US = 23424977
WORLD_WOE_ID = 1
US_WOE_ID = 23424977

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id=US_WOE_ID)

## test
#print world_trends
#print
#print us_trends

##GET STARTED WITH Udacity BEFORE CONTINUING!!###############################################

##Udacity Quizzes: Procedures
#def rest_of_string(s):
    #return s[1:]
##print rest_of_string('audacity')

#def square(x):
    #return x*x
##print square(5)


## This takes EXACTLY 3 arguments!!!!    
def sum3(x, y, z):
    return x+y+z
x=1
y=2
z=3
##print sum3(x, y, z)

def abbaize(x,y):
    return(x+y+y+x)
x='dog'
y='cat'
##print abbaize(x,y)

##def abbaize(a, b):
    ##return a + b + b + a
##print abbaize('a','b')
##print abbaize('dog', 'cat')
    
#print find_second(danton, 'audace')
danton = "De l'audace, encore de l'audace, toujours de l'audace"

def find_second(search, target):
    first = search.find(target)
    second = search.find(target, first+1)
    return second
##print find_second(danton, 'audace')

danton = "De l'audace, encore de l'audace, toujours de l'audace"
##def find_second(search, target):
    ##first = search.find(target)
    ##return search.find(target, first+1)
##print find_second(danton, 'audace')

##comparison signs, e.g., != not equal, == equal

def absolute(x):
    if x<0:
        x = -x
    return x
##print absolute(3)
    
def bigger(a, b):
    if a > b:
        return a
    return b
##print bigger (2, 5)

##def bigger(a, b):
    if a > b:
        return a
    if b > a:
        return b
##print bigger(2, 5)
        
##def bigger(a, b):
    if a > b:
        return a
    else:
        return b
##print bigger(2, 5)
        
##def bigger(a, b):
    if a > b:
        r = a
    else:
        r = b
    return r
##print bigger(2,5)

def is_friend(name):
    if name[0] =='D':
        return True
    else:
        return False
##print is_friend('Diane')
        
##def is_friend(name):
    return name[0]=='D'

##print is_friend('Pablo')

##def is_friend(name):
    if name[0]=='D':
        return True
    else:
        if name[0]=='N':
            return True
        else:
            return False
##print is_friend('Dave')

##def is_friend(name):
    if name[0]=='D':
        return True
    if name[0]=='N':
        return True
    return False
##print is_friend('Doug')

##def is_friend(name):
    if name[0]=='D':
        return True
    if name[0]=='N':
        return True
    else: 
        return False
##print is_friend('Doug')

## OR will stop if first operand is True

##def is_friend(name):
    return name[0]=='D'or name[0]=='N'
    
##print is_friend('Doug')
    

        
## YOU DON'T NEED TO TYPE PRINT AT THE END OF A PROCEDURE TO EXECUTE!!
def print_numbers(n):
    i = 0
    while i < n:
        i = i + 1
        print i
##print_numbers(3)

##def print_numbers(n):
    i = 0
    while i < n:
        i = i + 1
        print i
##print_numbers(0)
        
## use variable to keep track of the results so far

def factorial(n):
    result = 1
    while n >= 1:
        result = result * n
        n = n - 1
    return result
##print factorial(3)
    
##variable.find('string to find', starting point, e.g. 3)

##def sum3(a, b, c):
    ##print a+b+c
##sum3(1, 2, 3)

#def sum3(a,b,c):
    #return a+b+c
#print sum3(1, 2, 3)

##def factorial(n):
    #print n
    #print '*'
    #y = n-1
    #print y
    #print'*'
    #z = y -1
    #print z
##factorial(4)

##def factorial(n):
    #i = 1
    #while n>1:
        #i = i * n
        #print n
        #n = n - 1    
#factorial(3)

#def factorial(n):
    #result = 1
    #while n > 1:
        #result = result * n
        #n = n - 1
        #print result
        #print n
#factorial(3)

#def factorial(n):
    #print 1 * n
    #print '*'
    #while n > 1:
        #n = n - 1
        #print n
        #if n != 1:
            #print '*'
#factorial(4)

#############BACK TO TWITTER#########################
print world_trends
