from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='登録日時')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新日時')
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name='削除日時')
    is_deleted = models.BooleanField(default=False, verbose_name='削除フラグ')

    def __str__(self):
        return self.title

    def soft_delete(self):
        """論理削除を実行"""
        from django.utils import timezone
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        """論理削除を復元"""
        self.is_deleted = False
        self.deleted_at = None
        self.save()

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'イベント'
        verbose_name_plural = 'イベント'

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