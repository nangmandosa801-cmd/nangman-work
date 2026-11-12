cd /home/claude/w/int_fix
for d in 2244*/; do n=${d%/}; for f in $d*; do timeout 120 python3 /home/claude/helper/gas.py fput "블로그/협업/4_어사이드/원고/보완_1112/$n" "$f" >/dev/null 2>&1 || echo "FAIL $f"; done; echo "done $n"; done > /tmp/intup.log 2>&1; echo ALLDONE >> /tmp/intup.log
