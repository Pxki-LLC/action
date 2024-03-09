def submit_score(perf,score,other=''):
    global oldstats
    oldstats=[totperf,totscore]
    print('Submitting Score...')
    template=str(p2[beatsel])+';'+str(perf)+';'+str(score)+';'+other
    f=requests.get(apiurl+'api/submitscore?'+str(username)+';'+str(template),headers={'User-Agent': 'QluteClient-'+str(gamever)},timeout=10)
    f=f.text
    print(template)
    print(f)
    print('Submitted Score')
    reloadprofile()
