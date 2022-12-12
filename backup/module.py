# 載入內建的 sys 模組並取得資訊
#import sys as s
#print(s.platform)
#print(s.maxsize)

# 建立 geometry 模組，載入使用
#import geometry
#result=geometry.distance(1,1,5,5)
#print(result)
#result=geometry.slope(1,2,5,6)
#print(result)

# 調整搜尋模組的路徑
import sys
sys.path.append("modules") #在模組的搜尋路徑列表中【新增路徑】
print(sys.path) # 印出模組的搜尋路徑
import geometry
print(geometry.distance(1,1,5,5))# 若沒第15行會錯誤:模組的搜尋路徑不包含我們自己創建的資料夾
