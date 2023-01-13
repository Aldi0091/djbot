from django.db import models


class Message(models.Model):
    message = models.CharField(verbose_name="Message", max_length=200)
    def __str__(self) -> str:
        return super().__str__()


class Receiver(models.Model):
    receiver = models.CharField(verbose_name="Receiver", max_length=200)
    user_token = models.CharField(verbose_name="UserToken", max_length=200, null=True)
    def __str__(self) -> str:
        return super().__str__()


class User(models.Model):
    login = models.CharField(max_length=50, null=False)
    name = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=50)
    ifLogged = models.BooleanField(default=False)
    token = models.CharField(max_length=500, null=True, default="")
    telegram_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.telegram_id)


