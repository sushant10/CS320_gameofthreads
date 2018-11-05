from django.test import TestCase
from browser.models import File
from browser.models import System
from django.utils.dateparse import parse_date


class helper():
	
	def fileCompare(file1, file2):
		"""
		This method compares all attributes of a File object and 
		will return True only if they share the same values for all fields

		NOTE: Keep in mind that the FileID is converted to a string in the models.py file
		"""
		if file1 == None or file2 == None:
			return False

		isEqual = ((str(file1.FileID) == str(file2.FileID)) and (file1.name == file2.name) and
				  (file1.filePath == file2.filePath) and (file1.dataDate == file2.dataDate) and
				  helper.systemCompare(file1.SystemID, file2.SystemID))

		return isEqual


	def systemCompare(sys1, sys2):
		"""
		This method will return True only if both systems share the same id and name

		NOTE: Keep in mind that the SystemID is converted to a string in the models.py file
		"""
		if sys1 == None or sys2 == None:
			return False

		return (str(sys1.serialNumberInserv) == str(sys2.serialNumberInserv)) and (sys1.name == sys2.name)


class ModelsTests(TestCase):

	def setUp(self):
		"""
		Create objects that are put into a separate testing database
		"""
		self.system1212 = System.objects.create(serialNumberInserv= "1212",
												name= "Mr. Wu")

		self.file1212_2018_09_09 = File.objects.create(FileID= "121220180909", 
														name= "1212-2018-09-09.json", 
														filePath= "files/1212-2018-09-09.json", 
														dataDate= parse_date("2018-09-09"), 
														SystemID= self.system1212)

		self.file1212_2018_10_26 = File.objects.create(FileID= "121220181026", 
														name= "1212-2018-10-26.json", 
														filePath= "files/1212-2018-10-26.json", 
														dataDate= parse_date("2018-10-26"), 
														SystemID= self.system1212)



		self.system79806 = System.objects.create(serialNumberInserv= "79806",
												 name= "Echo")

		self.file79806_2018_09_09 = File.objects.create(FileID= "7980620180909", 
														name= "79806-2018-09-09.json", 
														filePath= "files/79806-2018-09-09.json", 
														dataDate= parse_date("2018-09-09"), 
														SystemID= self.system79806)


	def test_file_name(self):
		"""
		Simple Test that just checks to make sure that we can access something in the test database
		"""
		file = File.objects.get(pk=121220180909)
		self.assertEqual(file.name, "1212-2018-09-09.json")


	def test_single_system_and_file(self):
		"""
		Tests to make sure that a single system and single file was correctly created by our models.py file
		"""
		sys1 = System.objects.get(pk=1212)
		self.assertTrue(helper.systemCompare(sys1, self.system1212))

		file1 = File.objects.get(pk=121220181026)
		self.assertTrue(helper.fileCompare(file1, self.file1212_2018_10_26))


	def test_two_file_comparison(self):
		"""
		Tests to make sure that two files contain the data we assigned to them in the setUp method
		Then tests to make sure that they do not contain the same content
		"""

		file1 = File.objects.get(pk=121220180909)
		self.assertTrue(helper.fileCompare(file1, self.file1212_2018_09_09))

		file2 = File.objects.get(pk=7980620180909)
		self.assertTrue(helper.fileCompare(file2, self.file79806_2018_09_09))

		self.assertFalse(helper.fileCompare(file1, file2))


	def test_create_existing_system_and_file(self):
		"""
		Verify that a system cannot be created if the primary key is already in use.
		Verify that a file cannot be created if the primary key is already in use.
		"""
		
		try:
			# Try to create a system using an existing primary key, if created fail the test
			newSys = System.objects.create(serialNumberInserv= "79806",
												 name= "Copy")
			self.assertFalse(True)
		except:
			# If there was an exception (which there should be) then pass the test.
			self.assertFalse(False)

		
		try:
			# repeat previous process with a file
			newFile = File.objects.create(FileID= "7980620180909", 
											name= "79806-2018-09-09.json", 
											filePath= "files/79806-2018-09-09.json", 
											dataDate= parse_date("2018-09-09"), 
											SystemID= self.system79806)
			self.assertFalse(True)
		except:
			# Pass the test
			self.assertFalse(False)



