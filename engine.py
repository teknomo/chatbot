#chatbot Engine

class Chatbot():
	def __init__(self):
			
		# initially, load knowledge bases
		self.loadResponses()
		self.loadListeningWord()

	# controller of the response
	def respond(self,strInput):
		answer= self.findmatch(strInput)
		if answer=="":
			# cannot find correct answer
			# save this user input for later learning
			self.saveUnknownInput(strInput)
			return self.listen()
		else:
			# knowledge base has known the answer
			return answer


	# responds based on listening words
	def listen(self):
		from random import randint
		r=randint(0, len(self.listeningword)-1)
		answer= self.listeningword[r]
		return answer

	# responds based on user last words
	def findmatch(self,str):
		from random import randint
		values=[value for key, value in self.data.items() if str in key.lower()]
		if values==[]:
			chosen_response=""
		else:
			r=randint(0, len(values[0])-1)
			chosen_response=values[0][r]
		return chosen_response 

	# load knowledge base of common responses
	def loadResponses(self):
		import json
		with open('responses.json', 'r') as fp:
			self.data = json.load(fp)

	# load knowledge base of listening words 
	def loadListeningWord(self):
		import json
		with open('listeningword.json', 'r') as fp:
			self.listeningword = json.load(fp)

	# save the user input if cannot answer 
	# from knowledge base common responses
	def saveUnknownInput(self,strInput):
		f= open("unknownInput.txt","a+")
		f.write(strInput+"\n")
		f.close() 

	def saveConversation(self,strConversation):
		import datetime
		import time
		ts = time.time()
		time_id=datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S')
		f= open("conversation"+time_id+".txt","a+")
		f.write(strConversation)
		f.close() 	
################################
#
# use only for the first time
#
################################

	# to initialize the json
	def initialResponses(self):
		import json
		responses={"hello": ["hi", "hello"],"How are you": ["Fine, thank you. How do you do?", "happy", "Why are you happy?"]}
		with open('responses.json', 'w') as fp:
			json.dump(responses, fp)

	def initialListeningWords(self):
		import json
		listeningword=["And then ...?", "So?", "Ahh, okay, then?", "I am listening", "I am still listening", "I got it", "I understand", "understood",     "This is interesting. And then?", "This is getting interesting. Tell me more about it",     "What happen?", "tell me about it", "tell me about your friend", "what did you do today?",     "Is that so?", "what happen earlier?", "what happen next?", "Really? What happen next?", "Wow, that's great",     "I do not understand. Can you describe it more?", "What is so interesting about it?",     "Is that your opinion or a fact?", "how did you know about it?",     "Did you have a happy childhood?", "Did you hate your father?", "Did you hate your mother?", "Did you hate your sibling?"]
		with open('listeningword.json', 'w') as fp:
			json.dump(listeningword, fp)



# testing this module
if __name__ == "__main__":
	bot=Chatbot()
	print(bot.respond("hi"))
	strConversation="test"
	bot.saveConversation(strConversation)



