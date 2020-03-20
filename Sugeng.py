# -*- coding: utf-8 -*- 
from linepy import *
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from akad.ttypes import TalkException
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup as bSoup
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
from threading import Thread
from io import StringIO
from multiprocessing import Pool
from googletrans import Translator
from urllib.parse import urlencode
from random import randint
from shutil import copyfile
from youtube_dl import YoutubeDL
import subprocess, youtube_dl, humanize, traceback
import subprocess as cmd
import platform
import requests, json
import time, random, sys, json, null, pafy, codecs, html5lib ,shutil ,threading, glob, re, base64, string, os, requests, six, ast, pytz, wikipedia, urllib, urllib.parse, atexit, asyncio, traceback
import youtube_dl
_session = requests.session()
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2


#CREATOR BY sᴇʟғʙᴏᴛ ʙʏ ᴊᴀᴄᴋʏ ᴀʀᴇᴢᴀ  

botStart = time.time()
mulai = time.time()
#tokenOpen = codecs.open("boyfira.json","r","utf-8")
#token = json.load(tokenOpen)

print  ("Welcome login self")  
#boy = LINE("")
boy = LINE("EP7nGndyQU9S6K9UZmX5.4ZxksQ0C7L7Ybo1HVs8x5q.npx1HRpCVTUdxd2BA/O34hlBJpZwXbPavnz6vlaUG2w=")
boy.log("Auth Token : " + str(boy.authToken))
boy.log("Timeline Token : " + str(boy.tl.channelAccessToken))
print ("sᴇʟғʙᴏᴛ ʙʏ : ᴊᴀᴄᴋʏ ᴀʀᴇᴢᴀ")

#ubah mid di dalem admin,owner,creator.json dengan mid kalian
poll = OEPoll(boy)
call = boy
creator = ["u059095aa0cc2f6ef02d8ae72c3430163"]
owner = ["u059095aa0cc2f6ef02d8ae72c3430163"]
admin = ["u059095aa0cc2f6ef02d8ae72c3430163"]
staff = ["u073e3d1490d2bddc09f7a586af8e3da3"]
mid = boy.getProfile().mid
KAC = [boy]
ABC = [boy]
Bots = [mid]
Boy = admin + staff + creator

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
protectantijs = []
ghost = []

welcome = []
simisimi = []
translateen = []
translateid = []
translateth = []
translatetw = []
translatear = []


myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

boyProfile = boy.getProfile()
myProfile["displayName"] = boyProfile.displayName
myProfile["statusMessage"] = boyProfile.statusMessage
myProfile["pictureStatus"] = boyProfile.pictureStatus

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)
with open('admin.json', 'r') as fp:
    admin = json.load(fp)    

Setbot1 = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot1)
Setbot2 = codecs.open("settings.json","r","utf-8")
settings = json.load(Setbot2)
Setbot3 = codecs.open("wait.json","r","utf-8")
wait = json.load(Setbot3)
Setbot4 = codecs.open("read.json","r","utf-8")
read = json.load(Setbot4)

mulai = time.time()

msg_dict = {}
msg_dict1 = {}

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
            
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
    
def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.01)        
            page = page[end_content:]
    return items
    
def backupData():
    try:
        backup1 = Setmain
        f = codecs.open('setting.json','w','utf-8')
        json.dump(backup1, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup2 = settings
        f = codecs.open('settings.json','w','utf-8')
        json.dump(backup2, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup3 = wait
        f = codecs.open('wait.json','w','utf-8')
        json.dump(backup3, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup4 = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup4, f, sort_keys=True, indent=4, ensure_ascii=False)        
        return True
    except Exception as error:
        logError(error)
        return False     

def restartBot():
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)

def autoRestart():
    if time.time() - botStart > int(settings["timeRestart"]):
        backupData()
        time.sleep(0,1)
        restartBot()

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "ᴛᴏᴛᴀʟ ᴘᴇɴɢʜᴜɴɪ ʀᴜᴍᴀʜ「{}」\n\n  [ Mention ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(boy.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        boy.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        boy.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def sendMeention2(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@projecreza "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    boy.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "hayo ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x "
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(boy.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        boy.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        boy.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "ᴛᴏᴛᴀʟ ᴛᴜʏᴜʟ ᴍᴀsᴜᴋ「{}」\nʜᴀʟʟᴏ sᴀʟᴋᴇɴ ʏᴀ, ᴍᴏɢᴀ ʙᴇᴛᴀʜ ᴅɪᴍᴀʀɪ ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = boy.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nDi group "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(boy.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        boy.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        boy.sendMessage(to, None, contentMetadata={"STKID":"51626525","STKPKGID":"11538","STKVER":"1"}, contentType=7)
    except Exception as error:
        boy.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "╔═══════════════════════╗ ╠❂͜͡☬➣    SELAMAT JALAN SOBAT'      ║ ╚═══════════════════════╝ ╔═══════════════════════╗ ║  ☫☫☫☫☫☫☫εïзεïзεïз❁❁❁❁❁❁❁  ║ ╚═══════════════════════╝ รєใค๓คҭ  вєг♩มคกง ใมคг รคกค ๔ī ҭє๓рคҭ ұคกง вคгม ๔คก ใєвīђ ҭєกคกง...(-‿◦) ╔═══════════════════════╗ ║  ☫☫☫☫☫☫☫εïзεïзεïз❁❁❁❁❁❁❁  ║ ╚═══════════════════════╝ вұє вұє รคม๔คгคкม รєใค๓คҭ ♩คใคก....(*^ω^*) ╔═══════════════════════╗ ║  ☫☫☫☫☫☫☫εïзεïзεïз❁❁❁❁❁❁❁  ║ ╚═══════════════════════╝ รє๓๏งค кīҭค вєгҭє๓ม кє๓вคใī ๔ī ใมคг รคกค กคกҭī...(^_^)ノ ╔═══════════════════════╗ ║  ☫☫☫☫☫☫☫εïзεïзεïз❁❁❁❁❁❁❁  ║ ╚═══════════════════════╝ ╔═══════════════════════╗ ╠❂͜͡☬➣              กคђ īกī ๔īค กīђ               ║ ╠❂͜͡☬➣          ғ๏ҭ๏ кєใมคгงค кīҭค          ║ ╠❂͜͡☬➣         ұคกง вคгม รค♩ค рєгงī        ║ ╚═══════════════════════╝ ╠❂͜͡☬➣ ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = boy.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["leave"]+"\nᴅᴀʀɪ ɢʀᴏᴜᴘ "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(boy.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        boy.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        boy.sendMessage(op.param1, None, contentMetadata={"STKID":"12690685","STKPKGID":"1314362","STKVER":"1"}, contentType=7)
    except Exception as error:
        boy.sendMessage(to, "[ INFO ] Error :\n" + str(error))        

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x\n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,10,7)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = boy.getAllContactIds()
        gid = boy.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"➣ ⌚ᴊᴀᴍ : "+datetime.strftime(timeNow,'%H:%M:%S')+" ᴡɪʙ\n➣ 📕ɢʀᴏᴜᴘ : "+str(len(gid))+"\n➣ 🚶ᴛᴇᴍᴀɴ : "+str(len(teman))+"\n➣ 📠ᴋᴀᴅᴀʟᴜᴀʀsᴀ : In "+hari+"\n➣ 📖ᴠᴇʀsɪ : ᴘʏᴛʜᴏɴ3\n➣ 📅ᴛᴀɴɢɢᴀʟ : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n➣ 📆ʀᴜɴᴛɪᴍᴇ : \n • "+bot
        boy.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        boy.sendMessage(to, "[ INFO ] Error :\n" + str(error))
#==============================================================================#

simple = {
    "ChangeVideoProfilevid":{},
    "ChangeVideoProfilePicture":{},
}
#================================================================================#        

        
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = boy.genOBSParams({'oid': boyMID, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = boy.server.postContent('{}/talk/vp/upload.nhn'.format(str(boy.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        boy.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))
        os.remove("FadhilvanHalen.mp4")

#=====================================================================#
#          Def tamplate/flex/carousel/liff
#======================================================================#
def sendTemplate(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = boy.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
def sendTemplate(group, data):
    xyz = LiffChatContext(group)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = boy.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
def bcTemplate(gr, data):
    xyz = LiffChatContext(gr)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = boy.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
def bcTemplate2(friend, data):
    xyz = LiffChatContext(friend)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = boy.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
def sendCarousel(to, data):
    data = json.dumps(data)
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = boy.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    return requests.post(url, data=data, headers=headers)
def sendCarousel(to,col):
    col = json.dumps(col)
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = boy.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    return requests.post(url, data=col, headers=headers)
def sendflex(to, data):
    n1 = LiffChatContext(to)
    n2 = LiffContext(chat=n1)
    view = LiffViewRequest('1602687308-GXq4Vvk9', n2)
    token = boy.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

uagent = {
    "User-Agent": "Mozilla\t5.0"
}
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
def infomeme():
    helpMessage2 = """
    ❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.👿.👿.👿
    ❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.☆.👿.👿.👿.
    ❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.☆.👿.👿.👿.
    ❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.☆.👿.👿.👿.
"""
    return helpMessage2
def postFlex(self, to, data='', altText=''):
        self.allowLiff()
        token = self.issueLiffView(to)
        url = 'https://api.line.me/message/v3/share'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer %s' % token.accessToken
        }
        anu = {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Reza bot",
                                "wrap": True,
                                "color": "#000000",
                                "size" : "sm"
                            }
                        ]
                    }
                }
        altText = altText if altText else '%s sent a messages' % self.profile.displayName
        data = data if data else anu
        data = {
            'messages': [{'type': 'flex', 'altText' : altText, 'contents' : data}]
        }
        res = requests.post(url, headers=headers, data=json.dumps(data))
        return res
def sendFlex(self, to, data):
        token = self.issueLiffView(to)
        url = 'https://api.line.me/message/v3/share'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer %s' % token.accessToken
        }
        data = {
            'messages': [data]
        }
        res = requests.post(url, headers=headers, data=json.dumps(data))
        return res
def postFlex(self, to, data):
        token = self.issueLiffView(to)
        url = 'https://api.line.me/message/v3/share'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer %s' % token.accessToken
        }
        data = {
            'messages': [data]
        }
        res = requests.post(url, headers=headers, data=json.dumps(data))
        return res
        
