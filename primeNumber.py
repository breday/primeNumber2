def primeNum(number):
    
#0 and 1 are not prime numbers 
    if number < 2:
        print (number,"not considered a Prime number")

#number divisible by two
    elif number == 2:
        print (number,"is Prime number") 

#checks if the mod is zero to determine if items in range(2,x) are prime numbers 
    for n in range(2, number):
        if number % n == 0:
            return (number,"is not a Prime number")

    for n in range(2,number):
	    if (number % 2 == 0) or (number % 5 == 0):
	        return (n," is a Prime Number")
	        break
	

#returnresults
print(primeNum(28))
