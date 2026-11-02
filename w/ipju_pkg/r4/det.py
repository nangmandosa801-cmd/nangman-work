import sys
sys.path.insert(0,'/home/claude/watch')
import fetch
fetch.D='/home/claude/w/ipju_pkg/r4/'
for pb in sys.argv[1:]:
    h,t,p=fetch.detail(dict(kind='apt',pb=pb,hm=pb))
    print(pb,len(t),p)
