def say_hi(Name, Age, Hobby, Favourite_Food):
    print("Hi, my name is " + Name + "\n I am " + str(Age) + "years old" + "\n My hobby is " + Hobby + "\n My favourite food is " + Favourite_Food)

print("Program Started")

Name = input("Enter your Name: ")
Age = int(input("Enter your Age: "))
Hobby = input("Enter your Hobby: ")
Favourite_Food = input("Enter your Favourite Food: ")

say_hi(Name, Age, Hobby, Favourite_Food)