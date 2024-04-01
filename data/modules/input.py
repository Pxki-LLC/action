def get_input():
    global keys,activity,modshow,gobutton,useroverlay,replaymen,beatnowmusic,beatsel,beatsel,diffani,diffcon,beatnowmusic,change,setbutton,settingskeystore,fpsmode,firstcom,accounts
    for event in pygame.event.get():
        if event.type  ==  pygame.QUIT:
            stopnow()
        if event.type  ==  pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.mixer.Sound(samplepath+'click.wav').play()
            if activity==1:
                if menubutton  ==  1:
                    transitionprep(3)
                elif menubutton  ==  3:
                    transitionprep(6)
                elif menubutton  ==  4:
                    stopnow()
                elif menubutton  ==  5:
                    notification('S-Ranker',desc='Like to show off. huh?')
                elif topbutton  ==  1:
                    transitionprep(2)
                elif topbutton  ==  2:
                    accounts=not accounts
            elif activity==0:
                transitionprep(1)
            elif activity==5:
                if butt:
                    if replaymen:
                        transitionprep(6)
                        replaymen=not replaymen
                    else:
                        transitionprep(3)
            elif activity==2:
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
                  settingskeystore[5] = not settingskeystore[5]
                elif setbutton == 7:
                  transitionprep(99)
                elif setbutton == 8:
                  crash('This is a test')
                elif setbutton == 9:
                    transitionprep(0)
                    logotime=time.time()
                elif sysbutton:
                    transitionprep(1)


            elif activity==3 or activity==7:
                if event.button==1:
                    if sysbutton  ==  1:
                        if not activity==7:
                            transitionprep(1)
                        else:
                            activity=3
                    elif sysbutton == 2:
                        modshow=not modshow
                        print(modshow)
                    else:
                        if gobutton:        
                            if not activity==7:
                                if len(diff)>1:
                                    activity=7
                                else:
                                    preparemap()
                            else:
                                preparemap()
                        else:
                            if mod:
                                for a in range(1,len(modsen)+1):
                                    if mod==a:
                                        modsen[a-1]=not modsen[a-1]
                                        reloadstats()
                            else:
                                if button:
                                    if activity!=7:
                                        if button-1!=beatsel:
                                            beatnowmusic=1
                                            beatsel=button-1
                                            diffcon=0
                                        else:
                                            if not activity==7:
                                                if len(diff)>1:
                                                    activity=7
                                                else:
                                                    preparemap()
                                            else:
                                                preparemap()
                                    else:
                                        if button-1!=diffcon:
                                            diffcon=button-1
                                            diffani=Tween(begin=cross[1], end=diffcon,duration=1500,easing=Easing.CUBIC,easing_mode=EasingMode.OUT)
                                            diffani.start()
                                            reloadstats()
                                        else:
                                            preparemap()
                elif event.button==4:
                        if not activity==7:
                            song_change(0)
                        else:
                            diff_change(0)
                elif event.button==5:
                        if not activity==7:
                            song_change(1)
                        else:
                            diff_change(1)


        if event.type  ==  pygame.KEYDOWN:
            if event.key  ==  pygame.K_MINUS:
                volchg(0)
            elif event.key  ==  pygame.K_EQUALS:
                volchg(1)
            elif event.key  ==  pygame.K_F9:
                useroverlay=not useroverlay
            elif event.key  ==  pygame.K_q or event.key  ==  pygame.K_ESCAPE:
                if activity==4:
                    transitionprep(3)           
                elif not activity==7:
                    transitionprep(1)
                elif activity==7:
                    activity=3
                elif not activity==1:
                    stopnow()
            if activity==7 or activity==3:
                if event.key  ==  pygame.K_RETURN:
                    if not activity==7:
                        if len(diff)>1:
                            activity=7
                        else:
                            preparemap()
                    else:
                        preparemap()
                if activity==3:
                    if event.key == pygame.K_F2:
                        if len(fullbeatmapname)!=0:
                            beatsel=random.randint(1,len(fullbeatmapname))-1
                            beatnowmusic=1
                if event.key  ==  pygame.K_UP:
                    if activity!=7:
                        song_change(0)
                    else:
                        diff_change(0)
                if event.key  ==  pygame.K_DOWN:
                    if activity!=7:
                        song_change(1)
                    else:
                        diff_change(1)
                        
                if event.key  ==  pygame.K_e:
                    change_diff()    
            elif activity==5:
                if event.key == pygame.K_q:
                    if replaymen:
                        transitionprep(6)
                        replaymen=not replaymen
                    else:
                        transitionprep(3)
            elif activity==4:
                if event.key  ==  pygame.K_d:
                    keys[0]=1
                    keyslight[0]=time.time()
                if event.key  ==  pygame.K_f:
                    keys[1]=1
                    keyslight[1]=time.time()
                if event.key  ==  pygame.K_j:
                    keys[2]=1
                    keyslight[2]=time.time()
                if event.key  ==  pygame.K_k:
                    keys[3]=1
                    keyslight[3]=time.time()
                if event.key  ==  pygame.K_BACKQUOTE:
                    beatnowmusic=1
                    resetscore()
        if event.type  ==  pygame.KEYUP:
            if activity==4:
                if event.key  ==  pygame.K_t:
                    tip=0
                if event.key  ==  pygame.K_d:
                    keys[0]=0
                if event.key  ==  pygame.K_f:
                    keys[1]=0
                if event.key  ==  pygame.K_j:
                    keys[2]=0
                if event.key  ==  pygame.K_k:
                    keys[3]=0