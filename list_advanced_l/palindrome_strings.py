words = input().split()
palindrome = input()

lst_palindrome = [word for word in words if word == word[::-1]]
print(lst_palindrome)
print(f"Found palindrome {lst_palindrome.count(palindrome)} times")