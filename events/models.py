from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class User(models.Model):
    POSITION_CHOICES = [
        ('GK', 'ゴールキーパー'),
        ('DF', 'ディフェンダー'),
        ('MF', 'ミッドフィールダー'),
        ('FW', 'フォワード'),
    ]
    
    name = models.CharField(max_length=100, verbose_name='名前')
    age = models.PositiveIntegerField(verbose_name='年齢')
    position = models.CharField(max_length=2, choices=POSITION_CHOICES, verbose_name='ポジション')
    jersey_number = models.PositiveIntegerField(unique=True, verbose_name='背番号')
    
    def __str__(self):
        return f"{self.name} (#{self.jersey_number})"
    
    class Meta:
        ordering = ['jersey_number']