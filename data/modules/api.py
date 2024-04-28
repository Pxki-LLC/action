def submit_score(perf,score,other=''):
    global oldstats
    oldstats=[totperf,totscore,totacc]
    print('Submitting Score...')
    template=str(p2[beatsel].replace('\n','-'))+';'+str(perf)+';'+str(score)+';'+other
    f=requests.get(settingskeystore['apiurl']+'api/submitscore?'+str(settingskeystore['username'])+';'+str(settingskeystore['password'])+';'+str(template),headers={'User-Agent': 'QluteClient-'+str(gamever)},timeout=10)
    f=f.text
    reloadprofile()
    if f!='':
        print(f.rstrip('\n'))
        notification('QlutaBot',desc=f.rstrip('\n'))
