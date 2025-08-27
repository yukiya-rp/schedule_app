from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Position(models.Model):
    code = models.CharField(max_length=3, unique=True, verbose_name='ポジションコード')
    
    def __str__(self):
        return self.code
    
    class Meta:
        ordering = ['code']

class User(models.Model):
    name = models.CharField(max_length=100, verbose_name='名前')
    age = models.PositiveIntegerField(verbose_name='年齢')
    positions = models.ManyToManyField(Position, verbose_name='ポジション')
    jersey_number = models.PositiveIntegerField(unique=True, verbose_name='背番号')
    
    def __str__(self):
        return f"{self.name} (#{self.jersey_number})"
    
    def get_positions_display(self):
        return ', '.join([pos.code for pos in self.positions.all()])
    
    class Meta:
        ordering = ['jersey_number']