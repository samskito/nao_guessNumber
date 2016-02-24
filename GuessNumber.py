class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)

    def onLoad(self):
    	# Set the proxies
        self.memory = ALProxy("ALMemory")
        self.tts = ALProxy("ALTextToSpeech")

        # Insert values to Nao
        self.memory.insertData('minVal', 1)
        self.memory.insertData('maxVal', 10)

    def onInput_onStart(self):
    	# Greetings
        self.customLogger("Guessing number from 1 to 10, please think of a number")

        # Call the function that guesses the number
        self.guessNumber()

    def guessNumber(self):
        # Import random needed
        import random

        #Generate a random integer
        valMin = self.getValue("minVal")
        valMax = self.getValue("maxVal")
        randNumber = random.randint(valMin, valMax)

    	# Asked the person 
        self.customLogger('Is your number ' + str(randNumber) + '?')

        # Insert the guessed number into Nao's memory
        self.memory.insertData("guessedNumber", randNumber)

        # Wait for the touch sensor
        self.onStopped() 

    def onInput_Higher(self):
    	# Get the guessed number
        guessedNumber = self.getValue('guessedNumber')

        # Set the minimum value to the guessed number + 1
        self.memory.insertData('minVal', guessedNumber + 1)

        # Feedback
        self.customLogger('Higher than ' + str(guessedNumber))

        # Guess again
        self.guessNumber()

    def onInput_Lower(self):
        # Get the guessed number
        guessedNumber = self.getValue('guessedNumber')

        # Set the maximum value to the guessed number - 1
        self.memory.insertData('maxVal', guessedNumber - 1)

        # Feedback
        self.customLogger('Lower than ' + str(guessedNumber))

        # Guess again
        self.guessNumber()

    def onInput_Correct(self):
        # Get the guessed number, which is the correct one here
        guessedNumber = self.getValue('guessedNumber')
		
		# Feedback
        self.customLogger('The correct number was ' + str(guessedNumber))

        # Leave the Loop with custom output
        self.onInput_onStop()

    def customLogger(self, dataToLog):
    	# Log and Speak
    	self.logger.info(dataToLog)
        self.tts.say(dataToLog)

    def getValue(self, valueName):
    	# Get a value from Nao's memory
    	try:
    		return self.memory.getData(valueName)
    	except:
    		return "NULL"

    def onInput_onStop(self):
    	# Feedback while exiting
        self.customLogger('Leaving application')

        # Leave the behavior
        self.winning() 