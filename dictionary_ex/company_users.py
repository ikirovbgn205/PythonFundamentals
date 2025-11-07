companies = {}

while True:
    command = input().split(" -> ")
    if command[0] == "End":
        break

    company_name, employee_id = command[0], command[1]

    if company_name not in companies.keys():
        companies[company_name] = []

    if employee_id in companies[company_name]:
        continue
    else:
        companies[company_name].append(employee_id)

for company_name in companies.keys():
    print(f"{company_name}")
    for employee_id in companies[company_name]:
        print(f"-- {employee_id}")

