from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def days_to_month_end():
    date_str = input("日付を YYYY-MM-DD 形式で入力してください: ")
    try:
        # 指定された日付をdatetimeオブジェクトに変換
        specified_date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("無効な日付形式です。正しい形式で再入力してください。")
        return

    current_date = specified_date
    print(f"\n{specified_date.strftime('%Y-%m-%d')} から過去の各月末までの日数:")

    # 日付を遡り、各月末への日数を計算
    while current_date.year > 2020:  # 遡りたくない年を制限
        # 前月の末日を取得
        last_day_of_prev_month = (current_date.replace(day=1) - timedelta(days=1))
        days_diff = (specified_date - last_day_of_prev_month).days
        print(f"{last_day_of_prev_month.strftime('%Y-%m-%d')}: {days_diff} days ago")
        
        # 1か月前に移動
        current_date -= relativedelta(months=1)

days_to_month_end()
