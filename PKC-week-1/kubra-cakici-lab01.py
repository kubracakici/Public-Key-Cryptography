#Kubra Cakici

#Method 1: The Euclidean Algorithm


#This method is based on the principle that the greatest common divisor of two numbers does not change if the larger

#number is replaced by its difference with the smaller number. The algorithm can be implemented using recursion or iteration.



def gcd(a, b): #standard implementation of the Euclidean algorithm

    while b:

        a, b = b, a % b #here, we are using the property that gcd(a, b) = gcd(b, a % b)

    return a #we return the gcd of a and b



#-------------------------------------------------------------------------------------------------------------------------------------------------------



#Method 2: The Binary GCD Algorithm



#This method is based on the fact that the GCD of two even numbers is twice the GCD of their halves,

#the GCD of an even number and an odd number is the same as the GCD of the even number's half and the

#odd number, and the GCD of two odd numbers can be reduced to the GCD of their difference and the smaller number.



def binary_gcd(a, b): #standard implementation of the Binary GCD algorithm


    #these are the base cases

    if a == 0:

        return b

    if b == 0:

        return a



    # we find the greatest power of 2 that divides both a and b

    temp = 0



    #first while loop is for finding the greatest power of 2 that divides both a and b

    while ((a | b) & 1) == 0:

        a >>= 1

        b >>= 1

        temp += 1


    #second while loop is for finding the gcd using the properties of even and odd numbers

    while (a & 1) == 0:

        a >>= 1





    #third while loop is for finding the gcd but here were using the property that gcd(a, b) = gcd(b, a - b) when both a and b are odd

    while b != 0:

        while (b & 1) == 0:

            b >>= 1



        if a > b:

            a, b = b, a



        b -= a



    #returning the gcd of a and b multiplied by the greatest power of 2 that divides both a and b

    return a << temp



#-------------------------------------------------------------------------------------------------------------------------------------------------------

#Method 3: The Subtraction Method

#this method is based on the principle that the greatest common divisor of two numbers does not change

# if the larger number is replaced by its difference with the smaller number. The algorithm can be implemented using recursion or iteration.



def subtraction_gcd(a, b): #standard implementation of the Subtraction method



    #Base cases in case one of the numbers is zero

    if a == 0:

        return b

    if b == 0:

        return a

   



    while a != b: #while loop continues until a and b are equal

        if a > b:

            a -= b #if a is greater than b, we subtract b from a

        else:

            b -= a #if b is greater than a, we subtract a from b

    return a #we return the gcd of a and b





#-------------------------------------------------------------------------------------------------------------------------------------------------------



#comperative analysis of the three methods, which one is the most efficient and why



import time



test_cases = [(48, 0), (56, 98), (101, 103), (270, 192),

             (123456, 789012), (123456789, 987654321),

             (1000000007, 1000000009), (1234567890123456789, 9876543210987654321)] #from small to large numbers, including prime numbers and large composite numbers



print ("Comparative Analysis of GCD Algorithms:\n")



for a, b in test_cases:

    start_time = time.time()

    gcd_result = gcd(a, b)

    gcd_time = time.time() - start_time



    start_time = time.time()

    binary_gcd_result = binary_gcd(a, b)

    binary_gcd_time = time.time() - start_time



    start_time = time.time()

    subtraction_gcd_result = subtraction_gcd(a, b)

    subtraction_gcd_time = time.time() - start_time



    print(f"Test Case: GCD({a}, {b})")

    print(f"Euclidean Algorithm: GCD = {gcd_result}, Time Taken = {gcd_time:.10f} seconds")

    print(f"Binary GCD Algorithm: GCD = {binary_gcd_result}, Time Taken = {binary_gcd_time:.10f} seconds")

    print(f"Subtraction Method: GCD = {subtraction_gcd_result}, Time Taken = {subtraction_gcd_time:.10f} seconds\n")