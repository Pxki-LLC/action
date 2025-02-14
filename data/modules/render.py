hcol=(62,60,115),(42,40,95),(22,20,75),(82,80,135)
notewidth=100
noteheight=30
def render(type, arg=(0, 0) ,  text='N/A', bordercolor=forepallete, borderradius=0,relative=(0,0,0,0),surf=''):
    off=0
    grad2=False
    if surf=='':
      surf=screen
    try:
        bordercolor=mint(bordercolor[0],darkness),mint(bordercolor[1],darkness),mint(bordercolor[2],darkness)
        try:
            colour=mint(arg[1][0],darkness),mint(arg[1][1],darkness),mint(arg[1][2],darkness)
        except Exception:
            colour=mint(arg[1],darkness)
        relative=pygame.Rect(relative)
        if type == 'text':
            if "bold" in arg:
                ftype=3
            elif "min" in arg:
                ftype=1
            elif "grade" in arg:
                ftype=2
            else:
                ftype=0
            tmp = fonts[ftype].render(str(text),  True,  colour)
            txtrect=tmp.get_rect()
            if "center" in arg:
                out = tmp.get_rect(center=relative.center)
            else:
                out=arg[0]
                if "rtl" in arg:
                    out=out[0]-txtrect[2],out[1]
            if "tooltip" in arg:
                render('rect', arg=((out[0]-2,out[1]-2,txtrect[2]+4,txtrect[3]+4), (50,50,50), False),borderradius=5)
            surf.blit(tmp,  out)
            return tmp.get_rect()
        elif type == 'clear':
            screen.fill(arg)
        elif type == 'line':
            pygame.draw.line(surf,colour,arg[0],arg[2])
        elif type == 'rect':
#			print(arg[0][0], arg[0][1], arg[0][2], arg[0][3])
            pygame.draw.rect(surf, colour, (arg[0][0], arg[0][1], arg[0][2]-off, arg[0][3]-off), border_radius=borderradius)
            if arg[2]:
                pygame.draw.rect(surf, bordercolor, (arg[0][0], arg[0][1], arg[0][2]-off, arg[0][3]-off), 1, border_radius=borderradius)
            ## This was for a "Wireframe" Like Square
#            pygame.draw.rect(screen, (0, 255, 0), (arg[0][0], arg[0][1], arg[0][2], arg[0][3]), 1)
        elif type == 'header':
            render('rect', arg=((0, -40, w, 110), hcol[1], False), borderradius=20)
            render('rect', arg=((0, -40, w, 105), hcol[0], False), borderradius=20)
            render('rect',arg=((0,0,w,5),hcol[1],False))
        else:
            crash('Render unsupported Type')
    except Exception as error:
        print(error)
        exit()
        crash(str(error)+' (renderer)')
