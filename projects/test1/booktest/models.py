from django.db import models

# Create your models here.


class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()

    def __str__(self):
        return self.btitle.encode('utf-8')


class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=10000)
    hbook = models.ForeignKey(BookInfo)

    def gender(self):
        if self.hgender:
            return 'male'
        else:
            return 'female'

    gender.short_description = 'gender'

    def __str__(self):
        return self.hname.encode('utf-8')


