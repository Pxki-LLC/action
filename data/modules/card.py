def print_card(pp,score,name,pos,rank,isgrayed=False,home=False):
    if not rank<=0:
        if isgrayed:
            tmp=bgdefaultcolour[0]-25,bgdefaultcolour[1]-25,bgdefaultcolour[2]-25
            tmpt=150,150,150
        else:
            tmp=bgdefaultcolour[0]+25,bgdefaultcolour[1]+25,bgdefaultcolour[2]+25
            tmpt=forepallete
        #if not pos[0]+300>w:
        dim=25
        render('rect',arg=((pos[0],pos[1],300,80),(tmp),False),borderradius=10)
        render('text', text='#'+str(format(rank,',')), arg=((pos[0]+10,pos[1]+30), (tmp[0]-dim,tmp[1]-dim,tmp[2]-dim),'grade'))
        render('text', text=name, arg=((pos[0]+10,pos[1]+10), tmpt,'bold'))
        render('text', text='Accuracy - '+str(round(score,2))+'%', arg=((pos[0]+10,pos[1]+60), tmpt,'min'))
        render('text', text=str(format(int(pp),','))+'pp (Lv. '+str(format(int(int(pp)*0.0727),','))+')', arg=((pos[0]+10,pos[1]+40), tmpt,'min'))
            #+' (#'+str(format(rank,','))+')'
