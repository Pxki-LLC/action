shopref=1
sbt=[]
sbid=0
shopscroll=0
bgs=pygame.Surface((0,0))
downloadqueue=[]
def reload_background():
    global bgs
    bgs=pygame.Surface((0,0))
    bgst=requests.get(sentry[sbid-1]['covers']['card'],headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'},timeout=3)
    bgst=bgst.content
    bgst=io.BytesIO(bgst)
    bgst=pygame.image.load(bgst).convert_alpha()
    bgs=pygame.transform.scale(bgst, (350,180))

def shop_refresh():
    global sbt,sentry
    f = requests.get(beatmapapi+'search?limit=100',headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'},timeout=3)
    f=f.json()['found']
    sentry=f
    tmp=[]
    tick=0
    for a in sentry:
        if a['beatmaps'][0]['mode']=='mania':
            print(a['artist']+' - '+a['title']+' - '+a['beatmaps'][0]['mode'])
            tmp.append(a['artist']+' - '+a['title'])
        else:
            print('Not a mania map',time.time(),a['artist']+' - '+a['title']+' - '+a['beatmaps'][0]['mode'])
            del sentry[tick]
        tick+=1
    sbt=tmp
def downloads():
    global sysbutton,dq,dqs
    if activity==12:
        dq=[]
        dqu=[]
        for a in downloadqueue:
            dqu.append('Downloading - '+str(a[0]))
        render('rect', arg=((0,100,w,h-160), hcol[2], False))
        for a in range(1,len(downloadqueue)+1):
            dq.append(((w//2)-200,shopscroll+100+(80*(a-1)),400,80))
        dqs=menu_draw(dq,dqu,bradius=0,styleid=3,selected_button=sbid)
        render('rect', arg=((0,0,w,100), hcol[0], False))
        render('rect', arg=((0,h-60,w,60), hcol[0], False))
        render('text', text='Downloads', arg=((20,20), forepallete,'grade'))
        sysbutton=menu_draw(((-10,h-60,100,60),),('Back',),bradius=0,styleid=3)

def shopdirect():
    global activity,shopref,sysbutton,shopbutton
    if activity==6:
        if shopref:
            threading.Thread(target=shop_refresh).start()
            shopref=0
        render('rect', arg=((0,100,w,h-160), hcol[2], False))
        sb=[]
        for a in range(1,len(sbt)+1):
            sb.append((400*((w/800)-1),shopscroll+100+(80*(a-1)),400,80))
        shopbutton=menu_draw((sb),(sbt),bradius=0,styleid=3,selected_button=sbid)
        render('rect', arg=((0,h-60,w,60), hcol[0], False))
        render('rect', arg=((0,0,w,100), hcol[0], False))
        render('rect', arg=((w-400,100,400,h-160), hcol[1], False))
        render('text', text='Browse', arg=((20,20), forepallete,'grade'))
        if len(sb):
            render('rect', arg=((0,100,10,h-160), (80,80,80), False))
            t=(-shopscroll/-(80*(len(sbt)-1)))*((h-160)-((h-180)//len(sb)))
            render('rect', arg=((0,100-t,10,(h-180)//len(sb)), hcol[0], False))
        if sbid:
            crok=0
            entry=sentry[sbid-1]
            rank=getrank(entry['ranked'])
            render('rect', arg=((w-400+25,120,350,180), hcol[0], False))
            screen.blit(bgs,(w-400+25,120))
            render('text', text=entry['title'], arg=((w-400+25,335), forepallete))
            render('text', text=entry['artist'], arg=((w-400+25,360), forepallete))
            #render('text', text=entry['creator'], arg=((w-400+25,360), forepallete))
            render('text', text='BPM:'+str(entry['bpm'])+' - '+str(getpoint(entry['beatmaps'][0]['max_combo'],0,0,0,1,combo=entry['beatmaps'][0]['max_combo']))+'pp - '+clockify(entry['beatmaps'][0]['total_length']), arg=((w-400+25,310), forepallete))
            render('rect', arg=((w-400+30,250,100,40), rankmodes[rank][1], False),borderradius=10) # type: ignore
            render('text', text=rankmodes[rank][0], arg=((0,0), forepallete,'center'),relative=(w-400+30,250,100,40))
            print_card(0,0,entry['creator'],(w-400+25,390),0,hide=True) # type: ignore
        else:
            crok=999
        if sbid and entry['beatmaps'][0]['mode']!='mania':
            crok=999
            render('text', text='Beatmap not supported on '+gamename, arg=((w-400+25,470), forepallete))

        sysbutton=menu_draw(((-10,h-60,100,60),(w-140,crok+h-60,140,60)),('Back','Download'),bradius=0,styleid=3)