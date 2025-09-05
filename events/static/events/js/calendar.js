// カレンダー用のJavaScript
let currentDate = new Date();

// イベント名を適切に改行する関数（CSSで制御するため、ここでは改行文字を挿入）
function formatEventTitle(title) {
    // 長いイベント名の場合は適切な位置で改行を促す
    if (title.length > 20) {
        // 20文字を超える場合は、適切な位置で改行を促す
        const words = title.split(' ');
        if (words.length > 1) {
            const midPoint = Math.ceil(words.length / 2);
            const firstHalf = words.slice(0, midPoint).join(' ');
            const secondHalf = words.slice(midPoint).join(' ');
            return firstHalf + ' ' + secondHalf;
        }
    }
    return title;
}

// 祝日名を取得する関数
function getHolidayName(date) {
    const year = date.getFullYear();
    const month = date.getMonth() + 1;
    const day = date.getDate();

    // 2025年の祝日（固定日）
    const fixedHolidays2025 = {
        '2025-01-01': '元日',
        '2025-01-02': '振替休日',
        '2025-02-11': '建国記念の日',
        '2025-02-23': '天皇誕生日',
        '2025-02-24': '振替休日',
        '2025-03-21': '春分の日',
        '2025-04-29': '昭和の日',
        '2025-05-03': '憲法記念日',
        '2025-05-04': 'みどりの日',
        '2025-05-05': 'こどもの日',
        '2025-05-06': '振替休日',
        '2025-08-11': '山の日',
        '2025-09-23': '秋分の日',
        '2025-11-03': '文化の日',
        '2025-11-23': '勤労感謝の日',
        '2025-11-24': '振替休日'
    };

    // 2025年の祝日（月曜日振替）
    const mondayHolidays2025 = {
        '2025-01-13': '成人の日',
        '2025-07-21': '海の日',
        '2025-09-15': '敬老の日',
        '2025-10-13': 'スポーツの日'
    };

    // 2025年以外の場合は一般的な祝日判定
    if (year === 2025) {
        const dateString = `${year}-${month.toString().padStart(2, '0')}-${day.toString().padStart(2, '0')}`;
        return fixedHolidays2025[dateString] || mondayHolidays2025[dateString] || null;
    } else {
        // 一般的な祝日判定（固定日）
        const generalHolidays = {
            [`${year}-01-01`]: '元日',
            [`${year}-02-11`]: '建国記念の日',
            [`${year}-02-23`]: '天皇誕生日',
            [`${year}-05-03`]: '憲法記念日',
            [`${year}-05-04`]: 'みどりの日',
            [`${year}-05-05`]: 'こどもの日',
            [`${year}-08-11`]: '山の日',
            [`${year}-11-03`]: '文化の日',
            [`${year}-11-23`]: '勤労感謝の日'
        };

        const dateString = `${year}-${month.toString().padStart(2, '0')}-${day.toString().padStart(2, '0')}`;
        return generalHolidays[dateString] || null;
    }
}

// 祝日判定用の関数（後方互換性のため残す）
function isHoliday(date) {
    return getHolidayName(date) !== null;
}

