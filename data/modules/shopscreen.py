def shopdirect():
    global activity
    if activity==6:
        render('rect', arg=((0,100,w,h-160), hcol[2], False))
        render('rect', arg=((0,h-60,w,60), hcol[0], False))
        render('rect', arg=((0,0,w,100), hcol[0], False))
        render('rect', arg=((w//2,100,w//2,h-160), hcol[1], False))
        render('text', text='Browse', arg=((20,20), forepallete,'grade'))
        sysbutton=menu_draw(((-10,h-60,100,60),),('Back',),bradius=0,styleid=3)