var = []                            #basically this [] indicates LIST.
print(type(var))                    #square braces

print(" \
")

var = ["a","b",2,6,3.8]             #we can store any data type like string, number, decimal in list without any restrictions.
print(type(var))                    #list is mutable means

print(" \
")

var = ["a","b",2,6,3.8]            #var[1]= 'b' so it will show number 1 index which is 'b'
print(var[1])                        

print(" \
")

var = ["a","b",2,6,3.8]         #python LIST is mutable.
var[0] = 'dhoni'                #mutable = when somthing is changeable
print(var)                      #so "a" will replace by "dhoni"

print(" \
")

var1 = ['a','b']                #for add two LISTS/ LIST concatination.
var2 = [1,2]
print(var1 + var2)       

print(" \
")

##var = ["a","b",2,6,3.8]       #directory  (DOUBT)
##print(dir(var))

print(" \
")

var = ["a","b",2,6,3.8]             # if we use 'insert' function, data will shift forward
var.insert(0,'dhoni')               # out put will be ["dhoni","a","b",2,6,3.8] 
print(var)


print(" \
")


##var = ["a","b",2,6,3.8]            # it will give an error because we have only 0 to 4 index here, we dont have 10th index
##var[10] = 'dhoni'
##print(var)


print(" \
")

var = ["a","b",2,6,3.8]              # if we want to add any index in the very last so we can use 'var.append'
var.append('dhhoni')
print(var)

print(" \
")

var = ["a","b",2,6,3.8]
var.append(["dhoni","kohli"])        # if we want to add two data in index than we have to cover both by []. 
print(var)                        

print(" \
")

var = ["a","b",2,6,3.8]
var.extend(["dhoni","kohli"])       # if we want to add two more data or extend than we will have to use var.extend
print(var)                          # also cover with []

print(" \
")

var = ["anand","ashu","bharat","zip","ravi"]
var.sort()                            # if we want to sort data in ascending order we will have to use var.sort()
print(var)                           

var = [1,4,7,8,6765,234,546,567]    
var.sort()                            # same for numaric value as well
print(var)                    #we can't sort both numeric and string data in single index.

print(" \
")

var = ["anand","ashu","bharat","zip","ravi"]
var.sort(reverse = True)            # if we want sort in descending order than we will have to use var.sort(reverse = True)
print(var)


var = ["anand","ashu","bharat","zip","ravi"]
output = sorted(var)               # if we want to sort in a new variable than we can do like this.
print(output)
































