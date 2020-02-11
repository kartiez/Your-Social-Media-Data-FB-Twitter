import json
import facebook
from flask import Flask, request
from flask_cors import CORS
import pyodbc
import os
import tweepy as tw

app = Flask(__name__)
CORS(app)
@app.route("/getfbposts")
def fb():
    server = 'Your server' 
    database = 'Your DB Name' 
    username = 'Your Username' 
    password = 'YOur Password' 
    token = "Your Token"
    graph = facebook.GraphAPI(token)
    field = ['posts.limit(15){id,link,message,created_time,full_picture,type,source}']
    profile = graph.get_object('me',fields=field)
    JsonFile = profile['posts']['data']
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    cursor.execute("TRUNCATE TABLE [dbo].[fb_data]")
    for i in JsonFile:
        if ('full_picture' not in i) and ('source' not in i) and ('link' not in i):
            cursor.execute("INSERT INTO [dbo].[fb_data]([id],[link],[message],[created_time],[pic_url],[type],[video_url]) VALUES('{}','NULL','{}','{}','NULL','{}','NULL');".format(i['id'],i['message'],i['created_time'],i['type'])) 
            cnxn.commit()
            print("Inserted row {}".format(x))
        elif ('full_picture' not in i) and ('source' not in i):
            cursor.execute("INSERT INTO [dbo].[fb_data]([id],[link],[message],[created_time],[pic_url],[type],[video_url]) VALUES('{}','{}','{}','{}','NULL','{}','NULL');".format(i['id'],i['link'],i['message'],i['created_time'],i['type'])) 
            cnxn.commit()
            print("Inserted row {}".format(x))
        elif 'full_picture' not in i:
            cursor.execute("INSERT INTO [dbo].[fb_data]([id],[link],[message],[created_time],[pic_url],[type],[video_url]) VALUES('{}','{}','{}','{}','NULL','{}','{}');".format(i['id'],i['link'],i['message'],i['created_time'],i['type'],i['source'])) 
            cnxn.commit()
            print("Inserted row {}".format(x))
        elif ('message' not in i) and ('source' not in i):
            cursor.execute("INSERT INTO [dbo].[fb_data]([id],[link],[message],[created_time],[pic_url],[type],[video_url]) VALUES('{}','{}','NULL','{}','{}','{}','NULL');".format(i['id'],i['link'],i['created_time'],i['full_picture'],i['type'])) 
            cnxn.commit()
            print("Inserted row {}".format(x))
        elif ('message' not in i) and ('source' not in i) and ('link' not in i):
            cursor.execute("INSERT INTO [dbo].[fb_data]([id],[link],[message],[created_time],[pic_url],[type],[video_url]) VALUES('{}','NULL','NULL','{}','{}','{}','NULL');".format(i['id'],i['created_time'],i['full_picture'],i['type'])) 
            cnxn.commit()
            print("Inserted row {}".format(x))
        elif 'message' not in i :
            cursor.execute("INSERT INTO [dbo].[fb_data]([id],[link],[message],[created_time],[pic_url],[type],[video_url]) VALUES('{}','{}','NULL','{}','{}','{}','{}');".format(i['id'],i['link'],i['created_time'],i['full_picture'],i['type'],i['source'])) 
            cnxn.commit()
            print("Inserted row {}".format(x))
        elif ('source' not in i) and ('link' not in i) :
            cursor.execute("INSERT INTO [dbo].[fb_data]([id],[link],[message],[created_time],[pic_url],[type],[video_url]) VALUES('{}','NULL','{}','{}','{}','{}','NULL');".format(i['id'],i['message'],i['created_time'],i['full_picture'],i['type'])) 
            cnxn.commit()
            print("Inserted row {}".format(x))
        elif 'source' not in i :
            cursor.execute("INSERT INTO [dbo].[fb_data]([id],[link],[message],[created_time],[pic_url],[type],[video_url]) VALUES('{}','{}','{}','{}','{}','{}','NULL');".format(i['id'],i['link'],i['message'],i['created_time'],i['full_picture'],i['type'])) 
            cnxn.commit()
            print("Inserted row {}".format(x))
        else:
            cursor.execute("INSERT INTO [dbo].[fb_data]([id],[link],[message],[created_time],[pic_url],[type],[video_url]) VALUES('{}','{}','{}','{}','{}','{}','{}');".format(i['id'],i['link'],i['message'],i['created_time'],i['full_picture'],i['type'],i['source'])) 
            cnxn.commit()
            print("Inserted row {}".format(x))
        x+=1
     
        #os.system('cls')
    html = ""
    cursor.execute("SELECT * FROM [dbo].[fb_data]")
    for i in JsonFile:
        if i['type'] == 'photo':
            if ('full_picture' in i) and ('message' in i):
                html += ' <div class="col-md-12 mb">'
                html += ' <div class="message-p pn">'
                html += '<div class="message-header">'
                html += '<h5>###### posted a photo on Facebook</h5>'
                html += ' </div>'
                html += '  <div class="row">'
                html += '<div class="col-md-3 centered hidden-sm hidden-xs">'
                html += '<img src="{}" class="imageContainer" width="500">'.format(i['full_picture'])
                html += '</div>  '                  
                html += ' <div class="col-md-9" align="center">'
                html += '<p>'
                html += '  <name>Added a photo'
                html += '  </name>'
                html += ' <!-- sent you a message.-->'
                html += ' </p>'
                html += '  <p class="small">{}</p>'.format(i['created_time'])
                html += '<p class="message">{} </>'.format(i['message'])
                html += '</div>'
                html += '</div>'
                html += '</div>'             
                html += '</div>'
        if i['type'] == 'status':
            if 'message' in i:
                html += ' <div class="col-md-12 mb">'
                html += ' <div class="message-p pn">'
                html += '<div class="message-header">'
                html += '<h5>>###### wrote on Facebook</h5>'
                html += ' </div>'
                html += '  <div class="row">'
                html += '<div class="col-md-3 centered hidden-sm hidden-xs">'
                html += '<img src="img/post.png" width="100">'
                html += '</div>'                 
                html += ' <div class="col-md-9" >'
                html += '<p>'
                html += '  <name>Wrote..'
                html += '  </name>'
                html += ' <!-- sent you a message.-->'
                html += ' </p>'
                html += '  <p class="small">{}</p>'.format(i['created_time'])
                html += '<p class="message">{} </>'.format(i['message'])
                html += '</div>'
                html += '</div>'
                html += '</div>'             
                html += '</div>'
        if i['type'] == 'video':
            if 'source' in i:
                html += ' <div class="col-md-12 mb">'
                html += ' <div class="message-p pn">'
                html += '<div class="message-header">'
                html += '<h5>>###### Uploaded a video on Facebook</h5>'
                html += ' </div>'
                html += '  <div class="row">'
                html += '<div class="col-md-3 centered hidden-sm hidden-xs">'
                html += '<video width="500" controls>'
                html += '<source src="{}" type="video/mp4">'.format(i['source'])
                html += ' Your browser does not support HTML5 video.'
                html += '</video>'
                html += '</div>  '                  
                html += ' <div class="col-md-9" align="center">'
                html += '<p>'
                html += '  <name>Added a video'
                html += '  </name>'
                html += ' <!-- sent you a message.-->'
                html += ' </p>'
                html += '  <p class="small">{}</p>'.format(i['created_time'])
                html += '<p class="message">{} </>'.format(i['message'])
                html += '</div>'
                html += '</div>'
                html += '</div>'             
                html += '</div>'   
    return html

