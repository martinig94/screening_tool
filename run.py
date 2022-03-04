import pandas as pd
from utils import *

folder_path ='here the path to the folder containing the PDFs'
index_list, name_list, list_files = get_file_name_info(folder_path)

email_list =[]
for i in range(len(list_files)):
    file_path = os.path.join(folder_path, list_files[i])
    email_address = get_email(file_path)
    email_list.append(email_address)

df = pd.DataFrame({'Applicant id': index_list, 'Name Surname': name_list, 'email_address': email_list})