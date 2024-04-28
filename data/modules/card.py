def print_card(pp,score,name,pos,rank,isgrayed=False,home=False):
    if not rank<=0:
        if isgrayed:
            tmp=bgdefaultcolour[0]-25,bgdefaultcolour[1]-25,bgdefaultcolour[2]-25
            tmpt=150,150,150
        else:
            tmp=bgdefaultcolour[0]+25,bgdefaultcolour[1]+25,bgdefaultcolour[2]+25
            tmpt=forepallete
        #if not pos[0]+300>w:
        if not name:
            name='Guest'
            rank=0
        dim=35
        render('rect',arg=((pos[0],pos[1],300,80),(tmp),False),borderradius=10)
        if rank:
            if not pp<1:
                render('text', text='#'+str(format(rank,',')), arg=((pos[0]+290,pos[1]+30), (tmp[0]+dim,tmp[1]+dim,tmp[2]+dim),'grade','rtl'))
            render('text', text='Accuracy - '+str(round(score,2))+'%', arg=((pos[0]+10,pos[1]+60), tmpt,'min'))
            render('text', text=str(format(int(pp),','))+'pp (Lv. '+str(format(int(int(pp)*0.0727),','))+')', arg=((pos[0]+10,pos[1]+40), tmpt,'min'))
        else:
            render('text', text='Not Logged in', arg=((pos[0]+10,pos[1]+40), tmpt,'min'))
        render('text', text=name, arg=((pos[0]+10,pos[1]+10), tmpt,'bold'))
            #+' (#'+str(format(rank,','))+')'
