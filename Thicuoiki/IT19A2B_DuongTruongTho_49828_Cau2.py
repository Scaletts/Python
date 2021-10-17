
data=[]
n=0

class MatHang():
    def __init__(self, ma , ten ,sl,dg)->None:
        self.ma_mat_hang = ma
        self.ten_mat_hang = ten
        self.so_luong = sl
        self.don_gia = dg
    @property
    def thanh_tien(self):
        return self.so_luong * self.don_gia


def cv23():
        f=open('IT19A2B_DuongTruongTho_49828_inp.txt',mode='r',encoding='utf-8')
        n=int(f.readline())
        for i in range(0,n):
            row_data=f.readline().split("|")
            mat_hang=MatHang(row_data[0],row_data[1],int(row_data[2]),int(row_data[3]))
            data.append(mat_hang)
        f.close()
        print("====Đã đọc file=====")
    

def cv24():
    if len(data)==0:
        print("Ban can nhap thong tin mat hang")
    else:
        print("\n---Thông Tin Mặt Hàng---")
        print("\n{:<12} {:<15} {:>5} {:>10} {:>15}".format("Mã Mặt Hàng","Tên Mặt Hàng","Số Lượng","Đơn Gía","Thành Tiền"))
        for i in data:
            print("{:<12} {:<15} {:>5} {:>13} {:>15}".format(i.ma_mat_hang, i.ten_mat_hang, i.so_luong, i.don_gia, i.thanh_tien))


def cv25():
    print("====== Mat hang dat nhat =====")
    mathangdatnhat = data[0]
    for i in data:
        if i.don_gia> mathangdatnhat.don_gia:
             mathangdatnhat=i
        mathangdatnhat_str= mathangdatnhat.ma_mat_hang+"|"+ mathangdatnhat.ten_mat_hang+"|"+str( mathangdatnhat.so_luong)\
                +"|"+str( mathangdatnhat.don_gia)+"|"+str( mathangdatnhat.thanh_tien)+"\n"
    print(mathangdatnhat_str)
    print("=="*10)


def cv26():
    if len(data) == 0:
        print("Ban can chon nhap thong tin mat hang")
    else:
        f=open('IT19A2B_DuongTruongTho_49828_out.txt',mode='w',encoding='utf-8')
        f.write(str(len(data))+"\n")
        for i in data:
            s=i.ma_mat_hang+"|"+i.ten_mat_hang+"|"+str(i.so_luong)\
                +"|"+str(i.don_gia)+"|"+str(i.thanh_tien)+"\n"
            f.write(s)
        f.close()
        print("Đã ghi file")

        
while True:
            print('====MENU====')
            print('1.Nhap du lieu')
            print('2.Hien thi thong tin mat hang ')
            print('3.Mat hang co don gia cao nhat')
            print('4.Ghi thong tin mat hang')
            cv = input('\nVui long chon cong viec hoac an Q de ket thuc:')
            if cv == '1':
                cv23()
            if cv == '2':
                cv24()
            if cv == '3':
                cv25()
            if cv=='4':
                cv26()
            elif cv.upper()=='Q':
                break

