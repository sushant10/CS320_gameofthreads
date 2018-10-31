from django.test import TestCase
from .models import File

# Create your tests here.
class FileModelTests(TestCase):
	def file_contains_all_data(self):
		"""
		Every field for a file object should have something
		"""
		file = File.objects.get(pk=7980620180909)
		self.assertEqual(file.name, "79806-2018-09-09.json")
		self.assertEqual(file.filePath, "files/79806-2018-09-09.json")
		print(file.dataDate)
		#self.assertIs(file.dataDate, "2018")
		self.assertEqual(file.SystemID, "79806")
