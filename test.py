import random
from datetime import datetime, timedelta
# Sample data
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
sports = ["Football", "Basketball", "Tennis", "Cricket", "Baseball", "Hockey", "Golf", "Rugby", "Swimming", "Boxing"]
domains = ["example.com", "mail.com", "test.org"]

def generate_fav_sports():
    return ",".join(random.sample(sports, k=random.randint(6, len(sports))))

def generate_email(name):
    return f"{name.lower()}@{random.choice(domains)}"


def generate_random_dob(min_age=18, max_age=60):
    """Generate a random date of birth string (YYYY-MM-DD) for a person between min_age and max_age."""
    today = datetime.today()
    start_date = today - timedelta(days=365 * max_age)
    end_date = today - timedelta(days=365 * min_age)
    
    random_date = start_date + (end_date - start_date) * random.random()
    return random_date.strftime("%Y-%m-%d")

# Create the file
with open("person.txt", "w") as file:
    # Write header
    file.write("id\tname\tage\tdob\tfav_sports\temail\n")
    
    # Write data
    for i in range(1, 6):
        name = names[i - 1]
        age = random.randint(18,80)
        dob = generate_random_dob(min_age=18, max_age=80)
        fav_sports = generate_fav_sports()
        email = generate_email(name)
        file.write(f"{i}\t{name}\t{age}\t{dob}\t{fav_sports}\t{email}\n")

print("person.txt file created successfully.")
