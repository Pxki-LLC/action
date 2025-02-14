#!/usr/bin/python3
#
#    Just Beats! (Qlute)
#    2020-2024 Pxki Games (Formally known as ??)
#    (Using Slyph Engine, Tinyworld's Game Engine)
#
#
import random,re,json,zipfile,os
from random import randint
import pygame, time, sys, threading, requests, socket,hashlib,io
from tweener import *
nline='\n'
axe=0
gamename='Qlute'
gameeditions='stable','beta','canary','dev'
if not "gamever" in globals():
    gamever='0.0.0'
if not "gameedition" in globals() or not gameedition.isdigit():
    gameedition=gameeditions[-1]
else:
    gameedition=gameeditions[int(gameedition)]
sylphenginever=gamever
gameverspl=gamever.split('.')
#gameminserve=int(gameverspl[0])+((1+float(gameverspl[1]))*float(gameverspl[2]))
gamepath=datapath+'beatmaps/'
samplepath=syspath+'samples/'
downpath=datapath+'downloads/'
replaypath=datapath+'replays/'
skinpath=datapath+'skins/'
username='Guest'
propath=datapath+'profiles/'
profilepath=propath+username+'/'
gameupdateurl='https://github.com/pxkidoescoding/Qlute/'
gameauthor='Pxki Games'
print('Starting Game...')
button_size_height=33
stop=0
rankdiff='Easy','Normal','Hard','Extra','Expert','>n<','Devil'
rankdiffc=(0,100,200),(0,200,50),(150,200,0),(200,50,0),(0,0,0),(150,0,150)
sa=time.time()
gametime=0
ismusic=0
paths=datapath,gamepath,propath,profilepath,downpath,replaypath,skinpath
prestart=1
reloaddatabase=1
vol=100
volvismo=0
volvisual=0
isonline=False
menunotice=''
speed=1
leaderboard=[]
hitcolour=((100,120,200),(100,200,100),(200,200,100),(200,100,100))
for a in paths:
    if not os.path.isdir(a):
        os.mkdir(a)
        print('Created', a.replace('./', ''))
keyspeed=6
keyspeedb=13360/keyspeed
getpoints=0
debugmode=True
fps=0
update=False
offset=20,20
beatsel=0
beatnowmusic=1
score=0
maxperf=0
betaperf=0
comboburst=1000
perfbom=0.075
diff=[]
diffmode=''
diffcon=0
bgcolour=0
perf=0
maxobjec=255
objecon=0
oldupdatetime=0
totscore=0
tick=0
combo=0
lastms=0
darkness=0
stripetime=[]
bgtime=time.time()
objects=[]
speedvel=[0,0]
modsen=[0,0,0,0,0,0,0,0,0,0]
scoremult=1
modshow=False
msg=''
totrank=0
prevrank=0
uptime=time.time()
totperf=0
totscore=0
totacc=0
oldstats=[0,0]
rankmodes=('Ranked',(100,200,100)),('Unranked',(200,100,100)),('Special',(200,200,100)),('Loading...',(200,200,200)),

pygame.init()
fontname=resource_path(syspath+'font.ttf')
clock=pygame.time.Clock()
activity=0
select=False
cross=[0,0]
crossboard=0
realid='' 
firstcom=False
combotime=0
maxplay=50
menuback=0
backspeed=1
replaymen=0
beka='None'
actto=activity
transb=0
transa=0
voltime=0
#tmp!!!!
msgx=0
messagetime=0
change=False
colorstep = 0
loaded=[]
ama=0
bars=[0,0,0,0,0,0,0,0]
t=''
miss=0
go=False
hits=[0,0,0,0]
#hitperfect=keymap[0][1]
#hitperfect=keymap[0][1]
last=0
ismulti=False # Enabling this means Leaderboard is shown
keys=[0,0,0,0]
keyslight=[0,0,0,0]
pos=(64,192,320,448)
tip=0
sre=0
crox=[]
delta=0
mainurl='https://dev.catboy.best'
beatmapapi=mainurl+'/api/v2/'
beattitle=None
countersp=0
#def print(txt):
#    logbox.append((txt,time.time()))
drawtime=0.0000001
kiai=0
notemsg=['','']
noteani=[Tween(begin=0, end=100,duration=150,easing=Easing.CUBIC,easing_mode=EasingMode.OUT,boomerang=True),0]
notemaxh=1
useroverlay=0
upd=0
hittext='PERFECT!','GREAT','MEH','MISS'
hitcolour=(100, 120, 200),(100, 200, 100),(200, 200, 100),(200, 100, 100)
def notification(title,desc=''):
    global noteani,notemsg
    notemsg=[title,desc]
    noteani=[Tween(begin=0, end=notemaxh,duration=500,easing=Easing.CUBIC,easing_mode=EasingMode.OUT,boomerang=True),0]
    noteani[0].start()
