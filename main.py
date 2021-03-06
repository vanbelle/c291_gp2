import destroy_db
import pop_db
import retrieve_1
import retrieve_2
import retrieve_3
import sys

f = open("answers", "a", 1)
n = '\n'

def handleInputCommand(): 
	global inputCommand
	inputCommand = sys.argv[1]
	if inputCommand != "btree" and inputCommand != "hash" and inputCommand != "indexfile":
		print("Invalid startup paramater")
		sys.exit()

handleInputCommand()

while(1):
	print('')
	print('Main Menu')
	print('1. Create and populate a database')
	print('2. Retrieve records with a given key')
	print('3. Retrieve records with a given data')
	print('4. Retrieve records with a given range of key values')
	print('5. Destroy the database')
	print('6. Quit')	
	
	i = input('Select Option (1-6):')
	while(1):
		print('')
		if i == '1':
			p = pop_db.pop_db(inputCommand)
			break
		elif i == '2':
			key = input('Enter a key: ')
			value = retrieve_1.retrieve_1(inputCommand,key)
			try:
				f.write(key + n)
				f.write(value.value + n)
				f.write(n)
			except:
				pass
			break
		elif i == '3':
			data = input('Enter data: ')
			r = retrieve_2.retrieve_2(inputCommand,data)
			try:
				for item in r.keys:
					f.write(item + n)
					f.write(data + n)
					f.write(n)
			except:
				pass
			break
		elif i == '4':
			low = input('Enter the lower bound: ')
			high = input('Enter the upper bound: ')
			val = retrieve_3.retrieve_3(inputCommand,low,high)
			try:
				for item in val.keys:
					f.write(item[0] + n)
					f.write(item[1] + n)
					f.write(n)
			except:
				pass				
			break
		elif i == '5':
			d = destroy_db.destroy_db()
			break
		elif i == '6':
			f.seek(0)
			f.truncate()
			f.close()
			sys.exit()
		else: 
			print('Invalid Entry')
			i = input('Select Option (1-6):')
