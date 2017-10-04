import smtplib


class Document:
	def __init__(self, title='', content=''):
		self.title=title
		self.content=content

	# def rename_doc(self, title):
	# 	self.title=title
	# 	return self.title

	# Save file to document folder
	def add_content(self, content, file_name):
		self.write_file(file_name=file_name, file=content, folder='documents')

	# Read file from a folder
	def read_content(self, file_name):
		the_file = self.read_file(file_name=file_name, folder='documents')
		return the_file

	def share_doc(self, email_address):
		
		host ="smtp.gmail.com"
		port = 587
		username =""
		password =""
		to_email = [email_address]
		from_email = username

		email_conn = smtplib.SMTP(host,port)
		email_conn.ehlo()
		email_conn.starttls()
		email_conn.login(username,password)
		email_conn.sendmail(from_email,to_email,"")
		email_conn.quit

	@staticmethod
	def write_file(file_name, file, folder):
		file_path = folder + '/' + file_name
		with open(file_path, 'w') as new_file:
			new_file.write(file)

	@staticmethod
	def read_file(file_name, folder):
		file_path = folder + '/' + file_name
		with open(file_path) as read_file:
			the_file = read_file.read()
		return the_file




document = Document()
content = input("Please type something: ")
the_file_name = input("Enter a name to save your file: ")
the_file_name = the_file_name + '.txt'
document.add_content(file_name = the_file_name, content = content)
print('='*20)
print("The save you saved is: \n")
print(document.read_content(the_file_name))







