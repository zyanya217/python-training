#有序可變動列表 List
grades=[12,60,15,70,95]
grades[0]=55;#把它放到列表中第一個位子
print(grades[0])
print(grades[1:3])
grades[1:4]=[] #連續刪除
print(grades)

grades=grades+[33,100]#列表串接
print(grades)

lenght=len(grades)
print(lenght)

data=[[3,4,5],[6,7,8]]#巢狀列表:列表之中放列表
data=[0][0:2]=[5,5,5] #把[0](第一個列表)中的[3,4]換成[5,5,5]
print(data)

#有序不可變動列表 Tuple
data=(3,4,5)
#與List唯一的不同:
#data=[0]=5 #錯誤:Tuple的資料不可以變動
print(data[0:2])