def menu_draw(instruction, text=None,showicon=False,bradius=10,settings=False,beatmenu=0,ishomemenu=False,ignoremove=False, istextbox=False, selected_button=0,enabled_button=[],enable_border=False, hidebutton=False,bigmode=False,startlimit=1,endlimit=None,styleid=1,isblade=False,icon=0):
    global osam
    if endlimit==None:
        endlimit=len(instruction)
    elif endlimit>=len(instruction):
        endlimit=len(instruction)
    if startlimit<1:
        startlimit=1
    button=0
    if istextbox:
        button=0, 0, 0
    else:
        if settings or styleid==3:
            buttonc=82,80,135
            tcol=forepallete
        elif styleid==0:
            buttonc=30, 100, 120
            tcol=255,255,255
        elif styleid==1:
            buttonc=bgdefaultcolour[0]+15,bgdefaultcolour[1]+15,bgdefaultcolour[2]+15
            tcol=255,255,255
        elif styleid==2:
            buttonc=219, 219, 219
            tcol=0,0,0
    select=False
    for a in range(startlimit,  endlimit+1):	
        tmp=instruction[a-1]
        if not beatmenu:
            tmp=pygame.Rect(tmp[0],tmp[1],tmp[2],tmp[3])
        else:
            size=65
            tmp=pygame.Rect(w//2-tmp[0],(h//2)-tmp[1]-((size+5)*cross[0])+((size+5)*(a-1)),tmp[2],tmp[3])
        if tmp.collidepoint(pygame.mouse.get_pos()) and not select:
            select=True
            buttcolour = (buttonc[0]+10,buttonc[1]+10,buttonc[2]+10)
            if pygame.mouse.get_focused():
                button=a
                if osam!=button:
                    osam=button
                    pygame.mixer.Sound(samplepath+'hover.wav').play()
            else:
                osam=0
        else:
            buttcolour = buttonc
        b = (102,100,175)
        #drawRhomboid(screen, (255,255,255), 50, 50, 300, 200, 100, 3)
        if not hidebutton:
            if not isblade:
                if selected_button==a or (enabled_button!=[] and enabled_button[a-1]):
                    buttcolour=b
#                    enable_border=True
#                else:
#                    enable_border=False
                if settings:
                    render('rect', arg=(tmp, buttcolour, False))
                else:
                    render('rect', arg=((tmp), buttcolour, False),borderradius=bradius)
            else:
                if a==1:
                    buttcolour=mainmenucolor[0]
                elif text[a-1]=='Leave':
                    buttcolour=mainmenucolor[2]
                else:
                    buttcolour=mainmenucolor[1][0]-(10*(a-2)),mainmenucolor[1][1]-(10*(a-2)),mainmenucolor[1][2]-(10*(a-2))
                if ishomemenu:
                    if not ignoremove:
                        if button==a and not int(menupos[a-1])>19:
                            menupos[a-1]+=300*drawtime
                        elif button==a and int(menupos[a-1])==20:
                            pass
                        elif int(menupos[a-1])>0:
                            menupos[a-1]-=300*drawtime
                        moveid=menupos[a-1]
                    else:
                        moveid=0
                if button==a:
                    buttcolour=buttcolour[0]+5,buttcolour[1]+5,buttcolour[2]+5
                drawRhomboid(screen, buttcolour, tmp[0]-(moveid//2), tmp[1]-moveid, tmp[2]+moveid, tmp[3],25, 0)
            if not text == None:
                if bigmode:
                    render('text', text=text[a-1], arg=((0,0), forepallete,'center','grade'),relative=instruction[a-1])
                else:
                    if ishomemenu:
                        home=moveid
                    else:
                        home=0
                    if icon:
                        showicon=1
                        for b in icon:
                            screen.blit(b, (instruction[a-1][0], instruction[a-1][1]))
                    if not showicon:
                        if not settings:
                            s=text[a-1].split(' - ')
                            d=instruction[a-1][3]//len(s)
                            f=0
                            for e in s[::-1]:
                                if ishomemenu:
                                    sd=0
                                else:
                                    sd=(d*f)
                                render('text', text=e.replace('[no video]','').rstrip(' '), arg=((0,0), tcol,'center'),relative=(tmp[0],tmp[1]-home+sd,tmp[2],d))
                                f+=1
                        else:
                            render('text', text=text[a-1], arg=((0,0), forepallete,'center','min'),relative=tmp)
    return button
def clear(color):screen.fill(color)
def blend(opacity,bgcolour):
    return maxt(bgdefaultcolour[0]-opacity,bgcolour),maxt(bgdefaultcolour[1]-opacity,bgcolour),maxt(bgdefaultcolour[2]-opacity,bgcolour)

def drawRhomboid(surf, color, x, y, width, height, offset, thickness=0):
    points = [
        (x + offset, y), 
        (x + width + offset, y), 
        (x + width-offset, y + height), 
        (x-offset, y + height)]
    pygame.draw.polygon(surf, color, points, thickness)
def fullscreenchk():
    global w, h, w, h,background,fieldpos,modsv, beatani,diffani,screen,reload,transani,modsani, button_size_width, firstcom,tal,keymap,fonts,volani,noteheight,logopos,bladeani
    reload=False
    if not settingskeystore['fullscreen']:
        if not firstcom:
            w=800
            h=600
            screenw=w
            screenh=h
    else:
        if not firstcom:
            w=0
            h=0
            screenh=0
            screenw=0

    flags=pygame.RESIZABLE
    bit=24
    if settingskeystore['fullscreen']:
        if not firstcom:
            screen=pygame.display.set_mode((0, 0), pygame.FULLSCREEN|flags, bit)
            reload=True
    else:
        if not firstcom:
            screen=pygame.display.set_mode((w, h), flags, bit)
            reload=True
    if screen.get_size()[0]!=w and screen.get_size()[0]>=800:
        reload=True
    elif screen.get_size()[1]!=h and screen.get_size()[1]>=600:
        reload=True
    if not firstcom:
        firstcom=True
        logopos=Tween(begin=0, 
               end=100, #-100?
               duration=1200,
               easing=Easing.CUBIC,
               easing_mode=EasingMode.OUT,boomerang=True)
        beatani=[Tween(begin=cross[0], end=beatsel,duration=350,easing=Easing.CUBIC,easing_mode=EasingMode.OUT),0]
        beatani[0].start()
        diffani=[Tween(begin=-1, end=0,duration=1,easing=Easing.CUBIC,easing_mode=EasingMode.OUT),0]
        diffani[0].start()
        bladeani=[Tween(begin=0, end=101,duration=500,easing=Easing.CUBIC,easing_mode=EasingMode.OUT),0]
        modsv=0
        modsani=[Tween(begin=0, end=1,duration=350,easing=Easing.CUBIC,easing_mode=EasingMode.OUT),0]
        modsani[0].start()
        transani=[Tween(begin=0, end=100,duration=150,easing=Easing.CUBIC,easing_mode=EasingMode.OUT,boomerang=True),0]
        logopos.start()
        volani=Tween(begin=volvisual, end=vol,duration=250,easing=Easing.CUBIC,easing_mode=EasingMode.OUT)
        volani.start()
    ins=1
    if reload:
        if screen.get_width()<800:
            w=800
        else: 
            w=screen.get_width()
        if screen.get_height()<600:
            h=600
        else: 
            h=screen.get_height()
        f=24
        fonts = pygame.font.Font(fontname,  int(f//1.2)),pygame.font.Font(fontname,  f//2),pygame.font.Font(fontname,  f*2),pygame.font.Font(fontname,  int(f)),pygame.font.Font(fontname,  int(f/1.1))
        button_size_width=w//2
        print(time.time(),screen.get_size())
        reloadbg()
    tal=25*(w/25)//len(bars)
    scroll=h-30-noteheight
    fieldpos=(w//2,0)
    #scroll=h//2
    #keymap=((w//2-(50*4),scroll,100,noteheight),(w//2-(50*2),scroll,100,noteheight),(w//2-(50*0),scroll,100,noteheight),(w//2-(50*-2),scroll,100,noteheight),)
    keymap=((-(50*4),scroll,100,noteheight),(-(50*2),scroll,100,noteheight),(-(50*0),scroll,100,noteheight),(-(50*-2),scroll,100,noteheight),)