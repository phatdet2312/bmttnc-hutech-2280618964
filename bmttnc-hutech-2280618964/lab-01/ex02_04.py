#tạo danh sách rỗng lưu kết quả
j=[]
#duyệt trong khoảng 2000 -> 3200, i có chia hết cho 7 và không phải bội số của 5
for i in range(2000, 3201):
    if(i%7==0) and (i%5!=0):
        j.append(str(i))