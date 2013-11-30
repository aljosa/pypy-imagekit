from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import resize, crop

class Photo(models.Model):
    name = models.TextField()
    user = models.ForeignKey(User, related_name="+", null=True, blank=True, on_delete=models.SET_NULL)
    photo = models.ImageField(upload_to='user/photos/%Y/%m/%d')
    date = models.DateTimeField(auto_now_add=True)
    order = models.PositiveIntegerField(default=0)

    thumb = ImageSpecField(source='photo',
            processors=[resize.ResizeToFill(140, 140),],
            options={'quality': 90})
    thumbnail_image = ImageSpecField(source='photo',
            processors=[crop.Crop(100, 100),],
            options={'quality': 90})
    gallery_thumb = ImageSpecField(source='photo',
            processors=[resize.ResizeToFill(154, 114),],
            options={'quality': 90})
    popup = ImageSpecField(source='photo',
            processors=[resize.ResizeToFit(width=960),],
            options={'quality': 90})
    news_small = ImageSpecField(source='photo',
            processors=[crop.Crop(250, 100),],
            format='JPEG',
            options={'quality': 90})
    news_smallest = ImageSpecField(source='photo',
            processors=[crop.Crop(60, 60),],
            format='JPEG',
            options={'quality': 90})
    home_news_smallest = ImageSpecField(source='photo',
            processors=[resize.ResizeToFill(60, 60),],
            format='JPEG',
            options={'quality': 90})
    news = ImageSpecField(source='photo',
            processors=[crop.Crop(620, 360),],
            format='JPEG',
            options={'quality': 90})
    news_index = ImageSpecField(source='photo',
            processors=[resize.ResizeToFill(380, 160),],
            format='JPEG',
            options={'quality': 90})

    # avatar
    profile_thumb = ImageSpecField(source='photo',
            processors=[resize.ResizeToFill(160, 160),],
            format='JPEG',
            options={'quality': 90})

    # academia/level specs
    logo = ImageSpecField(source='photo',
            processors=[resize.ResizeToFit(140, 100),],
            format='JPEG',
            options={'quality': 90})
    list_thumb = ImageSpecField(source='photo',
            processors=[resize.ResizeToFill(44, 44),],
            format='JPEG',
            options={'quality': 90})
    list_thumb_fit = ImageSpecField(source='photo',
            processors=[resize.ResizeToFit(44, 44),],
            format='JPEG',
            options={'quality': 90})


    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('order', 'name',)
