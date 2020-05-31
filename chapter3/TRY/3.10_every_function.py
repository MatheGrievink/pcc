#Create a small list and print
countries = ['nederland', 'engeland', 'belgie', 'luxemburg', 'duitsland']
print(countries)

#Get a specific element from list in Title
print(f"Wannes woont in {countries[2].title()}.")

#Get the fist and last element from list
print(f"Ik woon in {countries[0].title()}, in een plaats vlak bij {countries[-1].title()}.")

#Change value
countries[3] = "frankrijk"
print("Let's change luxemburg for frankrijk:")
print(countries)    #nederland engeland belgie frankrijk duitsland

#Append value to end
countries.append('luxemburg')
print("Let's add luxemburg back:")
print(countries)    #nederland engeland belgie frankrijk duitsland luxemburg

#Insert value to beginning
countries.insert(0, 'Spanje')
print("Let's insert Spanje")
print(countries) #spanje nederland engeland belgie frankrijk duitsland luxemburg

#Delete value
del countries[3]
print("belgie is verwijderd:")
print(countries)    #spanje nederland engeland frankrijk duitsland luxemburg

#Pop a value
popped_country = countries.pop()
print("Let's pop the last country on the list:")
print(countries)        #spanje nederland engeland frankrijk duitsland
print(popped_country)

#Pop specific by number
pop_country = countries.pop(0)
print("Let's pop the first country on the list:")
print(countries)        #nederland engeland frankrijk duitsland
print(pop_country)

#Remove specific by value
rem_country = countries.remove('engeland')
print("Let's remove engeland by value")
print(countries)        #nederland frankrijk duitsland
print(rem_country)

#Add some more countries
countries.append('luxemburg')
countries.append('spanje')
countries.append('zweden')
countries.append('engeland')
print("Let's add some countries")
print(countries)    #nederland frankrijk duitsland luxemburg spanje zweden engeland

#Temporary sorted
print("This is the list alphabetic:")
print(sorted(countries))   #duitsland engeland frankrijk luxemburg nederland spanje zweden 

#Temporary reverse sorted
print("This is the list reverse alphabetic:")
print(sorted(countries, reverse=True)) #zweden spanje nederland luxemburg frankrijk engeland duitsland

#Reversed
print("This is the list in reverse:")
countries.reverse() 
print(countries) #engeland zweden spanje luxemburg duitsland frankrijk nederland

#Count
print(f"There are {len(countries)}  countries in the list")