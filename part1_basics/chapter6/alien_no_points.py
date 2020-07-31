#Create a dictionary with no 'points'
alien_0 = {'color': 'green', 'speed': 'slow'}

#Print 'points', results in KeyError
#print(alien_0['points'])

#Print 'points' using get
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)