import requests
def bpmparse(bpm):
    return bpm.split(',')[1]
def reloadstats():
    global objects,difficulty,background,metadata,timings,level,bpm,songoffset,maxperf,scoremult,ismulti,beattitle,perfect,great,ok,diffmode,beatmapid,beatmapsetid
    diffmode=diff[diffcon][1]
    beatmap=open(gamepath+fullbeatmapname[beatsel]+'/'+pref+'['+diffmode+']'+'.osu').read().rstrip('\n').split('\n')
    objects=beatmap[beatmap.index('[HitObjects]')+1:]
    b=0
    background=pygame.surface.Surface((0,0))
    if modsen[4]:
        print('RND MODE')
        lol=0
        tmp=''
        for a in objects:
            tmp=''
            tok=a.split(',')[1:]
            for b in tok:
                tmp+=','+str(b)
            key=randint(1,len(pos))-1
            objects[lol]=str(pos[key])+tmp
            lol+=1
    events=beatmap[beatmap.index('[Events]')+1:]
    events=events[:events.index("")]
    background=events[events.index('//Background and Video events')+1]
    if background[:3]=='0,0':
        background=background.split(',')[2].rstrip('"')[1:]
        b=0.50
        background=pygame.image.load(gamepath+fullbeatmapname[beatsel]+'/'+background).convert_alpha()
        background=pygame.transform.scale(background, (w, h))
        background.fill((255*b, 255*b, 255*b,128), special_flags=pygame.BLEND_RGBA_MULT)
    difficulty=beatmap[beatmap.index('[Difficulty]')+1:]
    keycheck=int(float(difficulty[1].replace('CircleSize:','')))
#    if keycheck!=4:
#        print('This Game only supports ONLY 4 Keys')
#        if len(bp2)>1:
#            diff_change(1)
#        else:
#            song_change(1)
    difficulty=difficulty[:difficulty.index('')]
    metadata=beatmap[beatmap.index('[Metadata]')+1:beatmap.index('[Difficulty]')-1]
    beatmapid=None
    beatmapsetid=None
    for a in metadata:
        if 'BeatmapID' in a:
            beatmapid=int(a.replace('BeatmapID:',''))
        elif 'BeatmapSetID' in a:
            beatmapsetid=int(a.replace('BeatmapSetID:',''))
    beattitle=p2[beatsel].replace('\n','-')+' ['+str(diffmode)+']'
    threading.Thread(target=getstat).start()
    timingst=beatmap[beatmap.index('[TimingPoints]')+1:]
    timings=[]
    for a in timingst:
        if not len(a)<2:
            timings.append(a)
        else:
            break
    bpm=float(bpmparse(timings[0]))
    songoffset=float(beatmap[beatmap.index('[TimingPoints]')+1:][0].split(',')[0])
    scoremult=1
    inc=0.5
    inf=0.1
    perfect=80
    #perfect=60
    great=perfect*2
    ok=perfect*3
    ismulti=modsen[4]
    for a in range(2,len(modsen)+1):
        if modsen[a-1] and a==2:
            scoremult+=inc*3
        elif modsen[a-1] and not a in (4,5):
            scoremult+=inc
        elif modsen[a-1] and a==4:
            scoremult-=inc
    maxperf=int(len(objects)*perfbom*scoremult)
def getstat():
    global ranktype,getpoints,leaderboard
    #print('Loading...')
    leaderboard=[]
    try:
            f = requests.get('https://api.chimu.moe/cheesegull/s/'+str(beatmapsetid),headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'},timeout=3)
            f=f.json()['RankedStatus']
#            print(f)
            ranktypetmp=int(f)
    except Exception as error:
        print(error,'(Returning as Unranked)')
        ranktypetmp=-99
    f=requests.get(apiurl+'api/getleaderboard?'+str(beatmapid))
    leaderboard=f.json()
#    if len(leaderboard)>0:
#        print(f.json(),'> Leaderboard')
#    else:
#        print('No Leaderboard')
#    for a in leaderboard:
#        print(a)
    #ranktypetmp=1
    getpoints=0
    #if id!=None:
#        print(ranktypetmp)
    if ranktypetmp==3:
#        print(rankmodes[2][0])
        ranktype=2
    elif ranktypetmp>0:
        ranktype=0
        getpoints=1
    else:
#        print(rankmodes[1][0])
        ranktype=1
        getpoints=0
def resetscore():
    global score,barclicked,prevrank,timestep,unstablerate,timetaken,perf,scorew,kiai,bgcolour,objecon,combo,sre,health,healthtime,combotime,hits,last,stripetime,ppcounter,pptime,pptmp,modshow,ranking
    last=0
    prevrank=totrank
    unstablerate=[]
    timestep=0
    healthtime=time.time()
    timetaken=time.time()
    combo=0
    kiai=0
    health=100
    stripetime=[]
    objecon=0
    pptime=time.time()
    pptmp=0
    modshow=False
    ppcounter=0
    if activity==4:
        bgcolour=235
    sre=0
    combotime=0
    hits=[0,0,0,0]
    score=0
    scorew=score
    perf=0
    barclicked=[]
def change_diff():
    global diffcon,beatnowmusic
    if not diffcon+1>=len(diff):
        diffcon+=1
    else:
        diffcon=0
def song_change(switch):
    global beatsel,beatnowmusic,diffcon,cross
    if not switch:
        if not beatsel-1<=-1:
            beatsel-=1
        else:
            beatsel=len(p2)-1
    else:
        if not beatsel+1>=len(p2):
            beatsel+=1
        else:
            beatsel=0
    beatnowmusic=1
    diffcon=0
    cross[1]=0
def diff_change(switch):
    global beatsel,beatnowmusic,diffcon,diffani
    if not switch:
        if not diffcon-1<=-1:
            diffcon-=1
        else:
            diffcon=len(diff)-1
    else:
        if not diffcon+1>=len(diff):
            diffcon+=1
        else:
            diffcon=0
    reloadstats()
    diffani=Tween(begin=cross[1], end=diffcon,duration=1500,easing=Easing.CUBIC,easing_mode=EasingMode.OUT)
    diffani.start()
def get_rank(num):
    #crok=256*oneperf
    crok=oneperf/2
    totrank=(crok+1)-int((num/oneperf)*crok)
    return int(totrank)
def reloadprofile():
    global totperf,totscore,totrank
#    for a in pend:
    f=requests.get(apiurl+'api/getstat?'+str(username)+'?full',headers={'User-Agent': 'QluteClient-'+str(gamever)},timeout=5)
    f=json.loads(f.text)
    totrank=int(f['rank'])
    totperf=int(f['points'])
    totscore=int(f['score'])
def ondemand():
    global totperf,totscore,totrank,nettick,issigned,qlutaerror,menunotice
    qlutaerror=True
    while True:
        if stop:
            exit()
        if int(time.time()-nettick)>9:
            if issigned:
                try:
                    reloadprofile()
                    if activity==4:
                        pre='Playing '
                    else:
                        pre='Listening to '
                    f=requests.get(apiurl+'api/setstatus?'+str(username)+'?playing?'+str(pre+str(beattitle)),headers={'User-Agent': 'QluteClient-'+str(gamever)},timeout=5)
                    f=f.text
                    menunotice=requests.get(apiurl+'api/menunotice',headers={'User-Agent': 'QluteClient-'+str(gamever)},timeout=5).text
                    qlutaerror=False
                except Exception as err:
                    totperf=0
                    totscore=0
                    totrank=0
                    menunotice='Server is Busy'
                    print(err)
                    #issigned=False
                    qlutaerror=True
            nettick=time.time()
        time.sleep(1/5)