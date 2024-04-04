import pygame
modsalias="Auto",'Blind','Slice','EZ','Random'#,'DT','HT'
modsaliasab='AT','BD','SL','EZ','RND'#,'DT','HT'
mods=''
def get_mods(bpos):
    global mods
    b=0
    tap=0
    mods=''
    for a in modsaliasab:
        if modsen[b]:
            pos=(bpos[0]+(15*tap),bpos[1])
            rec=icons[1].get_rect()
            screen.blit(icons[1],pos)
            mods+=a
            render('text', text=a, arg=((0,0), (0,0,0),'center'),relative=(pos[0],pos[1],rec[2],rec[3]))
            tap+=1
        b+=1
def beatmenu():
    global activity,beatsel,beatnowmusic,background,menuback,cross,diffcon,hits,modshow,mod,modsen,button,beatsel,speedvel,scoremult,msg,sysbutton,gobutton,go
    go=False
    if activity==3 or activity==7:
        beatani.update()
        diffani.update()
        try:
            if background:
                screen.blit(background, (0, 0))
        except Exception:
            background=0
        a=0
        tmp=(h//60)//2
        pp=int(int(getpoint(diffp[0][0],0,0,0,scoremult,combo=diffp[0][0]))),int(getpoint(diffp[-1][0],0,0,0,scoremult,combo=diffp[-1][0]))
        if len(diffp)<2 or activity==7:
            gotext='GO'
        else:
            gotext='>'
        if activity==7:
            soup=1
            sel=diffcon
            bp1=[]
            bp2=[]
            a=0
            for b in diff:
                bp1.append(((w//2-(cardsize//2),(h//2-size)-((size+5)*cross[1])+((size+5)*(a)),cardsize,size)))
                bp2.append(str(b[1]))
                a+=1
            button=menu_draw(bp1,bp2,selected_button=sel+1,startlimit=int(cross[1])-tmp+1,endlimit=int(cross[1])+tmp,styleid=1)
        else:
            soup=0
            sel=beatsel
            button=menu_draw(p1,p2,beatmenu=True,selected_button=sel+1,startlimit=int(cross[0])-tmp-1,endlimit=int(cross[0])+tmp+2,styleid=1)
        if len(p2)==0:
            crok=999
        else:
            crok=0
        sysbuttonpos=(-10,h-60,100+menuback,60),(140,h-50+crok,100,40),
        if modshow:
            render('rect', arg=((0,h-170,w,120), blend(opacity,0), False),borderradius=10)
            #(340,h-160,90,40) ~ Placeholder
            # This will be here for now, it WILL get better and more optimized over time
            t=(20,20,120,120,220,320,420,480)
            tm=[]
            for b in range(1,len(t)+1): # Ewwwwwww
                if (b == 2 and modsen[2]) or (b == 3 and modsen[1]):#modsen[3]
                    tm.append(-999)
                else:
                    tm.append(t[b-1])

            mod=menu_draw(((tm[0],h-160,90,40)
                           ,(tm[1],h-110,90,40)
                           ,(tm[2],h-160,90,40)
                           ,(tm[3],h-110,90,40)
                           ,(tm[4],h-160,90,40)
#                           ,(tm[5],h-160,90,40)
#                           ,(tm[6],h-160,90,40)
#                           ,(tm[7],h-160,90,40)
                           )
                           ,(modsalias),enabled_button=modsen)
            if mod==1:
                msg='view a "Perfect" play (0)'
            elif mod==2:
                msg="Beat to the rhythm (+1.5)"
            elif mod==3:
                msg='Half blind (+0.5)'
            elif mod==4:
                msg="makes everything easy (/0.5)"
            elif mod==5:
                msg='Adds new fun! (0)'
            elif mod==6:
                msg='Double the fun (+0.5)'
            elif mod==7:
                msg='We be easy on you (/0.5)'
        else:
            mod=0
            get_mods((150,h-110))
        render('rect', arg=((0,h-60,w,60), blend(opacity,0), False))
#        for systrocity in sysbuttonpos:
#            render('rect', arg=((systrocity), (100,100,150), True),bordercolor=(80,80,100),borderradius=10)
        gobutton=menu_draw(((w-125,h-80+crok,120,70),),(gotext,),bigmode=True,styleid=1)
        if scoremult==1:
            m='Mods'
        else:
            m=str(scoremult)+'x'
        sysbutton=menu_draw(sysbuttonpos,('Back',m),styleid=1)
        render('rect',arg=((0,h-5,w,5),blend(-opacity,0),False))
        if not qlutaerror:
            render('rect',arg=((w//2-155,(h-90),310,100),blend(-opacity,0),False),borderradius=10)
            render('rect',arg=((w//2-150,(h-75),300,75),blend(-opacity,0),False))
            print_card(totperf,totscore,username,(w//2-150,(h-85)),totrank)
#        if ranktype and not ranktype==3:
#            if not modshow:
#                of=110
#            else:
#                of=0
#            render('rect', arg=((40,h-200+of,250,25), blend(opacity//2,0), False),borderradius=5)
#            render('text', text='You will not earn Points', arg=((0,0), forepallete,"center"),relative=(40,h-200+of,250,25))
        cross[0]=beatani.value
        cross[1]=diffani.value
        if sysbutton==1:
            if not menuback>=30:
                menuback+=backspeed
        else:
            if not menuback<=0:
                menuback-=backspeed
        freeze=0
        tmp=0
        render('header')
        hax=300//2
        popupw=w//2-hax
        if len(p2)==0:
            render('text', text='No Beatmap added :sad:', arg=(offset, forepallete))
        else:
            diffpos=(popupw+20+hax,140)
            #pass#int(len(objects)*perfbom*scoremult)
            render('text', text=beattitle, arg=(offset, forepallete))
            render('rect',arg=((popupw,70,hax*2,110),blend(opacity,0),False),borderradius=20)
            render('text', text=rankmodes[ranktype][0], arg=((popupw+20+hax,80), rankmodes[ranktype][1])) # Rank Type
            if pp[0]!=pp[1]:
                render('text', text=str(pp[0])+'-'+str(pp[1])+'pp', arg=((popupw+20+hax,110), forepallete))
            render('text', text='BPM: '+str(int(60000/bpm)+1), arg=((popupw+20,80), forepallete))
            render('text', text='Lv. '+str(lvrating), arg=((popupw+20,145), forepallete))
            render('text', text=f'+{format(maxperf,',')}pp', arg=((popupw+20,110), forepallete))
            render('rect', arg=((diffpos[0]-(bgcolour//2),diffpos[1],100+bgcolour,30), (levelcol[0]-20,levelcol[1]-20,levelcol[2]-20), False),borderradius=10)
            render('rect', arg=((diffpos[0],diffpos[1],100,30), levelcol, False),borderradius=10)
            render('text', text=levelrating, arg=((0,0), forepallete,"center"),relative=(diffpos[0],diffpos[1],100,30))
            if pygame.Rect(0,(h//4),45,h//2).collidepoint(pygame.mouse.get_pos()):
                t=0
            else:
                t=225
            if 1==1:
                s=310
                c=0
                render('rect', arg=((220-t,(h//2)-(s//2),45,s), blend(opacity,25), False),borderradius=10)
                render('rect', arg=((-10-t,(h//2)-(s//2),250,s), blend(opacity,0), False),borderradius=10)
                for a in leaderboard[:5]:
                    if a['username']==username:
                        col=166, 207, 255
                    else:
                        col=forepallete
                    leadpos=(10-t,(10+((h//2)-(s//2)))+(60*c),220,50)
                    render('rect', arg=(leadpos, blend(opacity,50), False),borderradius=10)
                    render('text', text=str('#'+str(c+1)+' '+a["username"]), arg=((17-t,leadpos[1]+5), col))
                    render('text', text=f'{format(int(a['score']),',')} - {str(int(a["points"]))}pp ({str(int(a['combo']))}x) {timeform(int(time.time()-a['time']))}', arg=((17-t,leadpos[1]+30), col,'min'))
#                    render('text', text=, arg=((17,leadpos[1]+28), col,'min'))
                    #(((hits[0]*perfbom)+(hits[1]*(perfbom/2))+(hits[2]*(perfbom/3)))*scoremult)-(hits[3]*(perfbom*2))
                    c+=1
def timeform(t):
    if t==None:
        return 'Never Played'
    if t>=31536000:
        x=int(t//31536000)
        fix='yr'
    elif t>=2630000:
        fix='m'
        x=int(t//2630000)
    elif t>=86400:
        x=int(t//86400)
        fix='d'
    elif t>=3600:
        x=int(t//3600)
        fix='h'
    elif t>=60:
        x=int(t//60)
        fix='m'
    elif t<60:
        x=int(t)
        fix='s'
    return str(x)+fix
def preparemap():
    global beatnowmusic
    beatnowmusic=1
    resetscore()
    transitionprep(4)
