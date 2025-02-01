from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    question_translated = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields = ['id', 'question', 'question_translated', 'answer']

    def get_question_translated(self, obj):
        request = self.context.get('request')
        lang = request.GET.get('lang', 'en')  # Default to English
        return obj.get_translated_question(lang)
