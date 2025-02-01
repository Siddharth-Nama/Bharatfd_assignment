from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()

    # Language-specific translations
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.question_hi or not self.question_bn:
            translator = Translator()
            if not self.question_hi:
                self.question_hi = translator.translate(self.question, src='en', dest='hi').text
            if not self.question_bn:
                self.question_bn = translator.translate(self.question, src='en', dest='bn').text
        super().save(*args, **kwargs)

    def get_translated_question(self, lang="en"):
        translations = {
            "hi": self.question_hi,
            "bn": self.question_bn,
        }
        return translations.get(lang, self.question)

    def __str__(self):
        return self.question
