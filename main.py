import data_processing as dp
import user_interface as ui

evidence, labels = dp.load_data("job_profiles.csv")

ui.launch_interface()
