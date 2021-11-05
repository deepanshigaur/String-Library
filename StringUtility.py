class StringUtility:
	def __init__(self, string):
		'''
	stores the string as a parameter 
	args: self(class), string(string)
	return: none
		'''
		self.string = string
		

	def __str__(self):
		'''
	stores the internal string
	args: self(class)
	return: self.string(string)
		'''
		return self.string

	
	def vowels(self):
		'''
	counts the number of the string and returns the number of vowels if its <5 and 		returns many if its >5
	args: self(class)
	return: count(string), many(string)
		'''
		count = 0
		string= ''
		for i in self.string:
			if i in "aeiouAEIOU":
          			 count = count +1
	
		if count < 5:
			return str(count)
		else:
			return "many"
			
	def bothEnds(self):
		'''
	return a string made of the first 2 and last 2 chars of the original string
	args: self(class)
	return: self.string(string)
		'''
		if len(self.string) < 2:
    			return ''

		return self.string[0:2] + self.string[-2:]
		print (self.string)

	def fixStart(self):
		'''
	return a string where all occurrences of its first char have been changed to '*'
	args: self(class)
	return: self.string(string), final_answer(string)
		'''
		if len(self.string) <= 1:
			return self.string
		else:
			char = self.string[0]
			new_string = self.string.replace(char, '*')
			final_answer = char + new_string[1:]
		return final_answer
		

	def asciiSum(self):
		'''
	return an integer that is the sum of all ascii values in the string
	args: self(class)
	return: total(int)
		'''
		total = 0
		for char in self.string:
			AsciiArray = ord(char)
			total += ord(char)
		return total
		print (AsciiArray)

	def cipher(self):
		'''
	return an encoded string by incrementing all letters by the length of the string
	args: self(class)
	return: cipher(string)
		'''
		cipher = ""
		shift = 0
		for i in self.string:
			alphabet = ord(i)
			if i.isalpha():
				if i.isupper():
					shift = 65
				else:
					shift = 97
				alphabet = (alphabet - shift + len(self.string))% 26 + shift
			letter = chr(alphabet)
			cipher += letter
		return cipher
