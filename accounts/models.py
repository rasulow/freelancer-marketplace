from django.db import models

class Verification(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    code = models.SmallIntegerField()

    class Meta:
        db_table = 'verification'


    def __str__(self) -> str:
        return f'{self.user} --> {self.code}'