def sendPublik(to, text):
    data = {
                                        "type": "flex",
                                        "altText": "ᴀʀᴇᴢᴀ ᴛᴇᴀᴍ",
                                        "contents": {
"styles": {"body": {
"backgroundColor": "#000000"
},
"footer": 
{"backgroundColor": "#000000"
}},
"type": "bubble",
"size": "micro",
"body":
{
"contents": [
{
"contents": [
{
"type": "separator",
"color": "#33ffff"
},{
"type": "separator",
"color": "#33ffff"
},{
"contents": [
{
"type": "separator",
"color": "#33ffff"
},{
"contents": [
{
"text": text,
"size": "xxs",
"align": "center",
"color": "#FFFF00",
"wrap": True,
"weight": "bold",
"type": "text"
}],
"type": "box",
"spacing": "xs",
"layout": "vertical"
},{
"type": "separator",
"color": "#33ffff"
}],
"type": "box",
"layout": "horizontal"
},{
"type": "separator",
"color": "#33ffff"
},{
"contents": [
          {
            "type": "separator",
            "color": "#33ffff"
            },
             {
            "type": "image",
            "url": "https://1.bp.blogspot.com/-E0juNdy-4jA/XmYOQuENd-I/AAAAAAAAAYs/Wmym6YJiA_UXZuoJqEEruvdGRY5w2GNaACLcBGAsYHQ/s1600/1583745889408.jpg",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~jackyeza"
            },
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://1.bp.blogspot.com/-bSx6Add2DzI/XmYOQjCDRnI/AAAAAAAAAY0/JJ6txKAWNY0jpwSLG_PbJlkwp86A1EN3wCLcBGAsYHQ/s1600/1583745923732.jpg", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~jackyeza",             
           }, 
            "flex": 1            
          },
          {
        "type": "image",
            "url": "https://1.bp.blogspot.com/-kl82qcyNod0/XmYOQqdOKDI/AAAAAAAAAYw/HbGYRvRcGEgpwQBIjKk69qKCYokkIb4cQCLcBGAsYHQ/s1600/1583745957630.jpg", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/camera/"
          },
            "flex": 1
            },
          {
          "type": "image",
            "url": "https://1.bp.blogspot.com/-bSx6Add2DzI/XmYOQjCDRnI/AAAAAAAAAY0/JJ6txKAWNY0jpwSLG_PbJlkwp86A1EN3wCLcBGAsYHQ/s1600/1583745923732.jpg", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~jackyeza",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://1.bp.blogspot.com/-ym-P76sXdiA/XmYORjCYGDI/AAAAAAAAAY4/DLY76725dmUN88C9TVDbTx-_oVzhv6F6wCLcBGAsYHQ/s1600/1583745992055.jpg",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~jackyeza"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://1.bp.blogspot.com/-8S43W6aCZ8o/XmYORzOJuCI/AAAAAAAAAY8/dp_-ecuHwPwhJj6yotO1NWqhVtFigguMwCLcBGAsYHQ/s1600/G.jpg",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
            },
            "flex": 1
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  }
}
}
    boy.postTemplate(to, data)
#=========================================================================

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "╔═══════════════════════╗" + "\n" + \
                  "      📷sᴇʟғʙᴏᴛ ʙʏ ᴀʀᴇᴢᴀ📷  " + "\n" + \
                  "╚═══════════════════════╝" + "\n" + \
                  "╔═══════════════════════╗" + "\n" + \
                  "     📃ᴍᴇɴᴜ📃 " + "\n" + \
                  "╠═══════════════════════╝" + "\n" + \
                  "╠❂͜͡➣ " + key + "Help\n" + \
                  "╠❂͜͡➣ " + key + "Help 2\n" + \
                  "╠❂͜͡➣ " + key + "Help bot\n" + \
                  "╠❂͜͡➣ " + key + "Meme\n" + \
                  "╠❂͜͡➣ " + key + "Me\n" + \
                  "╠❂͜͡➣ " + key + "Mymid\n" + \
                  "╠❂͜͡➣ " + key + "Mid「@」\n" + \
                  "╠❂͜͡➣ " + key + "Info 「@」\n" + \
                  "╠❂͜͡➣ " + key + "K 「@」\n" + \
                  "╠❂͜͡➣ " + key + "Stat\n" + \
                  "╠❂͜͡➣ " + key + "Abo\n" + \
                  "╠❂͜͡➣ " + key + "Poin\n" + \
                  "╠❂͜͡➣ " + key + "Run\n" + \
                  "╠❂͜͡➣ " + key + "Creat\n" + \
                  "╠❂͜͡➣ " + key + "Speed/Sp\n" + \
                  "╠❂͜͡➣ " + key + "Sr\n" + \
                  "╠❂͜͡➣ " + key + "Pa/hai\n" + \
                  "╠❂͜͡➣ " + key + "Gin\n" + \
                  "╠❂͜͡➣ " + key + "Opn\n" + \
                  "╠❂͜͡➣ " + key + "Clo\n" + \
                  "╠❂͜͡➣ " + key + "Url\n" + \
                  "╠❂͜͡➣ " + key + "Rjt\n" + \
                  "╠❂͜͡➣ " + key + "Gl\n" + \
                  "╠❂͜͡➣ " + key + "Igp「angka」\n" + \
                  "╠❂͜͡➣ " + key + "Ime「angka」\n" + \
                  "╠❂͜͡➣ " + key + "Lur「on/off」\n" + \
                  "╠❂͜͡➣ " + key + "Lu\n" + \
                  "╠❂͜͡➣ " + key + "Sider「on/off」\n" + \
                  "╠❂͜͡➣ " + key + "Uf\n" + \
                  "╠❂͜͡➣ " + key + "Ugr\n" + \
                  "╠❂͜͡➣ " + key + "Bc:「Text」\n" + \
                  "╠❂͜͡➣ " + key + "Setkey「New Key」\n" + \
                  "╠❂͜͡➣ " + key + "Mykey\n" + \
                  "╠❂͜͡➣ " + key + "Resetkey\n" + \
                  "╠═══════════════════════╗" + "\n" + \
                  "      📷sᴇʟғʙᴏᴛ ʙʏ ᴀʀᴇᴢᴀ📷" + "\n" + \
                  "╚═══════════════════════╝"
    return helpMessage

def help1():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "╔═══════════════════════╗" + "\n" + \
                  "     🎡ʜɪʙᴜʀᴀɴ🎡" + "\n" + \
                  "╠═══════════════════════╝" + "\n" + \
                  "╠❂͜͡➣ " + key + "Stag:「jumlahnya」\n" + \
                  "╠❂͜͡➣ " + key + "Stag「@」\n" + \
                  "╠❂͜͡➣ " + key + "Scall:「jumlahnya」\n" + \
                  "╠❂͜͡➣ " + key + "Lagu:「Judulnya」\n" + \
                  "╠❂͜͡➣ " + key + "Scall\n" + \
                  "╠═══════════════════════╗" + "\n" + \
                  "      📷sᴇʟғʙᴏᴛ ʙʏ ᴀʀᴇᴢᴀ📷" + "\n" + \
                  "╚═══════════════════════╝"
    return helpMessage1

def help2():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage2 = "╔═══════════════════════╗" + "\n" + \
                  "     📝ᴘʀᴏᴛᴇᴄᴛ📝" + "\n" + \
                  "╠═══════════════════════╝" + "\n" + \
                  "╠❂͜͡➣ " + key + "Nt「ᴏɴ/ᴏғғ」\n" + \
                  "╠❂͜͡➣ " + key + "Tl「ᴏɴ/ᴏғғ」\n" + \
                  "╠═══════════════════════╗" + "\n" + \
                  "     ◄]·✪·sᴇᴛᴛɪɴɢ·✪·[►" + "\n" + \
                  "╠═══════════════════════╝" + "\n" + \
                  "╠❂͜͡➣ " + key + "Un「ᴏɴ/ᴏғғ」\n" + \
                  "╠❂͜͡➣ " + key + "Jointicket「on/ᴏғғ」\n" + \
                  "╠❂͜͡➣ " + key + "Str「ᴏɴ/ᴏғғ」\n" + \
                  "╠❂͜͡➣ " + key + "Res「ᴏɴ/ᴏғғ」\n" + \
                  "╠❂͜͡➣ " + key + "Rg「ᴏɴ/ᴏғғ」\n" + \
                  "╠❂͜͡➣ " + key + "Contact「ᴏɴ/ᴏғғ」\n" + \
                  "╠❂͜͡➣ " + key + "Ajo「ᴏɴ/ᴏғғ」\n" + \
                  "╠❂͜͡➣ " + key + "Autoadd「ᴏɴ/ᴏғғ」\n" + \
                  "╠❂͜͡➣ " + key + "Wl「ᴏɴ/ᴏғғ」\n" + \
                  "╠❂͜͡➣ " + key + "Simi「ᴏɴ/ᴏғғ」\n" + \
                  "╠❂͜͡➣ " + key + "Autoleave「ᴏɴ/ᴏғғ」\n" + \
                  "╠═══════════════════════╗" + "\n" + \
                  "     ◄]·✪·ᴀᴅᴍɪɴ·✪·[►" + "\n" + \
                  "╠═══════════════════════╝" + "\n" + \
                  "╠❂͜͡➣ " + key + "Fresh\n" + \
                  "╠❂͜͡➣ " + key + "Lb\n" + \
                  "╠❂͜͡➣ " + key + "La\n" + \
                  "╠❂͜͡➣ " + key + "Lp\n" + \
                  "╠❂͜͡➣ ᴋᴇᴛɪᴋ「 ғʀᴇsʜ」ᴊɪᴋᴀ sᴜᴅᴀʜ\n╠❂͜͡☬➣ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴄᴏᴍᴍᴀɴᴅ ᴅɪᴀᴛᴀs\n" + \
                  "╠═══════════════════════╗" + "\n" + \
                  "      📷sᴇʟғʙᴏᴛ ʙʏ ᴀʀᴇᴢᴀ📷" + "\n" + \
                  "╚═══════════════════════╝" 
    return helpMessage2
  
def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage3 = "╔═══════════════════════╗" + "\n" + \
                  "     📱sᴇʟғʙᴏᴛ ʙʏ ᴊᴀᴄᴋʏ ᴀʀᴇᴢᴀ📱" + "\n" + \
                  "╚═══════════════════════╝" + "\n" + \
                  "╔═══════════════════════╗" + "\n" + \
                  "     🔧·ʙᴏᴛ·🔧" + "\n" + \
                  "╠═══════════════════════╝" + "\n" + \
                  "╠✇➣ " + key + "Mytoken\n" + \
                  "╠✇➣ " + key + "Cek sider\n" + \
                  "╠✇➣ " + key + "Cek spam\n" + \
                  "╠✇➣ " + key + "Cek pesan\n" + \
                  "╠✇➣ " + key + "Cek respon\n" + \
                  "╠✇➣ " + key + "Cek welcome\n" + \
                  "╠✇➣ " + key + "Cek leave\n" + \
                  "╠✇➣ " + key + "Set si:「Text」\n" + \
                  "╠✇➣ " + key + "Set spam:「Text」\n" + \
                  "╠✇➣ " + key + "Set pesan:「Text」\n" + \
                  "╠✇➣ " + key + "Set re:「Text」\n" + \
                  "╠✇➣ " + key + "Set wl:「Text」\n" + \
                  "╠✇➣ " + key + "Set leave:「Text」\n" + \
                  "╠✇➣ " + key + "Mme:「Nama」\n" + \
                  "╠✇➣ " + key + "Gift:「Mid korban」「Jumlah」\n" + \
                  "╠✇➣ " + key + "Spam:「Mid korban」「Jumlah」\n" + \
				  "╠✇➣ " + key + "Stag:「jumlahnya」\n" + \
                  "╠✇➣ " + key + "Stag「@」\n" + \
                  "╠✇➣ " + key + "Scall:「jumlahnya」\n" + \
                  "╠✇➣ " + key + "Scall\n" + \
				  "╠✇➣ " + key + "Uf\n" + \
                  "╠✇➣ " + key + "Ugr\n" + \
                  "╠✇➣ " + key + "Bc:「Text」\n" + \
                  "╠✇➣ " + key + "Setkey「New Key」\n" + \
                  "╠✇➣ " + key + "Mykey\n" + \
                  "╠✇➣ " + key + "Resetkey\n" + \
				  "╠✇➣ " + key + "Self「ᴏɴ/ᴏғғ」\n" + \
				  "╠✇➣ " + key + "Hc\n" + \
				  "╠✇➣ " + key + "Leave:「Namagrup」\n" + \
                  "╠═══════════════════════╗" + "\n" + \
                  "     ◄]·✪·ʙʟᴀᴄᴋʟɪsᴛ·✪·[►" + "\n" + \
                  "╠═══════════════════════╝" + "\n" + \
                  "╠❂➣ " + key + "Blc\n" + \
                  "╠❂➣ " + key + "Ban:on\n" + \
                  "╠❂➣ " + key + "Unban:on\n" + \
                  "╠❂➣ " + key + "Ban「@」\n" + \
                  "╠❂➣ " + key + "Unban「@」\n" + \
                  "╠❂➣ " + key + "Talkban「@」\n" + \
                  "╠❂➣ " + key + "Untalkban「@」\n" + \
                  "╠❂➣ " + key + "Talkban:on\n" + \
                  "╠❂➣ " + key + "Untalkban:on\n" + \
                  "╠❂➣ " + key + "Banlist\n" + \
                  "╠❂➣ " + key + "Talkbanlist\n" + \
                  "╠❂➣ " + key + "Cb\n" + \
                  "╠❂➣ " + key + "Fresh\n" + \
                  "╠═══════════════════════╗" + "\n" + \
                  "      📷sᴇʟғʙᴏᴛ ʙʏ ᴊᴀᴄᴋʏ ᴀʀᴇᴢᴀ📷" + "\n" + \
                  "╚═══════════════════════╝"
    return helpMessage3
    
def infomeme():
    helpMessage4 = """
╔═══════════════════════╗
       👙sᴇʟғʙᴏᴛ ʙʏ ᴀʀᴇᴢᴀ👙
╚═══════════════════════╝
╔═══════════════════════╗
    ◄]·✪·ʟɪsᴛ ᴍᴇᴍᴇ·✪·[►
╠═══════════════════════╝
╠❂➣ Buzz
╠❂➣ Spongebob
╠❂➣ Patrick
╠❂➣ Doge
╠❂➣ Joker
╠❂➣ Xzibit
╠❂➣ You_tried
╠❂➣ cb
╠❂➣ blb
╠❂➣ wonka
╠❂➣ keanu
╠❂➣ cryingfloor
╠❂➣ disastergirl
╠❂➣ facepalm
╠❂➣ fwp
╠❂➣ grumpycat
╠❂➣ captain
╠❂➣ mmm
╠❂➣ rollsafe
╠❂➣ sad-obama
╠❂➣ sad-clinton
╠❂➣ aag
╠❂➣ sarcasticbear
╠❂➣ sk
╠❂➣ parta
╠❂➣ sad
╠❂➣ contoh:
╠❂➣ Meme@buzz@lu tau?@gatau
╠═══════════════════════╗
      📷sᴇʟғʙᴏᴛ ʙʏ ᴀʀᴇᴢᴀ📷
╚═══════════════════════╝
"""
    return helpMessage4

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait['leaveRoom'] == True:
                boy.leaveRoom(op.param1)   
        if op.type == 24:
            if wait['leaveRoom'] == True:
                boy.leaveRoom(op.param1)        
                
        if op.type == 5:
              if wait["autoAdd"] == True:
                  boy.findAndAddContactsByMid(op.param1)
                  sendMention(op.param1, op.param1, "ʜᴀʟʟᴏ ", ", ᴛʜᴀɴᴋs ᴜᴅᴀʜ ᴀᴅᴅ sᴀʏᴀ")
                  boy.sendText(op.param1, wait["message"])
                  boy.sendContact(op.param1,"u059095aa0cc2f6ef02d8ae72c3430163")
                                                
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        boy.acceptGroupInvitation(op.param1)
                        ginfo = boy.getGroup(op.param1)
                        boy.sendMessage(op.param1,"sᴇʟᴀᴍᴀᴛᴛɪɴɢɢᴀʟ\n Group " +str(ginfo.name))
                        boy.leaveGroup(op.param1)
                    else:
                        boy.acceptGroupInvitation(op.param1)
                        ginfo = boy.getGroup(op.param1)
                        boy.sendMessage(op.param1,"Hai " + str(ginfo.name))
                        
        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        boy.rejectGroupInvitation(op.param1)
                    else:
                        boy.acceptGroupInvitation(op.param1)
                        ginfo = boy.getGroup(op.param1)
                        boy.sendMessage(op.param1,"Haii semua yang ada di " + str(ginfo.name))

        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        boy.sendMessage(op.param1, wait["message"])

#===========KICK============#
        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
        if op.type == 19:
            if op.param3 in admin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).findAndAddContactsByMid("u059095aa0cc2f6ef02d8ae72c3430163")
                    random.choice(ABC).inviteIntoGroup(op.param1,["u059095aa0cc2f6ef02d8ae72c3430163"])
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
        if op.type == 19:
            if op.param3 in staff:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).findAndAddContactsByMid("u059095aa0cc2f6ef02d8ae72c3430163")
                    random.choice(ABC).inviteIntoGroup(op.param1,["u059095aa0cc2f6ef02d8ae72c3430163"])
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
        if op.type == 11:
            if op.param1 in protectqr:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
#===========Accepet===========#

            if op.param3 in mid:
                if op.param2 in Bots:
                    boy.acceptGroupInvitation(op.param1)

#===========Cancel============#

