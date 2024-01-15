import tkinter as tk
import os
import tkinter
from tkinter import *
from pathlib import Path
from threading import Thread

home = str(Path.home())
home = home.replace("\\", "\\\\")

exitt="exit"

vir_activate = "conda activate trygpu &&"
demo_directory = "cd " + home + "\\Downloads\\FYP\\FYP\\prog_file\\prog_file &&"
load_demo = "python demo.py --cpu --connect --debug"
load_demo_gpu = "python demo.py --connect --debug"
unity_directory = "cd " + home + "\\Downloads\\FYP\\FYP\\windows_x86_64\\windows_x86_64 && " 
load_unity = "unitychan.exe"
act_conda = "call " + home + "\\anaconda3\\Scripts\\activate.bat &&"

install_pip = "conda install pip -y"
install_numpy = "pip install numpy &&"
install_opencv = "pip install opencv-python &&"
install_dlib = "pip3 install dlib==19.8.1 &&"
install_cmake = "pip3 install cmake &&"
install_boost = "pip install boost-py &&"
install_wheel = "pip install wheel &&"

install_torch = "pip install torch==1.3.1 -f https://download.pytorch.org/whl/torch_stable.html &&"
install_torchvision = "pip install torchvision==0.4.1 &&"
install_cudatoolkit = "pip install cudatoolkit==11.2 &&"
install_scipy = "pip install scipy &&"
install_numba = "pip install numba &&"
install_onnx = "pip install onnxruntime-gpu &&"
install_tensorflow = "pip install tensorflow-gpu==1.15 &&"
install_cudnn = "pip install nvidia-cudnn==8.1.0 &&"
create_vir = "conda create -n trygpu python=3.6.6 -y"
deactivate = "conda deactivate"


class Win1:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x300")
        self.show_widgets()
        
        

    def show_widgets(self):
        self.frame = tk.Frame(self.master)
        canvas1 = tk.Canvas(self.master, width = 100, height = 100)
   

        self.master.configure(bg='#49A')
        frame1 = Frame( root, bg = "#88cffa")
        frame1.pack(pady = 1000)

        canvas1.pack()
        
        self.master.title("Starting page")
        vy = tk.Label(self.frame, text='Welcome to VY', font=('helvetica', 10, 'bold'))
    
        vy.pack()
        self.create_button("----New User----", Win2)
        self.create_button("---Used before---", Win3)

        self.frame.place(x= 140, y=100)
        
        
        
    def create_button(self, text, _class):
        "Button that creates a new window"
        tk.Button(
            self.frame, text=text,
            command=lambda: self.new_window(_class)).pack()

    def new_window(self, _class):
            global win2, win3

            try:
                if _class == Win2:
                    if win2.state() == "normal":
                        win2.focus()
            except:  
                win2 = tk.Toplevel(self.master)
                _class(win2)

            try:
                if _class == Win3:
                    if win3.state() == "normal":
                        win3.focus()
            except:  
                win3 = tk.Toplevel(self.master)
                _class(win3)

    def close_window(self):
        self.master.destroy()

class Win2(Win1):

    def show_widgets(self):
 
        
        "A frame with a button to quit the window"
        self.master.title("Download details")
        self.frame = tk.Frame(self.master)
        
        
        canvas1 = tk.Canvas(self.frame, width = 100, height = 100)
        
        
        
        canvas1.pack()

        def cpu ():
            os.system(act_conda + create_vir)
            os.system(act_conda + vir_activate + install_pip)
            os.system(act_conda + vir_activate + install_numpy + install_opencv + install_wheel + install_cmake + install_boost  + install_dlib + deactivate)
            os.system(exitt)
            
        def gpu ():
            os.system(act_conda + create_vir)
            os.system(act_conda + vir_activate + install_pip)
            os.system(act_conda + vir_activate + install_numpy + install_opencv  + install_wheel + install_cmake + install_boost  + install_dlib  + install_torchvision + install_tensorflow +  install_scipy  + install_numba + install_onnx + deactivate)
            os.system(exitt)
        

        tes = tk.Label(self.frame, text='choose a mode to download', font=('helvetica', 10, 'bold'))
        tes.place(x= -3, y=0)
        b2 = tk.Button(self.frame,text='CPU mode', command=cpu ,bg='green', fg='white', font=('helvetica', 8, 'bold'))
        b2.place(x= 25, y=40)
        b3 = tk.Button(self.frame,text='GPU mode', command=gpu ,bg='green', fg='white', font=('helvetica', 8, 'bold'))
        b3.place(x= 95, y=40)
        self.quit_button = tk.Button(
            self.frame, text=f" --  Back to starting page -- ",
            command=self.close_window)
        self.quit_button.pack()
        self.create_button(" -----Download completed----- ", Win3)
        self.frame.place(x= 100, y=100)



class Win3(Win2):

    def show_widgets(self):
        self.master.title("Execution page")
        self.frame = tk.Frame(self.master)
        canvas1 = tk.Canvas(self.frame, width = 100, height = 100)

        
        canvas1.pack()

        te = tk.Label(self.frame, text='choose a mode you ', font=('helvetica', 10, 'bold'))
        te.place(x= 10, y=0)
        te = tk.Label(self.frame, text='have downloaded', font=('helvetica', 10, 'bold'))
        te.place(x= 15, y=20)

        def unity ():
            os.system(unity_directory + load_unity) 
        

        def democpu ():
            os.system(act_conda + vir_activate + demo_directory + load_demo)
        

        def cpu1 ():
            if __name__ == '__main__':
                Thread(target = unity).start()
                Thread(target = democpu).start()
        c1=tk.Button(self.frame,text='Cpu mode', command=cpu1 ,bg='red', fg='white', font=('helvetica', 10, 'bold'))
        c1.place(x= 0, y=50)
        
        def demogpu ():
            os.system(act_conda + vir_activate + demo_directory + load_demo_gpu)

        def gpu1 ():
            if __name__ == '__main__':
                Thread(target = unity).start()
                Thread(target = democpu).start()
        g1=tk.Button(self.frame,text='Gpu mode', command=gpu1 ,bg='red', fg='white', font=('helvetica', 10, 'bold'))
        g1.place(x= 80, y=50)
            
            
        
        
        self.quit_button = tk.Button(
            self.frame, text=f" go back to perious page",
            command=self.close_window)
        
        self.quit_button.pack()
        self.frame.place(x= 120, y=50)



root = tk.Tk()
app = Win1(root)
root.mainloop()
