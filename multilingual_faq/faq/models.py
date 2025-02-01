from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator
from django.core.cache import cache

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()

    # Language-specific translations
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    question_fr = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.question_hi or not self.question_bn or not self.question_fr:
            translator = Translator()
            if not self.question_hi:
                self.question_hi = translator.translate(self.question, src='en', dest='hi').text
            if not self.question_bn:
                self.question_bn = translator.translate(self.question, src='en', dest='bn').text
            if not self.question_fr:
                self.question_fr = translator.translate(self.question, src='en', dest='fr').text
        super().save(*args, **kwargs)

    def get_translated_question(self, lang="en"):
        translations = {
            "hi": self.question_hi,
            "bn": self.question_bn,
            "fr": self.question_fr,
        }
        return translations.get(lang, self.question)

    def __str__(self):
        return self.question


def get_translated_question(self, lang="en"):
    faq_translation_key = f"faq_{self.id}_question_{lang}"
    translated_text = cache.get(faq_translation_key )

    if not translated_text:
        translations = {
            "hi": self.question_hi,
            "bn": self.question_bn,
            "fr": self.question_fr,
        }
        translated_text = translations.get(lang, self.question)
        cache.set('faq_translation_key', translated_text, timeout=3600)  # Cache for 1 hour

    return translated_text
