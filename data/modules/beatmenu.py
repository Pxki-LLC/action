import pygame
modsalias="Auto",'Blind','Slice','EZ','Random','Multi'
modsaliasab='AT','BD','SL','EZ','RND','MP'
def get_mods(bpos):
    b=0
    tap=0
    for a in modsaliasab:
        if modsen[b]:
            pos=(bpos[0]+(15*tap),bpos[1])
            rec=icons[1].get_rect()
            screen.blit(icons[1],pos)
            render('text', text=a, arg=((0,0), (0,0,0),'center'),relative=(pos[0],pos[1],rec[2],rec[3]))
            tap+=1
        b+=1
def beatmenu():
    global activity,beatsel,beatnowmusic,menuback,cross,diffcon,hits,modshow,mod,modsen,button,beatsel,speedvel,scoremult,msg,sysbutton,gobutton,go
    go=False
    if activity==3 or activity==7:
        screen.blit(background, (0, 0))
        a=0
        tmp=(h//60)//2
        if activity==7:
            soup=1
            sel=diffcon
            bp1=[]
            bp2=[]
            a=0
            for b in diff:
                bp1.append(((w//2-(cardsize//2)-((size+5)*cross[1])+((size+5)*(a)),(h//2-size)-((size+5)*cross[1])+((size+5)*(a)),cardsize,size)))
                bp2.append(str(b[1]))
                a+=1
            button=menu_draw(bp1,bp2,selected_button=sel+1,startlimit=int(cross[1])-tmp+1,endlimit=int(cross[1])+tmp,styleid=1)
        else:
            soup=0
            sel=beatsel
            button=menu_draw(p1,p2,selected_button=sel+1,startlimit=int(cross[0])-tmp-1,endlimit=int(cross[0])+tmp+2,styleid=1)
        if len(p2)==0:
            crok=999
        else:
            crok=0
        sysbuttonpos=(-10,h-60,100+menuback,60),(140,h-50+crok,100,40),
        if modshow:
            render('rect', arg=((0,h-200,500,43), blend(opacity,20), False),borderradius=10)
            render('rect', arg=((0,h-170,500,120), blend(opacity,0), False),borderradius=10)
            mod=menu_draw(((20,h-160,90,40),(20,h-110,90,40),(130,h-160,90,40),(130,h-110,90,40),(230,h-160,90,40),(340,h-160,90,40)),(modsalias),enabled_button=modsen)
            render('text', text=str(scoremult)+'x', arg=((20,h-195), forepallete))
            if mod==1:
                msg='view a "Perfect" play'
            elif mod==2:
                msg="i can't see anything"
            elif mod==3:
                msg='Half blind'
            elif mod==4:
                msg="makes everything easy"
            elif mod==5:
                msg='Adds new fun!'
            elif mod==6:
                msg='Enable Leaderboard'
        else:
            mod=0
            get_mods((150,h-110))
        render('rect', arg=((0,h-60,w,60), blend(opacity,0), False))
#        for systrocity in sysbuttonpos:
#            render('rect', arg=((systrocity), (100,100,150), True),bordercolor=(80,80,100),borderradius=10)
        gobutton=menu_draw(((w-125,h-80+crok,120,70),),("->",),bigmode=True,styleid=1)
        sysbutton=menu_draw(sysbuttonpos,('Back','Mods'),styleid=1)
        render('rect',arg=((0,h-5,w,5),blend(-opacity,0),False))
        if not qlutaerror:
            render('rect',arg=((w//2-155,h-90,310,100),blend(-opacity,0),False),borderradius=10)
            render('rect',arg=((w//2-150,h-75,300,75),blend(-opacity,0),False))
            print_card(totperf,totscore,username,(w//2-150,h-85),totrank)
#        if ranktype and not ranktype==3:
#            if not modshow:
#                of=110
#            else:
#                of=0
#            render('rect', arg=((40,h-200+of,250,25), blend(opacity//2,0), False),borderradius=5)
#            render('text', text='You will not earn Points', arg=((0,0), forepallete,"center"),relative=(40,h-200+of,250,25))
        speed=speedvel[soup]
        if cross[soup]>sel-0.01 and cross[soup]>sel+0.01:
            cross[soup]-=speed
            speedvel[soup]+=0.1*drawtime
        elif int(round(cross[soup]))<sel:
            cross[soup]+=speed
            speedvel[soup]+=0.1*drawtime
        else:
            speedvel[soup]=0
        if sysbutton==1:
            if not menuback>=30:
                menuback+=backspeed
        else:
            if not menuback<=0:
                menuback-=backspeed
        freeze=0
        tmp=0
        if maxperf>=1000:
            beatcol=rankdiffc[-1]
        elif maxperf>=800:
            beatcol=rankdiffc[3]
        elif maxperf>=80:
            beatcol=rankdiffc[2]
        elif maxperf>=31:
            beatcol=rankdiffc[1]
        elif maxperf<=30:
            beatcol=rankdiffc[0]
        beatname=rankdiff[rankdiffc.index(beatcol)]
        render('header')
        hax=300*(w//600)
        popupw=w//2-hax
        if len(p2)==0:
            render('text', text='No Beatmap added :sad:', arg=(offset, forepallete))
        else:
            diffpos=(popupw+20+hax,130)
            #pass#int(len(objects)*perfbom*scoremult)
            render('text', text=beattitle, arg=(offset, forepallete))
            render('rect',arg=((popupw,40,hax*2,130),blend(opacity,0),False),borderradius=20)
            render('text', text=rankmodes[ranktype][0], arg=((popupw+20+hax,70), rankmodes[ranktype][1])) # Rank Type
            render('text', text=str(int(int(diffp[0][0])*perfbom*scoremult))+'-'+str(int(int(diffp[-1][0])*perfbom*scoremult))+'pp', arg=((popupw+20+hax,100), forepallete))
            render('text', text='BPM - '+str(int(60000/bpm)+1), arg=((popupw+20,70), forepallete))
            render('text', text='Lv '+str(round(maxperf*0.123,2)), arg=((popupw+20,135), forepallete))
#            render('text', text=str(beatmapsetid)+' / '+str(beatmapid), arg=((popupw+20,135), forepallete))
            render('text', text='Max pp - '+str(format(maxperf,',')), arg=((popupw+20,100), forepallete))
            render('rect', arg=((diffpos[0]-(bgcolour//2),diffpos[1],140+bgcolour,30), (beatcol[0]-20,beatcol[1]-20,beatcol[2]-20), False),borderradius=10)
            render('rect', arg=((diffpos[0],diffpos[1],140,30), beatcol, False),borderradius=10)
            render('text', text=beatname, arg=((0,0), forepallete,"center"),relative=(diffpos[0],diffpos[1],140,30))
def preparemap():
    global beatnowmusic
    beatnowmusic=1
    resetscore()
    transitionprep(4)
