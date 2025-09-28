# 🧪 Civic Data Types Invocation

# Strings
greeting = "Welcome to Module 2"
print(greeting)

# Lists
tools = ["Python", "boto3", "requests"]
print("Tools we invoke:", tools)

# Dictionaries
learner = {"name": "Ganesan", "role": "Legacy Steward"}
print("Learner profile:", learner)
learner.update({"learningGoal": "Objective to become Cloud-AI Integration Engineer"})
print(f"{learner.get('name')} learning goal is: {learner.get('learningGoal')}")