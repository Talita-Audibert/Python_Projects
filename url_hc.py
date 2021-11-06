import requests
from datetime import datetime

now = datetime.now()
date_time = now.strftime("%B %d %Y %H:%M:%S")
readfile = open('URL_list.txt', 'r')
url_list = readfile.readlines()
readfile.close()

html_content = ''

html_content = f'<HTML><TITLE>Availability Report</TITLE><meta http-equiv="refresh" content="60"><BODY background-color:peachpuff><font color ="#99000 face="Microsoft Tai le"><H2>Availability Report </H2> <h3> {date_time} </h3></font><Table border=1 cellpadding=0 cellspacing=0><TR bgcolor=gray align=center><TD><B>URL</B></TD><TD><B>Status Code</B></TD><TD><B>Status Description</B></TD><TD><B>Response Length</B></TD><TD><B>Time Taken in secs</B></TD</TR>'

for url in url_list:
    try:
        r = requests.get(f'{url.strip()}', timeout=2)
        
        if r.ok:
            html_content += "<TR bgcolor=lightgreen>"
        else:
            html_content += "<TR bgcolor=red>"

        html_content += f"<TD>{url}</TD><TD align=center>{r.status_code}</TD><TD align=center>{r.reason}</TD><TD align=center>{r.__sizeof__()}</TD><TD align=center>{r.elapsed.total_seconds()}</TD></TR>"
    
    except requests.ConnectTimeout:
        html_content += "<TR bgcolor=red>"
        html_content += f"<TD>{url}</TD><TD align=center>DOWN</TD><TD align=center>{r.reason}</TD><TD align=center>{r.__sizeof__()}</TD><TD align=center>{r.elapsed.total_seconds()}</TD></TR>"


html_content += "</Table></BODY></HTML>"


hs = open("URLs_status.html", 'w')
hs.write(html_content)
print(html_content)
hs.close()