__author__ = 'harsh'
import imdb
import os
import re
ia = imdb.IMDb()
print(os.getcwd())
for i in os.listdir("/run/media/harsh/My Passport/movies/hollywood"):
    i=i.replace("."," ")
    i=i.strip("avi")
    i=i.strip("mkv")
    m=re.search("^(.+?)\s[\(\[\d].+",i)
    if m:
        name=m.group(1)
        s_result = ia.search_movie(name)
        if(len(s_result)>0):
            x=s_result[0]
            ia.update(x)
            print(x)
            print(name)
            if(x.has_key('genres') and x.has_key('rating')):
               print(name+"-"+str(x['rating'])+"  "+str(x['genres']))
