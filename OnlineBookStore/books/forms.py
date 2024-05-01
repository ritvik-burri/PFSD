from django import forms
from .models import Book, Request_Book, Feedback

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        
        
class RequestBookForm(forms.ModelForm):
    class Meta:
        model = Request_Book
        fields = ('book_name', 'author')

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'feedback']
