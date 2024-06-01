def gameedit():
    global sysbutton
    if activity==9:
        render('rect', arg=((0,0,w,h), (20,20,20), False))
        render('rect', arg=((0,h-60,w,60), hcol[0], False))
#        render('rect', arg=((0,0,w,120), hcol[0], False))
#        render('rect', arg=((-10,100,w+20,20), (40,40,40), True))
        render('text', text='Edit is not implemented', arg=((20,20), forepallete,'grade','center'),relative=(0,0,w,h))
        #sysbutton=menu_draw(((-10,h-60,100,60),(w-100,h-60,100,60),),('Back','Test'),bradius=0,styleid=3)
        sysbutton=menu_draw(((-10,h-60,100,60),),('Back',),bradius=0,styleid=3)