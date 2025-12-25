import random
import datetime

ZODIAC_SIGNS = [
    "牡羊座", "金牛座", "雙子座", "巨蟹座",
    "獅子座", "處女座", "天秤座", "天蠍座",
    "射手座", "魔羯座", "水瓶座", "雙魚座"
]

LUCKY_COLORS = ["紅色", "藍色", "綠色", "黃色", "紫色", "黑色", "白色"]

FORTUNE_QUOTES = [
    "適合主動嘗試新事物。",
    "保持耐心，事情會慢慢好轉。",
    "今天適合專注在自己身上。",
    "避免衝動決定，多思考再行動。",
    "與他人溝通會帶來意外收穫。",
    "放慢腳步，你會看得更清楚。"
]

def _stars():
    level = random.randint(2, 5)
    return "★" * level + "☆" * (5 - level)

def generate_fortune(zodiac=None):
    if zodiac not in ZODIAC_SIGNS:
        zodiac = random.choice(ZODIAC_SIGNS)

    today = datetime.date.today().isoformat()
    random.seed(today + zodiac)  
    # 👉 同一天、同星座運勢固定（很加分）

    fortune_text = f"""🔮 今日運勢（{zodiac}）

📅 日期：{today}

整體運勢：{_stars()}
愛情運勢：{_stars()}
財運運勢：{_stars()}
幸運色：{random.choice(LUCKY_COLORS)}

💡 一句話建議：
{random.choice(FORTUNE_QUOTES)}
"""
    return fortune_text
