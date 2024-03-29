def logo():
    global activity,gameverfake,logoflashtime,kd,logopos
    if activity==0:
        #if time.time()-logotime>1.5:
        #    activity=1
        toka=((1.5-(time.time()-logotime))/1)*190
        render('clear',arg=(0,0,0))
        tmp=(delta/0.01)
        #print(tmp)
        if toka<=-32:
            transitionprep(1)
        else:
            logopos.update()
        gamepre='Welcome to '+gamename
        gamesuf=''
        titlelogo=(255*(logopos.value/100),255*(logopos.value/100),255*(logopos.value/100))
        render('text', text=gamepre+gamesuf, arg=((0,0), titlelogo,'center','grade'),relative=(w//2,h//2+(100-(100*(logopos.value/100))),1,1))
        render('text', text='Branch: '+str(gameedition), arg=((10,10), (255,255,0),'min'))
