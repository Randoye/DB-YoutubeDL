from __future__ import unicode_literals
import youtube_dl
import mysql.connector as mc
import os
db_host = os.environ['dbhost']
db_name = os.environ['dbname']
user = os.environ['dbuser']
password = os.environ['dbpass']

try:
    con = mc.connect(host=db_host, database=db_name, user=user, password=password)
    cursor = con.cursor()
except mc.errors as e:
    print(e)
req = "SELECT * FROM youtube"
cursor.execute(req)
urllist = cursor.fetchall()
if urllist:
    for url in urllist:
        print(f"Working on Vidéo n°{url[0]} '{url[1]}' at {url[2]}")
        if url[1]:
            video_name = url[1]
        else:
            video_name = "%(title)s"
        ydl_opts = {
            'outtmpl': f"/output/{video_name}.%(ext)s"
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url[2]])
else:
    print("No Vidéos detected !")
cursor.close()
con.close()

