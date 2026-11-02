import sys; sys.path.insert(0,'/home/claude/blogkit')
from thumbnail import render
render('낭만부동산 · 실거래로 보기',
       ['2022년에 산 사람', '77.6%가 손해 봤습니다'],
       '경기도 아파트 · 같은 집 재거래 109만 4,695쌍',
       '/mnt/user-data/outputs/재배치/nangman/loss/nangman_loss_thumb.png')
print('ok')
