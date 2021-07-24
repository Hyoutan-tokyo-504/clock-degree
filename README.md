# clock-degree

this repository has two systems.

## 1.birthday_symbol.py
### description
if you write any dates, you can get the zodiac sign and the chinese zodiac sign on the day
### how to use
In a directory, if you write  
python birthday_symbol.py  
standard input are required like:  
日付を入力してください。  
you should write dates like :1998/11/15 2011/3/14 2017/9/18  
Then, the result below will be displayed  
1998/11/15 Scorpio 寅  
2011/3/14 Pisces 卯  
2017/9/18 Virgo 酉  

## 2.Clock_degree.py and test.py
### description
if you write a time on a day like 20 40, you can get the degree between the hour hand and the minute hand
### how to use
In a directory, if you write  
python Clock_degree.py  
standard input are required like:  
何時何分ですか？（入力例：22 40）  
you should write dates like :20 40
Then, the result below will be displayed  
Input         | Result
------------- | -------------
22 40         | 求まる角度は0度です。
26 40         | 第一引数は0\~23、第二引数は0\~59の整数値を入力してください。
aaa 0         | 整数値を入力してください。