// カレンダー表示関数
function renderCalendar() {
    console.log('renderCalendar called');
    console.log('eventData:', eventData);

    const year = currentDate.getFullYear();
    const month = currentDate.getMonth();

    document.getElementById('currentMonth').textContent =
        `${year}年${month + 1}月`;

    const firstDay = new Date(year, month, 1);
    const lastDay = new Date(year, month + 1, 0);

    // カレンダーの開始日を計算（前月の日曜日から）
    const startDate = new Date(firstDay);
    const firstDayOfWeek = firstDay.getDay(); // 0=日曜日, 1=月曜日, ...
    startDate.setDate(startDate.getDate() - firstDayOfWeek);

    const calendarDays = document.getElementById('calendarDays');
    calendarDays.innerHTML = '';

    const today = new Date();
    today.setHours(0, 0, 0, 0);

    // 6週間分の日付を生成（7列 × 6行 = 42日）
    for (let week = 0; week < 6; week++) {
        for (let dayOfWeek = 0; dayOfWeek < 7; dayOfWeek++) {
            const dayIndex = week * 7 + dayOfWeek;
            const currentDay = new Date(startDate);
            currentDay.setDate(startDate.getDate() + dayIndex);

            const dayElement = document.createElement('div');
            dayElement.className = 'calendar-day';

            // デバッグ用：日付と曜日をコンソールに出力
            console.log(`Week ${week}, Day ${dayOfWeek}: ${currentDay.toDateString()}, Day of week: ${currentDay.getDay()}`);

            if (currentDay.getMonth() !== month) {
                dayElement.classList.add('other-month');
            }

            if (currentDay.getTime() === today.getTime()) {
                dayElement.classList.add('today');
            }

            // 休日判定とクラス適用
            const currentDayOfWeek = currentDay.getDay();
            if (currentDayOfWeek === 0) { // 日曜日
                dayElement.classList.add('sunday');
            } else if (currentDayOfWeek === 6) { // 土曜日
                dayElement.classList.add('saturday');
            }

            // 祝日判定と祝日名表示
            const holidayName = getHolidayName(currentDay);
            if (holidayName) {
                dayElement.classList.add('holiday');
            }

            const dayNumber = document.createElement('div');
            dayNumber.className = 'day-number';
            dayNumber.textContent = currentDay.getDate();
            dayElement.appendChild(dayNumber);

            // 曜日と祝日名を表示（今月以外は表示しない）
            if (currentDay.getMonth() === month) {
                // 曜日と祝日名を横並びにするためのコンテナ
                const dayInfoContainer = document.createElement('div');
                dayInfoContainer.className = 'day-info-container';

                const dayOfWeekElement = document.createElement('div');
                dayOfWeekElement.className = 'day-of-week';
                const weekdays = ['日', '月', '火', '水', '木', '金', '土'];
                dayOfWeekElement.textContent = weekdays[currentDay.getDay()];
                dayInfoContainer.appendChild(dayOfWeekElement);

                // 祝日名を表示
                if (holidayName) {
                    const holidayElement = document.createElement('div');
                    holidayElement.className = 'holiday-name';
                    holidayElement.textContent = holidayName;
                    dayInfoContainer.appendChild(holidayElement);
                }

                dayElement.appendChild(dayInfoContainer);
            }

            // その日のイベントを表示
            const dayEvents = eventData.filter(event => {
                const eventDate = new Date(event.start_time);
                return eventDate.getDate() === currentDay.getDate() &&
                    eventDate.getMonth() === currentDay.getMonth() &&
                    eventDate.getFullYear() === currentDay.getFullYear();
            });

            // セルクリック時の処理を設定
            if (dayEvents.length > 0) {
                // イベントがある場合は詳細表示
                dayElement.classList.add('has-events');
                dayElement.classList.add('clickable');

                dayEvents.forEach(event => {
                    const eventElement = document.createElement('div');
                    eventElement.className = 'event-item';
                    eventElement.title = `${event.title} - ${event.location}`;

                    // タイトル（2行まで表示、CSSで制御）
                    const eventTitle = document.createElement('div');
                    eventTitle.className = 'event-title';
                    eventTitle.textContent = formatEventTitle(event.title);
                    eventTitle.title = event.title; // フルタイトルをツールチップに表示
                    eventElement.appendChild(eventTitle);

                    // 場所
                    if (event.location) {
                        const eventLocation = document.createElement('div');
                        eventLocation.className = 'event-location';
                        eventLocation.textContent = event.location;
                        eventElement.appendChild(eventLocation);
                    }

                    // 開始時間-終了時間（hh:mm-hh:mm形式）
                    const eventTime = document.createElement('div');
                    eventTime.className = 'event-time';
                    const startTime = `${event.start_time.getHours().toString().padStart(2, '0')}:${event.start_time.getMinutes().toString().padStart(2, '0')}`;
                    const endTime = `${event.end_time.getHours().toString().padStart(2, '0')}:${event.end_time.getMinutes().toString().padStart(2, '0')}`;
                    eventTime.textContent = `${startTime}-${endTime}`;
                    eventElement.appendChild(eventTime);

                    eventElement.onclick = (e) => {
                        e.stopPropagation(); // セルのクリックイベントを防ぐ

                        // デバッグ用ログ
                        console.log('Event clicked:', event);
                        console.log('Event ID:', event.id);

                        // イベント詳細ページに遷移
                        if (event.id) {
                            window.location.href = `/events/${event.id}/`;
                        } else {
                            console.error('Event ID is undefined:', event);
                            alert('イベントIDが取得できませんでした。');
                        }
                    };
                    dayElement.appendChild(eventElement);
                });

                // イベントがある日のセル全体のクリック処理（余白部分をクリックした時）
                dayElement.onclick = (e) => {
                    // イベント要素がクリックされた場合は何もしない（詳細ページに遷移）
                    if (e.target.closest('.event-item')) {
                        return;
                    }

                    // 余白部分がクリックされた場合はイベント追加ページに遷移
                    // 選択した日付を正しくフォーマット（時刻は9:00に設定）
                    const year = currentDay.getFullYear();
                    const month = String(currentDay.getMonth() + 1).padStart(2, '0');
                    const day = String(currentDay.getDate()).padStart(2, '0');

                    // 時刻は9:00に固定（一般的な営業開始時刻）
                    const hours = '09';
                    const minutes = '00';

                    const selectedDate = `${year}-${month}-${day}T${hours}:${minutes}`;

                    // デバッグ用ログ
                    console.log('Cell background clicked (add new event):', {
                        original: currentDay,
                        formatted: selectedDate,
                        year, month, day, hours, minutes
                    });

                    window.location.href = `/events/create/?date=${selectedDate}`;
                };
            } else {
                // イベントがない場合は追加画面に遷移
                dayElement.classList.add('clickable');
                dayElement.onclick = () => {
                    // 選択した日付を正しくフォーマット（時刻は9:00に設定）
                    const year = currentDay.getFullYear();
                    const month = String(currentDay.getMonth() + 1).padStart(2, '0');
                    const day = String(currentDay.getDate()).padStart(2, '0');

                    // 時刻は9:00に固定（一般的な営業開始時刻）
                    const hours = '09';
                    const minutes = '00';

                    const selectedDate = `${year}-${month}-${day}T${hours}:${minutes}`;

                    // デバッグ用ログ
                    console.log('Selected date:', {
                        original: currentDay,
                        formatted: selectedDate,
                        year, month, day, hours, minutes
                    });

                    window.location.href = `/events/create/?date=${selectedDate}`;
                };
            }

            calendarDays.appendChild(dayElement);
        }
    }
}

// 前月ボタン
function previousMonth() {
    currentDate.setMonth(currentDate.getMonth() - 1);
    renderCalendar();
}

// 次月ボタン
function nextMonth() {
    currentDate.setMonth(currentDate.getMonth() + 1);
    renderCalendar();
}



// ページ読み込み完了時の初期化
document.addEventListener('DOMContentLoaded', function () {
    // イベントデータが存在しない場合の初期化
    if (typeof eventData === 'undefined') {
        window.eventData = [];
    }

    // ボタンのイベントリスナーを設定
    const prevMonthBtn = document.getElementById('prevMonthBtn');
    const nextMonthBtn = document.getElementById('nextMonthBtn');

    if (prevMonthBtn) {
        prevMonthBtn.addEventListener('click', previousMonth);
    }

    if (nextMonthBtn) {
        nextMonthBtn.addEventListener('click', nextMonth);
    }

    // ウィンドウリサイズ時の処理
    let resizeTimeout;
    window.addEventListener('resize', function() {
        clearTimeout(resizeTimeout);
        resizeTimeout = setTimeout(function() {
            renderCalendar();
        }, 100); // 100ms後に再描画
    });

    // 初期表示
    renderCalendar();
});
