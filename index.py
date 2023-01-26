
import datetime
thday = {
    0: "วันอาทิตย์",
    1: "วันจันทร์",
    2: "วันอังคาร",
    3: "วันพุธ",
    4: "วันพฤหัสบดี",
    5: "วันศุกร์",
    6: "วันเสาร์"
}

thmonth = {
    1: "มกราคม",
    2: "กุมภาพันธ์",
    3: "มีนาคม",
    4: "เมษายน",
    5: "พฤษภาคม",
    6: "มิถุนายน",
    7: "กรกฎาคม",
    8: "สิงหาคม",
    9: "กันยายน",
    10: "ตุลาคม",
    11: "พฤศจิกายน",
    12: "ธันวาคม"
}


x = datetime.datetime.now()

'''print(x.year)
print(x.month)
print(x.day)
print(x.strftime("%a"))
print(x.strftime("%A"))
print(x.strftime("%w"))
print(x.strftime("%d"))
print(x.strftime("%b"))
print(x.strftime("%B"))
print(x.strftime("%m"))
print(x.strftime("%Y"))'''

print("Today is", x.strftime("%A"), x.strftime(
    "%d"), x.strftime("%B"), x.strftime("%Y"))
print("วันนี้ ", thday.get(int(x.strftime("%w"))), " ที่ ", x.strftime(
    "%d"), thmonth.get(int(x.strftime("%m"))), x.strftime("%Y"))
