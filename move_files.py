# import os
# import random
# import shutil

# 假设images、和labels两个文件夹内所有文件名一一对应，请自行修改此文件


# |----labels
# |     |---train
# |     |    |---0001.txt
# |     |    |---0002.txt
# |     |---val
# |          |----0003.txt
# |          |----0004.txt
# |----images
# |     |---train
# |     |    |---0001.jpg
# |     |    |---0002.jpg
# |     |---val
# |          |----0003.jpg
# |          |----0004.jpg


# path = 'images'
# files = os.listdir(path)
# random.shuffle(files)

# val_files = files[:1000]
# train_files = files[1000:]

# for file in val_files:
#     shutil.move(os.path.join(path, file), os.path.join('lbval', file))

# for file in train_files:
#     shutil.move(os.path.join(path, file), os.path.join('lbtrain', file))
    

import os
import shutil

src = 'labels'
dst = 'lbtrain'
dst2 = 'lbval'

for filename in os.listdir(src):
    if filename[:-4]+'.jpg' in os.listdir('imgval'):
        shutil.move(os.path.join(src, filename), os.path.join(dst2, filename))
    else:
        shutil.move(os.path.join(src, filename), os.path.join(dst, filename))