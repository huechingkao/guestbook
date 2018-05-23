from django.db import models

class Message(models.Model):
        user = models.CharField(max_length=50, verbose_name='姓名')
        subject = models.CharField(max_length=200, verbose_name='主旨')
        content = models.TextField(verbose_name='內容')      
        publication_date = models.DateTimeField(auto_now_add=True)

        def __str__(self):
                return self.subject        