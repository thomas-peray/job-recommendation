import tkinter as tk
import customtkinter as ctk
import data_processing as dp

def clear_frame(frame):
   for widgets in frame.winfo_children():
      widgets.destroy()


ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")

window = ctk.CTk()
window.geometry("1000x600")
window.title("Job recommendation")

mainframe = ctk.CTkFrame(window)
mainframe.pack(fill="both", expand=True)

evidence, labels = dp.load_data("job_profiles.csv")


window.mainloop()

