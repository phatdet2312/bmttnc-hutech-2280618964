import base64

def main():
    # Nhập thông tin cần mã hóa
    input_string = input("Nhập thông tin cần mã hóa: ")
    
    # Mã hóa chuỗi thành bytes
    bytes = base64.b64encode(input_string.encode("utf-8"))
    encoded_string = bytes.decode("utf-8")
    
    # Ghi chuỗi đã mã hóa vào file data.txt
    with open("data.txt", "w") as file:
        file.write(encoded_string)
    
    print("Đã mã hóa và ghi vào tệp data.txt")

if __name__ == "__main__":
    main()