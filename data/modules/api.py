def submit_score(perf,score,other=''):
    global oldstats
    oldstats=[totperf,totscore,totacc]
    print('Submitting Score...')
    template=str(p2[beatsel].replace('\n','-'))+';'+str(perf)+';'+str(score)+';'+other
    f=requests.get(apiurl+'api/submitscore?'+str(username)+';'+str(template),headers={'User-Agent': 'QluteClient-'+str(gamever)},timeout=10)
    f=f.text
    reloadprofile()
    if f!='':
        notification('QlutaBot',desc=f.rstrip('\n'))
