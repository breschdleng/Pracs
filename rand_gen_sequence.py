"""
Given a random num gen randint() from 1 to 5 construct
another set of rand nums between 1 to 7 with equal prob.
"""
import random




def gen_rand_in_range(m,n):

    if m>n:
        print("m should be greater than n")
        return None
    # 0,1,2,3,4 each with prob 0.2
    a = random.randint(1,m)
    b = random.randint(1,m)

    quotient = int((m**2+m)/n)
    new_rand = m*a+b

    if(new_rand < quotient*n):
        print(new_rand,quotient)
        ret_val = new_rand%n

        return ret_val
    else:
        return gen_rand_in_range(m,n)

if __name__ == '__main__':
    n = 7
    m = 5

    sol = gen_rand_in_range(m,n)
    print(sol)
