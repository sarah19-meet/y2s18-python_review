# Write your solution for 1.4 here!

# def is_prime(x):
# 	i =1

# 	pass
def main():
	n=1

is_prime(n)

def is_prime(a):
    x = True 
    for i in (2, a):
            while x:
               if a%i == 0:
                   x = False
               else:
                   x = True


    if x:
        print "prime"
    else:
        print "not prime"

main()
