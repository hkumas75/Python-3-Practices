# -*- coding: utf-8 -*-
# prime numbers presented by hkumas

input_list = []

while len (input_list)+1 <=20:
    try:
        input_int = int (input ("Enter a number: ")) 
        if input_int == 0:
            break        
        input_list.append (input_int)
    except:
        print ("Please enter an integer number!")
        
input_list_edited = [item for item in input_list if item > 1] #number "1" and negative numbers removed from the list

def is_prime_number (input_number): 
    sqrt_input_number = int (input_number**(1/2)) 
    for i in range (2, sqrt_input_number+1):
        if input_number % i == 0:
            return False
            break
    return True

prime_numbers_list = [x  for x in input_list_edited if is_prime_number (x)]

print ("All the numbers you have entered are: ", input_list)
print ("The prime numbers you have entered are: ", prime_numbers_list)
