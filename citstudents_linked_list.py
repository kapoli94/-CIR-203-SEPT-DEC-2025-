student1 = {
    "name": "Paul Ogutu",
    "adm_no": "CIT/00089/024",
    "subjects": {
        "Data structures": "B",
        "Algorithms": "A",
        "Databases": "B"
    },
    "next": None
}

student2 = {
    "name": "Hellen Wanjiru",
    "adm_no": "CIT/00090/024",
    "subjects": {
        "Data structures": "A",
        "Algorithms": "C",
        "Databases": "A"
    },
    "next": None
}

student3 = {
    "name": "Angela Paula",
    "adm_no": "CIT/00091/024",
    "subjects": {
        "Data structures": "B",
        "Algorithms": "A",
        "Databases": "C"
    },
    "next": None
}

# Linking the nodes
student1["next"] = student2
student2["next"] = student3

# Traversing the linked list
head = student1
current = head

while current is not None:
    print("Name:", current["name"])
    print("Admission Number:", current["adm_no"])
    print("Subjects and Grades:")
    for subject, grade in current["subjects"].items():
        print("   ", subject, ":", grade)
    print()
    current = current["next"]
