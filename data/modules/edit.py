def gameedit():
    global sysbutton
    if activity==9:
        render('rect', arg=((0,120,w,h-180), (20,20,20), False))
        render('rect', arg=((0,h-60,w,60), hcol[0], False))
        render('rect', arg=((0,0,w,120), hcol[0], False))
        render('rect', arg=((-10,100,w+20,20), (40,40,40), True))
        render('text', text='Edit Concept', arg=((20,20), forepallete,'grade'))
        sysbutton=menu_draw(((-10,h-60,100,60),(w-100,h-60,100,60),),('Back','Test'),bradius=0,styleid=3)