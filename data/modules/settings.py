if os.path.isfile(datapath+'settings.db'):
    if not len(open(datapath+'settings.db').read().rstrip("\n").split("\n"))<4:
        settingskeystore=open(datapath+'settings.db').read().rstrip("\n").split("\n")
        for a in range(len(settingskeystore)):
            if settingskeystore[a].isdigit() or settingskeystore[a] == 'True' or settingskeystore[a] == 'False':
              settingskeystore[a]=eval(settingskeystore[a])
        print(settingskeystore)
        if len(settingskeystore) >= 4 and str(settingskeystore[3]).isdigit():
            if int(settingskeystore[3]) in fpsmodes:
                fpsmode=int(settingskeystore[3])
                print('FPS set to '+str(fpsmodes[fpsmode]))
            elif test(fpsmodes, settingskeystore[3]):
                fpsmode=int(settingskeystore[3])
                print('FPS set to '+str(fpsmodes[fpsmode]))
            else:
                print('FPS '+str(settingskeystore[3])+' is not valid,  set back to 60 (Normal)')
                fpsmode=1
        else:
            for a in range(1,len(settingskeystore)+1):
                settingskeystore.append(0)
else:
    settingskeystore=[]
    for a in range(1, 5):
        settingskeystore.append(False)
    settingskeystore.append(0)

def settingspage():
    global settingskeystore, activity, screen, firstcom, change, fpsmode,totperf,totscore,msg,logotime
    if activity==2:
        if change:
            tmp=open(datapath+'settings.db', 'w')
            for a in settingskeystore:
                tmp.write(str(a)+'\n')
            tmp.close()
            change=False
        #settingskeystore[2], settingskeystore[1], fullscreen
        if str(fpsmodes[fpsmode])!='1000':
            tmp=str(fpsmodes[fpsmode])
        else:
            tmp='Unlimited'
        render('header')
        render('text', text=gamename + ' - Options', arg=(offset, forepallete))
        setuplist=['FPS: '+tmp,'Fullscreen: '+str(settingskeystore[0]),'Effects: '+str(not settingskeystore[1]),'Allow Skins: '+str(settingskeystore[2]),'Hitsounds: '+str(settingskeystore[4]),'Debug Info','Crash Test']
        setuplistpos=[]
#        for a in range(1,6):
#            setuplist.append('Unknown')
        for a in range(1,len(setuplist)+1):
            poof=offset[1]+10
            setuplistpos.append((w//2-110,  poof+(50*a),  220,  button_size_height))
        setbutton=menu_draw((setuplistpos), (setuplist))
        sysbutton=menu_draw(((-10,h-50,100,40),),('Back',))
        if setbutton == 1:
            msg='Changes how fast this game goes'
        elif setbutton == 2:
            msg='Makes the Screen Fullscreen, what do you expect'
        elif setbutton == 3:
            msg='Changes the Flashing Effect'
        elif setbutton == 4:
            msg='Allows Skinning'
        elif setbutton == 5:
            msg='Enable Hitsounds'
            
        for event in pygame.event.get():
            if event.type  ==  pygame.QUIT:
                stopnow()
            if event.type  ==  pygame.MOUSEBUTTONDOWN: 
                if setbutton:
                  change=True
                if setbutton  ==  1:
                    change=True
                    if fpsmode<1:
                        fpsmode=len(fpsmodes)-1
                    else:
                        fpsmode-=1
                    settingskeystore[3]=fpsmode
                elif setbutton == 2:
                  settingskeystore[0] = not settingskeystore[0]
                  firstcom=False
                elif setbutton == 3:
                  settingskeystore[1] = not settingskeystore[1]
                elif setbutton == 4:
                  settingskeystore[2] = not settingskeystore[2]
                elif setbutton == 5:
                  settingskeystore[4] = not settingskeystore[4]
                elif setbutton == 6:
                  transitionprep(99)
                elif setbutton == 7:
                  crash('This is a test')
                elif setbutton == 8:
                    transitionprep(0)
                    logotime=time.time()
                elif sysbutton:
                    transitionprep(1)

            if event.type  ==  pygame.KEYDOWN:
                if event.key  ==  pygame.K_q:
                    transitionprep(1)
