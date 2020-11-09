# BOT LOGIN
# KHIE WAS HERE
# </> NOOB CODER 2K17
from linepy import *
from akad.ttypes import Message
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from akad.ttypes import ContentType as Type
from akad.ttypes import TalkException
from KhieBots.thrift.protocol import TCompactProtocol
from KhieBots.thrift.transport import THttpClient
from KhieBots.ttypes import LoginRequest
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
from gtts import gTTS
from threading import Thread
from io import StringIO
from multiprocessing import Pool
from googletrans import Translator
from urllib.parse import urlencode
from wikiapi import WikiApi
from tmp.MySplit import *
from random import randint
from shutil import copyfile
from youtube_dl import YoutubeDL
from threading import Thread, activeCount
import LineService
import subprocess, youtube_dl, humanize, traceback
import subprocess as cmd
import time, random, sys, json, null, codecs, html5lib ,shutil ,threading, glob, re, base64, string, os, requests, six, ast, pytz, wikipedia, urllib, urllib.parse, atexit, asyncio, traceback
_session = requests.session()
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
#=====================================================================
#=====================================================================
noobcoder = LINE("primary",appName="IOS\t10.1.1\tIOS\t13.3.1")
Channel(noobcoder, "1602687308").getChannelResult().channelAccessToken
#=======================================================
waitOpen = codecs.open("noobcoder/wait.json","r","utf-8")
settingsOpen = codecs.open("noobcoder/temp.json","r","utf-8")
premiumOpen = codecs.open("noobcoder/user.json","r","utf-8")
#=====================================================================
#=====================================================================
noobcoderProfile = noobcoder.getProfile()
noobcoderSettings = noobcoder.getSettings()
noobcoderPoll = OEPoll(noobcoder)
noobcoderMID = noobcoder.getProfile().mid
#=====================================================================
loop = asyncio.get_event_loop()
admin =["mid owner"]
myAdmin = ["mid owner"]
botStart = time.time()
msg_dict = {}
wait = json.load(waitOpen)
settings = json.load(settingsOpen)
premium = json.load(premiumOpen)

peler = { 
    "receivercount": 0,
    "sendcount": 0
}

chatbot = {
    "admin": [],
    "botMute": [],
    "botOff": [],
}

read = { 
    "readMember": {},
    "readPoint": {}
}
#=====================================================================
#=====================================================================
settings["myProfile"]["displayName"] = noobcoderProfile.displayName
settings["myProfile"]["statusMessage"] = noobcoderProfile.statusMessage
settings["myProfile"]["pictureStatus"] = noobcoderProfile.pictureStatus
cont = noobcoder.getContact(noobcoderMID)
settings["myProfile"]["videoProfile"] = cont.videoProfile
coverId = noobcoder.getProfileDetail()["result"]["objectId"]
settings["myProfile"]["coverId"] = coverId
#=====================================================================
#=====================================================================
with open("noobcoder/temp.json", "r", encoding="utf_8_sig") as f:
    anu = json.loads(f.read())
    anu.update(settings)
    settings = anu
with open("noobcoder/wait.json", "r", encoding="utf_8_sig") as f:
    itu = json.loads(f.read())
    itu.update(wait)
    wait = itu

def sendFooter(to, isi):
    data = {
        "type": "text",
        "text": isi,
        "sentBy": {
            "label": "Lulz Crew",
            "iconUrl": "https://obs.line-scdn.net/{}".format(noobcoder.getContact(noobcoderMID).pictureStatus),
            "linkUrl": "line://nv/profilePopup/mid=u2cf74acf6ed04d122def4db8ffdd2e39"
        }
    }
    sendTemplate(to, data)
    
