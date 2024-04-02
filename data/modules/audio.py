def spectrum():
    global bars
    for a in range(1,len(bars)+1):
        ral=random.randint(1,100)
        bars[a-1]=ral
        render('rect', arg=(((tal)*(a-1),h-ral,(tal),ral), (255,255,255), False),borderradius=10)
def get_creation_time(item):
    item_path = os.path.join(gamepath, item)
    return os.path.getctime(item_path)
def beatmapload():
    global p2,p1,beatnowmusic,gc,gametime,beatani,diffani,beattitle,fullbeatmapname,objects,diffp,betaperf,reloaddatabase,maxperf,background,ranktype,diff,diffmode,pref,level,ismusic,bpm,realid,prestart,beatsel,tick,lastms,combotime,songoffset,metadata
    if reloaddatabase:
        p1=[]
        p2=[]
        fullbeatmapname=[]
        reloaddatabase=0
        for b in sorted(os.listdir(gamepath), key=get_creation_time):
            try:
                p1.append((((cardsize//2),(size),cardsize,size)))
                p2.append(str(b)[str(b).index(' ')+1:])
                fullbeatmapname.append(b)
            except Exception:
                pass
    if prestart:
        if len(fullbeatmapname)!=0:
            beatsel=random.randint(1,len(fullbeatmapname))-1
        prestart=0
    if ismusic:
        #gametime=pygame.mixer.music.get_pos()
        up=((time.time()-upd)/0.001)*10
        gametime=(((time.time()-gc)/0.001)-(up))*1
        pygame.mixer.music.set_volume((volvisual*0.01))
    else:
        background=pygame.Surface((0,0))
#        pygame.mixer.music.set_volume(0)
        #pygame.mixer.music.set_pos(time.time()-gametime)
        #pass
#        if gametime<0:
#            gametime=0
        #pygame.mixer.music.play(-1,(time.time()-gametime))
    try:
        if beatnowmusic:
            beatani=Tween(begin=cross[0], end=beatsel,duration=350,easing=Easing.CUBIC,easing_mode=EasingMode.OUT)
            beatani.start()
            diffani=Tween(begin=-1, end=0,duration=1,easing=Easing.CUBIC,easing_mode=EasingMode.OUT)
            diffani.start()
            gc=time.time()
            ranktype=3
            gametime=0
            tick=0
    #        if activity==4:
    #            if int(time.time()-wait)>=1:
    #                wait=time.time()+3
    #                pygame.mixer.music.stop()
    #        else:
    #            wait=int(time.time())
            ismusic=False
            if len(fullbeatmapname)!=0:
                aga=0
                if os.path.isdir(gamepath+fullbeatmapname[beatsel]):
                    ah=os.listdir(gamepath+fullbeatmapname[beatsel])
                    for bop in ah:
                        if bop.endswith('.mp3') or bop.endswith('.ogg'):
                            music=bop
                            aga=1
                            break
                    if aga:
                        ismusic=True
            if ismusic:
                #if not int(time.time()-wait)<=-1:
                if 1==1:
                    beatnowmusic=0
                    realid=fullbeatmapname[beatsel]
                    diff=[]
                    pref=''
                    if activity in allowed:
                        loop=-1
                        #print(loop)
                    else:
                        loop=0
                    for a in ah:
                        if a.endswith('.osu'):
                            ax=re.findall(r'\[(.*?)\]', a)
                            if len(str(ax))>2:
                                diff.extend(ax)
                        if pref=='' and a.endswith('.osu'):
                            pref=a.replace('.osu','')
                            pref=pref[:pref.index('[')]
                    diffp=[]
                    for difftmp in diff:
                        beatmap=open(gamepath+fullbeatmapname[beatsel]+'/'+pref+'['+difftmp+']'+'.osu').read().rstrip('\n').split('\n')
                        general=beatmap[beatmap.index('[General]')+1:]
                        general=general[:general.index("")]
                        for a in general:
                            if "AudioFilename" in a:
                                music=a.split(': ')[1]
                        objects=len(beatmap[beatmap.index('[HitObjects]')+1:])
                        difficulty=beatmap[beatmap.index('[Difficulty]')+1:]
                        difficulty=difficulty[:difficulty.index('')]
                        metadata=beatmap[beatmap.index('[Metadata]')+1:beatmap.index('[Difficulty]')-1]
                        diffp.append((objects,difftmp))
                    diffp=sorted(diffp, key=lambda x: x[0])
                    diff=diffp
#                    print(diffp)
                    pygame.mixer.music.load(gamepath+fullbeatmapname[beatsel]+'/'+music)
                    pygame.mixer.music.play(-1)
                    #print(ids)
                    gametime=pygame.mixer.music.get_pos()
                    reloadstats()
                    betaperf=0
                    ptick=0
                    gener=0
                    perfnerf=0.00975
                    perfntot=0
                    for a in objects:
                        if int(a.split(',')[2])//100>ptick:
                            ptick=int(a.split(',')[2])//100
                            perfntot=0
                        else:
                            perfntot+=perfnerf
                        betaperf+=perfntot
                    betaperf=betaperf
                    if betaperf>1500:
                        betaperf=1500
                    lastms=int(objects[-1].split(',')[2])
#                    else:
#                        ranktype=
            else:
                lastms=1
                bpm=60000
                level=1
                #objects=['','']
                #metadata=beatmap[beatmap.index('[Metadata]')+1:]
#            for a in beatmap[:3]:
#                print(a)
#            sys.exit()
    except Exception as error:
        print('Could not load Song: '+str(error))
        song_change(1)
def volchg(t):
    global vol,voltime,volani
    voltime=time.time()+1
    step=5
    if vol<100 and t:
        volani=Tween(begin=vol, end=vol+step,duration=250,easing=Easing.CUBIC,easing_mode=EasingMode.OUT)
        volani.start()
        vol+=step
    elif vol>0 and not t:
        volani=Tween(begin=vol, end=vol-step,duration=250,easing=Easing.CUBIC,easing_mode=EasingMode.OUT)
        volani.start()
        vol-=step
