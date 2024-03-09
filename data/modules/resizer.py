def fullscreenchk():
    global w, h, w, h, screen, button_size_width, firstcom,tal,keymap,fonts,transa,keysize
    reload=False
    if not settingskeystore[0]:
        if not firstcom:
            w=800
            h=600
            screenw=w
            screenh=h
        else:
            w=screen.get_width()
            h=screen.get_height()

    flags=pygame.DOUBLEBUF|pygame.RESIZABLE|pygame.HWSURFACE
    bit=24
    if settingskeystore[0]:
        if not firstcom:
            screen=pygame.display.set_mode((0, 0), pygame.FULLSCREEN|flags, bit)
            reload=True
    else:
        if not firstcom:
            screen=pygame.display.set_mode((w, h), flags, bit)
            reload=True
    if not firstcom:
        firstcom=True
    w=screen.get_width()
    h=screen.get_height()
    ins=1
    if reload:
        f=24
        fonts = pygame.font.Font(fontname,  int(f//1.2)),pygame.font.Font(fontname,  f//2),pygame.font.Font(fontname,  f*2),pygame.font.Font(fontname,  int(f))
        button_size_width=w//2
    tal=25*(w/25)//len(bars)
    keysize=30
    scroll=h-30-keysize
    #scroll=h//2
    keymap=((w//2-(50*4),scroll,100,keysize),(w//2-(50*2),scroll,100,keysize),(w//2-(50*0),scroll,100,keysize),(w//2-(50*-2),scroll,100,keysize),)
