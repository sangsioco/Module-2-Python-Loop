# Task 1 Randomly select mood for days
import random
moods = ["Happy", "Sad", "Enrgertic", "Calm"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for i in range(len(days)):
    random_mood = random.choice(moods)
print(f"On {days[i]}, I feel {random_mood}.")
