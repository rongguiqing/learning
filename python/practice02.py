#os模块
import os

#getcwd(),获取当前的工作目录，返回当前工作目录的字符串

mydir = os.getcwd()
print(type(mydir))
print(mydir)

#chdir(),改变当前的工作目录，返回值None

os.chdir("E:\learning")
mydir = os.getcwd()
print(mydir)

#listdir(),获取一个目录中所有子目录和文件的名称列表，返回列表

mylist = os.listdir()
print(mylist)

#makedirs(),递归创建文件夹，返回值None

#os.makedirs("rong/gui/qing")


#system(),运行系统shell命令，返回一个shell或者终端界面

rst = os.system("ls")
print(rst)
rst = os.system("touch pratice03.py")
print(rst)
rst = os.system("rm rong\gui\qing")
print(rst)