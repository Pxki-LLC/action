textboxid=0
logintext=['','']
restricted=0
maxletters=30
profilehealth=0
restrictedmsg='Your account has been restricted, You are not able to use any online features at this state'
def loginscreen():
    global sysbutton,l,logbutton
    if activity==10:
        render('rect', arg=((0,0,w,h), (20,20,20), False))
        render('rect', arg=((0,h-60,w,60), hcol[0], False))
        render('text', text='Login', arg=((20,20), forepallete,'grade'))
        if restricted:
            logbutton=0
            render('text', text='Your client has been locked!', arg=((20,80), forepallete))
            render('text', text=restrictedmsg, arg=((20,110), forepallete,'min'))
        else:
            if issigned:
                render('text', text='You are logged in as '+str(settingskeystore['username']), arg=((20,80), forepallete))
                logbutton=menu_draw(((w//2-50,h//2+90,100,25),),('Log out',),bradius=15,styleid=3)
            else:
                if textboxid:
                    l=[(255,255,255),(105,255,105)]
                else:
                    l=[(105,255,105),(255,255,255)]
                id=0
                for a in logintext:
                    if len(a)>=maxletters:
                        logintext[id]=logintext[id][:maxletters]
                    id+=1
                render('text', text='Username:', arg=((w//2-300,h//2-80), forepallete))
                render('text', text='Password: ('+format(len(logintext[1]),',')+' Characters)', arg=((w//2-300,h//2), forepallete))
                render('rect', arg=((w//2-300,h//2-50,600,40), (40,40,40), True),bordercolor=l[0])
                render('rect', arg=((w//2-300,h//2+30,600,40), (40,40,40), True),bordercolor=l[1])
                render('text', text=logintext[0], arg=((w//2-290,h//2-40), forepallete))
                render('text', text='*'*len(logintext[1]), arg=((w//2-290,h//2+40), forepallete))
                render('text', text='Login', arg=((20,20), forepallete,'grade'))
                render('text', text='For new users, please vist our site to sign up', arg=((20,80), forepallete))
                logbutton=menu_draw(((w//2-150,h//2+90,100,25),(w//2+20,h//2+90,100,25),),('Log in','Sign Up'),bradius=15,styleid=3)
        sysbutton=menu_draw(((-10,h-60,100,60),),('Back',),bradius=0,styleid=3)
