import http.client
import ssl
import json
from datetime import date
import datetime
import time
today = date.today()


conn = http.client.HTTPSConnection("in.adda.io",context = ssl._create_unverified_context())


booking_date = today + datetime.timedelta(days=1)
booking_date = booking_date.strftime("%d-%m-%Y")

print(booking_date)

payload = "{\"facilityId\":\"9127\",\"bookDate\":\"19-11-2023\",\"bookDate2\":\"\",\"bookTimeFrom\":\"10:00\",\"bookTimeTo\":\"11:00\",\"slot\":\"17:00:00,17:30:00,0.00,22825\",\"isCommunity\":false,\"flatId\":\"1728479\",\"comment\":\"\",\"facilityAvailable\":true,\"min\":\"\",\"hrs\":\"\",\"book_hours\":1,\"book_mins\":0,\"book_time\":\"01:00:00\",\"limit_time1\":\"00:00:00\",\"limit_time2\":\"24:00:00\",\"msg\":\"\",\"flag\":\"\",\"multiDays\":0,\"book_start_time\":\"\",\"book_end_time\":\"\",\"fac_book_type\":\"2\",\"facility_service_tax\":0,\"refundableDeposit\":\"0.00\",\"day_wise_enabled\":\"0\"}"
print(payload)
headers = {
    'authority': 'in.adda.io',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
    'content-type': 'application/json;charset=UTF-8',
    'Cookie: _gcl_au=1.1.1835289417.1700310386; hubspotutk=1b3f4441420ae74b00ae23744e7eab09; messagesUtk=c692026ef23246a99b79715e27fce274; _fbp=fb.1.1700310388201.1085434473; device_zone_code_v1=US; _ga_SYXTMZBR6G=GS1.1.1703259434.1.0.1703259434.0.0.0; _gid=GA1.2.344656454.1703259441; _clck=18jucqs%7C2%7Cfhr%7C0%7C1417; __hstc=176160765.1b3f4441420ae74b00ae23744e7eab09.1700310388082.1700319190854.1703259452313.3; __hssrc=1; __hssc=176160765.3.1703259452313; _ga_EYZ6F5FRM2=GS1.1.1703259445.3.1.1703259550.45.0.0; vt=220cd524d963a31adb4a081f306eb34a; PHPSESSID=3kgipht8roq238pq518qfbofcm; authtoken=220cd524d963a31adb4a081f306eb34a; new_authtoken=220cd524d963a31adb4a081f306eb34a; _ga=GA1.2.718244846.1700310386; _ga_2K7NVLSG14=GS1.2.1703259564.3.1.1703259576.0.0.0',
    'origin': 'https://in.adda.io',
    'referer': 'https://in.adda.io/',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
}
conn.request("POST", "/ajax/post_facility.php?action=bookFacility&selected_facility_id=9127", payload, headers)
res = conn.getresponse()
print(res)
data = res.read()
print(data.decode("utf-8"))
time.sleep(1)
