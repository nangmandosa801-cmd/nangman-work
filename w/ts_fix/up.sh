cd /home/claude
for d in w/ts_fix/out/*/; do n=$(basename $d); for f in $d*; do timeout 120 python3 helper/gas.py fput "블로그/협업/4_어사이드/티스토리/보완_1112/$n" "$f" >/dev/null 2>&1 || echo "FAIL $n $f"; done; echo "done $n"; done > /tmp/tsup.log 2>&1
echo ALLDONE >> /tmp/tsup.log
