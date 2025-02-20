import os
import requests
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 下載「文泉驛微米黑」字型檔案（使用你提供的新網址）

font_url = 'https://github.com/RichStrong/tiny_font/raw/refs/heads/master/hei.TTF'
font_path = 'hei.TTF'

if not os.path.exists(font_path):
    response = requests.get(font_url)
    response.raise_for_status()  # 確保下載成功
    with open(font_path, 'wb') as f:
        f.write(response.content)

# 指定 matplotlib 使用下載的字型檔案
prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = prop.get_name()
plt.rcParams['axes.unicode_minus'] = False

# 測試資料
labels = ['非常滿意', '還算滿意', '不太滿意', '非常不滿意', '不知道/無意見', '拒答']
sizes = [263, 481, 156, 62, 179, 1]

plt.figure(figsize=(8, 8))
patches, texts, autotexts = plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('對XXXX施政表現的滿意度調查結果', fontproperties=prop)
plt.axis('equal')

# 設定圖表上所有文字元件使用下載的字型
for text in texts + autotexts:
    text.set_fontproperties(prop)

plt.show()
