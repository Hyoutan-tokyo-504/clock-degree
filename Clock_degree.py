#!/usr/bin/env python
# coding: utf-8

# In[10]:


#this function returns the degree required
def clock_degree(hour, minute):
    if(hour>=12):
        hour = hour - 12
    hour_degree = 360*(hour/12)
    minute_degree = 360*(minute/60)
    degree = abs(hour_degree - minute_degree)
    if(degree>180):
        return int(360 - degree)
    else:
        return int(degree)

#the function getting standard input
def clockinput():
    print('何時何分ですか？（入力例：22 40）')
    hour, minute = input().split()
    return[hour,minute]

# the function judging input error
def errorjudge(hour,minute):
    try:
        hour = int(hour)
        minute = int(minute)
        if(hour < 0 or hour > 23 or minute < 0 or minute > 59):
            print('第一引数は0~23、第二引数は0~59の整数値を入力してください。')
            return True
        return False
    except ValueError:
        print('整数値を入力してください。')
        return True

#the function in charge of all processes
def clockmain():
    while True:
        clocklist = clockinput()
        error = errorjudge(*clocklist)
        if error == True:
            continue
        [hour, minute] = map(int,clocklist)
        print('求まる角度は'+str(clock_degree(hour, minute)) +'度です。')
        break
    
# In[ ]:
if __name__ == "__main__":
    clockmain()


