from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Post(models.Model):
    sn0 = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    content = RichTextField()
    slug = models.CharField( max_length=130)
    image=models.ImageField(upload_to='postimages')
    timeStamp = models.DateTimeField(default=timezone.now)
  

    def __str__(self):
        return self.title + ' by ' + self.author

    def save(self, *args, **kwargs):
        super(Post,self).save(*args, **kwargs)
        
        img = Image.open(self.image.path)
        if img.height > 500 or img.width >500:
            output_size = (500,500)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('blogPost', kwargs={'pk':self.pk})
    

    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile,self).save(*args, **kwargs)
        
        img = Image.open(self.image.path)
        if img.height > 300 or img.width >300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

