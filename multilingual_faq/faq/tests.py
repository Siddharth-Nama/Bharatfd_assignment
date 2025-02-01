from django.test import TestCase
from .models import FAQ

class FAQModelTest(TestCase):

    def setUp(self):
        """Set up test data"""
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="<p>Django is a Python web framework.</p>",
            question_hi="डीजैंगो क्या है?",
            question_bn="ডিজাঙ্গো কি?"
        )

    def test_faq_creation(self):
        """Test if FAQ object is created correctly"""
        faq = FAQ.objects.get(question="What is Django?")
        self.assertEqual(faq.question, "What is Django?")
        self.assertEqual(faq.question_hi, "डीजैंगो क्या है?")
        self.assertEqual(faq.question_bn, "ডিজাঙ্গো কি?")

    def test_translation_method(self):
        """Test if translation retrieval works"""
        faq = FAQ.objects.get(question="What is Django?")
        self.assertEqual(faq.get_translated_question("hi"), "डीजैंगो क्या है?")
        self.assertEqual(faq.get_translated_question("bn"), "ডিজাঙ্গো কি?")
        self.assertEqual(faq.get_translated_question("fr"), "What is Django?")  # Default to English

