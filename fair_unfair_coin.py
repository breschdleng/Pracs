import random

"""
Given an unfair coin, where probability of HEADS coming up is P and TAILS is (1-P), implement a fair coin from the given unfair coin

Approach: assume an unfair coin that gives HEADS with prob 0.3 and TAILS with 0.7. The objective is to convert this
to a fair set of probabilities of 0.5 each
Solution: use bayes theorem flip the coins twice, if HH or TT then p(HH) == 0.49, p(TT) = 0.09, p(HT) = p(TH) = 0.21

1) flip two coins
2) if HH or TT repeat 1)
3) if different then heads if HT and tails if TH

Bayes' Theorem:
p(head on the first flip / diff results) = p(diff results / head on the first flip)*p(head on the first flip) / p(diff results)
p(diff results / head on the first flip) = p(tails/heads) = 0.3
p(heads on first flip) = 0.7
p(diff results) = p(HT)+p(TH) = 0.21*2
p(head on the first flip / diff results) = 0.3*0.7/0.42 = 0.5  ---answer for a fair coin flip!

"""

"""
1: heads
0: tails
"""
def unfair_coin():
    p_heads = random.randint(0, 100)/100
    if p_heads > 0.5:
        return 1
    else:
        return 0

def unfair_to_fair(a,b):
    p, q = unfair_coin()
    print(b*p, a*q)

if __name__ == '__main__':

    a = unfair_coin()
    b = unfair_coin()

    if a==b:
        unfair_coin()

    if a == 1:
        print("heads")
    else:
        print("tails")



