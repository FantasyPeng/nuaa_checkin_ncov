import requests
import argparse

parser = argparse.ArgumentParser(description='Auto Check In for NUAA NCOV')
parser.add_argument('-u', dest='username', action='store', default='your username',  help='your username in nuaa')
parser.add_argument('-p', dest='password', action='store', default='your password', help='your password in nuaa')
args = parser.parse_args()
if __name__ == '__main__':
    username='username='+args.username
    pwd = 'password='+args.password
    loginData =username+'&'+pwd
    HEADERS = {'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'}
    req = requests.post(url="https://m.nuaa.edu.cn/uc/wap/login/check",headers=HEADERS,data=loginData)
    checkinUrl ='https://m.nuaa.edu.cn/ncov/wap/default/save';
    data_check='sfzhux=0&zhuxdz=&szgj=&szcs=&szgjcs=&sfjwfh=0&sfyjsjwfh=0&sfjcjwfh=0&sflznjcjwfh=0&sflqjkm=4&jkmys=1&sfjtgfxdq=0&id=13604782&uid=236781&date=20210122&tw=2&sfcxtz=0&sfyyjc=0&jcjgqr=0&jcjg=&sfjcbh=0&sfcxzysx=0&qksm=&remark=&address=%E6%B1%9F%E8%A5%BF%E7%9C%81%E4%B8%8A%E9%A5%B6%E5%B8%82%E9%84%B1%E9%98%B3%E5%8E%BF%E5%8F%A4%E5%8E%BF%E6%B8%A1%E9%95%87704%E5%8E%BF%E9%81%93&area=%E6%B1%9F%E8%A5%BF%E7%9C%81+%E4%B8%8A%E9%A5%B6%E5%B8%82+%E9%84%B1%E9%98%B3%E5%8E%BF&province=%E6%B1%9F%E8%A5%BF%E7%9C%81&city=%E4%B8%8A%E9%A5%B6%E5%B8%82&geo_api_info=%7B%22type%22%3A%22complete%22%2C%22position%22%3A%7B%22Q%22%3A29.067955186632%2C%22R%22%3A116.87585774739603%2C%22lng%22%3A116.875858%2C%22lat%22%3A29.067955%7D%2C%22location_type%22%3A%22html5%22%2C%22message%22%3A%22Get+ipLocation+failed.Get+geolocation+success.Convert+Success.Get+address+success.%22%2C%22accuracy%22%3A11561%2C%22isConverted%22%3Atrue%2C%22status%22%3A1%2C%22addressComponent%22%3A%7B%22citycode%22%3A%220793%22%2C%22adcode%22%3A%22361128%22%2C%22businessAreas%22%3A%5B%5D%2C%22neighborhoodType%22%3A%22%22%2C%22neighborhood%22%3A%22%22%2C%22building%22%3A%22%22%2C%22buildingType%22%3A%22%22%2C%22street%22%3A%22%E8%BF%8E%E5%AE%89%E5%A4%A7%E9%81%93%22%2C%22streetNumber%22%3A%22704%E5%8E%BF%22%2C%22country%22%3A%22%E4%B8%AD%E5%9B%BD%22%2C%22province%22%3A%22%E6%B1%9F%E8%A5%BF%E7%9C%81%22%2C%22city%22%3A%22%E4%B8%8A%E9%A5%B6%E5%B8%82%22%2C%22district%22%3A%22%E9%84%B1%E9%98%B3%E5%8E%BF%22%2C%22township%22%3A%22%E5%8F%A4%E5%8E%BF%E6%B8%A1%E9%95%87%22%7D%2C%22formattedAddress%22%3A%22%E6%B1%9F%E8%A5%BF%E7%9C%81%E4%B8%8A%E9%A5%B6%E5%B8%82%E9%84%B1%E9%98%B3%E5%8E%BF%E5%8F%A4%E5%8E%BF%E6%B8%A1%E9%95%87704%E5%8E%BF%E9%81%93%22%2C%22roads%22%3A%5B%5D%2C%22crosses%22%3A%5B%5D%2C%22pois%22%3A%5B%5D%2C%22info%22%3A%22SUCCESS%22%7D&created=1611282925&sfzx=0&sfjcwhry=0&sfcyglq=0&gllx=&glksrq=&jcbhlx=&jcbhrq=&sftjwh=0&sftjhb=0&fxyy=&bztcyy=4&fjsj=0&created_uid=0&sfjchbry=0&sfjcqz=&jcqzrq=&jcwhryfs=&jchbryfs=&xjzd=&sfsfbh=0&sfjcwzry=0&sftjwz=0&jhfjrq=&jhfjjtgj=&jhfjhbcc=&jhfjsftjwh=0&jhfjsftjhb=0&szsqsfybl=0&sfygtjzzfj=0&gtjzzfjsj=&sfsqhzjkk=0&sqhzjkkys=&is_fx_log=1&fxzrwjtw=&fxjrcjtw=1&fxjrzjtw=&fxsfzx=0&fxsfcyglq=0&fxsfcxtz=0&gwszdd=&sfyqjzgc=&jrsfqzys=&jrsfqzfy=&ismoved=0'
    cres = requests.post(url=checkinUrl,headers=HEADERS,data =data_check,cookies=req.cookies.get_dict())
    print(cres.text)
    
