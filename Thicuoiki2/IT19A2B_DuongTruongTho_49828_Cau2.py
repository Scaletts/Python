data=[]
n=0
class Sinhvien():
    def __init__(self,ma,ten,sdt,lt,tt)->None:
        self.ma_hoc_vien = ma
        self.ten_hoc_vien = ten
        self.so_dien_thoai=sdt
        self.diem_ly_thuyet=lt
        self.diem_thuc_hanh=tt
    @property
    def diem_trung_binh(self):
        return (self.diem_ly_thuyet+self.diem_thuc_hanh)/2
    @property
    def xep_loai(self):
        diem_trung_binh = (self.diem_ly_thuyet+self.diem_thuc_hanh) / 2
        if diem_trung_binh >= 9:
            return 'Xuất sắc'
        elif diem_trung_binh >= 8:
            return 'Giỏi'
        elif diem_trung_binh >= 7:
            return 'Khá'
        elif diem_trung_binh >= 5:
            return 'Trung bình'
        elif diem_trung_binh < 5:
            return 'Không đạt'

def cv23():
    f=open('IT19A2B_DuongTruongTho_49828_inp.txt',mode='r',encoding='utf-8')       
    n=int(f.readline())
    for i in range(0,n):
        row_data=f.readline().split("|")
        sinh_vien=Sinhvien(row_data[0],row_data[1],row_data[2],float(row_data[3]),float(row_data[4]))
        data.append(sinh_vien)
    f.close()
    print("====Đã đọc được file=====")


def cv24():
    if len(data)==0:
        print("Bạn cần nhập thông tin học viên!!")
    else:
        print("\n---Thông Tin Học Viên ---")
        print("\n{:<15} {:<25} {:<15} {:>20} {:>20} {:>20} {:>20}".format("Mã Học Viên","Tên Học Viên","Số Điện Thoại","Điểm Lý Thuyết","Điểm Thực Hành","Điểm Trung Bình","Xếp loại"))
        for i in data:
            print("{:<15} {:<25} {:<15} {:>14} {:>20} {:>20} {:>26}".format(i.ma_hoc_vien, i.ten_hoc_vien, i.so_dien_thoai, i.diem_ly_thuyet, i.diem_thuc_hanh,i.diem_trung_binh,i.xep_loai))


def cv25():
    if len(data) == 0:
        print('*Chưa có thông tin sinh viên,vui lòng kiểm tra lại!!!')
    else:
        print('\n---+SINH VIÊN CÓ ĐIỂM KHÁ TRỞ LÊN+---')
        print("\n{:<15} {:<25} {:<15} {:>20} {:>20} {:>20} {:>20}".format('Mã học viên', 'Tên Học Viên', 'Số Điện Thoại', 'Điểm Lý Thuyết', 'Điểm Thực Hành', 'Điểm Trung Bình', 'Xếp loại'))

        for i in data:
            if i.diem_trung_binh >= 7:
                print("{:<15} {:<25} {:<15} {:>20} {:>20} {:>20} {:>20}".format(i.ma_hoc_vien, i.ten_hoc_vien, i.so_dien_thoai, i.diem_ly_thuyet, i.diem_thuc_hanh, i.diem_trung_binh, i.xep_loai))


def cv26():
    if len(data) == 0:
        print('*Chưa có thông tin sinh viên, vui lòng kiểm tra lại')
    else:
        f = open('IT19A2B_DuongTruongTho_49828_out.txt', mode='w', encoding='utf-8')
        wF = '---+++SINH VIÊN CÓ ĐIỂM KHÁ TRỞ LÊN++++---'
        wF += "\n\n{:<15} {:<25} {:<15} {:>20} {:>20} {:>20} {:>20}".format('Mã học viên', 'Tên Học Viên', 'Số Điện Thoại', 'Điểm Lý Thuyết', 'Điểm Thực Hành', 'Điểm Trung Bình', 'Xếp loại')

        for i in data:
            if i.diem_trung_binh >= 7:
                wF += "\n{:<15} {:<25} {:<15} {:>20} {:>20} {:>20} {:>20}".format(i.ma_hoc_vien, i.ten_hoc_vien, i.so_dien_thoai, i.diem_ly_thuyet, i.diem_thuc_hanh, i.diem_trung_binh, i.xep_loai)

        f.write(wF)
        print('Ghi dữ liệu thành công!')




while True:
            print('====MENU====')
            print('1.Nhập dữ liệu học viên')
            print('2.Hiển thị thông tin học viên ')
            print('3.In thông tin học viên có điểm trung bình >7')
            print('4.Ghi thông tin học viên có điểm trung bình >7')
            cv = input('\nVui long lựa chọn công việc hoặc ấn Q để kết thúc công việc:')
            if cv == '1':
                cv23()
            if cv == '2':
                cv24()
            if cv == '3':
                cv25()
            if cv == '4':
                cv26()
            elif cv.upper()=='Q':
                break

