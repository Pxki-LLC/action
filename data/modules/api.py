import requests

def submit_score(perf,score,other=''):
    global oldstats
    oldstats=[totperf,totscore,totacc,level] # type: ignore
    print('Submitting Score...')
    template=str(p2[beatsel].replace('\n','-'))+';'+str(perf)+';'+str(score)+';'+other # type: ignore
    f=requests.get(settingskeystore['apiurl']+'api/submitscore?'+str(settingskeystore['username'])+';'+str(settingskeystore['password'])+';'+str(template),headers={'User-Agent': 'QluteClient-'+str(gamever)},timeout=10) # type: ignore
    f=f.text
    reloadprofile() # type: ignore
    if f!='':
        print(f.rstrip('\n'))
        notification('QlutaBot',desc=f.rstrip('\n')) # type: ignore
