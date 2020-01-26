import os,json

class brainfuck():
	ascii = ["", "SOH", "STX", "ETX", "EOT", "ENQ", "ACK", "BEL", "BS", "HT", "\n", "VT", "FF", "CR", "SO", "SI", "DLE", "DC1", "DC2", "DC3", "DC4", "NAK", "SYN", "ETB", "CAN", "EM", "SUB", "ESC", "FS", "GS", "RS", "US", " ", "!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "?", "@", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "[", "BACKSLASH", "]", "^", "_", "`", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "{", "|", "}", "~", "DEL", "\u00c7", "\u00fc", "\u00e9", "\u00e2", "\u00e4", "\u00e0", "\u00e5", "\u00e7", "\u00ea", "\u00eb", "\u00e8", "\u00ef", "\u00ee", "\u00ec", "\u00c4", "\u00c5", "\u00c9", "\u00e6", "\u00c6", "\u00f4", "\u00f6", "\u00f2", "\u00fb", "\u00f9", "\u00ff", "\u00d6", "\u00dc", "\u00f8", "\u00a3", "\u00d8", "\u00d7", "\u0192", "\u00e1", "\u00ed", "\u00f3", "\u00fa", "\u00f1", "\u00d1", "\u00aa", "\u00ba", "\u00bf", "\u00ae", "\u00ac", "\u00bd", "\u00bc", "\u00a1", "\u00ab", "\u00bb", "\u2591", "\u2592", "\u2593", "\u2502", "\u2524", "\u00c1", "\u00c2", "\u00c0", "\u00a9", "\u2563", "\u2551", "\u2557", "\u255d", "\u00a2", "\u00a5", "\u2510", "\u2514", "\u2534", "\u252c", "\u251c", "\u2500", "\u253c", "\u00e3", "\u00c3", "\u255a", "\u2554", "\u2569", "\u2566", "\u2560", "\u2550", "\u256c", "\u00a4", "\u00f0", "\u00d0", "\u00ca", "\u00cb", "\u00c8", "\u0131", "\u00cd", "\u00ce", "\u00cf", "\u2518", "\u250c", "\u2588", "\u2584", "\u00a6", "\u00cc", "\u2580", "\u00d3", "\u00df", "\u00d4", "\u00d2", "\u00f5", "\u00d5", "\u00b5", "\u00fe", "\u00de", "\u00da", "\u00db", "\u00d9", "\u00fd", "\u00dd", "\u00af", "\u00b4", "\u00ad", "\u00b1", "\u2017", "\u00be", "\u00b6", "\u00a7", "\u00f7", "\u00b8", "\u00b0", "\u00a8", "\u00b7", "\u00b9", "\u00b3", "\u00b2", "\u25a0", "nbsp"]
	ignore_comment = 0
	
	def __init__(self,file,output_file):
		if file[-3:] == '.bf':
			self.file = open(file,'r').read()
		else:
			self.file = file
		self.output = output_file

	def write(self):
		with open(self.output,"w") as file:
			file.write(
"""ascii = {}
line= [0]*512
pos = 256""".format(self.ascii[:127])
			)
			file.write(self.translate())
		with open("temp.py","w") as file:
			file.write(
"""ascii = {}
line= [0]*512
pos = 256""".format(self.ascii[:127])
			)
			file.write(self.translate())
	def translate(self):
		self.ident = 0
		self.comment = 0
		self.add = 0
		self.move = 0
		self.index = 0
			
		self.out = ""

		for i in self.file:
			self.index += 1
			if   i == '+':
				self.check(adding=1)
				self.add += 1
			elif i == '-':
				self.check(adding=1)
				self.add -= 1
			elif i == '>':
				self.check(moving=1)
				self.move += 1
			elif i == '<':
				self.check(moving=1)
				self.move -= 1
			elif i == '.':
				self.check()
				self.out += "\n"+"    "*self.ident+"print(ascii[line[pos]],end='')"
			elif i == ',':
				self.check()
				self.out += "\n"+"    "*self.ident+"line[pos] = ascii.index(input())"
			elif i == '[':
				self.check()
				self.out += "\n"+"    "*self.ident+"while line[pos] != 0:"
				self.ident += 1
			elif i == ']':
				self.check()
				self.ident -= 1

			elif not self.ignore_comment:
				if i == '\n': #ignore new lines in code
					self.check()
				elif self.comment:
					self.check(commenting=1)
					self.out += i
				elif i != ' ':
					self.check(commenting=1)
					self.out += "\n"+"    "*self.ident+"# "+i
					self.comment = 1

		return self.out
	
	def check(self,adding=0,moving=0,commenting=0):
		if not adding and self.add != 0:
			self.out += "\n"+"    "*self.ident+"line[pos] {0}= {1}".format(('+' if self.add>0 else "-"),abs(self.add))
			self.add = 0
		if not moving and self.move != 0:
			self.out += "\n"+"    "*self.ident+"pos {0}= {1}".format(('+' if self.move>0 else "-"),abs(self.move))
			self.move = 0
		
		if not commenting:
			self.comment = 0


if __name__ == "__main__":
	try:
		print("Welcome to a brainfuck interpreter by sadru.")
		income  = input("please enter the file name of your code or paste the code directly:\n")
		if income[-3:] == '.bf':
			print("recognized a bf file, now reading from {}".format(income))
		outcome = input("enter the output filename (leave blank if you don't want to create a new file): ")
		if outcome[-3:] == '.py':
			print("recognized a py file, now writing to {}".format(outcome))
		else:
			outcome = "temp.py"

		bf = brainfuck(income,outcome)
		bf.write()
		print("=== FINISHED READING ===")

		if outcome == "temp.py":
			run_infile = 1
		elif input("would you like to run {} [Y/N]: ".format(outcome)).upper() in ("Y","1","YES","RUN","START"):
			run_infile = 1
		else:
			run_infile = 0
		if run_infile:
			print("\n")
			import temp

	finally:
		os.remove("temp.py")
		os.remove("__pycache__/temp.cpython-37.pyc")
		os.removedirs("__pycache__")

	input("\n\n[Program Finished]")