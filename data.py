from faker import Faker

fake = Faker()

def new_user_created():
    return {
        "name": fake.name(),
        "address": fake.address(),
        "creation_year": fake.year()
    }

if __name__ == "__main__":
    print(new_user_created())