from django import forms
from . models import Review


# class ReviewForm(forms.Form):
#     user_name = forms.CharField(max_length=100, label='Your Name')
#     review_text = forms.CharField(widget=forms.Textarea, label='Your Feedback', max_length=500)
#     rating = forms.IntegerField(min_value=1, max_value=5, label='Your Rating')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        labels = {
            'user_name': 'Your Name',
            'review_text': 'Your Feedback',
            'rating': 'Your Rating',
        }