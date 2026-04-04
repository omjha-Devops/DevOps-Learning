def get_reward(average):
    if average >= 90:
        return "A", "Pizza"
    elif average >= 80:
        return "B", "Chocolate"
    elif average >= 70:
        return "C", "Ice cream"
    else:
        return "D", "Nothing"
#taking input from user
score1 = float(input("Enter score for subject 1: "))
score2 = float(input("Enter score for subject 2: "))
score3 = float(input("Enter score for subject 3: "))

average = (score1 + score2 + score3) / 3

grade, reward = get_reward(average)

#output
print("---Your Result---")
print(f"Your average score is: {average:.2f}")
print(f"Your grade is: {grade}")
print(f"Your reward is: {reward}")
if reward == "Nothing":
    print("I am not evil but you are not getting any reward, sorry son! ")
else:
    print(f"Congratulations! You grade is {grade} and you have won a {reward}!")