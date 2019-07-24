from django.shortcuts import render
import gspread
import datetime
from oauth2client.service_account import ServiceAccountCredentials
# Create your views here.

def sign(request):
    return render(request, "signup.html")

def log(request):
    return render(request, "login.html")



def home(request):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", \
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

    client = gspread.authorize(creds)

    sheet = client.open("test_sheet").sheet1

    data = sheet.get_all_records()

    cmp_date = datetime.datetime.now()

    day = cmp_date.strftime('%x')

    a = day[:2]

    if int(a) < 10:
        a = a[1]

    b = day[3:5]

    if int(b) < 10:
        b = b[1]

    y = day[6:]

    final = b + '-' + a + '-20' + y

    abc = []

    for x in data:
        if x['date'] == final:
            abc.append(x)

    if request.method == 'POST':
        return render(request, "login.html")

    return render(request, "front_page.html", {'data': data, 'current': abc})