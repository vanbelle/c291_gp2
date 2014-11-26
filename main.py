import destroy_db
import pop_db
import retrieve_1
import retrieve_2
import retrieve_3

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
	print('')

	while(1):
		if i == '1':
			
			break
		elif i == '2':
			key = input('Enter a key: ')
			value = retrieve_1.retrieve_1(type_option,key)
			print (key,value)
			break
		elif i == '3':
			data = input('Enter data: ')
			keys = retrieve_2.retrieve_2(type_option,data)
			for i in keys:
				print (key,data)
			break
		elif i == '4':
			low = input('Enter the lower bound: ')
			high = input('Enter the upper bound: ')
			values = retrieve_3.retrieve_3(type_option,low,high)
			for pair in values:
				print (pair[0],pair[1])
			break
		elif i == '5':
			destroy_db.destroy_db()
			break		
		elif i == '6':
			exit()
		else: 
			i = input('Invalid Entry, Select Option 1-6:')