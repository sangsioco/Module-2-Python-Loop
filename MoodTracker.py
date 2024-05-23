# Task 1 - Record mood based on the time of day using Nested Loop

import random
moods = ["Happy", "Sad", "Energetic", "Calm"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
times_of_day = ["morning", "afternoon", "evening"]

for day in days:
    for time in times_of_day:
        random_mood = random.choice(moods)
        print(f"On {day} {time}, I feel {random_mood}.")
