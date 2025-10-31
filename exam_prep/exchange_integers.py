a = int(input())
b = int(input())

saved_value_a = a
saved_value_b = b

a , b = b, a

print(f"Before:\na = {saved_value_a}\nb = {saved_value_b}")
print(f"After:\na = {a}\nb = {b}")