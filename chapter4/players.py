#Make a list
players = ['charles', 'martina', 'micheal', 'florance', 'eli']

#Print players 0,1,2
print(players[0:3])

#Print players 1,2,3
print(players[1:4])

#Print players 0,1,2,3
print(players[:4])

#Print players 2,3,4
print(players[2:])

#Print the last 3 players
print(players[-3:])

#For loop
print("Here are the first three players on my team:")
for player in  players[:3]:
    print(player.title())