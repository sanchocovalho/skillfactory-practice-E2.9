from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from datetime import datetime, timedelta
from django.utils import timezone
from threading import Timer #, Thread
from time import sleep

from sender_app.models import EmailSender, UNSENT_STATUS, SENT_STATUS, ERROR_STATUS
from sender_app.forms import EmailSenderForm

def send_mail_thread(mail_id, subject, message, email): #delay):
    try:
        # sleep(delay)
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False
        )
        mail = EmailSender.objects.get(id=mail_id)
        mail.send_time = timezone.get_current_timezone().localize(datetime.now())
        mail.send_status = SENT_STATUS
        mail.save()
    except:
        mail = EmailSender.objects.get(id=mail_id)
        mail.send_time = timezone.get_current_timezone().localize(datetime.now())
        mail.send_status = ERROR_STATUS
        mail.save()

class EmailSenderCreate(CreateView):
    model = EmailSender
    form_class = EmailSenderForm
    success_url = reverse_lazy('sender_app:email_list')
    template_name = 'email_send.html'

    def dispatch(self, request, *args, **kwargs):
        if 'btnSendMsg' in request.POST:
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            email = request.POST.get('email')
            delay = float(request.POST.get('delay'))
            time_zone = timezone.get_current_timezone()
            create_time = time_zone.localize(datetime.now())
            send_time = time_zone.localize(datetime.now() + timedelta(seconds=delay))
            mail = EmailSender.objects.create(
                subject=subject,
                message=message,
                email=email,
                delay=delay,
                create_time=create_time,
                send_time=send_time,
                send_status=UNSENT_STATUS
                )
            mail.save()
            # thread = Thread(target=send_mail_thread, args=(mail.id, subject, message, email, delay))
            # thread.start()
            timer_thread = Timer(interval=delay, function=send_mail_thread, args=(mail.id, subject, message, email))
            timer_thread.start()
            return redirect('/list/')
        return super(EmailSenderCreate, self).dispatch(request, *args, **kwargs)

class EmailSenderList(ListView):
    model = EmailSender
    template_name = 'email_list.html'

    def get_queryset(self):
    	return EmailSender.objects.order_by('create_time').reverse()[:10]

def update_status(request):
    queryset = EmailSender.objects.order_by('create_time').reverse()[:10]
    return render(request,'email_update.html',{'object_list': queryset})
