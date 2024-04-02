gradecolour=(114, 180, 181),(114, 142, 179),(105, 173, 99),(113, 85, 173),(173, 136, 61),(168, 70, 50),(20,20,20)
def beatres():
    global activity,replaymen,butt
    if activity==5:
        if replaymen:
            title='Replay Screen'
        else:
            title='Results Screen'
        grade=accuracy
        if grade>=100:
            gradet='X'
            gc=gradecolour[0]
        elif grade>95 and not hits[3]:
            gradet='S'
            gc=gradecolour[1]
        elif grade>90:
            gradet='A'
            gc=gradecolour[2]
        elif grade>85:
            gradet='B'
            gc=gradecolour[3]
        elif grade>69:
            gradet='C'
            gc=gradecolour[4]
        elif grade<1:
            gradet='?'
            gc=gradecolour[-1]
        else:
            gradet='D'
            gc=gradecolour[5]
        scale=(w//800,h//600)
        scrop=(w//2-((100//2)*scale[0]),(h//2+50-((460//2)*scale[1])),100*scale[0],50*scale[1])
        pup=[hits[0],hits[1],hits[2],hits[3]]
        #render('rect',arg=((w//2-310,h//2-110,620,260),(100,100,150),False),borderradius=20)
        #render('rect',arg=((0,(h//2-((500//2)*scale[1])),w,500*scale[1]),(50,50,50),True),bordercolor=(30,30,30),borderradius=20)
        render('rect',arg=(scrop,gc,False),borderradius=20)
        render('text', text=gradet, arg=((0,0), forepallete,'grade','center'),relative=scrop)
        render('text', text=str(format(int(perf/maxperf*1000000),',')), arg=((0,0), forepallete,'grade','center'),relative=(scrop[0],scrop[1]+80,scrop[2],scrop[3]))
        render('text', text='pp - '+str(str(format(int(perf),',')))+'/'+str(str(str(format(maxperf,','))))+' Acc - '+str(accuracy)+'%', arg=((0,0), forepallete,'center'),relative=(w//2,h//2-30,0,0))
        render('text', text='300 - '+str(pup[0]), arg=((0,0), forepallete,'center'),relative=((w//2,h//2,0,0)))
        render('text', text='100 - '+str(pup[1]), arg=((0,0), forepallete,'center'),relative=((w//2,h//2+25,0,0)))
        render('text', text='50 - '+str(pup[2]), arg=((0,0), forepallete,'center'),relative=((w//2,h//2+50,0,0)))
        render('text', text='Miss - '+str(pup[3]), arg=((0,0), forepallete,'center'),relative=((w//2,h//2+75,0,0)))
        if not username=='Guest':
            render('text', text='Overall Rank - #'+str(format(totrank,',')), arg=((0,0), forepallete,'center'),relative=(w//2+160,h//2+95,0,0))
            render('text', text='Overall Points - '+str(format(totperf,',')), arg=((0,0), forepallete,'center'),relative=(w//2-150,h//2+95,0,0))
           # render('text', text='Ranked Score - '+str(format(totscore,',')), arg=((0,0), forepallete,'center'),relative=(scrop[0],scrop[1]+300,scrop[2],scrop[3]))
            changed=[totrank-prevrank,totperf-oldstats[0],totrank,totperf]
            klap=(w//2+195,h//2+105),(w//2-100,h//2+105)
            for a in range(1,3):
                #print(changed)
                cha=(255, 155, 128),(186, 255, 171)
                if changed[a-1]<0:
                    chap=''
                    if a==1:
                        chac=cha[1]
                    else:
                        chac=cha[0]
                elif changed[a-1]>0:
                    chap='+'
                    if a==1:
                        chac=cha[0]
                    else:
                        chac=cha[1]
                if changed[a-1]!=changed[1+a] and changed[a-1]!=0:
                    render('text', text=chap+str(format(changed[a-1],',')), arg=((klap[a-1]), chac))
        else:
            render('text', text='Hey, Your not Logged in yet!', arg=((0,0), forepallete,'center'),relative=(scrop[0],scrop[1]+270,scrop[2],scrop[3]))
            render('text', text='You can compete if you Log in :3', arg=((0,0), forepallete,'center'),relative=(scrop[0],scrop[1]+290,scrop[2],scrop[3]))

        render('text', text=title, arg=((20,20), forepallete))
        butt=menu_draw(((scrop[0]-90,scrop[1]+350,scrop[2]*3-20,scrop[3]),),('Continue',),styleid=2)