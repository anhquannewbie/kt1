"""

B1: Tính tổng và tích các chữ số của một số nguyên được nhập từ bàn phím

a) Viết một hàm nhận vào 1 chuỗi các số nguyên lớn hơn 9. Sau đó trả về 1 tuple là một bộ 2 số,
số đầu tiên là tổng các chữ số của từng số trong chuỗi, số thứ 2 là tích các chữ số của từng chữ số trong chuỗi.

"""

def tong_tich(myString="10"):
    if myString.isdecimal() and int(myString) > 9:
        tong = tich = int(myString[0])
        for c in range(1, len(myString)):
            myC = int(myString[c])
            tong += myC
            tich *= myC
        return (tong, tich)
    else:
        return None

"""
b) Viết hàm main để nhận dữ liệu từ bàn phím và sử dụng hàm ở câu a để tính. Sau đó in ra dữ liệu
"""
if __name__ == '__main__':
    str = input("Nhap vao so > 9: ")
    rsTongTich = (tong_tich(str))
    if rsTongTich == None:
        print("Du lieu nhap vao khong hop le")
    else:
        print(rsTongTich)
        forPrint = ""
        for c in str:
            forPrint += c+ " "
        print("Tong va tich cua %sla %d va %d" % (forPrint, rsTongTich[0], rsTongTich[1]))