# 조건: 모은 돈 2억 · 월 250만 · 금리 4.5% · 30년 · 생애최초 LTV 70% · 한도 6억 · 떼는 돈 1,500만
import subprocess
print(subprocess.run('python3 /home/claude/tools/postkit/budget_map.py --equity 20000 --monthly 250 --rate 4.5 --years 30 --ltv 70 --cap 60000 --reserve 1500 --ym-from 202608 --ym-to 202610 --base-year 2026 --out ana.json'.split(),capture_output=True,text=True))
