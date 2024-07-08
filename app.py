import random
from sqlalchemy import func
from sqlalchemy import and_, not_, or_
from sqlalchemy.orm import sessionmaker
from models import User, engine, session



# Creating Users
user1 = User(username="phi_andhika")
user2 = User(username="pabanasurya")
user3 = User(username="mahakiimm")

# Creating relationships
user1.following.append(user2)
user2.following.append(user3)
user3.following.append(user1)

# Adding users to the session and comitting changes
session.add_all([user1,user2,user3])
session.commit()

print(f"{user1.following = }")
print(f"{user2.following = }")
print(f"{user3.following = }")







'''
# Creating Addresses
address1    = Address(city="New York", state="NY", zip_code="10001")
address2    = Address(city="Los Angeles", state="LA", zip_code="90001")
address3    = Address(city="Chicago", state="CH", zip_code="60601")

# Associating addresses with users
user1.addresses.extend([address1,address2])
user2.addresses.append(address3)

# adding users and addresses
session.add(user1)
session.add(user2)
session.commit()

print(f"{user1.addresses =}")
print(f"{user2.addresses =}")
print(f"{address1.user =}")

'''



'''
#Conditionally Chaining
only_iron_man = True
group_by_age = True

users = session.query(User)

if only_iron_man:
    users   = users.filter(User.name == "Iron Man")

if group_by_age:
    users = users.group_by(User.age)

users = users.all()

for user in users:
    print(f"User age : {user.age}, Name: {user.name}")
'''








#Group users by age
'''
users = session.query(User.name, func.count(User.id)).group_by(User.name).all()

print(users)
'''

#chaining
'''
users_tuple =(
    session.query(User.age, func.count(User.id))
    .filter(User.age > 24)
    .order_by(User.age)
    .filter(User.age < 50)
    .group_by(User.age)
    .all()
)

for age, count in users_tuple:
    print(f"Age: {age} - {count} users")
'''
    
#session.commit()













#CRUD method (Create, Read, Update, Delete)


#CREATE
#untuk menambahkan 1 saja
#user = User(name="Muhammad Hakim", age=21, activities="research")

#semisal banyak, kita bisa langsung add_all
'''
user_2 = User(name="Agni Pulung", age=22, activities="Teaching")
user_3 = User(name="Rafi Dhika", age=21, activities="Sports")
user_4 = User(name="Malvin Nugraha", age=21, activities="Bussines")
'''
#ini commentnya
#session.add_all([user_2,user_3,user_4])
#session.commit()

#READING --> QUERY

#users = session.query(User).all()

#Dapat membaca data secara spesifik, misal user pada index 0
'''
user = users[0]

print(user)
print(user.id)
print(user.name)
print(user.age)
print(user.activities)
'''

#bisa juga seperti ini
#for user in users:
#    print(f"User ID: {user.id},Name: {user.name},Age: {user.age}, Activities: {user.activities}")

#Dapat juga di filter, seperti ini
'''
user = session.query(User).filter_by(id=1).one_or_none()

session.delete(user)

session.commit()
'''


'''
names   = ["Andrew Pip", "Iron Man", "John Doe", "Phil Grave"]
ages    = [20, 21, 22, 23, 25, 27, 30, 35, 60]
act = ["athlete","research","bussines","study"]

for x in range(20):
    user = User(name=random.choice(names), age=random.choice(ages), activities=random.choice(act))
    session.add(user)
'''
#query all users ordered by age (ascending)
'''users = session.query(User).order_by(User.age.desc()).all()

for user in users:
    print(f"User age: {user.age}, Name: {user.name}, ID: {user.id}, 
          Activities: {user.activities}")

'''
#Session = sessionmaker(bind=engine)
#session = Session()
'''
#query all users with ae is equal to 30

users = (
    session.query(User).filter(
        or_(
           not_(User.name == "Iron Man"),
           and_(
               User.age >21,
               User.age<60
           )
        )
    )
).all()

for user in users:
    print(f"user age: {user.age} - {user.name} - {user.id}")

'''

