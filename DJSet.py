# Task 1 DJ Set

counter = 1

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

for genre in genres:
    print(f"Track {counter}: The genre of this track is {genre}")
    counter += 1

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

# Task 2 Remix Artist
counter = 1


stop_loop = False

while counter <= len(genres) and not stop_loop:
    genre = genres[counter - 1]
    print(f"Track {counter}: The genre of this track is {genre}")

    if genre == "Hip-hop":
        stop_loop = True
    
    counter += 1

# Task 3 Light Show

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']


for track_number in range(len(genres)):

    track_number += 1
    
    genre = genres[track_number - 1]
    
    if genre == "Classical":
       
        continue
 
    print(f"Track {track_number}: The light show is ready for {genre}!")
