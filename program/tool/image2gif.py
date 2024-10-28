import datetime as dt
from PIL import Image
import os

pictures = []

idir = "./"

for day in range(1,365+1):
    pic_name = f'bw_PTM_{day:03}.png'
    print(pic_name)
    pic_path = os.path.join(idir, pic_name)
    
    try:
        img = Image.open(pic_path)
        pictures.append(img)
    except FileNotFoundError as e:
        print(f"ファイル {pic_name} が存在しません。次のファイルに進みます。")
        continue  # エラーなら次のループへ

# gifアニメの出力
output_path = "./anime_bw_PTM.gif"
if pictures:
    pictures[0].save(output_path, save_all=True, append_images=pictures[1:],
                     optimize=False, duration=100, loop=0) #duration小->早い
    print("GIFアニメーションを保存しました。")
else:
    print("アニメーションを作成するための画像が存在しません。")
