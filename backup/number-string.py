#[數字運算]
x=3//9 #整數除法
print(x)

#[字串運算]
s="Hello\"0" #印出"
print(s)
t="Hello\nWorld" #\n代表換行
print(t)
r="""Hello

World""" 
#""" """就能直接換行(寫多行文字)
print(r)

i="Hello"*3+"World"
print(i)

#字串會對內部的字元編號(索引)，從0開始算起
n="Hello"
print(n[1:4]) #包含開頭不包含結尾
print(n[1:]) 
print(n[:3]) 