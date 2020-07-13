import random
from csv import DictWriter

from faker import Faker

faker = Faker()

with open("employees.csv", "w", newline="") as file:
    fieldnames = [
        "first_name",
        "last_name",
        "role",
        "email",
        "username",
        "password",
    ]
    writer = DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for a in range(1, 200):
        first_name = faker.first_name()
        last_name = faker.last_name()
        role = faker.job()
        email = f"{first_name}_{last_name}@employeeregister.com"
        username = f"{first_name}{random.randint(0, 999)}"
        password = faker.uuid4()

        writer.writerow(
            {
                "first_name": first_name,
                "last_name": last_name,
                "role": role,
                "email": email,
                "username": username,
                "password": password,
            }
        )
