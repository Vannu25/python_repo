def simple_interest(p, t, r):
    si = (p * t * r) / 100
    print("the simple interest is :", si)


principal_amt = int(input("The principal amount is? "))
time = int(input("The time period is? "))
rate_of_interest = int(input("The ROI is? "))
simple_interest(principal_amt, time, rate_of_interest)
