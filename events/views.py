from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Event
from .forms import EventForm

def event_list(request):
    events = Event.objects.all().order_by('start_time')
    return render(request, 'events/event_list.html', {'events': events})

def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'イベントが正常に追加されました。')
            return redirect('event_list')
    else:
        form = EventForm()
        # URLパラメータから日付を取得
        selected_date = request.GET.get('date')
        if selected_date:
            try:
                # ISO形式の日付文字列をパース
                from datetime import datetime
                parsed_date = datetime.fromisoformat(selected_date)
                
                # 終了時刻を開始時刻から1時間後に設定
                end_time = parsed_date.replace(hour=parsed_date.hour + 1)
                
                # デバッグ用ログ
                print(f"Selected date from URL: {selected_date}")
                print(f"Parsed date: {parsed_date}")
                print(f"End time: {end_time}")
                
                # フォームの初期値を設定
                form.initial = {
                    'start_time': parsed_date,
                    'end_time': end_time
                }
            except ValueError as e:
                print(f"Date parsing error: {e}")
                pass  # 日付のパースに失敗した場合は無視
    
    return render(request, 'events/event_create.html', {'form': form})

def event_detail(request, event_id):
    try:
        event = Event.objects.get(id=event_id)
        return render(request, 'events/event_detail.html', {'event': event})
    except Event.DoesNotExist:
        messages.error(request, '指定されたイベントが見つかりません。')
        return redirect('event_list')

def event_delete(request, event_id):
    try:
        event = Event.objects.get(id=event_id)
        if request.method == 'POST':
            event_title = event.title
            event.delete()
            messages.success(request, f'イベント「{event_title}」が削除されました。')
            return redirect('event_list')
        else:
            return render(request, 'events/event_confirm_delete.html', {'event': event})
    except Event.DoesNotExist:
        messages.error(request, '指定されたイベントが見つかりません。')
        return redirect('event_list')