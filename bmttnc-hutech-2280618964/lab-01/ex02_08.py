#hàm kiểm tra số nhị phân có chia hết cho 5
def chia_het_cho_5(sonhiphan):
    #chuyển nhị phân sang thập phân
    sothapphan = int(sonhiphan, 2)
    #kiểm tra xem số thập phân có chia hết cho 5
    if sothapphan % 5 == 0:
        return True
    else:
        return False
#Nhập chuỗi số nhị phân
chuoisonhiphan = input("Nhập chuỗi nhị phân (Phân tích bởi dấu phẩy): ")
#tách chuổi thành các số nhị phân kiẻm tra cha hết cho 5
sonhiphan_list = chuoisonhiphan.split(',')
sochiahetcho_5 = [so for so in sonhiphan_list if chia_het_cho_5(so)]

#in ra các số nhị phân chia hết cho 5
if len(sochiahetcho_5)>0:
    ketqua = ','.join(sochiahetcho_5)
    print("Các số nhị phân chia hết cho 5 là:", ketqua)
else:
    print("Không có số nhị phân nào chia hết cho 5 trong chuỗi đã nhập.!")