employee_happiness = list(map(int, input().split()))
factor = int(input())

employees = list(map(lambda x : x * factor, employee_happiness))
filtered = list(filter(lambda x : x >= (sum(employees) / len(employees)), employees))

if len(filtered) >= len(employee_happiness) / 2:
    print(f'Score: {len(filtered)}/{len(employees)}. Employees are happy!')
else:
    print(f'Score: {len(filtered)}/{len(employees)}. Employees are not happy!')