@app.route("/gettweets")
def tweet():
    server = 'Your server' 
    database = 'Your DB Name' 
    username = 'Your Username' 
    password = 'YOur Password' 
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    cursor.execute("TRUNCATE TABLE [dbo].[tw_data]")
    consumer_key= 'Your Consumer Key'
    consumer_secret= 'Your Consumer Secret'
    access_token= 'Your Access Token'
    access_token_secret= 'Your Token Secret'
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth)
    html = ""
    mytweet = api.user_timeline(screen_name = 'Your Name', count = 15, include_rts = True)
    #print(mytweet)
    for tweet in mytweet:
        html += ' <div class="col-md-12 mb">'
        html += ' <div class="message-p pn">'
        html += '<div class="message-header">'
        html += '<h5>@>###### tweeted </h5>'
        html += ' </div>'
        html += '  <div class="row">'
        html += '<div class="col-md-3 centered hidden-sm hidden-xs">'
        if 'media' in tweet.entities:
            if 'media' in tweet.extended_entities:
                for media in tweet.extended_entities['media']:
                    if media['type'] == 'photo':
                        print(media['media_url'])
                        cursor.execute("INSERT INTO [dbo].[tw_data]([id],[createdtime],[text],[photolink],[videolink])VALUES('{}','{}','{}','{}','NULL');".format(tweet.id,tweet.created_at,tweet.text,media['media_url'],'NULL')) 
                        cnxn.commit()
                        html += '<img src="{}" class="imageContainer" width="500">'.format(media['media_url'])
                    elif media['type'] == 'video':
                        print(media['video_info']['variants'][0]['url'])
                        cursor.execute("INSERT INTO [dbo].[tw_data]([id],[createdtime],[text],[photolink],[videolink])VALUES('{}','{}','{}','NULL','{}');".format(tweet.id,tweet.created_at,tweet.text,media['video_info']['variants'][0]['url'])) 
                        cnxn.commit()
                        html += '<video width="500" controls>'
                        html += '<source src="{}" type="video/mp4">'.format(media['video_info']['variants'][0]['url'])
                        html += ' Your browser does not support HTML5 video.'
                        html += '</video>'
        else:
                html += '<img src="img/tw.png" class="imageContainer" width="150">'
                try :
                    cursor.execute("INSERT INTO [dbo].[tw_data]([id],[createdtime],[text],[photolink],[videolink])VALUES('{}','{}','{}','NULL','NULL');".format(tweet.id,tweet.created_at,tweet.text))
                    cnxn.commit()
                except:
                    print(tweet.id,tweet.created_at,tweet.text)
        html += '</div>  '                  
        html += ' <div class="col-md-9" align="center">'
        html += '<p>'
        html += '  <name>@KartieSuresh wrote..'
        html += '  </name>'
        html += ' <!-- sent you a message.-->'
        html += ' </p>'
        html += '  <p class="small">{}</p>'.format(tweet.created_at)
        html += '<p class="message">{} </>'.format(tweet.text)
        html += '</div>'
        html += '</div>'
        html += '</div>'             
        html += '</div>'
    return html

if __name__ == "__main__":

    app.run(debug=True,port=8080)

