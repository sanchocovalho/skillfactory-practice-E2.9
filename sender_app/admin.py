from django.contrib import admin
from sender_app.models import EmailSender

@admin.register(EmailSender)
class EmailSenderAdmin(admin.ModelAdmin):
    pass
