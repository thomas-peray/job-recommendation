import tkinter as tk
import customtkinter as ctk

def clear_frame(frame):
   for widgets in frame.winfo_children():
      widgets.destroy()


def launch_interface():
    
    def search():
        pass
    
    ctk.set_appearance_mode("system")
    ctk.set_default_color_theme("dark-blue")

    window = ctk.CTk()
    window.geometry("1000x700")
    window.title("Job recommendation")

    mainframe = ctk.CTkFrame(window)
    mainframe.pack(fill="both", expand=True)
    
    title_frame = ctk.CTkFrame(mainframe)
    title_frame.pack(fill="x", side="top")

    label = ctk.CTkLabel(title_frame, text="Job recommendation", font=("Roboto", 24))
    label.pack(pady=12, padx=10)
    
    input_frame = ctk.CTkFrame(mainframe)
    input_frame.pack(fill="x", side="top")
    
    # === Experience ===
    experience_frame = ctk.CTkFrame(input_frame)
    experience_frame.pack(fill="x", side="left")
    
    label_exp = ctk.CTkLabel(experience_frame, text="Experience", font=("Roboto", 14))
    label_exp.pack(pady=12, padx=10, side="top")
    
    min_years = [str(i) for i in range(6)]
    min_year_exp = ctk.CTkComboBox(experience_frame, values=min_years)
    min_year_exp.pack(side="left")
    
    label_to= ctk.CTkLabel(experience_frame, text="to", font=("Roboto", 12))
    label_to.pack(padx=12, side="left")
    
    max_years = [str(i) for i in range(5, 16)]
    max_year_exp = ctk.CTkComboBox(experience_frame, values=max_years)
    max_year_exp.pack(side="left")
    
    # === Qualification ===
    qualifications_frame = ctk.CTkFrame(input_frame)
    qualifications_frame.pack(fill="x", side="left", padx=8)
    
    label_qual = ctk.CTkLabel(qualifications_frame, text="Qualification", font=("Roboto", 14))
    label_qual.pack(pady=12, padx=10, side="top")
    
    qualifications = ["B.Com", "B.Tech", "BA", "BBA", "M.Com", "M.Tech", "MBA", "MCA", "PhD"]
    qualifications_cbox = ctk.CTkComboBox(qualifications_frame, values=qualifications)
    qualifications_cbox.pack(side="top")
    
    # === Salaray Range ===
    salary_frame = ctk.CTkFrame(input_frame)
    salary_frame.pack(fill="x", side="left")
    
    label_salary = ctk.CTkLabel(salary_frame, text="Salary Range", font=("Roboto", 14))
    label_salary.pack(pady=12, padx=10, side="top")
    
    min_salary = ctk.CTkEntry(salary_frame, placeholder_text="Min range (in $K)")
    min_salary.pack(side="left")
    
    label_to = ctk.CTkLabel(salary_frame, text="to", font=("Roboto", 12))
    label_to.pack(padx=12, side="left")
    
    max_salary = ctk.CTkEntry(salary_frame, placeholder_text="Max range (in $K)")
    max_salary.pack(side="left")
    
    # === Location ===
    location_frame = ctk.CTkFrame(input_frame)
    location_frame.pack(fill="x", side="left", padx=8)
    
    label_loc = ctk.CTkLabel(location_frame, text="Location", font=("Roboto", 14))
    label_loc.pack(pady=12, padx=10, side="top")
    
    entry_location = ctk.CTkEntry(location_frame, placeholder_text="Douglas, New York, ...")
    entry_location.pack(side="left")
    
    # === Country ===
    input_frame2 = ctk.CTkFrame(mainframe)
    input_frame2.pack(fill="x", side="top")
    
    country_frame = ctk.CTkFrame(input_frame2)
    country_frame.pack(fill="x", side="left")
    
    label_country = ctk.CTkLabel(country_frame, text="Country", font=("Roboto", 14))
    label_country.pack(pady=12, padx=10, side="top")
    
    entry_country = ctk.CTkEntry(country_frame, placeholder_text="France, Spain, ...")
    entry_country.pack(side="left")
    
    # === Work type ===
    work_type_frame = ctk.CTkFrame(input_frame2)
    work_type_frame.pack(fill="x", side="left", padx=8)
    
    label_wt = ctk.CTkLabel(work_type_frame, text="Work type", font=("Roboto", 14))
    label_wt.pack(pady=12, padx=10, side="top")
    
    work_types = ["Contract", "Full-time", "Intern" "Part-time", "Temporary"]
    work_types_cb = ctk.CTkComboBox(work_type_frame, values=work_types)
    work_types_cb.pack(side="left")
    
    # === Company size ===    
    company_size_frame = ctk.CTkFrame(input_frame2)
    company_size_frame.pack(fill="x", side="left")
    
    label_cs = ctk.CTkLabel(company_size_frame, text="Compagny Size", font=("Roboto", 14))
    label_cs.pack(pady=12, padx=10, side="top")
    
    company_size = ["Small (12,000 to 40,000)", "Medium (40,000 to 100,000)", "Large (100,000+)"]
    company_size_cb = ctk.CTkComboBox(company_size_frame, values=company_size)
    company_size_cb.pack(side="left")
    
    # === Genre ===
    genre_frame = ctk.CTkFrame(input_frame2)
    genre_frame.pack(fill="x", side="left", padx=8)
    
    label_cs = ctk.CTkLabel(genre_frame, text="Genre", font=("Roboto", 14))
    label_cs.pack(pady=12, padx=10, side="top")
    
    genres = ["Female", "Male"]
    genre_cb = ctk.CTkComboBox(genre_frame, values=genres)
    genre_cb.pack(side="left")
    
    btn_search = ctk.CTkButton(input_frame2, text="Search", command=search)
    btn_search.pack(pady=12, padx=10, side="right")
    
    # === Job results
    label_jr = ctk.CTkLabel(mainframe, text="Job recommended", font=("Roboto", 14))
    label_jr.pack(pady=12, padx=10, side="top")
    
    scrollable_frame = ctk.CTkScrollableFrame(mainframe, width=200, height=400)
    scrollable_frame.pack(fill="x", side="top")
        

    window.mainloop()