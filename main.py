import json
import os
from pathlib import Path
from typing import *
MYJSONTYPE = Dict[
    Literal['name', 'phone', 'email', 'address'],
    Union[str, float]
]
BASE_DIR=Path(__file__).resolve().parent
CONTACTJSON=BASE_DIR/'data'/'contact.json'
def append_contact():
    if not os.path.exists(CONTACTJSON):
        print("chưa tồn tại.")
        return 
    with open(CONTACTJSON,'r', encoding='utf-8') as f:
        content: MYJSONTYPE = json.load(f)
        return content['address']
 
# lưu vào file json
def save_contact(contact):
    with open(CONTACTJSON,'w', encoding='utf-8') as f:
        json.dump(contact,f, ensure_ascii=False, indent=4)
# thêm liên hệ vào
def add_contact(name, phone, address, email)->MYJSONTYPE:
    new_contact:MYJSONTYPE={
        'name':name,
        'Phone':phone,
        'address':address,
        "email":email

    }
    contact=[]
    contact.append(new_contact)
    with open(CONTACTJSON, 'w', encoding='utf-8') as f:
        json.dump(contact, f, ensure_ascii=False, indent=4)
    print(f'Thêm Liên Hệ Tên {name}')

# xem liên hệ
def view_contatc():
       if not os.path.exists(CONTACTJSON):
            print("Danh bạ trống .")
       with open(CONTACTJSON, 'r', encoding='utf-8') as f:
           contact:list[MYJSONTYPE]=json.load(f)
       for c in contact:
        print(f'Tên: {c.get("name")}')
        print(f'Phone: {c.get("phone") or c.get("Phone")}')
        print(f'Email: {c.get("email")}')
        print(f'Địa chỉ: {c.get("address")}')
# tìm kiếm liên hệ
def search_contact(contact):
    name = input("Nhập tên cần tìm: ")
    with open(CONTACTJSON, 'r', encoding='utf-8') as f:
           contact:MYJSONTYPE=json.load(f)
    if(name in contact):
        print(f'Tên {contact["name"]}')
        print(f'Phone {contact["phone"]}')
        print(f'Email {contact["email"]}')
        print(f'địa chỉ {contact["address"]}')
    else:
         print("ko tìm thấy liên hệ")

# xóa liên hệ
def delete_contact(contact):
    name = input("Nhập tên muốn xóa: ")
    with open(CONTACTJSON, 'r', encoding='utf-8') as f:
           contact:MYJSONTYPE=json.load(f)
    if name in contact:
        del contact['name']
        print(f'đã xóa name {name}')
    else:
        print("Không tìm thấy liên hệ.")
# Cập nhật liên hệ
def update_contact(name, phone, email, address):
    if not os.path.exists(CONTACTJSON):
        print("Chưa có file dữ liệu.")
        return
    with open(CONTACTJSON, "r", encoding="utf-8") as f:
        contacts = json.load(f)
    for c in contacts:
        if c["name"]== name:
            c["phone"] = phone
            c["email"] = email
            c["address"] = address
            with open(CONTACTJSON, "w", encoding="utf-8") as f:
                json.dump(contacts, f, indent=4, ensure_ascii=False)
            print("Đã cập nhật:", name)
            
    else:
        print("Không tìm thấy:", name)

if __name__ == "__main__":
    choice = input("Nhập lựa chọn: ")

    if choice == "1":
        name = input("Tên: ")
        phone = input("Số điện thoại: ")
        address = input("Địa chỉ: ")
        email = input("Email: ")
        add_contact(name, phone, address, email)
    elif choice == "2":
        view_contatc()

    elif choice == "3":
        name = input("Tên cần tìm: ")
        search_contact(name)

    elif choice == "4":
        name = input("Tên cần xóa: ")
        delete_contact(name)

    elif choice == "5":
        name = input("Tên cần cập nhật: ")
        phone = input("Số điện thoại mới: ")
        email = input("Email mới: ")
        address = input("Địa chỉ mới: ")
        update_contact(name, phone, email, address)

    elif choice == "0":
        print("Thoát chương trình.")



