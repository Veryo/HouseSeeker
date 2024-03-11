from bs4 import BeautifulSoup
import requests
import re
import time 
import webbrowser

def extract_times(text):
    pattern = r'\bDzisiaj o (\d{2}:\d{2})\b'
    matches = re.findall(pattern, text)
    times_as_integers = []
    for match in matches:
        hours, minutes = match.split(":")
        hours_int = (int(hours) +2) * 60
        minutes_int = int(minutes)
        times_as_integers=hours_int+minutes_int
    if times_as_integers == []:
        return None
    return times_as_integers

def show_time(time):
    hours = time // 60
    minutes = time % 60
    return(hours,minutes)

def found_home(url):
    li=[]
    li_2 =[]
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    house = soup.find_all(class_='css-veheph er34gjf0')
    link = soup.find_all(class_='css-rc5s2u')

    for x in range(0,len(house)-1):
        if extract_times(house[x].text) != None:
            li.append(extract_times(house[x].text))
            li_2.append(link[x].get('href'))

    print(li_2[li.index(max(li))])
    print(max(li),"funkcja",show_time(max(li)))
    return max(li),li_2[li.index(max(li))]

url = 'https://www.olx.pl/nieruchomosci/mieszkania/wynajem/krakow/?search%5Bfilter_enum_rooms%5D%5B0%5D=three&search%5Bfilter_enum_rooms%5D%5B1%5D=two&search%5Bfilter_float_m%3Afrom%5D=30&search%5Bfilter_float_price%3Ato%5D=2900&search%5Border%5D=created_at%3Adesc'

new_result = found_home(url)
i=0
while True:
    try:
        while True:
            time.sleep(60)
            i+=1
            result = found_home(url)
            print(show_time(result[0]),result[0],"result",show_time(new_result[0]),new_result[0],"new_result",'po raz',i)
            if result[0]>new_result[0]:
                new_result = result
                if 'otodom' in new_result[1]:
                    webbrowser.open(new_result[1])
                else:
                    webbrowser.open("https://www.olx.pl/"+new_result[1])
    except:
        pass