#___________________________________________________
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if msg._from in admin:
                  if wait["invite"] == True:
                    msg.contentType = 0
                    contact = boy.getContact(msg.contentMetadata["mid"])
                    invite = msg.contentMetadata["mid"]
                    groups = boy.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if invite in wait["blacklist"]:
                            boy.sendMessage(msg.to, "「ᴀᴡᴀs ᴋɪᴋɪʟ ʙᴏss... ђคрมร вใ ᴅᴜʟᴜ ʙᴀʀᴜ ɪɴᴠɪᴛᴇ ʟᴀɢɪ ʙᴏss...!!!」")
                            break
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                         for target in targets:
                            try:
                                boy.findAndAddContactsByMid(target)
                                boy.inviteIntoGroup(msg.to,[target])
                                fira = boy.getContact(target)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Sukses Invite 」\nNama "
                                ret_ = "「Ketik Invite off jika sudah done」"
                                fa = str(fira.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':fira.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                boy.sendMessage(msg.to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                wait["invite"] = False
                                break
                            except:
                                boy.sendText(msg.to,"ʟɪᴍɪᴛ ʙᴏss...!!!")
                                wait["invite"] = False
                                break

        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if wait["invite"] == True:
                    _name = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = boy.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            boy.sendText(msg.to, _name + "sᴜᴅᴀʜ ᴅɪ ᴅᴀʟᴀᴍ ɢʀᴜᴘ")
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                boy.findAndAddContactsByMid(target)
                                boy.inviteIntoGroup(msg.to,[target])
                                boy.sendText(msg.to,"Invite " + _name)
                                wait["invite"] = False
                                break                              
                            except:             
                                    boy.sendText(msg.to,"ᴇʀʀᴏʀ")
                                    wait["invite"] = False
                                    break

                return

        if op.type == 55:
            try:
                if op.param1 in Setmain["AFreadPoint"]:
                   if op.param2 in Setmain["AFreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["AFreadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = boy.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = boy.getContact(op.param2)
                        data = {
                                      "type": "flex",
                                      "altText": "mata jelalatan",
                                      "contents": {
"styles": {"body": {"backgroundColor": "#000000"},"footer": {"backgroundColor": "#bfff00"}},"type": "bubble","size": "micro","body": {"contents": [{"type": "separator","color": "#FF00FF"},{"contents": [{"type": "separator","color": "#FF00FF"},{"url": "https://obs.line-scdn.net/{}".format(boy.getContact(op.param2).pictureStatus),"type": "image"},{"type": "separator","color": "#FF00FF"},{
"text": "ᴋᴇʙɪᴀsᴀᴀɴ ᴋᴀɴ\n\nsɪɴɪ ɢᴀʙᴜɴɢ\n\nᴊᴀɴɢᴀɴ ɴɢɪɴᴄᴇɴɢ ᴍᴜʟᴜ","size": "xxs","color": "#00FF33","wrap": True,"weight": "bold","type": "text"},{"type": "separator","color": "#FF00FF"}],"type": "box","spacing": "md","layout": "horizontal"},{"type": "separator","color": "#FF00FF"},{"contents": [{"contents": [{
"text": "ᴛᴇʀsᴀɴɢᴋᴀ :〘 {} 〙".format(boy.getContact(op.param2).displayName),"size": "xxs","margin": "none","color": "#FFFF00","wrap": True,"weight": "regular","type": "text"}],"type": "box","layout": "baseline"}],"type": "box","layout": "vertical"}],"type": "box","spacing": "md","layout": "vertical"},"footer": {"type": "box","layout": "vertical","contents": [{"type": "box","layout": "horizontal","contents": [{
"type": "button","flex": 2,"style": "primary","color": "#660000","height": "sm","action": {"type": "uri","label": "ᴀᴜᴛᴏ ᴄɪᴘᴏᴋ","uri": "https://line.me/ti/p/~jackyeza"}}]}]}}}
                        sendTemplate(op.param1, data)
                                                
                        
                    
        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = boy.getGroup(at)
                                Boy = boy.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "╭━━━━━━━━━━━━━━━━━━━\n┝         「 ɢᴀᴍʙᴀʀ ᴅɪʜᴀᴘᴜs 」┝━━━━━━━━━━━━━━━━━━━\n┝➲ ɴᴀᴍᴀ ᴛᴇʀsᴀɴɢᴋᴀ : "
                                ret_ = "┝➲ ɴᴀᴍᴀ ɢʀᴜᴘ : {}".format(str(ginfo.name))
                                ret_ += "\n┝➲ ᴡᴀᴋᴛᴜ ɴɢɪʀɪᴍ : {}".format(str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(Boy.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':Boy.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                boy.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                boy.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = boy.getGroup(at)
                                Boy = boy.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "╭━━━━━━━━━━━━━━━━━━━\n┝         「 ᴘᴇsᴀɴ ᴅɪʜᴀᴘᴜs 」\n┝━━━━━━━━━━━━━━━━━━━\n"
                                ret_ += "┝➲ ɴᴀᴍᴀ ᴛᴇʀsᴀɴɢᴋᴀ : {}".format(str(Boy.displayName))
                                ret_ += "\n┝➲ ɴᴀᴍᴀ ɢʀᴜᴘ : {}".format(str(ginfo.name))
                                ret_ += "\n┝➲ ᴡᴀᴋᴛᴜ ɴɢɪʀɪᴍ : {}".format(str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n┝➲ ᴘᴇsᴀɴ ᴛᴇʀᴀᴋʜɪʀɴʏᴀ : {}\n╰━━━━━━━━━━━━━━━━━━━".format(str(msg_dict[msg_id]["text"]))
                                boy.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = boy.getGroup(at)
                                Boy = boy.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "╭━━━━━━━━━━━━━━━━━━━\n┝         「 sᴛɪᴄᴋᴇʀ ᴅɪʜᴀᴘᴜs」\n┝━━━━━━━━━━━━━━━━━━━\n"
                                ret_ += "┝➲ ɴᴀᴍᴀ ᴛᴇʀsᴀɴɢᴋᴀ : {}".format(str(Boy.displayName))
                                ret_ += "\n┝➲ ɴᴀᴍᴀ ɢʀᴜᴘ : {}".format(str(ginfo.name))
                                ret_ += "\n┝➲ ᴡᴀᴋᴛᴜ ɴɢɪʀɪᴍ : {}\n╰━━━━━━━━━━━━━━━━━━━".format(str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                boy.sendMessage(at, str(ret_))
                                boy.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message                    
               if msg.to in simisimi:
                   try:
                       if msg.text is not None:
                           simi = msg.text
                           r = requests.get("http://corrykalam.pw/api/chatbot.php?text="+simi)
                           data = r.text
                           data = json.loads(data)
                           if data["status"] == 200:
                               boy.sendMessage(msg.to, str(data["answer"])) 
                   except Exception as error:
                       pass
      #LIKES#                           
        
                         ##Likes##
                   
               if msg.to in translateen:
                   try:
                       if msg.text is not None:
                           kata = msg.text                           
                           translator = Translator()
                           hasil = translator.translate(kata, dest='en')
                           A = hasil.text
                           boy.sendMessage(msg.to, A)
                   except Exception as error:
                       pass                           
                           
               if msg.to in translateid:
                   try:
                       if msg.text is not None:
                           kata = msg.text                           
                           translator = Translator()
                           hasil = translator.translate(kata, dest='id')
                           A = hasil.text
                           boy.sendMessage(msg.to, A)
                   except Exception as error:
                       pass 
                   
               if msg.to in translateth:
                   try:
                       if msg.text is not None:
                           kata = msg.text                           
                           translator = Translator()
                           hasil = translator.translate(kata, dest='th')
                           A = hasil.text
                           boy.sendMessage(msg.to, A)
                   except Exception as error:
                       pass
                   
               if msg.to in translatetw:
                   try:
                       if msg.text is not None:
                           kata = msg.text                           
                           translator = Translator()
                           hasil = translator.translate(kata, dest='zh-tw')
                           A = hasil.text
                           boy.sendMessage(msg.to, A)
                   except Exception as error:
                       pass 
                   
               if msg.to in translatear:
                   try:
                       if msg.text is not None:
                           kata = msg.text                           
                           translator = Translator()
                           hasil = translator.translate(kata, dest='ar')
                           A = hasil.text
                           boy.sendMessage(msg.to, A)
                   except Exception as error:
                       pass

        if op.type == 25 or op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   tz = pytz.timezone("Asia/Jakarta")
                   timeNow = datetime.now(tz=tz)
                   contact = boy.getContact(msg._from)
                   image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           boy.sendMessage(msg.to, wait["Respontag"])
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentiongift"] == True:
                   tz = pytz.timezone("Asia/Jakarta")
                   timeNow = datetime.now(tz=tz)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           idth = ["a0768339-c2d3-4189-9653-2909e9bb6f58","ec4a14ea-7437-407b-aee7-96b1cbbc1b4b","f35bd31f-5ec7-4b2f-b659-92adf5e3d151","ba1d5150-3b5f-4768-9197-01a3f971aa34","2b4ccc45-7309-47fe-a006-1a1edb846ddb","168d03c3-dbc2-456f-b982-3d6f85f52af2","d4f09a5f-29df-48ac-bca6-a204121ea165","517174f2-1545-43b9-a28f-5777154045a6","762ecc71-7f71-4900-91c9-4b3f213d8b26","2df50b22-112d-4f21-b856-f88df2193f9e"]
                           plihth = random.choice(idth)
                           jenis = ["5","6","7","8"]
                           plihjenis = random.choice(jenis)
                           boy.sendMessage(msg.to, "Yang suka ngetag minta di gift yaa!?\nCek di chat, udah aku gift tuh...")
                           boy.sendMessage(msg._from, None, contentMetadata={"PRDID":plihth,"PRDTYPE":"THEME","MSGTPL":plihjenis}, contentType=9)
                           break                       
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           boy.sendMessage(msg.to, "Jangan tag saya....")
                           boy.kickoutFromGroup(msg.to, [msg._from])
                           break
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    boy.sendMessage(msg.to,"「Cek ID Sticker」\n╠❂➣ STKID : " + msg.contentMetadata["STKID"] + "\n╠❂➣ STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n╠❂➣ STKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    boy.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = boy.getContact(msg.contentMetadata["mid"])
                        path = boy.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        boy.sendMessage(msg.to,"\n╠❂➣ Nama : " + msg.contentMetadata["displayName"] + "\n╠❂➣ MID : " + msg.contentMetadata["mid"] + "\n╠❂➣ Status : " + contact.statusMessage + "\n╠❂➣ Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        boy.sendImageWithURL(msg.to, image)


        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.contentType == 0:
                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                
            if msg.contentType == 1:
                    path = boy.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
            if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\n╭━━━━━━━━━━━━━━━━━━━\n┝         「 ɪɴғᴏ sᴛɪᴄᴋᴇʀɴʏᴀ」\n┝━━━━━━━━━━━━━━━━━━━"
                   ret_ += "\n╠➲ ɪᴅ sᴛɪᴄᴋᴇʀ : {}".format(stk_id)
                   ret_ += "\n╠➲ ᴠᴇʀsɪ sᴛɪᴄᴋᴇʀ : {}".format(stk_ver)
                   ret_ += "\n╠➲ sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋᴀɢᴇ : {}".format(pkg_id)
                   ret_ += "\n╠➲ sᴛɪᴄᴋᴇʀ ᴜʀʟ : line://shop/detail/{}".format(pkg_id)
                   ret_ += "\n╠➲ sᴇʟғʙᴏᴛ ʙʏ : ↙↪ᴊᴀᴄᴋʏ ᴀʀᴇᴢᴀ↩↘\n┝━━━━━━━━━━━━━━━━━━━"
                   ret_ += "\n╠➲       🔄ᴘᴇɴᴀᴍᴘᴀᴋᴀɴɴʏᴀ ᴅɪʙᴀᴡᴀʜ🔄\n╰━━━━━━━━━━━━━━━━━━━"
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = boy.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
                        
        
                            
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    boy.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    boy.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = boy.getContact(msg.contentMetadata["mid"])
                        path = boy.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        boy.sendMessage(msg.to,"📝 ɴᴀᴍᴀ : " + msg.contentMetadata["displayName"] + "\n📰 ᴍɪᴅ : " + msg.contentMetadata["mid"] + "\n📖 sᴛᴀᴛᴜs : " + contact.statusMessage + "\n✏️ ᴘɪᴄᴛᴜʀᴇ ᴜʀʟ : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        boy.sendImageWithURL(msg.to, image)
                        
#===========ADD BLACKLIST============#
                 if msg._from in admin:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        boy.sendMessage(msg.to,"Contact itu sudah ada di blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        boy.sendMessage(msg.to,"Berhasil menambahkan ke blacklist user")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        boy.sendMessage(msg.to,"Berhasil menghapus dari blacklist user")
                    else:
                        wait["dblacklist"] = True
                        boy.sendMessage(msg.to,"Contact itu tidak ada di blacklist")
#===========TALKBAN============#
                 if msg._from in admin:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        boy.sendMessage(msg.to,"Contact itu sudah ada di Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        boy.sendMessage(msg.to,"Berhasil menambahkan ke Talkban user")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        boy.sendMessage(msg.to,"Berhasil menghapus dari Talkban user")
                    else:
                        wait["Talkdblacklist"] = True
                        boy.sendMessage(msg.to,"Contact itu tidak ada di Talkban")


#===========UPDATE FOTO============#
               if msg.contentType == 1:
                 if msg._from in admin:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = boy.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            boy.sendMessage(msg.to, "sᴜᴄᴄᴇs ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ғᴏᴛᴏ")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = boy.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     boy.updateGroupPicture(msg.to, path)
                     boy.sendMessage(msg.to, "sᴜᴄᴄᴇs ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ғᴏᴛᴏ ɢʀᴏᴜᴘ")

               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["AFfoto"]:
                            path = boy.downloadObjectMsg(msg_id)
                            del Setmain["AFfoto"][mid]
                            boy.updateProfilePicture(path)
                            boy.sendMessage(msg.to,"ғᴏᴛᴏ ʙᴇʀʜᴀsɪʟ ᴅɪɢᴀɴᴛɪ")               

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        boy.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               helpMessage = help()
                               helpMessage1 = help1()
                               boy.sendMessage(msg.to, "Help \nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                               boy.sendMessage(msg.to,str(helpMessage))
                               boy.sendMessage(msg.to,str(helpMessage1))
                                                                                       
                        if cmd == "self on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                boy.sendMessage(msg.to, "sᴇʟғʙᴏᴛ ᴅɪᴀᴋᴛɪғᴋᴀɴ")
                                
                        elif cmd == "self off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                boy.sendMessage(msg.to, "sᴇʟғʙᴏᴛ ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ")

                        elif cmd == "help2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               helpMessage2 = help2()
                               boy.sendMessage(msg.to, "🔗ʜᴇʟᴘ ʙᴏᴛs🔗\n??ᴛᴀɴɢɢᴀʟ : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n⌚ᴊᴀᴍ [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                               boy.sendMessage(msg.to, str(helpMessage2))
                           
                               
                        elif cmd.startswith("mn: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = boy.getProfile()
                                profile.displayName = string
                                boy.updateProfile(profile)
                                boy.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                            
                        elif cmd == "help bot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               helpMessage3 = helpbot()
                               boy.sendMessage(msg.to, "🔗ʜᴇʟᴘ ʙᴏᴛs🔗\n📅ᴛᴀɴɢɢᴀʟ : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n⌚ᴊᴀᴍ [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                               boy.sendMessage(msg.to, str(helpMessage3))
                               
                               
                               
                        elif cmd == "meme":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               helpMessage4 = infomeme()
                               boy.sendMessage(msg.to, "Help Fun\n📅ᴛᴀɴɢɢᴀʟ : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n⌚ᴊᴀᴍ [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                               boy.sendMessage(msg.to, str(helpMessage4))
                               

                        if cmd == "uns on":
                            if msg._from in admin:
                                wait["unsend"] = True
                                boy.sendMessage(msg.to, "ᴅᴇᴛᴇᴋsɪ ᴜɴsᴇɴᴅ ᴏɴ")
                                
                        if cmd == "uns off":
                            if msg._from in admin:
                                wait["unsend"] = False
                                boy.sendMessage(msg.to, "ᴅᴇᴛᴇᴋsɪ ᴜɴsᴇɴᴅ ᴏғғ")                                

                        elif cmd == "status":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "  ┏━━━━━━━━━━━━━━━━━\n┃┃          ❂͜͡☬➣sᴛᴀᴛᴜs❂͜͡☬➣\n┃┣━━━━━━━━━━━━━━━━━━━━\n"
                                if wait["unsend"] == True: md+="┃┃❂͜͡➣ √ ᴜɴsᴇɴᴅ「ᴏɴ」\n"
                                else: md+="┃┃❂͜͡➣ ✖ ᴜɴsᴇɴᴅ「ᴏғғ」\n"                                
                                if wait["sticker"] == True: md+="┃┃❂͜͡➣ √ sᴛɪᴄᴋᴇʀ「ᴏɴ」\n"
                                else: md+="┃┃❂͜͡➣ ✖ sᴛɪᴄᴋᴇʀ「ᴏғғ」\n"
                                if wait["contact"] == True: md+="┃┃❂͜͡➣ √ ᴄᴏɴᴛᴀᴄᴛ「ᴏɴ」\n"
                                else: md+="┃┃❂͜͡➣ ✖ ᴄᴏɴᴛᴀᴄᴛ「ᴏғғ」\n"
                                if wait["talkban"] == True: md+="┃┃❂͜͡➣ √ ᴛᴀʟᴋʙᴀɴ「ᴏɴ」\n"
                                else: md+="┃┃❂͜͡➣ ✖ ᴛᴀʟᴋʙᴀɴ「ᴏғғ」\n"
                                if wait["Mentionkick"] == True: md+="┃┃❂͜͡➣ √ ɴᴏᴛᴀʟ「ᴏɴ」\n"
                                else: md+="┃┃❂͜͡➣ ✖ ɴᴏᴛᴀʟ「ᴏғғ」\n"
                                if wait["detectMention"] == True: md+="┃┃❂͜͡➣ √ ʀᴇsᴘᴏɴ「ᴏɴ」\n"
                                else: md+="┃┃❂͜͡➣ ✖ ʀᴇsᴘᴏɴ「ᴏғғ」\n"
                                if wait["Mentiongift"] == True: md+="┃┃❂͜͡➣ √ ʀᴇsᴘᴏɴsɪғ「ᴏɴ」\n"
                                else: md+="┃┃❂͜͡➣ ✖ ʀᴇsᴘᴏɴsɪғ「ᴏғғ」\n"                                
                                if wait["autoJoin"] == True: md+="┃┃❂͜͡➣ √ ᴀᴜᴛᴏᴊᴏɪɴ「ᴏɴ」\n"
                                else: md+="┃┃❂͜͡➣ ✖ ᴀᴜᴛᴏᴊᴏɪɴ「ᴏғғ」\n"
                                if settings["autoJoinTicket"] == True: md+="┃┃❂͜͡➣ √ ᴊᴏɪɴᴛɪᴄᴋᴇᴛ「ᴏɴ」\n"
                                else: md+="┃┃❂͜͡➣ ✖ ᴊᴏɪɴᴛɪᴄᴋᴇᴛ「ᴏғғ」\n"                                
                                if wait["autoAdd"] == True: md+="┃┃❂͜͡➣ √ ᴀᴜᴛᴏᴀᴅᴅ「ᴏɴ」\n"
                                else: md+="┃┃❂͜͡➣ ✖ ᴀᴜᴛᴏᴀᴅᴅ「ᴏғғ」\n"                                
                                if wait["Timeline"] == True: md+="┃┃❂͜͡➣ √ ᴛɪᴍᴇʟɪɴᴇ「ᴏɴ」\n"
                                else: md+="┃┃❂͜͡➣ ✖ ᴛɪᴍᴇʟɪɴᴇ「ᴏғғ」\n"
                                if msg.to in welcome: md+="┃┃❂͜͡➣ √ ᴡᴇʟᴄᴏᴍᴇ「ᴏɴ」\n"
                                else: md+="┃┃❂͜͡➣ ✖ ᴡᴇʟᴄᴏᴍᴇ「ᴏғғ」\n"
                                if msg.to in simisimi: md+="┃┃❂͜͡➣ √ sɪᴍɪsɪᴍɪ「ᴏɴ」\n"
                                else: md+="┃┃❂͜͡➣ ✖ sɪᴍɪsɪᴍɪ「ᴏғғ」\n"                                
                                if wait["autoLeave"] == True: md+="┃┃❂͜͡➣ √ ᴀᴜᴛᴏʟᴇᴀᴠᴇ「ᴏɴ」\n"
                                else: md+="┃┃❂͜͡➣ ✖ ᴀᴜᴛᴏʟᴇᴀᴠᴇ「ᴏғғ」\n"                                      
                                boy.sendMessage(msg.to, md+"┃┣━━━━━━━━━━━━━━━━━━━━\n┃┃❧ 📅ᴛᴀɴɢɢᴀʟ : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n┃┃❧ ⌚ᴊᴀᴍ [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]\n  ┗━━━━━━━━━━━━━━━━━")
                                
                                
                        elif cmd == "creat" or text.lower() == 'creat':
                            if msg._from in admin:
                                boy.sendMessage(msg.to,"➣ ɪɴɪ ʙʀᴏ ᴄʀᴇᴀᴛᴏʀ ʙᴏᴛɴʏᴀ...!!!") 
                                ma = ""
                                for i in creator:
                                    ma = boy.getContact(i)
                                    boy.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "abo" or cmd == "informasi":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention(msg.to, sender, "「sᴇʟғʙᴏᴛ ʙʏ : ᴊᴀᴄᴋʏ ᴀʀᴇᴢᴀ ᴛᴇᴀᴍ」\n")
                               boy.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif cmd.startswith('penyewa'):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            try:
                                arr = []
                                today = datetime.today()
                                thn = 2025
                                bln = 12    #isi bulannya yg sewa
                                hr = 11    #isi tanggalnya yg sewa
                                future = datetime(thn, bln, hr)
                                days = (str(future - today))
                                comma = days.find(",")
                                days = days[:comma]
                                contact = boy.getContact(mid)
                                favoritelist = boy.getFavoriteMids()
                                grouplist = boy.getGroupIdsJoined()
                                contactlist = boy.getAllContactIds()
                                blockedlist = boy.getBlockedContactIds()
                                eltime = time.time() - mulai
                                bot = runtime(eltime)
                                start = time.time()
                                boy.sendMessage("u059095aa0cc2f6ef02d8ae72c3430163", 'Cek dulu')
                                elapsed_time = time.time() - start
                                ryan = boy.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 ɪɴғᴏʀᴍᴀsɪ sᴇʟғʙᴏᴛ 」\n• User : "
                                ret_ = "• Group : {} Group".format(str(len(grouplist)))
                                ret_ += "\n• Friend : {} Friend".format(str(len(contactlist)))
                                ret_ += "\n• Blocked : {} Blocked".format(str(len(blockedlist)))
                                ret_ += "\n• Favorite : {} Favorite".format(str(len(favoritelist)))
                                ret_ += "\n• Version : 「Self Bots 」"
                                ret_ += "\n• Expired : {} - {} - {}".format(str(hr), str(bln), str(thn))
                                ret_ += "\n• In days : {} again".format(days)
                                ret_ += "\n「 Speed Respon 」\n• {} detik".format(str(elapsed_time))
                                ret_ += "\n「 Selfbot Runtime 」\n• {}".format(str(bot))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                boy.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                boy.sendContact(to, "u059095aa0cc2f6ef02d8ae72c3430163")
                            except Exception as e:
                                boy.sendMessage(msg.to, str(e))

                        elif cmd == "aku" or text.lower() == 'gue':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': msg._from}
                               boy.sendMessage(msg)

                        elif text.lower() == "mymid":
                            if msg._from in admin:
                               boy.sendMessage(msg.to, msg._from)

                        elif ("Mid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = boy.getContact(key1)
                               boy.sendMessage(msg.to, "┝➲ 👤ɴᴀᴍᴀ : "+str(mi.displayName)+"\n┝➲ 🔄ᴍɪᴅ : " +key1)
                               boy.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Cek " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = boy.getContact(key1)
                               boy.sendMessage(msg.to, "╭━━━━━━━━━━━━━━━━━━━\n┝➲ 👤ɴᴀᴍᴀ : "+str(mi.displayName)+"\n┝➲ 📋ᴍɪᴅ : " +key1+"\n┝➲ 📝sᴛᴀᴛᴜs : "+str(mi.statusMessage))
                               boy.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(boy.getContact(key1)):
                                   boy.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   boy.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd == "mb":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               boy.sendMessage(msg)

                        elif text.lower() == "hc":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   boy.removeAllMessages(op.param2)
                                   boy.sendMessage(msg.to,'🚮ᴄʜᴀᴛ ᴅɪʜᴀᴘᴜs ʙᴏssǫɪᴜ...!!!')
                               except:
                                   pass

                        elif cmd.startswith("bc: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = boy.getGroupIdsJoined()
                               for group in saya:
                                   boy.sendMessage(group,"=======[ʙʀᴏᴀᴅᴄᴀsʜ]=======\n\n"+pesan+"\n\nCreator : ◄]·✪line.me/R/ti/p/~jackyeza✪·[►")

                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               boy.sendMessage(msg.to, "「Mykey」\nSetkey bot mu「 " + str(Setmain["keyCommand"]) + " 」")
                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   boy.sendMessage(msg.to, "Gagal mengganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   boy.sendMessage(msg.to, "「Setkey」\nSetkey diganti jadi「{}」".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               boy.sendMessage(msg.to, "「Setkey」\nSetkey mu back ke awal")

                        elif cmd == "poin":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               boy.sendMessage(msg.to, "ʀᴇsᴛᴀʀᴛ...!!!")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                            
                        elif cmd == "run":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "ʙᴏᴛ ᴛᴇʟᴀʜ ᴀᴋᴛɪғ sᴇʟᴀᴍᴀ" +waktu(eltime)
                               boy.sendMessage(msg.to,bot)
                            
                        elif cmd == "gin":
                          if msg._from in admin:
                            try:
                                G = boy.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "ᴅɪɢᴇᴍʙᴏᴋ ʀᴀᴘᴀᴛ"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "ᴛᴇʀʙᴜᴋᴀ"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(boy.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                boy.sendMessage(msg.to, "╭━━━━━━━━━━━━━━━━━━━\n┝❂͜͡     🎡ʙᴏᴛ ɢʀᴏᴜᴘ ɪɴғᴏ🎡\n┝━━━━━━━━━━━━━━━━━━━\n┝➲ ɴᴀᴍᴀ ɢʀᴏᴜᴘ : {}".format(G.name)+ "\n┝➲ ɪᴅ ɢʀᴏᴜᴘ : 🔽ɪᴅ ᴅɪʙᴀᴡᴀʜ🔽\n┝➲ {}".format(G.id)+ "\n┝➲ ᴘᴇᴍʙᴜᴀᴛ : {}".format(G.creator.displayName)+ "\n┝➲ ᴡᴀᴋᴛᴜ ᴅɪʙᴜᴀᴛ : {}".format(str(timeCreated))+ "\n┝➲ ᴊᴜᴍʟᴀʜ ᴍᴇᴍʙᴇʀ : {}".format(str(len(G.members)))+ "\n┝➲ ᴊᴜᴍʟᴀʜ ᴘᴇɴᴅɪɴɢ : {}".format(gPending)+ "\n┝➲ ɢʀᴏᴜᴘ ǫʀ : {}".format(gQr)+ "\n┝➲ ɢʀᴏᴜᴘ ᴛɪᴄᴋᴇᴛ : 🔽ʟɪɴᴋ🔽\n┝➲ {}\n╰━━━━━━━━━━━━━━━━━━━".format(gTicket))
                                boy.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                boy.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                boy.sendMessage(msg.to, str(e))

                        elif cmd.startswith("igr "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = boy.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = boy.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(boy.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "╭━━━━━━━━ ♨ʙᴏᴛ ɢʀᴏᴜᴘ ɪɴғᴏ♨"
                                ret_ += "\n╠➲ 👤ɴᴀᴍᴀ : {}".format(G.name)
                                ret_ += "\n╠➲ 📃ɪᴅ ɢʀᴏᴜᴘ : \n┝➲ {}".format(G.id)
                                ret_ += "\n╠➲ ⏳ᴄʀᴇᴀᴛᴏʀ : {}".format(gCreator)
                                ret_ += "\n╠➲ ⏰ᴄʀᴇᴀᴛᴇᴅ ᴛɪᴍᴇ : {}".format(str(timeCreated))
                                ret_ += "\n╠➲ 👪ᴍᴇᴍʙᴇʀ : {}".format(str(len(G.members)))
                                ret_ += "\n╠➲ 🚶ᴘᴇɴᴅɪɴɢ : {}".format(gPending)
                                ret_ += "\n╠➲ 👙ǫʀ : {}".format(gQr)
                                ret_ += "\n╠➲ 📠ᴛɪᴄᴋᴇᴛ : \n╠➲ {}\n╰━━━━━━━━ ↙↪ᴊᴀᴄᴋʏ ᴀʀᴇᴢᴀ↩↘".format(gTicket)
                                ret_ += ""
                                boy.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("ime "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = boy.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = boy.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "┝➲ "+ str(no) + ". " + mem.displayName
                                boy.sendMessage(to," ╭━━━━━━━━━━━━━━━━━━━\n ┝➲👤ɴᴀᴍᴀ ɢʀᴏᴜᴘ : [ " + str(G.name) + " ]\n ┝━━━━━━━━━━━━━━━━━━━\n ┝➲        🎡[ ᴍᴇᴍʙᴇʀ]🎡\n ┝━━━━━━━━━━━━━━━━━━━" + ret_ + "\n ┝━━━━━━━━━━━━━━━━━━━\n ┝➲     ♨「ᴛᴏᴛᴀʟ %i ᴍᴇᴍʙᴇʀ」♨\n ╰━━━━━━━━━━━━━━━━━━━" % len(G.members))
                            except: 
                                pass

                        elif cmd.startswith("leave: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = boy.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = boy.getGroup(i)
                                if ginfo == group:
                                    k1.leaveGroup(i)
                                    k2.leaveGroup(i)
                                    k3.leaveGroup(i)
                                    k4.leaveGroup(i)
                                    k5.leaveGroup(i)
                                    k6.leaveGroup(i)
                                    k7.leaveGroup(i)
                                    k8.leaveGroup(i)
                                    k9.leaveGroup(i)
                                    k10.leaveGroup(i)
                                    boy.sendMessage(msg.to,"ʙᴇʀʜᴀsɪʟ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ ɢʀᴏᴜᴘ " +str(ginfo.name))

                        elif cmd == "fl":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = boy.getAllContactIds()
                               for i in gid:
                                   G = boy.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃┃ " + str(a) + ". " +G.displayName+ "\n"
                               boy.sendMessage(msg.to,"┏━━[ ʟɪsᴛ ᴛᴇᴍᴀɴ ]\n┃┃\n"+ma+"┃┃\n┗━━[ ᴛᴏᴛᴀʟ「"+str(len(gid))+"」ғʀɪᴇɴᴅs ]")

                        elif cmd == "gl":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = boy.getGroupIdsJoined()
                               for i in gid:
                                   G = boy.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃┃ " + str(a) + ". " +G.name+ "\n"
                               boy.sendMessage(msg.to,"┏━━[ ʟɪsᴛ ɢʀᴏᴜᴘ ]\n┃┃\n"+ma+"┃┃\n┗━━[ ᴛᴏᴛᴀʟ「"+str(len(gid))+"」ɢʀᴏᴜᴘs ]")

                        elif cmd == "gl1":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = ki.getGroupIdsJoined()
                               for i in gid:
                                   G = k1.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃┃ " + str(a) + ". " +G.name+ "\n"
                               k1.sendMessage(msg.to,"┏━━[ ʟɪsᴛ ɢʀᴏᴜᴘ ]\n┃┃\n"+ma+"┃┃\n┗━━[ Total「"+str(len(gid))+"」Groups ]")


                        elif cmd == "opn":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = k1.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   k1.updateGroup(X)
                                   k1.sendMessage(msg.to, "ᴜʀʟ ᴛᴇʟᴀʜ ᴅɪʙᴜᴋᴀ")

                        elif cmd == "clo":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = k1.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   k1.updateGroup(X)
                                   k1.sendMessage(msg.to, "ᴜʀʟ ᴛᴇʟᴀʜ ᴅɪᴛᴜᴛᴜᴘ")

                        elif cmd == "url":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = k1.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      k1.updateGroup(x)
                                   gurl = k1.reissueGroupTicket(msg.to)
                                   k1.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)
                                   
                                   
                        elif cmd == "rjt":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                              ginvited = boy.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      boy.rejectGroupInvitation(gid)
                                  boy.sendMessage(to, "ʙᴇʀʜᴀsɪʟ ᴛᴏʟᴀᴋ sᴇʙᴀɴʏᴀᴋ {} ᴜɴᴅᴀɴɢᴀɴ ɢʀᴏᴜᴘ ".format(str(len(ginvited))))
                              else:
                                  boy.sendMessage(to, "ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴜɴᴅᴀɴɢᴀɴ ᴛᴇʀᴛᴜɴᴅᴀ")  
                                  
                        
                        elif 'lc ' in text.lower():
                                try:
                                    typel = [1001,1002,1003,1004,1005,1006]
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = boy.getContact(u).mid
                                    s = boy.getContact(u).displayName
                                    hasil = boy.getHomeProfile(mid=a)
                                    st = hasil['result']['feeds']
                                    for i in range(len(st)):
                                        test = st[i]
                                        result = test['post']['postInfo']['postId']
                                        boy.likePost(str(sender), str(result), likeType=random.choice(typel))
                                        boy.createComment(str(sender), str(result), 'ʜᴀᴅɪʀ ᴅᴜʟʟ, ᴊᴀɴɢᴀɴ ʙᴜᴀᴛ sᴛᴀᴛᴜs ɢᴀsʟᴏɴ ᴍᴏʟᴏ ʟᴀʜ :)')
                                    boy.sendMessage(msg.to, 'ᴜᴅᴀʜ ᴀᴋᴜ ʟɪᴋᴇ + ᴄᴏᴍᴇɴᴛ ᴛᴜʜ ᴛᴏᴛᴀʟ '+str(len(st))+' ᴅᴀʀɪ sᴛᴀᴛᴜs ɢᴀsʟᴏɴᴍᴜ ᴋᴀᴋ ' + str(s))
                                except Exception as e:
                                    boy.sendMessage(receiver, str(e))
   #================= zona js===================#                                 
                        elif cmd == "nice":
                          if msg._from in admin:
                            if msg.toType == 2:
                               group = boy.getGroup(to)
                               gMembers = [contact.mid for contact in group.members]
                               for i in gMembers:
                                   time.sleep(0.008)
                                   boy.kickoutFromGroup(to,[i])
                               boy.sendMessage(to,"Just Some Casual Cleasing")
                            else:
                               boy.sendMessage(to,"failed >_<")

#===========BOT UPDATE============#
                        elif cmd == "ugp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                boy.sendMessage(msg.to,"ᴋɪʀɪᴍ ғᴏᴛᴏɴʏᴀ......")
                                
                        elif cmd == "uf":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["AFfoto"][mid] = True
                                boy.sendMessage(msg.to,"ᴋɪʀɪᴍ ғᴏᴛᴏɴʏᴀ......")
                                
                        elif cmd.startswith("mme: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = boy.getProfile()
                                profile.displayName = string
                                boy.updateProfile(profile)
                                boy.sendMessage(msg.to,"ɴᴀᴍᴀ ᴅɪɢᴀɴᴛɪ ᴊᴀᴅɪ" + string + "")
                                
#===========Hiburan============#
                        elif cmd.startswith("lagu "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    data = {
                                            "type": "flex",
                                            "altText": "Musik",
                                            "contents": {
"styles": {"body": {"backgroundColor": "#000000"},"footer": {"backgroundColor": "#bfff00"}},"type": "bubble","size": "micro","body": {"contents": [{"contents": [{"url": "https://obs.line-scdn.net/{}".format(boy.getContact(sender).pictureStatus),"type": "image"},{"type": "separator","color": "#FF00FF"},{
"text": "ᴍᴜsɪᴄ ʙᴏᴛ\n\nᴍᴘ3 ᴘʟᴀʏ ᴍᴜsɪᴄ\n\nsᴏɴɢ ᴀʟʙᴜᴍ","size": "xs","color": "#00FF33","wrap": True,"weight": "bold","type": "text"}],"type": "box","spacing": "md","layout": "horizontal"},{"type": "separator","color": "#FF00FF"},{"contents": [{"contents": [{
"text": "💻ᴊᴜᴅᴜʟ :〘 " + vid.title + " 〙","size": "xxs","margin": "none","color": "#FFFF00","wrap": True,"weight": "regular","type": "text"}],"type": "box","layout": "baseline"}],"type": "box","layout": "vertical"}],"type": "box","spacing": "md","layout": "vertical"},"footer": {"type": "box","layout": "vertical","contents": [{"type": "box","layout": "horizontal","contents": [{
"type": "button","flex": 2,"style": "primary","color": "#660000","height": "sm","action": {"type": "uri","label": "ᴘʟᴀʏ ᴅɪʙᴀᴡᴀʜ","uri": "https://line.me/ti/p/~jackyeza"}}]}]}}}
                                sendTemplate(to, data)
                                boy.sendAudioWithURL(msg.to, me)
                            except Exception as e:
                                boy.sendMessage(msg.to,str(e))


#===========BOT UPDATE============#
                        elif cmd == "pa" or text.lower() == 'hai':
                          if msg._from in admin:
                               group = boy.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4, jml = [], [], [], [], len(nama)
                               if jml <= 20:
                                   mentionMembers(msg.to, nama)
                               if jml > 20 and jml < 40:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, len(nama)-1):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                               if jml > 40 and jml < 60:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, len(nama)-1):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                               if jml > 60 and jml < 80:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (80, len(nama)-1):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                               if jml > 80 and jml < 100:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, len(nama)-1):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm4)
                                   
                        elif cmd == "♨" or text.lower() == 'sugeng':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                            	group = boy.getGroup(msg.to)
                          Rmem = [contact.mid for contact in group.members]
                          Dmem = len(Rmem)//20
                          try:                          	
                              for mentionMembers in range(Dmem+1):
                                  no = 0
                                  ret_ = "╭──「ᴅᴀғᴛᴀʀ ᴀʜʟɪ ᴛɪᴋᴜɴɢ」  "
                                  dataMid = []
                                  for dataMention in group.members[mentionMembers*20 : (mentionMembers+1)*20]:
                                      dataMid.append(dataMention.mid)
                                      no += 1
                                      ret_ += "\n│◈ @!".format(str(no))
                                  ret_ += "\n╰──「ᴛᴏᴛᴀʟ ᴀʜʟɪ ᴛɪᴋᴜɴɢ」{} ".format(str(len(dataMid)))
                                  sendMeention2(msg.to, ret_, dataMid)
                          except Exception as Ewe:
                              print(Ewe)
                                
                        elif cmd == "bme":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                G = boy.getGroup(msg.to)
                                boy.sendMessage(msg.to, "◈ Bye bye fams ◈"+str(G.name))
                                boy.leaveGroup(msg.to)
                                
                        elif cmd == "sr":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = boy.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = boy.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = boy.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                boy.sendMessage(msg.to, " ❧ ʙᴏᴛ sᴘᴇᴇᴅ ʀᴇsᴘᴏɴ \n\n - ɢᴇᴛ ᴘʀᴏғɪʟᴇ\n   %.10f\n - ɢᴇᴛ ᴄᴏɴᴛᴀᴄᴛ\n   %.10f\n - ɢᴇᴛ ɢʀᴏᴜᴘ\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               boy.sendMessage(msg.to, "💿[ʟᴏᴀᴅɪɴɢ] sᴘᴇᴇᴅ...!!!")
                               elapsed_time = time.time() - start
                               took = time.time() - start
                               a = "ᴋᴇᴄᴇᴘᴀᴛᴀɴ : %.3f ᴅᴇᴛɪᴋ ʙᴏssǫɪᴜ" % (took)
                               data = {
                                           "type": "text",
                                           "text": "{}".format(str(a)),
                                           "sentBy": {
                                           "label": "ᴊᴀᴄᴋʏ ᴀʀᴇᴢᴀ",
                                           "iconUrl": "http://jackyeza.xtgem.com/downloads/bahan.gif",
                                           "uri": "line://ti/p/~jackyeza"
                                         }
                                     }
                               sendTemplate(to, data)

                        elif cmd == "lur on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['AFreadPoint'][msg.to] = msg_id
                                 Setmain['AFreadMember'][msg.to] = {}
                                 boy.sendMessage(msg.to, "Lurking berhasil diaktifkan\n\n??ᴛᴀɴɢɢᴀʟ : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n⌚ᴊᴀᴍ [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lur off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['AFreadPoint'][msg.to]
                                 del Setmain['AFreadMember'][msg.to]
                                 boy.sendMessage(msg.to, "Lurking berhasil dinoaktifkan\n\n📅ᴛᴀɴɢɢᴀʟ : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n⌚ᴊᴀᴍ [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lu":
                          if msg._from in admin:
                            if msg.to in Setmain['AFreadPoint']:
                                if Setmain['AFreadMember'][msg.to] != {}:
                                    nad = []
                                    for x in Setmain['AFreadMember'][msg.to]:
                                        nad.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Lurkers ]\n1. ".format(str(len(nad)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in nad:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(nad):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(boy.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\n📅ᴛᴀɴɢɢᴀʟ : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n⌚ᴊᴀᴍ [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        boy.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['AFreadPoint'][msg.to]
                                        del Setmain['AFreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['AFreadPoint'][msg.to] = msg.id
                                    Setmain['AFreadMember'][msg.to] = {}
                                else:
                                    boy.sendMessage(msg.to, "User kosong...")
                            else:
                                boy.sendMessage(msg.to, "Ketik lurking on dulu")

                        elif cmd == "intip":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  a = "sɪᴀᴘ ᴍᴇɴᴄʏᴅᴜᴋ ʙᴏss 👀"
                                  data={"type": "flex","altText": "cyduk para jones","contents": {"type": "bubble","size": "nano","styles": {"body": {"backgroundColor": '#000000'},},"body": {"type": "box","layout": "vertical","contents": [{"type": "separator","color": "#FF00FF"},{"type": "text","text": a,"color": "#00FF00","size": "xxs","align":"center","weight":"bold"},{"type": "separator","color": "#FF00FF"},]},}}
                                  sendTemplate(to, data)
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "inoff":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  a = "ᴍᴀᴛɪ\n📅ᴛᴀɴɢɢᴀʟ : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n⌚ᴊᴀᴍ      : "+ datetime.strftime(timeNow,'%H:%M:%S')+""
                                  data = {"type": "flex","altText": "pemburu jones telah dibunuh","contents": {"type": "bubble","size": "nano","styles": {"body": {"backgroundColor": '#000000'},},"body": {"type": "box","layout": "vertical","contents": [{"type": "separator","color": "#FF00FF"},{"type": "text","text": a,"color": "#00FF00","wrap": True,"size": "xxs"},{"type": "separator","color": "#FF00FF"},]},}}
                                  sendTemplate(to, data)
                              else:
                                  boy.sendMessage(msg.to, "sᴜᴅᴀʜ ᴛɪᴅᴀᴋ ᴀᴋᴛɪғ")

                        elif cmd.startswith("stag: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["AFlimit"] = num
                                boy.sendMessage(msg.to,"ᴛᴏᴛᴀʟ sᴘᴀᴍᴛᴀɢ ᴅɪᴜʙᴀʜ ᴍᴇɴᴊᴀᴅɪ " +strnum)

                        elif cmd.startswith("scall: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                boy.sendMessage(msg.to,"ᴛᴏᴛᴀʟ sᴘᴀᴍᴄᴀʟʟ ᴅɪᴜʙᴀʜ ᴍᴇɴᴊᴀᴅɪ " +strnum)

                        elif cmd.startswith("chipok "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Setmain["AFlimit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                boy.sendMessage(msg)
                                            except Exception as e:
                                                boy.sendMessage(msg.to,str(e))
                                    else:
                                        boy.sendMessage(msg.to,"Jumlah melebihi 1000")
                                        
                        elif cmd == "naik coy":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = boy.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                #boy.sendMessage(msg.to, "ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢɪʀɪᴍ {} ᴜɴᴅᴀɴɢᴀɴ ᴄᴀʟʟ ɢʀᴏᴜᴘ ".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        boy.sendMessage(msg.to,str(e))
                                else:
                                    boy.sendMessage(msg.to,"Jumlah melebihi batas")

                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      boy.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '5'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      boy.sendMessage(midd, str(Setmain["AFmessage1"]))                                                                       
                        elif 'Mbt' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in creator:
                               boy.sendMessage(msg.to,"📷sᴇʟғʙᴏᴛ ʙʏ ᴊᴀᴄᴋʏ ᴀʀᴇᴢᴀ📷\n"+boy.authToken)

#==============================================================================# 
                       

#===========Settings============#
                        elif 'Simi ' in msg.text:
                              spl = msg.text.replace('Simi ','')
                              if spl == 'on':
                                  if msg.to in simisimi:
                                       msgs = "Simi-simi sudah aktif"
                                  else:
                                       simisimi.append(msg.to)
                                       ginfo = boy.getGroup(msg.to)
                                       msgs = "Simi-simi Diaktifkan\nDi Group : " +str(ginfo.name)
                                  boy.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in simisimi:
                                         simisimi.remove(msg.to)
                                         ginfo = boy.getGroup(msg.to)
                                         msgs = "Simi-simi Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Simi-simi Sudah Tidak Aktif"
                                    boy.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs) 
                                    
                        elif 'Wl ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Wl ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "ᴘᴇɴʏᴀᴍʙᴜᴛᴀɴ sᴜᴅᴀʜ ᴀᴋᴛɪғ"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = boy.getGroup(msg.to)
                                       msgs = "ᴡᴇʟᴄᴏᴍᴇ ᴍsɢ ᴅɪᴀᴋᴛɪғᴋᴀɴ\n ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                  boy.sendMessage(msg.to, "「ᴅɪᴀᴋᴛɪғᴋᴀɴ」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = boy.getGroup(msg.to)
                                         msgs = "ᴡᴇʟᴄᴏᴍᴇ ᴍsɢ ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ\nᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                    else:
                                         msgs = "ᴘᴇɴʏᴀᴍʙᴜᴛᴀɴ sᴜᴅᴀʜ ᴛɪᴅᴀᴋ ᴀᴋᴛɪғ"
                                    boy.sendMessage(msg.to, "「ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ」\n" + msgs)
                                    
#===========KICKOUT============#
                        elif ("!?? " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           G = boy.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           boy.updateGroup(G)
                                           invsend = 0
                                           Ticket = boy.reissueGroupTicket(msg.to)
                                           boy.kickoutFromGroup(msg.to, [target])
                                           X = boy.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           boy.updateGroup(X)
                                       except:
                                           pass

                        elif ("!!/ " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass
                                
                      #  elif  text.lower() == "virus" or text.lower () == "Crash":
                     #     if wait["selfbot"] == True:
                            #if msg._from in admin:
                       #       dia = ("CACAT MAINANNYA CRASH","Tercyduck ingin ngecrash!","Kamu asu ngecrash terus!","crash cresh crash cresh, bikin hp orang lag anjing!")
                #              ngkol = random.choice(dia)
                #              random.choice(ABC).sendText(msg.to,ngkol)
                       #       random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                       #       random.choice(ABC).sendText(msg.to,"Mampus!")
                      #        if msg.text in ["!cipok",".desah","!makan","!","?","!kickall",".kickall","Nuke","Cleanse","Ratakan","Mayhem","MB Mayhem","Kick all","kickall","!rata","play","sory","sorry","maaf","sexi",".",","]:
                 #             	Peringatan = ("Manual kek jangan pake bot.","Cupu lu! Ratain pake bot!","Lain kali liat liat dulu~","ＴＥＲＣＹＤＵＣＫ")
                         #     Vonis = random.choice(Peringatan)
                #              random.choice(ABC).sendText(msg.to, Vonis)
                    #          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                              
                             #  for x in key["MENTIONEES"]:
                                  #  targets.append(x["M"])
                           #    for target in targets:
                               #    if target not in Bots:
                                   #    try:
                                        #   random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                      # except:
                                        #   pass
                                        
                        elif cmd == "fresh" or text.lower() == 'kinclong':
                            if msg._from in admin:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                wait["invite"] = False
                                boy.sendMessage(msg.to,"ʙᴇʀʜᴀsɪʟ ᴅɪʀᴇғʀᴇsʜ....!!!")

                        elif cmd == "ca" or text.lower() == 'ca':
                                ma = ""
                                for i in admin:
                                    ma = boy.getContact(i)
                                    boy.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#===========COMMAND ON OFF============#
                        elif cmd == "nt on" or text.lower() == 'nt on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                boy.sendMessage(msg.to,"ɴᴏᴛᴀɢ ᴅɪᴀᴋᴛɪғᴋᴀɴ")

                        elif cmd == "nt off" or text.lower() == 'nt off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = False
                                boy.sendMessage(msg.to,"ɴᴏᴛᴀɢ ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ")

                        elif cmd == "timeline on" or text.lower() == 'tl on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Timeline"] = True
                                boy.sendMessage(msg.to," sᴛᴀᴛᴜs ᴛɪᴍᴇʟɪɴᴇ ɢʜᴅ\nᴜsᴇʀ: @! \nsᴇɴᴅ ʏᴏᴜʀ ᴘᴏsᴛ,\nʟɪᴋᴇ ᴅᴏɴᴇ-> ᴛᴏ ᴏғғ: ᴛɪᴍᴇʟɪɴᴇ ᴏғғ")

                        elif cmd == "timeline off" or text.lower() == 'tl off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Timeline"] = False
                                boy.sendMessage(msg.to," sᴛᴀᴛᴜs ᴛɪᴍᴇʟɪɴᴇ ɢʜᴅ\nᴜsᴇʀ: @! \nᴅᴇᴛᴇᴄᴛɪᴏɴ ᴛɪᴍᴇʟɪɴᴇ ᴏғғ")
                                
                        elif cmd == "invi on" or text.lower() == 'invi on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["invite"] = False
                                boy.sendMention(msg.to, "「 Status Invite 」\nUser ", "\nSilahkan kirim kontaknya,\nKetik invite off jika sudah slesai")

                        elif cmd == "invi off" or text.lower() == 'invi off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["invite"] = True
                                boy.sendMention(msg.to, "「 Status Invite 」\nUser ", " \nInvite via contact dinonaktifkan")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                boy.sendMessage(msg.to,"Deteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                boy.sendMessage(msg.to,"Deteksi contact dinonaktifkan")
                                
                        elif cmd == "rg on" or text.lower() == 'rg on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentiongift"] = True
                                boy.sendMessage(msg.to,"ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ɢɪғᴛ ᴅɪᴀᴋᴛɪғᴋᴀɴ")

                        elif cmd == "rg off" or text.lower() == 'rg off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentiongift"] = False
                                boy.sendMessage(msg.to,"ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ɢɪғᴛ ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ")                                
                                
                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                boy.sendMessage(msg.to,"Auto Leave Diaktifkan")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                boy.sendMessage(msg.to,"Auto Leave Dimatikan")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                boy.sendMessage(msg.to,"Auto Add Diaktifkan")                              

                        elif cmd == "ajo on" or text.lower() == 'ajo on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                boy.sendMessage(msg.to,"Autojoin diaktifkan")

                        elif cmd == "ajo off" or text.lower() == 'ajo off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                boy.sendMessage(msg.to,"Autojoin dinonaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                boy.sendMessage(msg.to,"Auto Add Dimatikan")

                        elif cmd == "str on" or text.lower() == 'str on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                boy.sendMessage(msg.to,"ᴅᴇᴛᴇᴋsɪ sᴛɪᴄᴋᴇʀ ᴅɪᴀᴋᴛɪғᴋᴀɴ...!!!")

                        elif cmd == "str off" or text.lower() == 'str off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = False
                                boy.sendMessage(msg.to,"ᴅᴇᴛᴇᴋsɪ sᴛɪᴄᴋᴇʀ ᴅɪᴍᴀᴛɪᴋᴀɴ...!!!")

                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = False
                                boy.sendMessage(msg.to,"Auto Join Ticket Diaktifkan")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = True
                                boy.sendMessage(msg.to,"Auto Join Ticket Dimatikan")
                                
                        elif cmd == "unsend on" or text.lower() == 'us on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["unsend"] = True
                                boy.sendMessage(msg.to,"detect unsend diaktifkan")

                        elif cmd == "unsend off" or text.lower() == 'us off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["unsend"] = False
                                boy.sendMessage(msg.to,"detect unsend dinonaktifkan")

#===========COMMAND BLACKLIST============#
                        elif ("Talkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           boy.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Untalkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           boy.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkwblacklist"] = True
                                boy.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkdblacklist"] = True
                                boy.sendMessage(msg.to,"Kirim kontaknya...")

                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           boy.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           boy.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                boy.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = True
                                boy.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                boy.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +boy.getContact(m_id).displayName + "\n"
                                boy.sendMessage(msg.to,"⏩ Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["Talkblacklist"] == {}:
                                boy.sendMessage(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +boy.getContact(m_id).displayName + "\n"
                                boy.sendMessage(msg.to,"⏩ Talkban User\n\n"+ma+"\nTotal「%s」Talkban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "blc" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    boy.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = boy.getContact(i)
                                        boy.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "cb" or text.lower() == 'cb':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = boy.getContacts(wait["blacklist"])
                              mc = "���%i」User Blacklist" % len(ragets)
                              boy.sendMessage(msg.to,"Sukses membersihkan " +mc)

#===========ADMIN ADD============#
                        elif ("Adm " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin[target] = True
                                           f=codecs.open('admin.json','w','utf-8')
                                           json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)                                            
                                           boy.sendMessage(msg.to,"Berhasil menambahkan admin")
                                       except:
                                           pass

                        elif ("Sa " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff.append(target)
                                           boy.sendMessage(msg.to,"Berhasil menambahkan staff")
                                       except:
                                           pass

                        elif ("Ba " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.append(target)
                                           boy.sendMessage(msg.to,"Berhasil menambahkan bot")
                                       except:
                                           pass

                        elif ("Ad " in msg.text):
                            if msg._from in creator:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del admin[target]
                                           f=codecs.open('admin.json','w','utf-8')
                                           json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)                                            
                                           boy.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Sd " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   for target in targets:
                                       try:
                                           staff.remove(target)
                                           boy.sendMessage(msg.to,"Berhasil menghapus staff")
                                       except:
                                           pass

                        elif ("Bd " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   for target in targets:
                                       try:
                                           Bots.remove(target)
                                           boy.sendMessage(msg.to,"Berhasil menghapus bot")
                                       except:
                                           pass
#===========COMMAND SET========================#

                        elif msg.contentType == 16:
                           if wait["Timeline"] == True:
                              msg.contentType = 0
                              msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                              boy.sendMessage(msg.to, "ʟɪᴋᴇ ᴅᴏɴᴇ ʙᴏss")

                        elif 'Set pesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  boy.sendMessage(msg.to, "Gagal mengganti Pesan Message")
                              else:
                                  wait["message"] = spl
                                  boy.sendMessage(msg.to, "「Pesan Msg」\nPesan Message diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set welcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  boy.sendMessage(msg.to, "Gagal mengganti Welcome Message")
                              else:
                                  wait["welcome"] = spl
                                  boy.sendMessage(msg.to, "「Welcome Msg」\nWelcome Message diganti jadi :\n\n「{}」".format(str(spl)))
                                  
                        elif 'Set leave: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set leave: ','')
                              if spl in [""," ","\n",None]:
                                  boy.sendMessage(msg.to, "Gagal mengganti Leave Message")
                              else:
                                  wait["leave"] = spl
                                  boy.sendMessage(msg.to, "「Leave Msg」\nLeave Message diganti jadi :\n\n「{}」".format(str(spl)))                                    

                        elif 'Set respon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  boy.sendMessage(msg.to, "Gagal mengganti Respon Message")
                              else:
                                  wait["Respontag"] = spl
                                  boy.sendMessage(msg.to, "「Respon Msg」\nRespon Message diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set spam: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  boy.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["AFmessage1"] = spl
                                  boy.sendMessage(msg.to, "「Spam Msg」\nSpam Message diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set sider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  boy.sendMessage(msg.to, "Gagal mengganti Sider Message")
                              else:
                                  wait["mention"] = spl
                                  boy.sendMessage(msg.to, "「Sider Msg」\nSider Message diganti jadi :\n\n「{}」".format(str(spl)))

                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               boy.sendMessage(msg.to, "「Pesan Msg」\nPesan Message lu :\n\n「 " + str(wait["message"]) + " 」")

                        elif text.lower() == "cek welcome":
                            if msg._from in admin:
                               boy.sendMessage(msg.to, "「Welcome Msg」\nWelcome Message lu :\n\n「 " + str(wait["welcome"]) + " 」")
                               
                        elif text.lower() == "cek leave":
                            if msg._from in admin:
                               boy.sendMessage(msg.to, "「Leave Msg」\nLeave Message lu :\n\n「 " + str(wait["leave"]) + " 」")                                 

                        elif text.lower() == "cek respon":
                            if msg._from in admin:
                               boy.sendMessage(msg.to, "「Respon Msg」\nRespon Message lu :\n\n「 " + str(wait["Respontag"]) + " 」")

                        elif text.lower() == "cek spam":
                            if msg._from in admin:
                               boy.sendMessage(msg.to, "「Spam Msg」\nSpam Message lu :\n\n「 " + str(Setmain["AFmessage1"]) + " 」")

                        elif text.lower() == "cek sider":
                            if msg._from in admin:
                               boy.sendMessage(msg.to, "「Sider Msg」\nSider Message lu :\n\n「 " + str(wait["mention"]) + " 」")
                               
                               #RESPON PUBLIG#
                        elif text.lower() == "me2":
                               contact = boy.getContact(sender)
                               sendTemplate(to,{"type":"flex","altText": "ᴀʀᴇᴢᴀ ʙᴏᴛ","contents":{"type":"bubble","size": "nano","footer":{"type":"box","layout":"horizontal","contents":[{"color":"#FF69B4","size":"xxs","wrap":True,"action":{"type":"uri","uri":"line://app/1636169025-yQ7bGMVA?type=profile"},"type":"text","text":"ᴀʀᴇᴢᴀ ʙᴏᴛ","align":"center","weight":"bold"},{"type":"separator","color":"#FF00FF"},{"color":"#FF69B4","size":"xxs","wrap":True,"action":{"type":"uri","uri":"line://ti/p/~jackyeza"},"type":"text","text":"ᴄʜᴀᴛ ᴍᴇ","align":"center","weight":"bold"}]},"styles":{"footer":{"backgroundColor":"#FFD2E6"},"body":{"backgroundColor":"#000000"}},"body":{"type":"box","contents":[{"type":"box","contents":[{"type":"separator","color":"#FF00FF"},{"aspectMode":"cover","gravity":"bottom","aspectRatio":"1:1","size":"sm","type":"image","url":"https://1.bp.blogspot.com/-wFKL1ebm1DA/XZ1I2I-2p9I/AAAAAAAAAGM/0ew18QpWoLsmy2IoGTQ5JkJvOeRQ87cGgCLcBGAsYHQ/s1600/logo.jpg"},{"type":"separator","color":"#FF00FF"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://raw.githubusercontent.com/achinkmaulana/png/master/YT-Logo.png"},{"type":"separator","color":"#FF00FF"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://media.giphy.com/media/qqWB4u3mrTlrG/giphy.gif"},{"type":"separator","color":"#FF00FF"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://i.pinimg.com/originals/a6/94/ec/a694ec9773292abec803f07befd73e74.gif"},{"type":"separator","color":"#FF00FF"}],"layout":"vertical","spacing":"none","flex":1},{"type":"separator","color":"#FF00FF"},{"type":"box","contents":[{"type":"separator","color":"#FF00FF"},{"color":"#413877","size":"md","wrap":True,"type":"text","text":"ᴀʀᴇᴢᴀ ᴘʀᴏᴊᴇᴄᴛ","weight":"bold"},{"type":"separator","color":"#FF00FF"},{"color":"#413877","size":"md","wrap":True,"type":"text","text":"{}".format(contact.displayName),"weight":"bold"},{"type":"separator","color":"#FF00FF"},{"color":"#FF69B4","size":"xs","wrap":True,"type":"text","text":"Status Profile:","weight":"bold"},{"type":"text","text":"{}".format(contact.statusMessage),"size":"xxs","wrap":True,"color":"#422002"}],"layout":"vertical","flex":2}],"layout":"horizontal","spacing":"md"},"hero":{"aspectMode":"cover","margin":"xxl","aspectRatio":"1:1","size":"micro","type":"image","url":"https://obs.line-scdn.net/{}".format(contact.pictureStatus)}}})
                              #KARYAKU SENDIRI#  
                        elif text.lower() == "id" or text.lower() == "mid":
                               contact = boy.getContact(msg._from)
                               xname = contact.displayName
                               a = "Nama: "+ xname + "\nMid: " + msg._from+"\nStatus: {}".format(contact.statusMessage)
                               data = {
                                           "type": "text",
                                           "text": "{}".format(str(a)),
                                           "sentBy": {
                                           "label": "@{}".format(str(xname)),
                                           "iconUrl": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                           "uri": "line://ti/p/~jackyeza"
                                         }
                                     }
                               sendTemplate(to, data)
                        elif text.lower() == "nah":
                               contact = boy.getContact(msg._from)
                               xname = contact.displayName
                               a = "ɴᴀʜ ᴍᴏʟᴏ, ʙᴏsᴇɴ ᴀɴᴇ ᴅᴇɴɢᴇʀɴʏᴀ"
                               b = ""+xname+""
                               data={"type": "flex","altText": "semvak bolong","contents": {"type": "bubble","size": "nano","styles": {"body": {"backgroundColor": '#000000'},},"body": {"type": "box","layout": "vertical","contents": [{"type": "separator","color": "#FF00FF"},{"type": "text","text": a,"color": "#00FF00","align":"center","wrap": True,"size": "xxs"},{"type": "separator","color": "#FF00FF"},{"type": "text","text": b,"color": "#00FF00","align":"center","wrap": True,"size": "xxs"},{"type": "separator","color": "#FF00FF"},]},}}
                               sendTemplate(to, data) 
                        elif 'odir' in msg.text:
                               contact = boy.getContact(msg._from)
                               xname = contact.displayName
                               a = "ᴋᴀᴅɪʀ ʙᴏss "
                               b = ""+xname+""
                               data={"type": "flex","altText": "semvak bolong","contents": {"type": "bubble","size": "nano","styles": {"body": {"backgroundColor": '#000000'},},"body": {"type": "box","layout": "vertical","contents": [{"type": "separator","color": "#FF00FF"},{"type": "text","text": a,"color": "#00FF00","align":"center","wrap": True,"size": "xxs"},{"type": "separator","color": "#FF00FF"},{"type": "text","text": b,"color": "#00FF00","align":"center","wrap": True,"size": "xxs"},{"type": "separator","color": "#FF00FF"},]},}}
                               sendTemplate(to, data) 
                        elif text.lower() == "absen":
                               contact = boy.getContact(msg._from)
                               xname = contact.displayName
                               a = " ᴋᴀᴅɪʀ ʙᴏss"
                               b = ""+xname+""
                               data={"type": "flex","altText": "semvak bolong","contents": {"type": "bubble","size": "nano","styles": {"body": {"backgroundColor": '#000000'},},"body": {"type": "box","layout": "vertical","contents": [{"type": "separator","color": "#FF00FF"},{"type": "text","text": a,"color": "#00FF00","align":"center","wrap": True,"size": "xxs"},{"type": "separator","color": "#FF00FF"},{"type": "text","text": b,"color": "#00FF00","align":"center","wrap": True,"size": "xxs"},{"type": "separator","color": "#FF00FF"},]},}}
                               sendTemplate(to, data) 
                        elif 'ssala' in msg.text:
                               contact = boy.getContact(msg._from)
                               xname = contact.displayName
                               a = "وَعَلَيْكُمُ الْسَّــــــــــلاَمُ وَرَحْمَةُ اللَّــــــــــهِ وَبَرَكَــــــــــاتُةُ"
                               b = ""+xname+""
                               data={"type": "flex","altText": "salam religi","contents": {"type": "bubble","size": "nano","styles": {"body": {"backgroundColor": '#000000'},},"body": {"type": "box","layout": "vertical","contents": [{"type": "separator","color": "#FF00FF"},{"type": "text","text": a,"color": "#FF7F00","align":"center","wrap": True,"size": "xxs"},{"type": "separator","color": "#FF00FF"},{"type": "text","text": b,"color": "#00FF00","align":"center","wrap": True,"size": "xxs"},{"type": "separator","color": "#FF00FF"},]},}}
                               sendTemplate(to, data)
                        elif text.lower() == "waalaikumsalam":
                               contact = boy.getContact(msg._from)
                               xname = contact.displayName
                               a = "ɴᴀʜ ᴄᴀᴋᴇᴘ ɴɪʜ ᴀᴅᴀ ʏᴀɴɢ sᴀʟᴀᴍ ʟᴀɴɢsᴜɴɢ ᴅɪᴊᴀᴡᴀʙ"
                               b = ""+xname+""
                               data={"type": "flex","altText": "semoga diberikan rejeki yg melimpah amin","contents": {"type": "bubble","size": "nano","styles": {"body": {"backgroundColor": '#000000'},},"body": {"type": "box","layout": "vertical","contents": [{"type": "separator","color": "#FF00FF"},{"type": "text","text": a,"color": "#FF7F00","align":"center","wrap": True,"size": "xxs"},{"type": "separator","color": "#FF00FF"},{"type": "text","text": b,"color": "#00FF00","align":"center","wrap": True,"size": "xxs"},{"type": "separator","color": "#FF00FF"},]},}}
                               sendTemplate(to, data) 
                        elif 'naik' in msg.text:
                               contact = boy.getContact(msg._from)
                               xname = contact.displayName
                               a = "ɴᴀɪᴋ-ɴᴀɪᴋ ᴋᴇᴘᴜɴᴄᴀᴋ ɢᴜɴᴜɴɢ 😂"
                               b = ""+xname+""
                               data={"type": "flex","altText": "pasti dimodusin kalau naik","contents": {"type": "bubble","size": "nano","styles": {"body": {"backgroundColor": '#000000'},},"body": {"type": "box","layout": "vertical","contents": [{"type": "separator","color": "#FF00FF"},{"type": "text","text": a,"color": "#FF7F00","align":"center","wrap": True,"size": "xxs"},{"type": "separator","color": "#FF00FF"},{"type": "text","text": b,"color": "#00FF00","align":"center","wrap": True,"size": "xxs"},{"type": "separator","color": "#FF00FF"},]},}}
                               sendTemplate(to, data) 
                        elif text.lower() == "jirr" or text.lower() == "njir":
                               contact = boy.getContact(msg._from)
                               Muid = contact.displayName
                               a = "Astaghfirullah tobatlah kau nak"
                               data = {"type": "text","text": "{}".format(str(a)),"sentBy": {"label": " ☛❲"+Muid+"❳☚","iconUrl": "http://jackyeza.xtgem.com/downloads/bahan.gif"}}
                               sendTemplate(to, data)
                        
                        
               #RESPON WITH NAME#
                        elif text.lower() == "me":
                               contact = boy.getContact(msg._from)
                               xname = contact.displayName
                               a = "me ayam special ea kαk ☛❲" + xname +"❳☚ \nharga Rp 10.000 bonus gelas pecah"
                               data = {"type": "text","text": "{}".format(str(a)),"sentBy": {"label": "ᴍᴇ ᴀʏᴀᴍ ɴʏᴀ ᴀᴅᴀ ᴅɪʙᴀᴡᴀʜ ʏᴀ","iconUrl": "http://jackyeza.xtgem.com/downloads/bahan.gif","uri": "line://ti/p/~jackyeza"}}
                               sendTemplate(to, data)
                               data = {
                        "type": "template",
                        "altText": "bonus gelas pecah",
                        "template": {
                            "type": "image_carousel",
                            "columns": [
                                {
                                     "imageUrl": "https://1.bp.blogspot.com/-v3n3NTQScm8/XaYMCcg_AnI/AAAAAAAAAIk/kgjGo3Ve5TcjwV9gFad8JJguEGOb-2ssACLcBGAsYHQ/s1600/403fe3ce-f18d-4730-8a4b-18252c321724.jpg",
                                     "size": "micro",
                                     "action": {
                                         "type": "uri",
                                          "uri": "line://ti/p/~jackyeza"
                                     }
                                }
                            ]
                        }
                    }
                               sendTemplate(to, data)
                               time.sleep(1)
                        elif 'mantul' in msg.text:
                               contact = boy.getContact(msg._from)
                               xname = contact.displayName
                               boy.sendMessage(to, "mαntul mαntαp kunthulll wkwkw víss vrσh ✌✌ " + xname)
                               #====== token==========#
                               #======template========#
                        
                        elif text.lower() == "pening" or text.lower() == "hadeh":
                            gifnya = ["https://1.bp.blogspot.com/-W5KMfrRpSHU/XZ8edqmIDjI/AAAAAAAAAIA/AFCJvSoM6ogQoZPQ2Hg4ELOYDwg-Va-zwCLcBGAsYHQ/s1600/AW3566516_11.gif"]
                            data = {
                        "type": "template",
                        "altText": "Reset",
                        "template": {
                            "type": "image_carousel",
                            "columns": [
                                {
                                     "imageUrl": "{}".format(random.choice(gifnya)),
                                     "size": "micro",
                                     "action": {
                                         "type": "uri",
                                          "uri": "line://ti/p/~jackyeza"
                                     }
                                }
                            ]
                        }
                    }
                            sendTemplate(to, data)
                            time.sleep(1)
                        elif text.lower() == "hadeh" or text.lower() == "tuman":
                            gifnya = ["https://1.bp.blogspot.com/-ASSmvL_jl8A/XZ1J4k2NKmI/AAAAAAAAAGc/uvfnIZgE7ao3Q-kgELrdhRz-Ejv6cYyJgCLcBGAsYHQ/s1600/AS001630_08.gif"]
                            data = {
                        "type": "template",
                        "altText": "Reset",
                        "template": {
                            "type": "image_carousel",
                            "columns": [
                                {
                                     "imageUrl": "{}".format(random.choice(gifnya)),
                                     "size": "micro",
                                     "action": {
                                         "type": "uri",
                                          "uri": "line://ti/p/~jackyeza"
                                     }
                                }
                            ]
                        }
                    }
                            sendTemplate(to, data)
                            time.sleep(1)
                        elif text.lower() == "cipok":
                            gifnya = ["https://media.giphy.com/media/l2Je2M4Nfrit0L7sQ/giphy.gif"]
                            data = {
                        "type": "template",
                        "altText": "sini tak sedot untumu",
                        "template": {
                            "type": "image_carousel",
                            "columns": [
                                {
                                     "imageUrl": "{}".format(random.choice(gifnya)),
                                     "size": "micro",
                                     "action": {
                                         "type": "uri",
                                          "uri": "line://ti/p/~jackyeza"
                                     }
                                }
                            ]
                        }
                    }
                            sendTemplate(to, data)
                            time.sleep(1)
                        elif text.lower() == "kak metta":
                            gifnya = ["https://1.bp.blogspot.com/-zZKARByqH5o/XabMsob-uwI/AAAAAAAAAJs/8o984zZFo6cA9Tdp9gwMjovJ3Ll9uY4RgCLcBGAsYHQ/s1600/1571206697023.png"]
                            data = {
                        "type": "template",
                        "altText": "Hayo kak meta kacian deh lu",
                        "template": {
                            "type": "image_carousel",
                            "columns": [
                                {
                                     "imageUrl": "{}".format(random.choice(gifnya)),
                                     "size": "micro",
                                     "action": {
                                         "type": "uri",
                                          "uri": "line://ti/p/~jackyeza"
                                     }
                                }
                            ]
                        }
                    }
                            sendTemplate(to, data)
                            time.sleep(1)
                        elif text.lower() == "jomblo":
                            gifnya = ["https://1.bp.blogspot.com/-RzGKoaBTgzg/XacK1W7UH1I/AAAAAAAAAKI/JkGLyg0VrGU74DJIc8VGxxJv17QXPi2JQCLcBGAsYHQ/s1600/Screenshot_2019-10-16-19-08-08-037_com.instagram.android.png"]
                            data = {
                        "type": "template",
                        "altText": "jones ngenes",
                        "template": {
                            "type": "image_carousel",
                            "columns": [
                                {
                                     "imageUrl": "{}".format(random.choice(gifnya)),
                                     "size": "micro",
                                     "action": {
                                         "type": "uri",
                                          "uri": "line://ti/p/~jackyeza"
                                     }
                                }
                            ]
                        }
                    }
                            sendTemplate(to, data)
                            time.sleep(1)
                        
                        elif text.lower() == "wkwk":
                            gifnya = ["https://1.bp.blogspot.com/-JFkZtQzeRU0/XacSViP1YaI/AAAAAAAAAKs/uCdgK1G9iAEY41yTwkKZfx1Cn7KPeXmGQCLcBGAsYHQ/s1600/images.jpeg"]
                            data = {
                        "type": "template",
                        "altText": "jones ngenes",
                        "template": {
                            "type": "image_carousel",
                            "columns": [
                                {
                                     "imageUrl": "{}".format(random.choice(gifnya)),
                                     "size": "micro",
                                     "action": {
                                         "type": "uri",
                                          "uri": "line://ti/p/~jackyeza"
                                     }
                                }
                            ]
                        }
                    }
                            sendTemplate(to, data)
                            time.sleep(1)
                        elif text.lower() == "gombal":
                            gifnya = ["https://1.bp.blogspot.com/-2L0P-Wimjog/XacR_hnwzWI/AAAAAAAAAKg/VWS_ZJbhYYsKa41nQAlA6j9XhlhAIQ_vACLcBGAsYHQ/s1600/1570862901283.jpg"]
                            data = {
                        "type": "template",
                        "altText": "jones ngenes",
                        "template": {
                            "type": "image_carousel",
                            "columns": [
                                {
                                     "imageUrl": "{}".format(random.choice(gifnya)),
                                     "size": "micro",
                                     "action": {
                                         "type": "uri",
                                          "uri": "line://ti/p/~jackyeza"
                                     }
                                }
                            ]
                        }
                    }
                            sendTemplate(to, data)
                            time.sleep(1)
                        elif text.lower() == "goyang":
                            gifnya = ["https://1.bp.blogspot.com/-5xzJVZOuFz8/XacSHpbJ_iI/AAAAAAAAAKk/ynBpCDwXwcITSFuJM5zcdZqDoVh2SUM6QCLcBGAsYHQ/s1600/1570862909424.jpg"]
                            data = {
                        "type": "template",
                        "altText": "jones ngenes",
                        "template": {
                            "type": "image_carousel",
                            "columns": [
                                {
                                     "imageUrl": "{}".format(random.choice(gifnya)),
                                     "size": "micro",
                                     "action": {
                                         "type": "uri",
                                          "uri": "line://ti/p/~jackyeza"
                                     }
                                }
                            ]
                        }
                    }
                            sendTemplate(to, data)
                            time.sleep(1)
                        
                        elif text.lower() == "karin" or text.lower() == "dor":
                            gifnya = ["https://1.bp.blogspot.com/-c_5WSrYmuKE/Xakg2bGksyI/AAAAAAAAALs/hZPzlxN3d6YzetZAh4xdjRKHtVKaq_bHwCLcBGAsYHQ/s1600/1571364252044-picsay.png"]
                            data = {"type": "template","altText": "Artis cuy","template": {"type": "image_carousel","columns": [{"imageUrl": "{}".format(random.choice(gifnya)),"size": "micro","action": {"type": "uri","uri": "line://ti/p/~jackyeza"}}] } }
                            sendTemplate(to, data)
                            time.sleep(1)
                        elif text.lower() == "anime" or text.lower() == "gambar":
                            gifnya = ["https://1.bp.blogspot.com/-S_wmz9EufTY/Xak5C_1oeQI/AAAAAAAAAMg/DhTYO2466gI_eMqkGQ3MVgNUJFwm52pfACLcBGAsYHQ/s1600/reza.gif"]
                            data = {"type": "template","altText": "orang ganteng","template": {"type": "image_carousel","columns": [{"imageUrl": "{}".format(random.choice(gifnya)),"size": "micro","action": {"type": "uri","uri": "line://ti/p/~jackyeza"}}] } }
                            sendTemplate(to, data)
                            time.sleep(1)
                        elif text.lower() == "jepret" or text.lower() == "jos":
                            gifnya = ["https://1.bp.blogspot.com/-WL90L9G8VQY/Xal9fcUIAzI/AAAAAAAAAM0/s1n0W3hzFkcSRvNzVMZ6qcUphF6EBAGuQCLcBGAsYHQ/s1600/AW4007617_10.gif"]
                            data = {"type": "template","altText": "foto grafer karin dudul","template": {"type": "image_carousel","columns": [{"imageUrl": "{}".format(random.choice(gifnya)),"size": "micro","action": {"type": "uri","uri": "line://ti/p/~jackyeza"}}] } }
                            sendTemplate(to, data)
                            time.sleep(1)
                        elif text.lower() == "hoho" or text.lower() == "hihihi":
                            gifnya = ["https://1.bp.blogspot.com/-cxDBUTyRPPU/Xal9feDJJQI/AAAAAAAAAM4/dBVK3e3Q9UUfQMZSGVC6yWvNSysLpMNJwCLcBGAsYHQ/s1600/AW4007617_04.gif"]
                            data = {"type": "template","altText": "Ngukuk hahha","template": {"type": "image_carousel","columns": [{"imageUrl": "{}".format(random.choice(gifnya)),"size": "micro","action": {"type": "uri","uri": "line://ti/p/~jackyeza"}}] } }
                            sendTemplate(to, data)
                            time.sleep(1)
                        
                        elif text.lower() == "salsa" or text.lower() == "imuetz":
                            gifnya = ["https://1.bp.blogspot.com/-z9hAVYQsdFw/XaqFlO0S8RI/AAAAAAAAANs/2I2F3qj6a28ALftzUuKFEmUyRguBhVDSACLcBGAsYHQ/s1600/salsa.gif"]
                            data = {"type": "template","altText": "senyuman salsa","template": {"type": "image_carousel","columns": [{"imageUrl": "{}".format(random.choice(gifnya)),"size": "micro","action": {"type": "uri","uri": "line://ti/p/~jackyeza"}}] } }
                            sendTemplate(to, data)
                            time.sleep(1)
                        
                        elif text.lower() == "blackpink" or text.lower() == "rose":
                            gifnya = ["https://1.bp.blogspot.com/-efa3jw6nxLk/XaviL-C6lvI/AAAAAAAAAPU/9bDyWln3TNAJGMvMCcvWqPLFbjePTksKQCLcBGAsYHQ/s1600/tumblr_pcv2mnsTmK1w8sgt6o3_250.png"]
                            data = {"type": "template","altText": "rose blackpink","template": {"type": "image_carousel","columns": [{"imageUrl": "{}".format(random.choice(gifnya)),"size": "micro","action": {"type": "uri","uri": "line://ti/p/~jackyeza"}}] } }
                            sendTemplate(to, data)
                            time.sleep(1)
                        elif text.lower() == "reza" or text.lower() == "setia":
                            gifnya = ["https://1.bp.blogspot.com/-AqWFjJ4xwCk/Xa1xtR5BH9I/AAAAAAAAAPs/Td_5mtdxYgkCGt5RhY3ELplbpOINpmsQACLcBGAsYHQ/s1600/1571647358335-picsay.png"]
                            data = {"type": "template","altText": "pesan bijak bang reza ganteng","template": {"type": "image_carousel","columns": [{"imageUrl": "{}".format(random.choice(gifnya)),"size": "micro","action": {"type": "uri","uri": "line://ti/p/~jackyeza"}}] } }
                            sendTemplate(to, data)
                            time.sleep(1)
                        elif text.lower() == "cie" or text.lower() == "modus":
                            gifnya = ["https://1.bp.blogspot.com/-5C_Zk8AMbqo/Xa2BwMj32qI/AAAAAAAAAQE/AsDkc8qM6PUVsLMV5B1ZTaPNUcri1pxugCLcBGAsYHQ/s1600/unnamed.gif"]
                            data = {"type": "template","altText": "pesan bijak bang reza ganteng","template": {"type": "image_carousel","columns": [{"imageUrl": "{}".format(random.choice(gifnya)),"size": "micro","action": {"type": "uri","uri": "line://ti/p/~jackyeza"}}] } }
                            sendTemplate(to, data)
                            time.sleep(1)
                        
                        elif text.lower() == "bawel" or text.lower() == "tatto":
                            gifnya = ["https://1.bp.blogspot.com/-47UJJ7HjyEc/Xa7_YLZgS4I/AAAAAAAAAQ4/D_qjdfWTKNMZ6UcrW_dfH1nRxLp9-gdqQCLcBGAsYHQ/s1600/1571749583567.png"]
                            data = {"type": "template","altText": "artis bfc lagi eksis","template": {"type": "image_carousel","columns": [{"imageUrl": "{}".format(random.choice(gifnya)),"size": "micro","action": {"type": "uri","uri": "line://ti/p/~jackyeza"}}] } }
                            sendTemplate(to, data)
                            time.sleep(1)
                        elif text.lower() == "gejora":
                            gifnya = ["https://1.bp.blogspot.com/-mWU3mG4z27g/Xa_h-gTbNJI/AAAAAAAAARY/hRM3xkKliyECthB0nSlX70ppHebB1A2SwCLcBGAsYHQ/s1600/1571806619644-picsay.png"]
                            data = {"type": "template","altText": "si tomboy beraksi","template": {"type": "image_carousel","columns": [{"imageUrl": "{}".format(random.choice(gifnya)),"size": "micro","action": {"type": "uri","uri": "line://ti/p/~jackyeza"}}] } }
                            sendTemplate(to, data)
                            time.sleep(1)
                        elif text.lower() == "embe" or text.lower() == "ntah apa yg merasukimu":
                            gifnya = ["https://1.bp.blogspot.com/-4sE0a7nzEOQ/Xbae1geKigI/AAAAAAAAASk/2KXn_3tSMaYljpL93Jdl6Kn4fRNzUBFWACLcBGAsYHQ/s1600/1572249199192.jpg"]
                            data = {"type": "template","altText": "azab anu hahaha","template": {"type": "image_carousel","columns": [{"imageUrl": "{}".format(random.choice(gifnya)),"size": "micro","action": {"type": "uri","uri": "line://ti/p/~jackyeza"}}] } }
                            sendTemplate(to, data)
                            time.sleep(1)
                        
                        elif text.lower() == "kibar" or text.lower() == "cawet":
                            gifnya = ["https://1.bp.blogspot.com/-MJO5YXXtfo4/XcEScHjd-jI/AAAAAAAAATk/cTWk-8oUDPkckSuf4VxPiqtjhuYtEskWgCLcBGAsYHQ/s1600/1572933887472.jpg"]
                            data = {"type": "template","altText": "hadiah untukmu bosskuh","template": {"type": "image_carousel","columns": [{"imageUrl": "{}".format(random.choice(gifnya)),"size": "micro","action": {"type": "uri","uri": "line://ti/p/~jackyeza"}}] } }
                            sendTemplate(to, data)
                            time.sleep(1)
                        elif text.lower() == "hahaha" or text.lower() == "njirr":
                            gifnya = ["https://1.bp.blogspot.com/--pY-vcM4P8E/XcEvuXZlJsI/AAAAAAAAAT8/5t-CE71mSbkZPJaYw8q6pNByA66zFRsuACLcBGAsYHQ/s1600/1572673045886.jpg"]
                            data = {"type": "template","altText": "wanita tercantik yg pernah terlahir","template": {"type": "image_carousel","columns": [{"imageUrl": "{}".format(random.choice(gifnya)),"size": "micro","action": {"type": "uri","uri": "line://ti/p/~jackyeza"}}] } }
                            sendTemplate(to, data)
                            time.sleep(1)
                        elif 'yank' in msg.text:
                            gifnya = ["https://1.bp.blogspot.com/-0R6D5VMYi9U/XcEza4UIOyI/AAAAAAAAAUs/UH5HJuFV8cYuf0Ec9q7hxT58B65THU1XQCLcBGAsYHQ/s1600/1572673045886-picsay.jpg"]
                            data = {"type": "template","altText": "yank ndasmu peang","template": {"type": "image_carousel","columns": [{"imageUrl": "{}".format(random.choice(gifnya)),"size": "micro","action": {"type": "uri","uri": "line://ti/p/~jackyeza"}}] } }
                            sendTemplate(to, data)
                            time.sleep(1)
                        elif 'beb' in msg.text:
                            gifnya = ["https://1.bp.blogspot.com/-k0-wVSfSMdY/XcEzWmZW0DI/AAAAAAAAAUo/sux2slIbNRIWkItNZ6BqnB88LRbQFlwwwCLcBGAsYHQ/s1600/1572673045886-picsay.jpg"]
                            data = {"type": "template","altText": "bebek kale wkwk","template": {"type": "image_carousel","columns": [{"imageUrl": "{}".format(random.choice(gifnya)),"size": "micro","action": {"type": "uri","uri": "line://ti/p/~jackyeza"}}] } }
                            sendTemplate(to, data)
                            time.sleep(1)
                        elif text.lower() == "piala" or text.lower() == "juara 1":
                            gifnya = ["https://1.bp.blogspot.com/-Tf0UJXyiv_Q/XcKFTZ33LBI/AAAAAAAAAV0/Kc4DHv_ZK4ItUwIqiKfqFV5X7TgCL903gCLcBGAsYHQ/s1600/1562758460687.jpg"]
                            data = {"type": "template","altText": "salah satu penghargaan yg ajaib","template": {"type": "image_carousel","columns": [{"imageUrl": "{}".format(random.choice(gifnya)),"size": "micro","action": {"type": "uri","uri": "line://ti/p/~jackyeza"}}] } }
                            sendTemplate(to, data)
                            time.sleep(1)
                        elif text.lower() == "wiwin" or text.lower() == "tukang selingkuhan":
                            gifnya = ["https://1.bp.blogspot.com/-wQGhWaMmfvQ/Xc0qpy9ROXI/AAAAAAAAAWM/ao1FJEhvX8Mx-Qps_-2LFf62_nEDIIzswCLcBGAsYHQ/s1600/1573726808980.png"]
                            data = {"type": "template","altText": "salah satu orang yg suka selingkuh wkwk","template": {"type": "image_carousel","columns": [{"imageUrl": "{}".format(random.choice(gifnya)),"size": "micro","action": {"type": "uri","uri": "line://ti/p/~jackyeza"}}] } }
                            sendTemplate(to, data)
                            time.sleep(1)
               #-----------------&&------------------#
                        elif cmd == "re on" or text.lower() == 'on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                boy.sendMessage(msg.to,"ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴅɪᴀᴋᴛɪғᴋᴀɴ √")

                        elif cmd == "re off" or text.lower() == 'off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                boy.sendMessage(msg.to,"ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ ")

                        elif cmd == "la":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = "╠⏩"
                                mb = "╠⏩"
                                mc = "╠⏩"
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +boy.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +boy.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +boy.getContact(m_id).displayName + "\n"
                                boy.sendMessage(msg.to,"╭━⏩ᴀᴅᴍɪɴ ᴀʀᴇᴢᴀ ʙᴏᴛ⏩\n╠\n╠⏩ᴄʀᴇᴀᴛᴏʀ ʙᴏᴛ:\n"+ma+"╠\n╠⏩ᴀᴅᴍɪɴ:\n"+mb+"╠\n╠⏩sᴛᴀғғ:\n"+mc+"╠\n╠⏩ᴛᴏᴛᴀʟ「%s」\n╰━━━━━━━⏩ʀᴇᴢᴀ ʙᴏᴛ⏩" %(str(len(owner)+len(admin)+len(staff))))
#bot respon# 

#===========JOIN TICKET============#
                        elif msg.text.lower().startswith("cvpurl"):
                                link = removeCmd("cvpurl", text)
                                contact = boy.getContact(sender)
                                boy.sendMessage(to, "Type: Profile\n • Detail: Change video url\n • Status: Download...")
                                print("Sedang Mendownload Data ~")
                                pic = "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                                subprocess.getoutput('youtube-dl --format mp4 --output TeamAnuBot.mp4 {}'.format(link))
                                pict = boy.downloadFileURL(pic)
                                vids = "TeamAnuBot.mp4"
                                changeVideoAndPictureProfile(pict, vids)
                                eza = "• Status: Succes"
                                data = {"type": "text","text": "{}".format(eza),"sentBy": {"label": "Rezabot", "iconUrl": "https://obs.line-scdn.net/{}".format(boy.getContact(boyMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u6e4534dd63e82642f29205d2c993c642"}}
                                sendTemplate(to,data)
                                os.remove("TeamAnuBot.mp4")
                    
                        
                        elif cmd == "kondisi":
                            if msg._from in admin or msg._from in owner:
                               try:boy.inviteIntoGroup(to, [mid]);has = "OK"
                               except:has = "NOT"
                               try:boy.kickoutFromGroup(to, [mid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒. Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               boy.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil)) 
  
                                
    except Exception as error:
        print (error)

while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
               # bot(op)
                # Don't remove this line, if you wan't get error soon!
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                #thread1.daemon = True
                thread1.start()
                thread1.join()
    except Exception as e:
        pass
