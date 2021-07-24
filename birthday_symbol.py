#!/usr/bin/env python
# coding: utf-8

# ## the relationship between date and zodiac signs and chinese zodiac signs

# In[17]:
#日付だけスプリットされた配列が引数に入る['11','29']
import sys

zodiaclist = [['Aries',321,419],['Taurus',420,520],['Gemini',521,621],
              ['Cancer',622,722],['Leo',723,822],['Virgo',823,922],
              ['Libra',923,1023],['Scorpio',1024,1122],['Sagittarius',1123,1221],
              ['Aquarius',120,218],['Pisces',219,320]]
chinesezodiaclist = [['子',4],['丑',5],['寅',6],['卯',7],
                     ['辰',8],['巳',9],['午',10],['未',11],
                     ['申',0],['酉',1],['戌',2],['亥',3]]


# In[18]:


def zodiacsigns(date):
    zodiacint = int(date[0])*100 + int(date[1])
    for i in range(len(zodiaclist)):
        if zodiacint >= zodiaclist[i][1] and zodiacint <= zodiaclist[i][2]:
            zodiac = zodiaclist[i][0]
            break
        if i == len(zodiaclist) - 1:
            zodiac = 'Capricorn'
    return zodiac
def chinesezodiacsigns(year):
    year = int(year)
    surplus = year%12
    for i in range(len(chinesezodiaclist)):
        if surplus == chinesezodiaclist[i][1]:
            chinese = chinesezodiaclist[i][0]
    return chinese


# In[19]:


if __name__ == "__main__":
    if sys.version_info.major == 3:
        date = input('日付を入力してください。')
    else:
        date = raw_input('日付を入力してください。')
    date = date.split()
    split_date = []
    for i in range(len(date)):
        split_date.append(date[i].split('/'))
    for i in range(len(split_date)):
        zodiac = zodiacsigns([split_date[i][1],split_date[i][2]])
        chinesezodiac = chinesezodiacsigns(split_date[i][0])
        print(date[i]+' '+zodiac+' '+chinesezodiac)


# In[ ]:




