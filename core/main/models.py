from django.db import models

# Create your models here.


class HomeMenu(models.Model):
    name = models.CharField('HomeMenu name', max_length=50)
    name1 = models.CharField('HomeMenu name1', max_length=50)
    name2 = models.CharField('HomeMenu name2', max_length=50)
    name3 = models.CharField('HomeMenu name3', max_length=50)
    name4 = models.CharField('HomeMenu name4', max_length=50)
    name5 = models.CharField('HomeMenu name5', max_length=50)
    name6 = models.CharField('HomeMenu name6', max_length=50)
    about = models.TextField('HomeMenu about')
    about1 = models.TextField('HomeMenu about1')
    about2 = models.TextField('HomeMenu about2')
    about3 = models.TextField('HomeMenu about3')
    about4 = models.TextField('HomeMenu about4')
    about5 = models.TextField('HomeMenu about5')
    about6 = models.TextField('HomeMenu about6')
    about7 = models.TextField('HomeMenu about7')
    img = models.ImageField('HomeMenu image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'HomeMenu'
        verbose_name_plural = 'HomeMenues'



class SingleImage(models.Model):
    name = models.CharField('SingleImage name', max_length=50)
    about = models.TextField('SingleImage about')
    about1 = models.TextField('SingleImage about1')
    img = models.ImageField('SingleImage image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'SingleImage'
        verbose_name_plural = 'SingleImages'



class RightImage(models.Model):
    name = models.CharField('RightImage name', max_length=30)
    name1 = models.CharField('RightImage name1', max_length=30)
    about = models.TextField('RightImage about')
    about1 = models.TextField('RightImage about1')
    about2 = models.TextField('RightImage about2', null=True)
    img = models.ImageField('RightImage image', upload_to='media')

    def __str__(self):
       return self.name

    class Meta:
        verbose_name = 'RightImage'
        verbose_name_plural = 'RightImages' 



