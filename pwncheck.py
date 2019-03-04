#!/usr/bin/env python3

import tkinter
import hashlib
import urllib.request
import urllib.error


class App:
  def __init__(self, master):
    frame = tkinter.Frame(master, padx=10, pady=10)
    frame.pack()

    font = ("Helvetica", 14)
    label = tkinter.Label(frame, text="Password", padx=4)
    label.pack(side=tkinter.LEFT)
    label.config(font=font)

    self.entry = tkinter.Entry(frame, show="*")
    self.entry.pack(side=tkinter.RIGHT, expand=1)
    self.entry.config(font=font)
    self.entry.bind("<Return>", self.check_pwn)
    self.entry.focus()

    frame2 = tkinter.Frame(master, pady=6)
    frame2.pack()

    button = tkinter.Button(
        frame2, text="Have I been pwned?", command=self.check_pwn
    )
    button.pack(expand=1)
    button.config(font=font)

    self.result = tkinter.Label(
        frame2, text="Click to find out."
    )
    self.result.pack(expand=1)

    frame3 = tkinter.Frame(master, pady=6)
    frame3.pack()

    attribution = tkinter.Label(
        frame3, text="Source: haveibeenpwned.com"
    )
    attribution.pack(expand=1)

  def check_pwn(self, event=None):
    password = self.entry.get()
    if (len(password) == 0):
      self.result["text"] = "Please input a password."
      return

    m = hashlib.sha1()
    m.update(bytes(password, encoding="utf-8"))
    pass_hash = m.hexdigest().upper()

    try:
      req = urllib.request.Request(
          "https://api.pwnedpasswords.com/range/%s" % pass_hash[:5],
          data=None,
          headers={
              "User-Agent": "Simple-Tkinter-Pwncheck"
          })
      data = urllib.request.urlopen(req).read().decode("utf-8")
    except urllib.error.HTTPError as error:
      self.result["text"] = "Error %s: %s" % (error.code, error.msg)
      return

    self.entry.delete(0, tkinter.END)

    items = data.splitlines()
    keyval = dict([item.split(":") for item in items])
    pwn_count = keyval.get(pass_hash[5:], None)
    if pwn_count is None:
      msg = "No."
    else:
      msg = "Yes. %s times." % pwn_count
    self.result["text"] = msg


root = tkinter.Tk()
root.title("Tkinter Pwncheck")

app = App(root)
root.mainloop()
