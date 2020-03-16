from django import forms
from sender_app.models import EmailSender

class EmailSenderForm(forms.ModelForm):

    subject = forms.CharField(
        label='Заголовок',
        widget=forms.TextInput(
            attrs={
                'required': True,
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Введите заголовок письма'
            }
        )
    )

    message = forms.CharField(
        label='Сообщение',
        widget=forms.Textarea(
            attrs={
                'required': True,
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Введите сообщение письма'
            }
        )
    )

    email = forms.CharField(
        label='Получатель',
        widget=forms.TextInput(
            attrs={
                'required': True,
                'class': 'form-control',
                'placeholder': 'Введите электронную почту'
            }
        )
    )

    delay = forms.IntegerField(
        label='Задержка отправки',
        widget=forms.TextInput(
            attrs={
                'required': True,
                'type': 'number',
                'class': 'form-control',
                'placeholder': 'Введите задержку отправки письма'
            }
        )
    )

    class Meta:
        model = EmailSender
        fields = ('subject', 'message', 'email', 'delay')
