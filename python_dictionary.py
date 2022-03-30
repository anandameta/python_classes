var = {}                    #in python any var that get inclosed by {} curly braces is called dictionary.
print(var)                    
print(type(var))

var = {"dhoni",33}          #if we add two var like this it is called 'set'
print(var)                     
print(type(var))


var = {'name':'dhoni' , 'age':33} #if we want to add two var in dictionary we have to use : between both var.
print(var)


##var = {'name':'dhoni' , 'age':33}   #it will give error because ....
##print(var[0])                

#no index based direct data retrieval(output) in dictionary.
#in dictionary data's are manipulated(operate) or used via key.
#dictionary is called key value pair.
#because each data we use needs to be stored with specific key.
#storing data with key is generally called as "Hashing" or "Hashtable"


var = {"name":"dhoni", "age": 33} #dictionary is mutable type means
var ['name']= "kohli"             #if the value can change it is called mutable
print(var)                        #while if the value can't change, it is called immutable.


var = {"name":"dhoni","age":33,"name":"ashu"}   #if we use duplicate value, key will be taking last one.  (name:ashu)
print(var)                                  

#keys are unique, you can not repeat
#dictionary is called as "un oredered collection"

var = {'name':'dhoni',9:33,9.43:'ashu',('a','b'):'veena',True:"rahul"} 
var["name"]="kohli"                   #we can store string,number,decimal num, tuple,reserved word as key of dictionary.
print(var)                           # but only if the data is immutable.

var = {"name":"dhoni"}               #if we want to add a new key in existing distionary than we can add like this.
var["country"] = "india"
print(var)

var = {"name":"dhoni","team":"csk"}
output = var["team"]            #if we want output of particuler key than we can use this method.
print(output)

var = {"name":"dhoni","team":"csk"}
var1 = {"age":33}               #if we want to add two or more dictionary we can add like this. {**var,**var1,**var2}
var2 = {"country":"india"}
output = {**var,**var1,**var2}
print(output)

var = {"name":["dhoni","kohli"],"team":("csk","rcb"),"sports":{"cricket":["sachin","dravid"]}}
print
(var)                        #we can add list,tuple and one more dictionary in Dictionary as well.


var = {"name":["dhoni","kohli"],"team":("csk","rcb"),"sports":{"cricket":["sachin","dravid"]}}
output = var["sports"]["cricket"][1]    #if we want output as "sachin" thn we can follow this method.
print(output)

var = {"name":["dhoni","kohli"],"team":("csk","rcb"),"sports":{"cricket":["sachin","dravid"]}}
var["name"][1] = "rohit"  #if we want to replace any key with other key than we can do like this.
print(var)

##var = {"name":["dhoni","kohli"],"team":("csk","rcb"),"sports":{"cricket":["sachin","dravid"]}}
##output = var("country")   # it will give an error because we dont have any var as "country" 
##print(output)

var = {"name":["dhoni","kohli"],"team":("csk","rcb"),"sports":{"cricket":["sachin","dravid"]}}
output = var.get("country", "sorry key not found")
print(output)
print("welcome")            #but if we use var.get function, it will show "sorry key not found" and it will continue on the next line.


