import tkinter as tk
import customtkinter as ctk
import job_recommender as jr

def clear_frame(frame):
   for widgets in frame.winfo_children():
      widgets.destroy()


def launch_interface():
    
    def search():
        # Reset the result frame
        clear_frame(scrollable_frame)
        
        experience_min = min_year_exp.get()
        experience_max = max_year_exp.get()
        experience = f"{experience_min} to {experience_max} Years"
        
        qualifications = qualifications_cbox.get()

        salary_min = min_salary.get()
        salary_max = max_salary.get()
        salary_range = f"${salary_min}K-${salary_max}K"
        
        skills = entry_skills.get()
        
        profile = {
            'Experience': experience,
            'Qualifications': qualifications,
            'Salary Range': salary_range,
            'Skills': skills,
        }
        
        predictions = jr.predict(profile)
        
        for p in predictions:
            result_frame = ctk.CTkFrame(scrollable_frame)
            result_frame.pack(fill="x", side="top", pady=8)
            
            label_title = ctk.CTkLabel(result_frame, text=p['Job Title'], font=("Roboto", 14))
            label_title.pack(pady=4, side="top")
            
            infos = p["Salary Range"] + " · " + p["Experience"]
            label_infos = ctk.CTkLabel(result_frame, text=infos, font=("Roboto", 14))
            label_infos.pack(pady=4, side="top")
            
            label_description = ctk.CTkLabel(result_frame, text=p['Job Description'], font=("Roboto", 12))
            label_description.pack(pady=4, side="top")
        
            

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
    
    label_to = ctk.CTkLabel(experience_frame, text="to", font=("Roboto", 12))
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
    
    # === Skills ===
    skills_frame = ctk.CTkFrame(input_frame)
    skills_frame.pack(fill="x", side="left", padx=8)
    
    label_skills = ctk.CTkLabel(skills_frame, text="Skills", font=("Roboto", 14))
    label_skills.pack(pady=12, padx=10, side="top")
    
    entry_skills = ctk.CTkEntry(skills_frame, placeholder_text="some skills, with space between",  width=200)
    entry_skills.pack(side="left")
    
    # === Search button ===
    search_frame = ctk.CTkFrame(mainframe)
    search_frame.pack(fill="x", side="top")
    
    search_button = ctk.CTkButton(search_frame, text="Search", command=search)
    search_button.pack(pady=12, padx=10, side="top")

    
    # === Job results
    label_jr = ctk.CTkLabel(mainframe, text="Job recommended (take about 10 second to process, please wait after clicking Search)", font=("Roboto", 14))
    label_jr.pack(pady=12, padx=10, side="top")
    
    scrollable_frame = ctk.CTkScrollableFrame(mainframe, width=200, height=400)
    scrollable_frame.pack(fill="x", side="top")

    window.mainloop()