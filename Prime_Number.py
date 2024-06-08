class PrimeNumber:
    def is_prime_num(num):
        if num <= 1:
            return False
        elif num == 2:
            return True
        else:
            for i in range (2, num):
                if num % i == 0:
                    return False
            return True
    
    isprime = []
    val1 = int(input("starting Value"))
    val2 = int(input("End Value"))
    for num in range (val1,val2):
        if is_prime_num(num):
            isprime.append(num)
         
    print("Prime numbers from 1 to 30:", isprime)
