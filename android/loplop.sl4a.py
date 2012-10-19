import base64,hashlib as l,re,android as a
P=' password'
A='Account'+P
r=lambda o:o.result.encode('utf8')
d=a.Android()
n=r(d.dialogGetInput('Nickname','Enter [[len]*]nickname'))
m=r(d.dialogGetPassword('Master'+P,'Enter master'+P))
M=re.search('^(\d*)\*(.*)$',n)
L,n=M and M.groups() or (16,n)
L=int(L or 8)
h=base64.urlsafe_b64encode(l.md5(m+n).digest()).replace('=','').decode('ascii')
f=re.search('\\d+',h)
if not f:h='1'+h
elif f.start()>L-1:h=f.group()+h
p=h[:L]
d.setClipboard(p)
d.dialogCreateAlert(A,A+' (copied to clipboard): '+p)
d.dialogSetPositiveButtonText('Continue')
d.dialogShow()
d.dialogGetResponse()
