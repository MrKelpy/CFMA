"""
© Copyright Alexandre Silva - 2020

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

Created at 19/12/2020
"""
import tkinter as tk
import tkinter.ttk as ttk
import threading
from click_events import on_install_click_wrapper


class Installer:
    def __init__(self, master=None):
        # build ui
        self.mainwindow = ttk.Frame(master)
        self.label_2 = ttk.Label(self.mainwindow)
        self.label_2.config(compound='top', font='{Sans} 20 {bold}', takefocus=True, text='CF Modpack Architect')
        self.label_2.place(anchor='center', relx='0.5', rely='0.08', x='0', y='0')
        self.install = ttk.Button(self.mainwindow)
        self.install.config(takefocus=False, text='Install Mods')
        self.install.place(anchor='center', relwidth='.5', relx='.5', rely='.9', x='0', y='0')
        self.install.configure(command=self.on_install_click)
        self.wait = ttk.Label(self.mainwindow)
        self.wait.config(font='{Sans} 8 {}', takefocus=False, text='Please wait...')
        self.wait.place(anchor='center', relx='.5', rely='.9', x='0', y='0')
        self.wait.place_forget()
        self.output = tk.Text(self.mainwindow)
        self.output.config(blockcursor='false', cursor='arrow', font='TkDefaultFont', height='10')
        self.output.config(setgrid='true', tabstyle='wordprocessor', takefocus=False, undo='false')
        self.output.config(width='50', wrap='char')
        _text_ = ""
        self.output.insert('0.0', _text_)
        self.output.config(state='disabled')
        self.output.place(anchor='center', relheight='.7', relwidth='.8', relx='.5', rely='.5', x='0', y='0')
        self.mainwindow.config(height='400', takefocus=False, width='500')
        self.mainwindow.pack(side='top')

    def on_install_click(self):
        install_thread = threading.Thread(target=on_install_click_wrapper, args=(self,))
        install_thread.start()

    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    root.title("CFMA")
    app = Installer(root)
    app.run()

