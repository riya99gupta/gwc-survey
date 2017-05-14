import yaml

d = {}

#This function turns the input letter into an index from the string, which corresponds to the choices in the YAML file 
#which is then used to determine the point value. 
def convert(answer): 
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	return alphabet.index(answer) 

print "Welcome to the Girls Who Code survey! Read the following questions, and choose the answer that best fits you."	
print "Type the lowercase letter of the answer choice you pick, and hit enter." 
print "Finish all the questions to recieve your answer of whether GWC is a good fit for you!"
print "  "

class question: 
	#initialize the variable (basically, this is the basic setup for classes)
	def __init__(self, query, key, choices): 
		self.query = query
		self.choices = choices
		self.key = key 

	def ask(self):
		print " "
		print self.query #print the question
		for each in self.choices: 
			print each["choice"] #print all the answer choices
		print " "
		answer = raw_input()  #collect the user's input. it is collected as a string. 
		
		d[str(self.key)] = str(answer) 
		#this is just a way to store their answers in case you ever want to access it in the terminal. To display 
		#the dictionary of answers after each question, remove the # from line 35 
		
		#print d 

		#Manipulating the input string to store an answer:
		if answer == "": 
			print "Don't forget to pick an answer!"
			return self.ask() 
			#if the user accidentally hits enter without an answer, the question will be asked again. 

		value = convert(answer[0]) #this calls the function to convert the input into a value, using only the 
		#first letter of the input string. 

		if value == -1 or value >= len(self.choices):  #this asks the question again, in case the user enters an invalid answer
			print "You need to chose one of the given answers! Try again:"
			return self.ask()
		
		return self.choices[value]["points"] #finds the point value for the corresponding answer choice (that was stored as a number value)

#in the end, the entire function returns a number for a point value that is stored in the total variable. 

data = yaml.load(open("fun.yaml").read())  #this loads the YAML file into python


survey = []
for q in data["survey"]:
	survey.append(question(q["query"], q["key"], q["choices"]))
#survey is a list of the objects in the classes. Remember that each object has several attributes about it (query, key, choices)

total = 0 
for each in survey: 
	total += each.ask() #this is the part that's actually running the function. The ask function calculates the point value after asking the question,
	#and then this adds that point value to a final score. 

# You can chose whether or not to print the final score. Just remove the hashtage in front of line 68. 
# print "your total score is " + str(total)

#To print the response message after gathering the input data from the survey.
for each in data["score"]:  #iterate through the ranges to find the one that the total is in. print that message
	if total in range(*each["Range"]):  #this is breaking up the range from YAML into something usable in python. 
		print str(each["Message"]) 


