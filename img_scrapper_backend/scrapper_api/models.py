from django.db import models


class Image(models.Model):
    image_link = models.URLField(max_length=300)

    def __str__(self):
        return self.image_link