def main():
    global fps, activity,oneperf,change,upd,noteani,voltime,delta,transi,volvisual,volvismo,notemsg,flashylights,logopos,oneperfk,mtext, ingame, screen, settingskeystore,reloaddatabase,totrank, debugmode,sa,bgcolour,tick,scale,size,cardsize,bgtime,replaymen,allowed,posmouse,drawtime,scoremult,msg
    if change:
        tmp=open(datapath+'settings', 'w')
        tmp.write(json.dumps(settingskeystore))
        tmp.close()
        change=False
    if gameedition!=gameeditions[0]:
        gs='/'+gameedition
    else:
        gs=''
    msg=''
    if beattitle!=None and activity==4:
        alttitle=beattitle
    else:
        alttitle=''
    pygame.display.set_caption(gamename+gs+' '+str(gamever)+' '+alttitle)
    if not firstcom:
        pygame.display.set_icon(programIcon)
    if activity in (9,10):
        pygame.mouse.set_visible(True)
    else:
        pygame.mouse.set_visible(False)
    update=time.time()
    posmouse=pygame.mouse.get_pos()
#    if modsen[0]:
#        scoremult=1

    if time.time()-sa>0.1:
        sa=time.time()
        fps=int(clock.get_fps())
    allowed=[0,1,2,3,5,6,7,8,11,12,99]
    upd=time.time()
    fullscreenchk()
    size=60
    scale=(w/400)
    if scale>=2:
        scale=2
    cardsize=int(300*scale)
    if activity==2:
        ingame=True
    else:
        ingame=False

    if "bpm" in globals() and "beatmaps" in globals():
        if activity in allowed or kiai:
            if beatmaps!=0:
                if not activity in (3,7):
                    clear((maxt(bgdefaultcolour[0],bgcolour),maxt(bgdefaultcolour[1],bgcolour),maxt(bgdefaultcolour[2],bgcolour)))
                else:
                    clear((maxt(20,bgcolour),maxt(20,bgcolour),maxt(20,bgcolour)))
            else:
                clear(bgdefaultcolour)
            flashylights=(1-((gametime/bpm)-tick))
            if flashylights<0:
                flashylights=0
            elif flashylights>1:
                flashylights=1
            elif gametime<=-1:
                flashylights=0
            if settingskeystore['effects']:
                bgcolour=30*flashylights
            else:
                bgcolour=0
        if gametime//bpm>tick:
            tick+=1
    for a in os.listdir(downpath):
        if a.endswith('.osz'):
            if not os.path.isdir(gamepath+a.replace('.osz','')):
                os.mkdir(gamepath+a.replace('.osz',''))
                with zipfile.ZipFile(downpath+a, 'r') as zip_ref:
                    zip_ref.extractall(gamepath+a.replace('.osz','/'))
                    reloaddatabase=1
                notification('Beatmap Imported',desc=a)
            os.remove(downpath+a)
    if totrank<1:
        totrank=1
    transi=((100-transani[0].value)/100)
    get_input()
    beatmapload()
    logo()
    mainmenu()
    beatres()
    settingspage()
    beatmenu()
    customization()
    shopdirect()
    gameedit()
    loginscreen()
    downloads()
    if useroverlay:
        render('rect', arg=((0,-15,w,h//2), (60,60,60), False), borderradius=15)
        posy=10
        for a in range(1,25):
            posx=10+(310*(a-1))
            if posx>=w:
                posy+=90
            print_card(totperf,totscore,'aqua'+str(a),(posx,posy),a)
    try:
        game()
    except Exception as error:
        raise TypeError
        crash(error)
        activity=1
    if not notemsg[0]=='':
        sh=0
        sw=0
        for a in range(1,3):
            tmp = fonts[a-1].render(str(notemsg[a-1]),  True,  (0,0,0))
            txtrect=tmp.get_rect()
            if txtrect[2]+20>sw:
                sw+=txtrect[2]+20
            sh+=txtrect[3]+30
        notepos=w//2-(sw//2),(noteani[0].value*120)-100,sw,sh
        fcolor=(forepallete[0]*noteani[0].value,forepallete[1]*noteani[0].value,forepallete[2]*noteani[0].value)
        render('rect', arg=(notepos, (noteani[0].value*92,noteani[0].value*90,noteani[0].value*145), False), borderradius=15)
        render('text', arg=((0,0), fcolor, False,'center'),text=notemsg[0],relative=(notepos[0],notepos[1]+15,notepos[2],10))
        render('text', arg=((0,0), fcolor, False,'center','min'),text=notemsg[1],relative=(notepos[0],notepos[1]+20,notepos[2],notepos[3]-20))
        if noteani[0].value==notemaxh and not noteani[1]:
            if noteani[1]==0:
                noteani[1]=time.time()
            noteani[0].pause()
        elif noteani[1]!=0 and time.time()-noteani[1]>3:
            noteani[0].resume()
            if noteani[0].value==0:
                noteani[0].pause()
                notemsg=['','']
                noteani[1]=0
    noteani[0].update()
    if msg!='':
        tmp=(posmouse[0]+15,posmouse[1]+15,25,25)
        render('text',text=msg,arg=((tmp[0],tmp[1]),forepallete,'min','tooltip'))
        msg=''
    render('rect', arg=(((w//2)*(1-((transani[0].value)*0.01)),(h//2)*(1-((transani[0].value)*0.01)),(w)*((transani[0].value)*0.01),h*((transani[0].value)*0.01)), (0,0,0), False))
    if transani[1]:
        transani[0].update()
        if transani[0].value>99:
            activity=actto
        elif transani[0].value==0:
            transani[1]=0
    #updateraw=(time.time()-update)/0.001
    #spectrum()
    if activity==1:
        of=35
    else:
        of=0
    volvisual=volani.value
    if int(volvisual)>int(vol) or int(volvisual)<int(vol):
        volani.update()
        v=1
    else:
        v=0
    if v:
        voltime=time.time()
    if not int(time.time()-voltime)>1:
        volpos=(20, h//2-100, 20, 200)
        render('rect', arg=((-15,h//2-105,115,210), (60,60,100), False), borderradius=15)
        render('rect', arg=(volpos, (20,20,20), False), borderradius=15)
        render('rect', arg=((volpos[0],volpos[1]+1+volpos[3]-((volvisual*0.01)*volpos[3]),volpos[2],(volvisual*0.01)*volpos[3]), (168*(volvisual*0.01), 232*(volvisual*0.01), 255*(volvisual*0.01)), False), borderradius=15)
        render('text',text=str(int(volvisual))+'%',arg=((0,0),forepallete,'center'),relative=(volpos[0]+50,volpos[1],0,volpos[3]))
    if debugmode:
        updatetime=(time.time()-upd)/0.001
        if updatetime>=10:
            fpscolour=(150,50,50)
        else:
            fpscolour=(50,150,50)
        render('rect', arg=((w-98, of+17, 110, 45), (fpscolour), False), borderradius=10)
        render('text', text=f'{fps} fps', arg=((w - 120, 23), forepallete, 'center'), relative=(w - 107, of + 20, 120, 20))
        render('text', text=f'{str(round(updatetime,2))}ms', arg=((w - 120, 43), forepallete, 'center'), relative=(w - 107, of + 40, 120, 20))        #render('text',text='TICK:'+str(tick)+'/'+str(gametime//bpm)+'/'+str(gametime)+'/'+str(bpm),arg=((20, 43),forepallete))
        #render('rect', arg=((5, 5, struct, 5), (0,255,0), False), borderradius=10)
#    x=0
#    for a in logbox[::-1][:10]:
#        if time.time()-a[1]>4:
#            logbox.remove(a)
#        render('rect', arg=((10, 10+(60*x), 150, 50), (20,20,20), False), borderradius=10)
#        render('text', text=a[0], arg=((0,0), forepallete, 'center'), relative=(10, 10+(60*x), 150, 50))
#        x+=1
    #print((time.time()-gametime)/0.001)
    if activity in allowed:
        render('rect', arg=((posmouse[0]-10,posmouse[1]-10,20,20), (102, 155, 212), True),borderradius=20)
#    if not (posmouse[0],posmouse[1]) in crox:
#        crox.append((posmouse[0],posmouse[1]))
    pygame.display.flip()
    drawtime=clock.tick(fpsmodes[fpsmode])/1000
    delta=drawtime
    #print(drawtime)
nettick=0
timetaken=0
welcometext='Welcome to '+str(gamename)
logbox=[('Started Engine',time.time())]
def gamesession():
    while True:
        main()
if os.path.isfile(datapath+'.developer'):
    modsen[0]=1 # Automatically enables Auto Mod
if __name__  ==  "__main__":
    try:
        if os.path.isfile(datapath+'devsettings'):
            devset=open(datapath+'devsettings').read().split('\n')
            for a in devset:
                amp=a.split('=')
                if a[0][0]!='#':
                    if amp[0]=='apiurl':
                        apiurl=amp[1]
                    elif amp[0]=='username':
                        username=amp[1]
                    elif amp[0]=='vol':
                        vol=int(amp[1])
                    elif amp[0]=='welcometext':
                        welcometext=amp[1]
        if prestart:
            logotime=time.time()
        greph=[]
        for a in modsen:
            greph.append(randint(1,2)-1)
        icons={}
        for a in os.listdir(resource_path(syspath+'icons/')):
            icons[a]=(pygame.image.load(resource_path(syspath+'icons/'+a))) # Icons!
        programIcon = pygame.image.load(resource_path(syspath+'icon.png'))
        threading.Thread(target=ondemand).start()
        #threading.Thread(target=loginwindow).start()
        #for a in range(1,3):
            #threading.Thread(target=gamesession).start(
        while True:
            if stop:
                sys.exit()
            main()
    except Exception as error:
        crasha(str(error))
