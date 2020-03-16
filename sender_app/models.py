from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

UNSENT_STATUS = 1
SENT_STATUS = 2
ERROR_STATUS = 3

class EmailSender(models.Model):

    STATUS_CHOICES = [
        (UNSENT_STATUS, "Неотправлено"),
        (SENT_STATUS, "Отправлено"),
        (ERROR_STATUS, "Ошибка отправки"),
    ]

    subject = models.CharField(
        verbose_name = u"Заголовок",
        max_length=100
        )
    message = models.TextField(
        verbose_name = u"Сообщение",
        )
    email = models.EmailField(
        verbose_name = u"Получатель",
        )
    delay = models.IntegerField(
        verbose_name = u"Задержка отправки",
        validators=[
            MinValueValidator(0),
            MaxValueValidator(24 * 60 * 60) # 24 часа в секундах
            ]
        )
    create_time = models.DateTimeField(
        verbose_name = u"Создано",
        auto_now_add=True
        )
    send_time = models.DateTimeField(
        verbose_name = u"Отправлено",
        auto_now_add=True
        )
    send_status = models.SmallIntegerField(
        verbose_name = u"Статус отправки",
        choices=STATUS_CHOICES,
        default=UNSENT_STATUS
        )

    class Meta:
        verbose_name = u"Письма"
        verbose_name_plural = u"Письма"

    def __str__(self):
        return f'{self.subject} {self.email}'

