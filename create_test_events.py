#!/usr/bin/env python
import os
import sys
import django
from datetime import datetime, timedelta

# Djangoの設定を読み込み
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'schedule_app.settings')
django.setup()

from events.models import Event

def create_test_events():
    """テスト用のイベントデータを作成"""
    
    # 既存のイベントを削除
    Event.objects.all().delete()
    
    # 今日の日付を取得
    today = datetime.now().date()
    
    # テストイベントを作成
    events = [
        {
            'title': '朝の会議',
            'location': '会議室A',
            'start_time': datetime.combine(today, datetime.min.time().replace(hour=9, minute=0)),
            'end_time': datetime.combine(today, datetime.min.time().replace(hour=10, minute=0)),
            'description': '週次朝会議'
        },
        {
            'title': 'ランチミーティング',
            'location': 'カフェ',
            'start_time': datetime.combine(today, datetime.min.time().replace(hour=12, minute=0)),
            'end_time': datetime.combine(today, datetime.min.time().replace(hour=13, minute=0)),
            'description': 'チームランチ'
        },
        {
            'title': 'プロジェクトレビュー',
            'location': '会議室B',
            'start_time': datetime.combine(today, datetime.min.time().replace(hour=15, minute=0)),
            'end_time': datetime.combine(today, datetime.min.time().replace(hour=16, minute=30)),
            'description': '月次プロジェクトレビュー'
        }
    ]
    
    # 明日のイベントも作成
    tomorrow = today + timedelta(days=1)
    tomorrow_events = [
        {
            'title': 'クライアントMTG',
            'location': 'オンライン',
            'start_time': datetime.combine(tomorrow, datetime.min.time().replace(hour=14, minute=0)),
            'end_time': datetime.combine(tomorrow, datetime.min.time().replace(hour=15, minute=0)),
            'description': '新規案件について'
        }
    ]
    
    # イベントを作成
    for event_data in events + tomorrow_events:
        Event.objects.create(**event_data)
        print(f"Created event: {event_data['title']}")
    
    print(f"Total events created: {Event.objects.count()}")

if __name__ == '__main__':
    create_test_events()
