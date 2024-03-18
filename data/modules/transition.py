def transitionprep(act):
    global transani,actto
    actto=act
    transani[1]=1
    transani[0].start()