def song_progress():
    slop=(gametime/lastms)
    if slop>1:
        slop=1
    render('rect', arg=((10,h-20,w-20,10), (50,50,50), False),borderradius=10)
    render('rect', arg=((10,h-20,slop*(w-20),10), (255,255,255), False),borderradius=10)
def iscatched(block,isauto,ob,fir,id):
    lean=(perfect,great,ok,miss)
    tick=0
    if ob==fir:
        agree=True
    else:
        agree=False
    if block>=h-lean[3]:
        lastcall=True
        tick=3
    elif block>=keymap[0][1]-lean[0] and block<=keymap[0][1]+keymap[0][3]+lean[0] and agree:
        lastcall=True
        tick=0
    elif block>=keymap[0][1]-lean[1] and block<=keymap[0][1]+keymap[0][3]+lean[1] and not isauto and agree:
        lastcall=True
        tick=1
    elif block>=keymap[0][1]-lean[2] and block<=keymap[0][1]+keymap[0][3]+lean[2] and not isauto :
        lastcall=True
        tick=2
    else:
        lastcall=False
    tim=block
    return (lastcall,tick,tim)
def game():
    global activity,debugmode,beatnowmusic,kiai,unstablerate,fpsmode,score,scorew,keyspeed,bgcolour,totperf,totscore,objecon,healthtime,health,ranking,oldupdatetime,t,tip,gametime,combo,sre,combotime,sre,hits,last,stripetime,tmp,pptime,pptmp,ppcounter,perf
    if activity==4:
        if bgcolour>=1:
            bgcolour-=1
        playfield=(maxt(20,bgcolour),maxt(20,bgcolour),maxt(20,bgcolour))
        screen.fill(playfield)
        tmp=0.1
        sretemplate=(tmp-(time.time()-combotime))/tmp
        sre=(sretemplate)*20
        if sre<=0:
            sre=0
        #if reall<0:
        #    pygame.mixer.music.play(-1,0)

        b=0
        perf=(((hits[0]*perfbom)+(hits[1]*(perfbom/2))+(hits[2]*(perfbom/3))-(hits[3]*(perfbom*2)))*scoremult)
        accuracy=((maxperf-(hits[1]*(perfbom/2))-(hits[2]*(perfbom/3))-(hits[3]*(perfbom*2)))/maxperf)*100
        #accuracy=100
        if int(maxperf)!=0:
            end=(perf/maxperf)
        else:
            end=0
        if health<0:
            health=100
            transitionprep(3)
        elif health>=110:
            health=110
        t1=0.01
        maxt1=0.15
        if combo!=0:
            t1=t1*combo
        if t1>=maxt1:
            t1=maxt1
        reall=int(gametime)
        ob=0
        temp=h//2+reall
        render('rect', arg=((keymap[0][0],keymap[0][1]-10,keymap[0][2]*4,10), (100,140,220), False),borderradius=0)
        for a in keys:
            mopa=(0.1-(time.time()-keyslight[b]))/0.1
            if mopa<0:
                mopa=0
            co=(100,int(100+(20*mopa)),int(100+(120*mopa)))
            render('rect', arg=(keymap[b], co, False),borderradius=0)
            render('line',arg=((keymap[b][0],0),(255,255,255),(keymap[b][0],keymap[b][1]+keysize)))
            b+=1
        render('line',arg=((keymap[3][0]+100,0),(255,255,255),(keymap[3][0]+100,keymap[3][1]+keysize)))
        clicked=0
        hit=-1
        tip=1
        hidden=0
        for a in objects[objecon:maxobjec+objecon]:
            tok=a.split(',')
            #if tok[2]==firstobject:
            block=temp-(int(tok[2]))+(h//2)
            if (block <=h+100 and block>=-40 and not modsen[2]) or (block <=h+100 and block>=h//2 and modsen[2]):
                if ob==0:
                    if not end*1000000 >=999000 and (modsen[0] and health>1):
                        health-=t1
                ob+=1
                if ob==1:
                    #if not keys:
                    firstobject=int(block)
                notfound=True
                for kik in range(1,len(pos)+1):
                    if int(tok[0])==pos[kik-1]:
                        keypos=keymap[kik-1][0]
                        notfound=False
                        break
                if notfound:
                    for a in range(1,6):
                        if a-1>=4:
                            ax=3
                        else:
                            ax=a-1
                        if int(tok[0])>=512-(128*(a-1)):
                            keypos=keymap[ax][0]
                            break
#                if modsen[1]:
#                    notecolour=(mint(int(playfield[0]),int((500/block)*48)), mint(int(playfield[1]),int((500/block)*183)), mint(int(playfield[2]),int((500/block)*255)))
#                else:
                notecolour=(48, 183, 255)
                if not (keypos,int(tok[2])) in barclicked:
#                    if not modsen[1]:
#                        if tip:
#                            render('rect', arg=((keypos,block-30,100,30), (255,0,0), False),borderradius=0)
#                        else:
                    render('rect', arg=((keypos,block-30,100,30), (notecolour), False),borderradius=0)
                    #render('text',text=block,arg=((keypos,block-30),(255,255,255)))
                    tip=0
                judge=iscatched(block,modsen[0],block,firstobject,ob)
                if modsen[0]:
                    if judge[0]:
                        keys[kik-1]=1
                        keyslight[kik-1]=time.time()
                    else:
                        keys[kik-1]=0
                if (judge[0] and keys[kik-1]) or judge[1]==3: 
                    hit=judge[1]
                    clicked=1
                    if keys[kik-1]:
                        keys[kik-1]=0
                    stripetime.append((keypos,int(tok[2])))
                    #print((keypos,int(tok[2])))
                if pygame.Rect.colliderect(pygame.Rect(0,h+45,w,20),pygame.Rect(keypos,block,100,30)):
                    objecon+=1
            #print(time.time(),firstobject,tok[2])
        if clicked:
            for notes in stripetime:
                if not (notes[0],int(notes[1])) in barclicked:
                    if hit==3:
                        health-=t1
                    else:
                        health+=10
                    hits[hit]+=1
                    bgcolour+=1
                    barclicked.append((notes[0],int(notes[1])))
                    ton=(time.time(),hit)
                    unstablerate.append(ton)
                    if not hit==3:
                        combo+=1
                        combotime=time.time()
                        t=a.split(':')[-1]
                        if not t=='' and settingskeystore[4]:
                            pygame.mixer.Sound(gamepath+realid+'/'+str(t)).play()
                            print('Played',t)
                    else:
                        combotime=time.time()
                        combo=0
                        health-=t1
            stripetime=[]
        
        if modsen[5]:
            players=1
            t=1
            playboard[len(playboard)-1]=(username,(255,255,0),int(end*1000000))
            for tmp in sorted(playboard, key=lambda x: x[2],reverse=True):
                if tmp[0]==username:
                    pcolor=(50,50,150)
                else:
                    pcolor=(50,50,100)
                if tmp[0]==username:
                    ranking=players
                if ranking>=players-3 and ranking<=players+3:
                    render('rect', arg=((-30,65+(50*(t)),225,50), pcolor, False),borderradius=20)
                    #render('text',text='#'+str(players),arg=((20, 80+(50*(t))),(pcolor[0]-20,pcolor[1]-20,pcolor[2]-20)))
                    render('text',text=tmp[0],arg=((20, 70+(50*(t))),tmp[1])) #'#'+str(players)+' '+
                    render('text',text='#'+str(players)+' '+str(tmp[2]),arg=((20, 95+(50*(t))),tmp[1],'min'))
                    t+=1
                players+=1
        if end*1000000<0:
            t=(255,0,0)
        else:        
            t=forepallete
        render('rect', arg=((0,-20,w,55), (50,50,60), False),borderradius=20)
        render('rect', arg=((w//2-200,19,401,61), (50,50,80), False),borderradius=20)
        render('text',text=format(int(end*1000000),','),arg=((20, 20),t,'grade','center'),relative=(w//2-200,22,400,60))
        render('text',text='Acc - '+str(accuracy)+'%',arg=((20, 170),forepallete,'center'),relative=(w//2-200,82,400,20))
        if combo!=0:
            kek=(keymap[0][0],100,400,100)
            comboo=str(format(int(combo),','))
            if sre:
                render('text',text=comboo,arg=((0,0),(255,0,0),'grade','center'),relative=(kek[0]-sre,kek[1],kek[2],kek[3]))
                render('text',text=comboo,arg=((0,0),(0,0,255),'grade','center'),relative=(kek[0]+sre,kek[1],kek[2],kek[3]))
                render('text',text=comboo,arg=((0,0),(0,255,0),'grade','center'),relative=(kek[0],kek[1]+sre,kek[2],kek[3]))
            render('text',text=comboo,arg=((0,0, h-80-sre),forepallete,'grade','center'),relative=kek)
        #render('text',text=h//2+reall-(int(objects[0].split(',')[2])),arg=((20, 80),forepallete))
        render('text',text=str(hits),arg=((20, 130),forepallete))
        render('line',arg=((0,h-miss),(255,255,255),(w,h-miss)))
        render('text',text='pp - '+str(perf),arg=((20, 150),forepallete))
#        render('text',text='Key Speed: '+str(keyspeed)+' ('+str(0)+'ms)',arg=((20, 70),forepallete))
        render('rect', arg=((w//2-200,5,400,10), (20,20,20), False),borderradius=10)
        #render('rect', arg=((w//2-200,50,((maxscore-score)/maxscore)*400,20), (255,0,0), True),borderradius=10)
        tmp=(health/100)*400
        if tmp<0:
            tmp=0
        elif tmp>400:
            tmp=400
        render('rect', arg=((w//2-200,5,tmp,10), (0,180,0), False),borderradius=10)
        fon=0
        for a in timings[::-1]: # 7 == Kiai
            tim=a.split(',')
            if reall>=int(tim[0]) and not fon:
                if int(tim[7])==1:
                    kiai=1
                else:
                    kiai=0
                fon=1
          #  tim=temp-(int(tim[0]))+(h//2)
            #if tim <=h+100 and tim>=-40:
#                render('rect', arg=((keymap[0][0]-keymap[0][2],tim,keymap[0][2]*6,5), (255,255,255), False),borderradius=20)
        b=0
        for a in unstablerate[::-1]:
            if time.time()-a[0]>0.5:
                unstablerate.remove(a)
            if b>16:
                break
            else:
                render('rect', arg=((keymap[3][0]+110,keymap[0][1]-50-(25*b),20*(1+b),20), hitcolour[a[1]], False))
                render('rect', arg=((keymap[0][0]-30-(20*(b)),keymap[0][1]-50-(25*b),20*(b+1),20), hitcolour[a[1]], False))
                b+=1
            
#        tmp=end*400
#        if tmp<0:
#            tmp=0
#        elif tmp>400:
#            tmp=400
#        render('rect', arg=((w//2-200,5,tmp,10), (0,150,0), False),borderradius=10)
#        for a in range(1,len(keys)+1):
#            if keys[a-1]:
#                keys[a-1]=0
        song_progress()
        if  gametime>=lastms+1000:# or combo>49:
            render('rect', arg=((0,h//2-50,w,100), (255,255,255), False))
            render('text',text='Loading...',arg=((20, 20),(0,0,0),'grade','center'),relative=(w//2-100,h//2-50,200,100))
            pygame.display.update()
            print('Completed')
            if 1==1:
                submit_score(perf,combo,other=str(beatmapid)
                             +';'+str(hits[0])+';' # PERFECT / OUTRAGOUS
                             +str(hits[1])+';' #GREAT
                             +str(hits[2])+';' # OK
                             +str(hits[3])+';' # BAD
                             +str(diffmode)+';' # Difficulty
                             +str(scoremult)+';' # More Points yas
                             +str(maxperf)+';' # Max Points
                             +str(int(time.time()-timetaken)))
            transitionprep(5)

