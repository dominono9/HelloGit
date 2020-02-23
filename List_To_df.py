#python標準リストからデータフレームを作成する
import pandas as pd
list1 = [[0, 1, 2], [3, 4, 5]]

df = pd.DataFrame(list1)
df
#出力結果
#    0  1  2
# 0  0  1  2
# 1  3  4  5
