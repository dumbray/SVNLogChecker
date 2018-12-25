# coding:UTF-8

import tkinter
import cx_Oracle

window = tkinter.Tk()
window.title("SVN日志查询")
window.geometry("600x200")
# 连接数据库


# 查询时段
date_lable = tkinter.Label(window, text="查询时段", font=("黑体", 11), width=10, height=2)
date_lable.grid(row=0, column=0)

from_date = tkinter.Entry(width=10)
from_date.grid(row=0, column=1)

end_date = tkinter.Entry(width=10)
end_date.grid(row=0, column=2)

# 部门
dept_lable = tkinter.Label(window, text="部门", font=("黑体", 11), width=10, height=2)
dept_lable.grid(row=0, column=3)

dept_check = tkinter.Checkbutton()
window.mainloop()