def textbox(pos,size,text='',center=False,min=False,border_colour=(255,255,255),bg_colour=(40,40,40)):
    hw=(pos[0],pos[1],pos[2],size)
    if center:
        c='center'
    else:
        c=''
    if min:
        b='min'
    else:
        b=''
    render('rect', arg=(hw, bg_colour, True),bordercolor=border_colour)
    render('text', text=text, arg=((pos[0],pos[1]), forepallete,c,b),relative=hw)