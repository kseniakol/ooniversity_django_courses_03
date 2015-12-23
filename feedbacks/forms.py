from django import forms
from feedbacks.models import Feedback


# Create your views here.
class FeedbackForm(forms.ModelForm):
    from_email = forms.EmailField(required=False)

    class Meta:
        model = Feedback
