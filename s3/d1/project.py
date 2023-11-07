
def allocate_projects(employees, projects):
    assignments = []

    for employee in employees:
        for project in projects:
            if employee["current_project"] is None and set(project["required_skills"]).issubset(set(employee["skills"])):
                employee["current_project"] = project["name"]
                assignments.append({"employee": employee["name"], "project": project["name"]})
                break

    return assignments


employees = [
    {"name": "John", "skills": ["Python", "Database"], "current_project": None},
    {"name": "Emma", "skills": ["Java", "Testing"], "current_project": None},
    {"name": "Kelly", "skills": ["Python", "Java"], "current_project": None}
]

projects = [
    {"name": "Project A", "required_skills": ["Python", "Database"]},
    {"name": "Project B", "required_skills": ["Java", "Testing"]},
    {"name": "Project C", "required_skills": ["Python", "Java"]}
]

assignments = allocate_projects(employees, projects)
print(assignments)

