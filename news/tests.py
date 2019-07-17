from django.test import TestCase
from .models import Editor, Article, tags

# Create your tests here.
class EditorTestclass(TestCase):
    def setUp(self):
        self.kimberly = Editor(first_name = 'kimberly',last_name = 'kardashian', email='kimkay@gmail.com')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.kimberly,Editor))
    
    def test_save(self):
        self.kimberly.save_Editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors)>0)
        