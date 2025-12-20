from faker import Faker

fake = Faker('ru_RU')

print(fake.name())
print(fake.address())
print(fake.email())

user_data = {
    "name": fake.name(),
    "email": fake.email(),
    "address": fake.address(),
    "age": fake.random_int(min=18, max=100)
}
print(user_data)
print(user_data)