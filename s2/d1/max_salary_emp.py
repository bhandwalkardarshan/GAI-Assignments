def max_salary_emp(emp):
    if len(emp)==0:
        return None
    
    maxSal = emp[0]["salary"]
    maxSalEmp = emp[0]

    for e in emp:
        if e["salary"] > maxSal:
            maxSal = e["salary"]
            maxSalEmp = e
        
    return maxSalEmp


employees = [
    {"name":"John","salary":3000,"designation":"developer"},
    {"name":"Emma","salary":4000,"designation":"manager"},
    {"name":"Kelly","salary":3500,"designation":"tester"}
]

ans = max_salary_emp(employees)
print("The maximum salary employee is: ", ans)