import json
fpsmodes=[30,60,120,240,480,1000]
if os.path.isfile(datapath+'settings'):
    print('Using SettingsV2...')
    settingskeystore=json.load(open(datapath+'settings'))
    print('Completed')
else:
    settingskeystore={
        'hitsound' : True,
        'leaderboard' : True,
        'fullscreen' : False,
        'effects' : True,
        'skinning' : True,
        'username' : None,
        'password' : None,
        'apiurl' : 'https://qlute.pxki.us.to/',
        'fps' : 480
    }
    tmp=open(datapath+'settings', 'w')
    tmp.write(json.dumps(settingskeystore))
    tmp.close()
fpsmode=fpsmodes.index(settingskeystore['fps'])
print(fpsmode,settingskeystore['fps'])
setupid=1
setupcatagory=('General','Skinning','Audio','Graphics','Debug','Account')
setupcatpos=[]
b=0
for a in setupcatagory:
    setupcatpos.append((0+(100*b),80,100,20))
    b+=1
#                            render('rect', arg=(pos, (43, 163, 237), False))

def settingspage():
    global settingskeystore, activity,catbutton, screen, firstcom, change, fpsmode,totperf,totscore,msg,logotime,setbutton,sysbutton
    if activity==2:
        if change:
            tmp=open(datapath+'settings', 'w')
            tmp.write(json.dumps(settingskeystore))
            tmp.close()
            change=False
        #settingskeystore[2], settingskeystore[1], fullscreen
        if str(fpsmodes[fpsmode])!='1000':
            tmp=str(fpsmodes[fpsmode])
        else:
            tmp='Unlimited'
        render('rect', arg=((0,0,w,h), (42,40,95), False))
        render('rect', arg=((0,0,w,100), (62,60,115), False))
#        b=0
        catbutton=menu_draw((setupcatpos), (setupcatagory),settings=True,selected_button=setupid)
#        for a in setupcatagory:
#            pos=(0+(100*b),80,100,20)
#            render('rect', arg=(pos, (43, 163, 237), False))
#            render('text', text=a, arg=((0,0), forepallete,'center','min'),relative=pos)
#            b+=1
        render('text', text='Settings', arg=(offset, forepallete,'grade'))
        if not settingskeystore['username']:
            user='Guest'
        else:
            user=settingskeystore['username']
        setuplist={'general': {'Leaderboards':settingskeystore['leaderboard'],'Effects':settingskeystore['effects']},'skinning':{'Note Width':'->','Note Height':'->','Note Colour':'->','Background Colour':'->','Insanity Level':'->',},'audio':{'Hitsounds':settingskeystore['hitsound']},'graphics':{'FPS':tmp,'Fullscreen':settingskeystore['fullscreen']},'debug':{},'account':{'Username':user}}
        #setuplist=['FPS: '+tmp,'Fullscreen: '+str(settingskeystore['fullscreen']),'Effects: '+str(settingskeystore['effects']),'Allow Skins: '+str(settingskeystore['skinning']),'Hitsounds: '+str(settingskeystore['hitsound']),'Leaderboards: '+str(settingskeystore['leaderboard']),'Debug Info','Crash Test']
        setuplistpos=[]
#        for a in range(1,6):
#            setuplist.append('Unknown')
        b=0
        if setupid==2:
            render('rect', arg=((w//2,100,w//2,h-100), (20,20,20), False))
        if setupid==5:
            render('text',text='Game Name - '+str(gamename),arg=((20,120+(23*0)),forepallete))
            render('text',text='Game Version - '+str(gamever),arg=((20,120+(23*1)),forepallete))
            render('text',text='Slyph Engine Version - '+str(sylphenginever),arg=((20,120+(23*2)),forepallete))
            render('text',text='Module Initial Time - '+str(moduletime),arg=((20,120+(23*3)),forepallete))
            render('text',text='Ping Speed - '+str(pingspeed)+'ms',arg=((20,120+(23*4)),forepallete))
        else:
            setuptxt=[]
            for a in setuplist[setupcatagory[setupid-1].lower()]:
                b+=1
                poof=offset[1]+40
                if setupid==2:
                    posw=20
                else:
                    posw=w//2-110
                setuplistpos.append((posw,  poof+(50*b),  220,  button_size_height))
                setuptxt.append(a+' : '+str(setuplist[setupcatagory[setupid-1].lower()][a]))
            if len(setuptxt)<1:
                setbutton=0
            else:
                setbutton=menu_draw((setuplistpos), (setuptxt),styleid=3)
            if setbutton == 1 and setupid==4:
                msg='Changes how fast this game goes'
            elif setbutton == 2 and setupid==4:
                msg='Makes the Screen Fullscreen, what do you expect'
            elif setbutton == 2 and setupid==1:
                msg='Changes the Flashing Effect'
            elif setbutton == 1 and setupid==3:
                msg='Enable Hitsounds'
            elif setbutton == 1 and setupid==1:
                msg='Enable Leaderboards'
        sysbutton=menu_draw(((-10,h-60,100,60),),('Back',),bradius=0,styleid=3)
