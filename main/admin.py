from django.contrib import admin

# Register your models here.

##### Added on 10july2020
from .models import *

admin.site.register(Consult)

admin.site.register(Profile)
admin.site.register(Astro_Profile)
admin.site.register(Wallet)

################################################### Horoscope models

admin.site.register(PersonalHoroscope)

admin.site.register(CreatedHoroscope)

admin.site.register(DailyHoroscope)

admin.site.register(WeeklyHoroscope)

admin.site.register(MonthlyHoroscope)

admin.site.register(YearlyHoroscope)

##################################################### Panchang models

admin.site.register(DailyPanchang)

admin.site.register(DailySolarCycle)

admin.site.register(HinduMonthYear)

admin.site.register(DailyTimings)

################################################### Kundli models

admin.site.register(Kundli)

admin.site.register(KundliMatch)

################################################### Numerology Models

admin.site.register(DailyNumerology)

admin.site.register(WeeklyNumerology)

admin.site.register(MonthlyNumerology)

admin.site.register(YearlyNumerology)

################################################## Tarot Models

admin.site.register(YearlyTarot)

admin.site.register(TarotArticle)

admin.site.register(TarotQuestion)

admin.site.register(TarotAnswer)

################################################# Love Models

admin.site.register(Love)

admin.site.register(Post)

##############################################


admin.site.register(PalmReading)

admin.site.register(PalmReply)

admin.site.register(Festivals)

admin.site.register(ChineseZodiac)

admin.site.register(BabyNames)