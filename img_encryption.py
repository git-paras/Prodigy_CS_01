from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("300x200")

def encrypt_img():
    file1=filedialog.askopenfile(mode="r", filetypes=[('jpg file','*.jpg')])
    if file1 is not None:
        file_name=file1.name
        key=input1.get(1.0, END)
        print(file_name, key)
        fi=open(file_name, "rb")
        image=fi.read()
        fi.close()
        image=bytearray(image)
        for i, value in enumerate(image):
            image[i]=value^int(key)
        fi1=open(file_name, "wb")
        fi1.write(image)
        fi1.close()


b1=Button(root, text="Encrypt", command=encrypt_img)
b1.place(x=60,y=10)

b2=Button(root, text="Decrypt", command=encrypt_img)
b2.place(x=180,y=10)

input1=Text(root, height=1, width=8, fg="black")
input1.place(x=100,y=50)

root.mainloop()