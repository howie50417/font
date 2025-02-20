import os
import requests
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_url = 'https://cdn.jsdelivr.net/gh/howie50417/font/WenQuan.ttf'
font_path = 'WenQuan.ttf'

if not os.path.exists(font_path):
    response = requests.get(font_url)
    response.raise_for_status()
    with open(font_path, 'wb') as f:
        f.write(response.content)

prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = prop.get_name()
plt.rcParams['axes.unicode_minus'] = False

labels = ['非常滿意', '還算滿意', '不太滿意', '非常不滿意', '不知道/無意見', '拒答']
sizes = [263, 481, 156, 62, 179, 1]

plt.figure(figsize=(8, 8))
patches, texts, autotexts = plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('對XXXX施政表現的滿意度調查結果', fontproperties=prop)
plt.axis('equal')

for text in texts + autotexts:
    text.set_fontproperties(prop)

plt.show()
