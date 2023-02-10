# import csv

# with open('Recipes.csv') as csvfile:
# readCSV = csv.reader(csvfile, delimiter=',')
# for row in readCSV:
	# print(row)
	# print(row[0])
	# print(row[0],row[1],row[2],)

# import csv

# with open('Recipes.csv') as csvfile:
# readCSV = csv.reader(csvfile, delimiter=',')
# recipeName = []
# ingredients = []
# for row in readCSV:
	# rName = row[0]
	# ingredient = row[3]

	# recipeName.append(rName)
	# ingredients.append(ingredient)

# print(recipeName)
# print(ingredients)

import csv

with open('Recipes.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	dates = []
	recipeName = []
	ingredients = []
	instructions = []
	nutritionalValue = []
	
	for row in readCSV:
		date = row[0]
		rName = row[1]
		ing = row[2]
		ins = row[3]
		nValue = row[4]

		dates.append(date)
		recipeName.append(rName)
		ingredients.append(ing)
		instructions.append(ins)
		nutritionalValue.append(nValue)

	print(dates)
	print(recipeName)
	print(ingredients)
	print(instructions)
	print(nutritionalValue)

# now, remember our lists?

whatDate = input('What recipe for the date: ')
dateVal = dates.index(whatDate)
theRecipeName = recipeName[dateVal]
theIngredients = ingredients[dateVal]
theInstructions = instructions[dateVal]
# print('The recipe of',whatDate,'is:',theRecipeName)
# print('The ingredients of ',theRecipeName,' are:\n',theIngredients,sep='')
# print('Instructions:\n',theInstructions,sep='')

RecipeNameVar = 'The recipe for '+whatDate+ ' is ' +theRecipeName+ '.\n'
#print(RecipeNameVar)
IngredientsVar = 'The ingredients for '+theRecipeName+ ' are: \n' +theIngredients+ '.'
#print(IngredientsVar)
InstructionsVar = 'The instructions for '+theRecipeName+ ' are: \n' +theInstructions+ '.'
#print(InstructionsVar)

recipeForTheDay = RecipeNameVar + IngredientsVar + InstructionsVar

from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "ACe2ebb8fe83dbb6cf051567c368ba577e" 
AUTH_TOKEN = "603a10e2cc0f650f9e66c8bcd5c387b8" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
client.messages.create(
	to="+15624139276", 
	from_="+15624453551", 
    body=recipeForTheDay, 
    # media_url="https://c1.staticflickr.com/3/2899/14341091933_1e92e62d12_b.jpg", 
)