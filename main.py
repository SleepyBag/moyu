import datetime
import lunardate

YEAR_NUMBERS = "〇一二三四五六七八九"
MONTH_NUMBERS = "〇一二三四五六七八九十冬腊"
DAY_NAMES = [None] + ['初' + i for i in "一二三四五六七八九十"] + \
	['十' + i for i in "一二三四五六七八九"] + \
	['二十'] + ['廿' + i for i in "一二三四五六七八九"] + \
	['三十']
WEEKDAY_NAMES = ['星期' + dayname for dayname in "一二三四五六日"]
GAP_NAMES = ['今天', '明天', '后天', '大后天', '四天后', '五天后']

today = datetime.datetime.now()
lunardate = lunardate.LunarDate.fromSolarDate(today.year, today.month, today.day)

def lunardate_to_str(lunardate):
	ans = ''
	for y in str(lunardate.year):
		y = int(y)
		ans += YEAR_NUMBERS[y]
	ans += "年"
	ans += MONTH_NUMBERS[lunardate.month] + "月"
	ans += DAY_NAMES[lunardate.day]
	return ans

weekday = today.weekday()
print(today.strftime("%Y-%m-%d"), WEEKDAY_NAMES[weekday])
print("阴历：", lunardate_to_str(lunardate), sep='')

print("""
%s好，打工人，工作再累，一定不要忘记摸鱼哦！
有事没事起身去 茶水间/厕所/走廊 走一走，久坐不利于身心健康，钱是老板的，但命是自己的
""" % ("下午" if today.hour >= 12 else "上午"))

weekend_gap = max(4 - weekday, 0)
print(GAP_NAMES[weekend_gap] + "周末")

class Holiday:
	def __init__(self, name, month, day, lunar=False):
		self.name = name
		self.month = month
		self.day = day
		self.lunar = lunar

import chinese_calendar

HOLIDAY_NAMES = {
	'National Day': '国庆节',
	'Labour Day': '劳动节',
	"New Year's Day": '元旦',
	'Tomb-sweeping Day': '清明节',
	'Spring Festival': '春节',
	'Dragon Boat Festival': '端午节',
	'Mid-autumn Festival': '中秋节',
}

holidays = chinese_calendar.get_holidays(today, datetime.date(today.year, 12, 31))
holiday_gaps = {}
for holiday in holidays:
	_, holiday_name = chinese_calendar.get_holiday_detail(holiday)
	if holiday_name is not None:
		holiday_name = HOLIDAY_NAMES[holiday_name]
		if holiday_name not in holiday_gaps:
			holiday_gaps[holiday_name] = (holiday - today.date()).days - 1

for holiday_name in holiday_gaps:
	print('距离', holiday_name, '假期还有', holiday_gaps[holiday_name], '天')