def sendTemplate(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = noobcoder.liff.issueLiffView(view)
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
    token = client.liff.issueLiffView(view)
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
    token = noobcoder.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

def debug():
    get_profile_time_start = time.time()
    get_profile = noobcoder.getProfile()
    get_profile_time = time.time() - get_profile_time_start
    get_group_time_start = time.time()
    get_group = noobcoder.getGroupIdsJoined()
    get_group_time = time.time() - get_group_time_start
    get_contact_time_start = time.time()
    get_contact = noobcoder.getContact(get_profile.mid)
    get_contact_time = time.time() - get_contact_time_start
    elapsed_time = time.time() - get_profile_time_start
    return " 「 Debug 」\n - Send Message\n   %.5f\n - Get Profile\n   %.5f\n - Get Contact\n   %.5f\n - Get Group\n   %.5f" % (elapsed_time,get_profile_time,get_contact_time,get_group_time)
#=====================================================================
def powpow():
    Headers = {
    'User-Agent': "Line/8.9.1",
    'X-Line-Application': "IOSIPAD\t11.2.5\tiPhone X\t11.2.5",
    "x-lal": "ja-US_US",
    }
    return Headers
#=====================================================================
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
#=====================================================================
#def Template(to):
def sendMessageCustom(to, text, icon , name):
    annda = {'MSG_SENDER_ICON': icon,
        'MSG_SENDER_NAME':  name,
    }
    noobcoder.sendMessage(to, text, contentMetadata=annda)
def sendMessageCustomContact(to, icon, name, mid):
    annda = { 'mid': mid,
    'MSG_SENDER_ICON': icon,
    'MSG_SENDER_NAME':  name,
    }
    noobcoder.sendMessage(to, '', annda, 13)

def B64e(to, url):
	import base64
	return noobcoder.sendMessage(to, base64.b64encode(url.encode()).decode())

def B64d(to, url):
	import base64
	return noobcoder.sendMessage(to, base64.b64decode(url.encode()).decode())
	
def sendMention(to, mid, firstmessage='', lastmessage=''):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        try:
            noobcoder.sendMessage(to, text, {'MSG_SENDER_NAME': noobcoder.getContact(mid).displayName,'MSG_SENDER_ICON': "http://dl.profile.line-cdn.net/" + noobcoder.getContact(mid).pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        except Exception as e:
            noobcoder.sendMessage(to, text, {'MSG_SENDER_NAME': noobcoder.getContact("u085311ecd9e3e3d74ae4c9f5437cbcb5").displayName,'MSG_SENDER_ICON': 'http://dl.profile.line-cdn.net/' + noobcoder.getContact("u085311ecd9e3e3d74ae4c9f5437cbcb5").pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        print(error)
def mentions(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@KhieGans  "
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
    noobcoder.sendMessage(to, textx, {'AGENT_NAME':'LINE OFFICIAL', 'AGENT_LINK': 'line://ti/p/~{}'.format(noobcoder.getProfile().userid), 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + noobcoder.getContact("u085311ecd9e3e3d74ae4c9f5437cbcb5").picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = noobcoder.genOBSParams({'oid': noobcoderMID, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = noobcoder.server.postContent('{}/talk/vp/upload.nhn'.format(str(noobcoder.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        noobcoder.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))
        os.remove("noobcoderWasHere.mp4")
#=====================================================================
def speedtest(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weaks, days = divmod(days,7)
    if days == 0:
        return '%02d' % (secs)
    elif days > 0 and weaks == 0:
        return '%02d' %(secs)
    elif days > 0 and weaks > 0:
        return '%02d' %(secs)
        
def change(url):
	import base64
	return base64.b64encode(url.encode()).decode()
	
def tagdia(to, text="",ps='', mids=[]):
        arrData = ""
        arr = []
        mention = "@MentionOrang "
        if mids == []:
            raise Exception("Invalid mids")
        if "@!" in text:
            if text.count("@!") != len(mids):
                raise Exception("Invalid mids")
            texts = text.split("@!")
            textx = ''
            h = ''
            for mid in range(len(mids)):
                h+= str(texts[mid].encode('unicode-escape'))
                textx += str(texts[mid])
                if h != textx:slen = len(textx)+h.count('U0');elen = len(textx)+h.count('U0') + 13
                else:slen = len(textx);elen = len(textx) + 13
                arrData = {'S':str(slen), 'E':str(elen), 'M':mids[mid]}
                arr.append(arrData)
                textx += mention
            textx += str(texts[len(mids)])
        else:
            textx = ''
            slen = len(textx)
            elen = len(textx) + 18
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
            arr.append(arrData)
            textx += mention + str(text)
        noobcoder.sendMessage(to, textx, {'MSG_SENDER_NAME': client.getContact(ps).displayName,'MSG_SENDER_ICON': "http://dl.profile.line-cdn.net/" + noobcoder.getContact(ps).pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
#=====================================================================
def logError(text):
    noobcoder.log("ERROR 404 !\n" + str(text))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + " | " + inihari.strftime('%H:%M:%S')
    with open("noobcoder/errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
#=====================================================================
#=====================================================================
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
#=====================================================================
#=====================================================================
def removeCmd(cmd, text):
	key = settings["keyCommand"]
	if settings["setKey"] == False: key = ''
	rmv = len(key + cmd) + 1
	return text[rmv:]
def backupData():
    try:
        backup = settings
        f = codecs.open('noobcoder/temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = wait
        f = codecs.open('noobcoder/wait.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = premium
        f = codecs.open('noobcoder/user.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
#=====================================================================
def bcTemplate(gr, data):
    xyz = LiffChatContext(gr)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = noobcoder.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
#=====================================================================
async def noobcoderBot(op):
    try:
        if settings["restartPoint"] != None:
            noobcoder.sendMessage(settings["restartPoint"], 'Activated♪')
            settings["restartPoint"] = None
        if op.type == 0:
            return
                        
        if op.type in [22,24]:
            client.leaveRoom(op.param1)
#=====================================================================
        if op.type == 13:
            if noobcoder.getProfile().mid in op.param3:
                G = noobcoder.getCompactGroup(op.param1)
                if settings["autoJoin"] == True:
                    noobcoder.acceptGroupInvitation(op.param1)
        if op.type in [25, 26]:
            if op.type == 25: print ("[ 25 ] SEND MESSAGE")
            else: print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message               
            text = msg.text
            msg_id = msg.id
            receiver = msg.to             
            sender = msg._from
            s = noobcoder.getProfile().mid
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False:
               setKey = ''
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:                    	
                    if sender != noobcoder.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if msg.contentType == 0:
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if sender != s:
                	        peler["receivercount"] += 1
                        if sender == s:
                	        peler["sendcount"] += 1

#=====================================================================
#==========================================
#==========================================
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != noobcoderMID: to = sender
                else: to = receiver
                if msg.contentType == 6:
                    try:
                        contact = noobcoder.getContact(sender)
                        if msg.toType == 2:
                            anu = noobcoder.getGroup(to)
                            if msg.contentMetadata['GC_EVT_TYPE'] == 'S' and msg.contentMetadata['GC_MEDIA_TYPE'] == 'LIVE':
                                anu = msg.contentMetadata={'GC_EVT_TYPE': 'S', 'GC_CHAT_MID': to, 'RESULT': 'INFO', 'SKIP_BADGE_COUNT': 'false', 'GC_IGNORE_ON_FAILBACK': 'false', 'TYPE': 'G', 'DURATION': '0', 'GC_MEDIA_TYPE': 'VIDEO', 'VERSION': 'X', 'CAUSE': '16'}
                    except Exception as e:
                        noobcoder.sendMessage(to, str(e))                                                  
                if msg.contentType in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]:
                    if msg.toType == 0:
                        if settings["autoRead"] == True:
                            noobcoder.sendChatChecked(to, msg_id)
                    if msg.toType == 2:
                        if settings["autoRead1"] == True:
                            noobcoder.sendChatChecked(to, msg_id)
                if msg.contentType == 0:
                    if "/ti/g/" in text.lower():
                        if settings["autoJoin"] == True:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                   n_links.append(l)
                            for ticket_id in n_links:
                                group = noobcoder.findGroupByTicket(ticket_id)
                                if len(group.members) >= wait["Members"]:
                                    noobcoder.acceptGroupInvitationByTicket(group.id,ticket_id)
                                else:
                                    noobcoder.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    noobcoder.leaveGroup(group.id)
#==========================================
                    if cmd == "threads":
                        noobcoder.sendMessage(to,'Threads: {}'.format(threading.active_count()))
                        log.info("Debug Threads.")                            
#==========================================
                    elif cmd.startswith("#down "):
                        if msg._from in "u2cf74acf6ed04d122def4db8ffdd2e39":
                           number = removeCmd("#down", text)
                           if len(number) > 0:
                               if number.isdigit():
                                   number = int(number)
                                   if number > 5000:                                             
                                       noobcoder.sendMessage(to,"invalid >_< ! Max: 5000.")
                                   else:
                                       for i in range(0,number):
                                           noobcoder.sendMessage(to,str(number))
                                           number -= 1
                                           time.sleep(0.008)
                               else:
                                  noobcoder.sendMessage(to,"Please specify a valid number.")
                    elif cmd == "cpp" :
                        if msg._from in myAdmin:
                            settings["changePicture"] = True
                            sendFooter(to, "Send a Image to change picture.")
#==========================================
                    if cmd == "kiss me":
                        noobcoder.generateReplyMessage(msg.id)
                        noobcoder.sendReplyMessage(msg.id, to,"。。・゜゜・❤ "+noobcoder.getContact(sender).displayName+" ❤ \n(づ￣ ³￣)づ")
                    elif cmd == "help":
                    	noobcoder.sendMessage(to, "Command Client :\n\n1. login ➡ (SELF BOTS)\n2. login js ➡ (JAVA SCRIPT)\n3. logout ➡ (MATIKAN BOTS)\n4. logout js ➡ (MATIKAN JS)\n5. token ➡ (TOKEN)\n\nOwner Command :\n\n1. Addsb <@tag>\n2. addjs <@tag>\n3. delsb <num>\n4. deljs <num>\n5. list user\n6. screen vps \n8. deldir <nama> (hapus screen)")
#==========================================
                    elif text.lower() == "login js" and msg._from not in premium['listLogin'] and to not in chatbot["botMute"]:
                        if msg._from in premium["myService"]:
                            user = premium["myService"][msg._from]
                            try:
                                 def frzky():
                                     a = powpow()
                                     a.update({'x-lpqs' : '/api/v4/TalkService.do'})
                                     transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4/TalkService.do')
                                     transport.setCustomHeaders(a)
                                     protocol = TCompactProtocol.TCompactProtocol(transport)
                                     client = LineService.Client(protocol)
                                     qr = client.getAuthQrcode(keepLoggedIn=1, systemName='noobcoderBot-PC')
                                     link = "line://au/q/" + qr.verifier
                                     noobcoder.sendMention(msg.to, '「 Request Login 」\nClick link @!, only 2 minutes\n{}'.format(link),"",[msg._from])
                                     a.update({"x-lpqs" : '/api/v4/TalkService.do', 'X-Line-Access': qr.verifier})
                                     json.loads(requests.session().get('https://gd2.line.naver.jp/Q', headers=a).text)
                                     a.update({'x-lpqs' : '/api/v4p/rs'})
                                     transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4p/rs')
                                     transport.setCustomHeaders(a)
                                     protocol = TCompactProtocol.TCompactProtocol(transport)
                                     client = LineService.Client(protocol)
                                     req = LoginRequest()
                                     req.type = 1
                                     req.verifier = qr.verifier
                                     req.e2eeVersion = 1
                                     res = client.loginZ(req)
                                     if msg._from not in premium['listLogin']:
                                         premium['listLogin'][msg._from] =  '%s' % user
                                         isi = "{}".format(res.authToken)
                                         os.system('cp -r khiejs {}'.format(user))
                                         os.system('cd {} && echo -n "{}" > token1.txt'.format(user, isi))
                                         os.system('screen -dmS {}'.format(user))
                                         os.system('screen -r {} -X stuff "cd {} && python3 staff2.py \n"'.format(user, user))
                                         noobcoder.sendMention(msg.to, '「 Succes 」\n> @!\n> User name : {}'.format(user),' ', [msg._from])
                                     else:
                                         noobcoder.sendMention(msg.to, '「 Req Login 」\n• Status : Failed\n• User: @!',' ', [msg._from])
                                 thread = threading.Thread(target=frzky)
                                 thread.daemon = True
                                 thread.start()
                            except:
                                 noobcoder.sendMention(msg.to, '「 Reg Login 」\n• Status : Failed\n •User: @!',' ', [msg._from])
# FAKE LOGIN
#==========================================
                    elif text.lower() == "login js" and msg._from in premium['listLogin'] and to not in chatbot["botMute"]:
                        if msg._from in premium["myService"]:
                            noobcoder.sendMention(msg.to, '「 Reg Login 」\n• Status : Failed\n• User :  @!\nType  < Logout js >',' ', [msg._from])
                    elif text.lower() == "logout js" and msg._from in premium['listLogin'] and to not in chatbot["botMute"]:
                        if msg._from in premium["myService"]:
                            del premium['listLogin'][msg._from]
                            user = premium["myService"][msg._from]
                            os.system("screen -S {} -X quit".format(str(user)))
                            os.system('rm -rf {}'.format(str(user)))
                            time.sleep(2)
                            noobcoder.sendMention(msg.to, '「  Logout 」\n• Status : Succes\n• User: @!',' ', [msg._from])
                    elif text.lower() == "logout js" and msg._from not in premium['listLogin'] and to not in chatbot["botMute"]:
                        if msg._from in premium["myService"]:
                            noobcoder.sendMention(msg.to, '「  Logout 」\n• Status : Failed\n• User : @!\nType  < Login js >',' ', [msg._from])
                    elif text.lower().startswith("addme ") and msg._from in myAdmin and to not in chatbot["botMute"]:
                        if msg._from not in premium['myService']:
                            nama = str(text.split(' ')[1])
                            premium['myService'][msg._from] =  '%s' % nama
                            noobcoder.sendMention(msg.to, "「 Add Me 」 \nAdd @! to Login..","",[msg._from])
                        else:
                            noobcoder.sendMention(msg.to, "「Add Me 」\nOwner @! already in List..","",[msg._from])
                    elif text.lower().startswith("addsb ") and msg._from in myAdmin and to not in chatbot["botMute"]:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                key = eval(msg.contentMetadata["MENTION"])
                                key1 = key["MENTIONEES"][0]["M"]
                                if key1 not in premium['myService']:
                                    nama = str(text.split(' ')[1])
                                    premium['myService'][key1] =  '%s' % nama
                                    noobcoder.sendMention(msg.to, '「 Add Service  」\nAdded @! SUCCES silahkan login👌','', [key1])
                                else:
                                    noobcoder.sendMention(msg.to, '「 Add Service  」\nUser @! SUCCES silahkan login👌','', [key1])

                    elif text.lower().startswith("addjs ") and msg._from in myAdmin and to not in chatbot["botMute"]:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                key = eval(msg.contentMetadata["MENTION"])
                                key1 = key["MENTIONEES"][0]["M"]
                                if key1 not in java['Service']:
                                    nama = str(text.split(' ')[1])
                                    java['Service'][key1] =  '%s' % nama
                                    noobcoder.sendMention(msg.to, '「 Add Service  」\nAdded @! SUCCES silahkan login JS👌','', [key1])
                                else:
                                    noobcoder.sendMention(msg.to, '「 Add Service  」\nUser @! SUCCES silahkan login JS👌','', [key1])

                    elif text.lower().startswith("delsb ") and msg._from in myAdmin and to not in chatbot["botOff"]:
                        h = [a for a in premium['myService']]
                        mid = h[int(text.lower().split(' ')[1])-1]
                        user = premium["myService"][mid]
                        if mid in premium['myService'] and mid not in premium['listLogin']:
                            del premium['myService'][mid]
                            noobcoder.sendMention(to, ' Service Delete @! in service ','', [mid])
                        if mid in premium['listLogin']:
                            del premium['listLogin'][mid]
                            del premium['myService'][mid]
                            os.system("screen -S {} -X kill".format(user))
                            os.system('rm -r {}'.format(user))
                        noobcoder.sendMention(to, "User @! has been deleted.","",[mid])                        
                    elif text.lower().startswith('deljs '):
                        h = [a for a in java['Service']]
                        mid = h[int(text.lower().split(' ')[1])-1]
                        user = java["Service"][mid]
                        if mid in java['Service'] and mid not in java['Login']:
                            del java['Service'][mid]
                            noobcoder.sendMention(to, ' Service Delete @!in service ','', [mid])
                    elif text.lower() == "list user" and msg._from in myAdmin and to not in chatbot["botMute"]:
                        h = [a for a in premium['myService']]
                        k = len(h)//20
                        for aa in range(k+1):
                            msgas = '「 List Service 」\n'
                            no=0
                            for a in h:
                                no+=1
                                if premium['myService'][a] == "":cd = "None."
                                else:cd = premium['myService'][a]
                                if no == len(h):msgas+='\n{}. @!\nFile : {}'.format(no,cd)
                                else:msgas+='\n{}. @!\nFile : {}'.format(no,cd)
                            noobcoder.sendMention(msg.to, msgas,'', h)
                    elif text.lower() == "help login" and to not in chatbot["botMute"]:
                        if msg._from in premium["myService"]:
                            noobcoder.sendMention(msg.to, 'Hai @!\n\n1. Type : Login js\n2. Check Personal Chat\n3. Press the Link Qr\n4. Type "Help" To see your command',' ', [msg._from])
                    elif text.lower() == "logout" and msg._from in premium['listLogin'] and to not in chatbot["botMute"]:
                        if msg._from in premium["myService"]:
                            del premium['listLogin'][msg._from]
                            user = premium["myService"][msg._from]
                            os.system("screen -S {} -X quit".format(str(user)))
                            os.system('rm -rf {}'.format(str(user)))
                            time.sleep(2)
                            noobcoder.sendMention(msg.to, '「  Logout 」\n> @! LogOut From Selfbot',' ', [msg._from])
                    elif text.lower() == "logout js" and msg._from not in premium['listLogin'] and to not in chatbot["botMute"]:
                        if msg._from in premium["myService"]:
                            noobcoder.sendMention(msg.to, '「  Logout 」\nHai @!Sorry Please You Login First By Type < Login js >',' ', [msg._from])
                    elif text.lower() == "restart" and to not in chatbot["botMute"]:
                        if msg._from in premium["myService"]:
                            user = premium["myService"][msg._from]
                            os.system("screen -S {} -X quit".format(str(user)))
                            os.system('screen -dmS {}'.format(user))
                            os.system('screen -r {} -X stuff "cd {} && python3 staff.py \n"'.format(user, user))
                            time.sleep(3)
                            noobcoder.sendMention(msg.to, '「  Restart Sb  」\n> @! Succes Restart selfbot',' ', [msg._from])
                    elif text.lower().startswith("deldir"):
                        if msg._from in myAdmin:
                            sep = text.split(" ")
                            anu = text.replace(sep[0] + " ","")
                            os.system("screen -S {} -X quit".format(str(anu)))
                            os.system('rm -rf {}'.format(str(anu)))
                            time.sleep(2)
                            noobcoder.sendMention(to, '「 Delete 」\n• Status : Succes\n • User @!\n• Deleted file : {}'.format(str(anu)),' ', [msg._from])
#==========================================
                    elif cmd.startswith("$"):
                        if msg._from in myAdmin:
                            kntl = removeCmd("$", text)
                            ikkeh = os.popen("{}".format(str(kntl)))
                            enaena = ikkeh.read()
                            noobcoder.sendMessage(to, "{}".format(str(enaena)))
                            ikkeh.close()
                    elif cmd == "screen vps":
                        if msg._from in myAdmin:
                            proses = os.popen("screen -list")
                            a = proses.read()
                            noobcoder.sendMessage(to, "{}".format(str(a)))
                            proses.close()
#==========================================
                    elif cmd.startswith("#name "):
                        if msg._from in "ua3e46be368346a83c7c961bc6c23937e":
                            string = removeCmd("#name", text)
                            if len(string) <= 10000000000:
                                pname = noobcoder.getContact(sender).displayName
                                profile = noobcoder.getProfile()
                                profile.displayName = string
                                noobcoder.updateProfile(profile)
                                noobcoder.sendMessage(to, "「 Update Name 」\nStatus : Success\nFrom : "+str(pname)+"\nTo :"+str(string))
                    elif cmd.startswith("#status "):
                        if msg._from in "ua3e46be368346a83c7c961bc6c23937e":
                            string = removeCmd("#status", text)
                            if len(string) <= 10000000000:
                                pname = noobcoder.getContact(sender).statusMessage
                                profile = noobcoder.getProfile()
                                profile.statusMessage = string
                                noobcoder.updateProfile(profile)
                                noobcoder.sendMessage(to, "「 Update Status 」\nStatus : Success\nFrom : "+str(pname)+"\nTo :"+str(string))
#==========================================
#==========================================
                    elif cmd == "ping":
                        if msg._from in "ua3e46be368346a83c7c961bc6c23937e":
                            noobcoder.sendMention(to, "PONG ! @!","",[msg._from])
                    elif cmd == "hi":
                        foro(to, "Hi to")
#==========================================
#==========================================
                    elif cmd == "#join on":
                        if msg._from in "ua3e46be368346a83c7c961bc6c23937e":
                            if settings["autoJoin"] == True:
                                msgs=" 「 Join 」\nJoin already Enable♪"
                            else:
                                msgs=" 「 Join 」\nJoin set to Enable♪"
                                settings["autoJoin"] = True
                            sendFooter(to, msgs)
                    elif cmd == "#join off":
                        if msg._from in "ua3e46be368346a83c7c961bc6c23937e":
                            if settings["autoJoin"] == False:
                                msgs=" 「 Join 」\nJoin already DISABLED♪"
                            else:
                                msgs=" 「 Join 」\nJoin set to DISABLED♪"
                                settings["autoJoin"] = False
                            sendFooter(to, msgs)
#==========================================
#==========================================
                    elif cmd == "mentions":
                        group = noobcoder.getGroup(to);nama = [contact.mid for contact in group.members];nama.remove(noobcoder.getProfile().mid)
                        noobcoder.datamention(to,'Mentions',nama)
#==========================================
#==========================================
                    elif cmd == "about":
                        try:
                            arr = []
                            today = datetime.today()
                            thn = 2018 
                            bln = 8    #isi bulannya yg sewa
                            hr = 9   #isi tanggalnya yg sewa
                            future = datetime(thn, bln, hr)
                            days = (str(future - today))
                            comma = days.find(",")
                            days = days[:comma]
                            h = noobcoder.getContact(noobcoderMID)
                            groups = noobcoder.getGroupIdsJoined()
                            contactlist = noobcoder.getAllContactIds()
                            noobcodertag = "ua3e46be368346a83c7c961bc6c23937e"
                            kontak = noobcoder.getContacts(contactlist)
                            favorite = noobcoder.getFavoriteMids()
                            fil = noobcoder.getSettings().privacyReceiveMessagesFromNotFriend
                            seal = noobcoder.getSettings().e2eeEnable
                            blockedlist = noobcoder.getBlockedContactIds()
                            src = noobcoder.getSettings().privacySearchByUserid
                            kontak2 = noobcoder.getContacts(blockedlist)
                            status = {"kick": "", "invite": ""}
                            try:noobcoder.kickoutFromGroup(to, [noobcoderMID]);status["kick"] = "Normal"
                            except:status["kick"] = "Limit"
                            try:noobcoder.inviteIntoGroup(to, [noobcoderMID]);status["invite"] = "Normal"
                            except:status["invite"] = "Limit"
                            if src == True:alid = "Add From LineID : True"
                            else:alid = "Add From LineID : False"                            
                            if seal == True:letsel = "Letter Sealing : True"
                            if seal == False:letsel = "Letter Sealing : False"
                            if fil == True:fpes = "Filter Message : False"
                            if fil == False:fpes = "Filter Message : True"
                            ret_ = "About Bots :\n"
                            ret_ += "\nBots : {}".format(h.displayName)
                            ret_ += "\nGroup : {}".format(str(len(groups)))
                            ret_ += "\nFriend : {}".format(str(len(kontak)))
                            ret_ += "\nFavorite: {}".format(str(len(favorite)))
                            ret_ += "\nBlocked : {}".format(str(len(kontak2)))
                            ret_ += "\nChat send : {}".format(str(peler["sendcount"]))
                            ret_ += "\nChat received : {}".format(str(peler["receivercount"]))
                            ret_ += "\n{}".format(alid)
                            ret_ += "\n{}".format(letsel)
                            ret_ += "\n{}".format(fpes)
                            ret_ += "\nKick : %s" % status["kick"]
                            ret_ += "\nInvite : %s" % status["invite"]
                            ret_ += "\n\nType : Bot Login"
                            ret_ += "\nVersion : V.08"
                            ret_ += "\nMaker :\n"
                            ret_ += "- @!     "
                            mentions(to, str(ret_),[noobcodertag])
                        except Exception as e:
                            noobcoder.sendMessage(to, str(e))
#==========================================
                    elif cmd == "#debug":
                       if msg._from in "ua3e46be368346a83c7c961bc6c23937e":
                            noobcoder.sendMessage(to, debug())
                    elif cmd == "speed":
                        start = time.time()
                        noobcoder.sendMessage("ua3e46be368346a83c7c961bc6c23937e", '</>')
                        elapsed_time = time.time() - start
                        noobcoder.sendMessage(to,"Time:\n%s"%str(round(elapsed_time,5)))
#==========================================
                    elif cmd == "#glist":
                       if msg._from in "ua3e46be368346a83c7c961bc6c23937e":
                            key = settings["keyCommand"].title()
                            if settings['setKey'] == False:key = ''
                            gid = noobcoder.getGroupIdsJoined()
                            sd = noobcoder.getGroups(gid)
                            ret = "「 Group List 」\n"
                            no = 0
                            total = len(gid)
                            cd = "\n\nTotal {} Groups".format(total)
                            for G in sd:
                                member = len(G.members)
                                no += 1
                                ret += "\n{}. {} | {}".format(no, G.name[0:20], member)
                            ret += cd
                            k = len(ret)//10000
                            for aa in range(k+1):
                                noobcoder.generateReplyMessage(msg.id)
                                noobcoder.sendReplyMessage(msg.id, to,'{}'.format(ret[aa*10000 : (aa+1)*10000]))
                    elif cmd.startswith("#bcast"):
                      if msg._from in "ua3e46be368346a83c7c961bc6c23937e":
                        tod = text.split(" ")
                        hey = text.replace(tod[0] + " ", "")
                        text = "{}".format(hey)
                        groups = noobcoder.getGroupIdsJoined()
                        friends = noobcoder.getAllContactIds()
                        for gr in groups:
                            data = {
                                "type": "text",
                                "text": "「 Group Broadcast 」\n\n{}".format(text),
                                "sentBy": {
                                    "label": "Group Broadcast",
                                    "iconUrl": "https://obs.line-scdn.net/{}".format(noobcoder.getContact(noobcoderMID).pictureStatus),
                                    "linkUrl": "line://nv/profilePopup/mid=u2cf74acf6ed04d122def4db8ffdd2e39"
                                }
                            }
                            bcTemplate(gr, data)
                            time.sleep(1)
                        noobcoder.sendMessage(to, "Succes Group cast to {} group ".format(str(len(groups))))
                    elif cmd.startswith("#openqr "):
                      if msg._from in "ua3e46be368346a83c7c961bc6c23937e":
                            number = removeCmd("#openqr", text)
                            groups = noobcoder.getGroupIdsJoined()
                            try:
                                group = groups[int(number)-1]
                                G = noobcoder.getGroup(group)
                                try:
                                    G.preventedJoinByTicket = False
                                    noobcoder.updateGroup(G)
                                    gurl = "https://line.me/R/ti/g/{}".format(str(noobcoder.reissueGroupTicket(G.id)))
                                except:
                                    G.preventedJoinByTicket = False
                                    noobcoder.updateGroup(G)
                                    gurl = "https://line.me/R/ti/g/{}".format(str(noobcoder.reissueGroupTicket(G.id)))
                                noobcoder.sendMessage(to, "「 Open Qr 」\n\nGroup : " + G.name + "\nLink: " + gurl)
                            except Exception as error:
                                noobcoder.sendMessage(to, str(error))
                    elif text.lower() == "#reboot":
                        if msg._from in "ua3e46be368346a83c7c961bc6c23937e":
                            noobcoder.sendMention(to, "@! Brb , going to pee",' ', [msg._from])
                            restartBot()
                        else:pass
                    if text.lower() == "login" and msg._from not in premium["myService"]:
                        noobcoder.sendMention(to, '「 Login 」\n• Status : Failed\n> Sorry @!\nyou are not list in Service',' ', [msg._from])
                    if text.lower() == "restart" and msg._from not in premium["myService"]:
                        noobcoder.sendMention(to, '「 Restart 」\n• Status : Failed\n> Sorry @!\nyou are not list in Service',' ', [msg._from])
                    if text.lower() == "logout" and msg._from not in premium["myService"]:
                        noobcoder.sendMention(to, '「 Logout 」\n• Status : Failed\n> Sorry @!\nyou are not list in Service',' ', [msg._from])
                    if text.lower() == "help login" and msg._from not in premium["myService"]:
                        noobcoder.sendMention(to, '「 Help login 」\n• Status : Failed\n> Sorry @!\nyou are not list in Service',' ', [msg._from])
#==========================================
#==========================================
        if op.type == 55:
            print("[ 55 ] NOTIFIED READ MESSAGE")
            try:
                if op.param1 in wait['readPoint']:
                    if op.param2 in wait['ROM1'][op.param1]:
                        wait['setTime'][op.param1][op.param2] = op.createdTime
                    else:
                        wait['ROM1'][op.param1][op.param2] = op.param2
                        wait['setTime'][op.param1][op.param2] = op.createdTime
                        try:
                            if wait['lurkauto'] == True:
                                if len(wait['setTime'][op.param1]) % 5 == 0:
                                    anulurk(op.param1,wait)
                        except:pass
                elif op.param2 in wait['readPoints']:
                    wait['lurkt'][op.param1][op.param2][op.param3] = op.createdTime
                    wait['lurkp'][op.param1][op.param2][op.param3] = op.param2
                else:pass
            except:
                pass
        backupData()
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)
    
def run():
    while True:
        try:
            ops = noobcoderPoll.singleTrace(count=50)
            if ops != None:
                for op in ops:
                   loop.run_until_complete(noobcoderBot(op))
                   noobcoderPoll.setRevision(op.revision)
        except Exception as e:
            logError(e)
            
if __name__ == "__main__":
    run()