#'Sometime heaven doesn't ordain a companion for us, some of us  are meant to  travel alone...'

#IMPORTING LIBS AND RESOURCES
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import  os
import  random
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle , Spacer
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


uplifter_thought = [
    '"Success is stumbling from failure to failure with no loss of enthusiasm." - Winston Churchill',
    '"Success is not final, failure is not fatal: it is the courage to continue that counts." - Winston Churchill',
    '"The only way to do great work is to love what you do." - Steve Jobs',
    '"This inspiring quote can encourage students not to focus on their limitations but on their unique strengths." - Canva',
    '"Paper has more patience than people" - Anne Frank',
    '"success has many fathers, failure is an orphan" - John F. Kennedy'
    'THIS PROJECT IS DEVELOPED BY `V`-'
]
rand_var = random.randint(0, 5)
thought = uplifter_thought[rand_var]

xlsx_file_paths = []


def export_pdf():
    pass
    root.after(7000, root.destroy)

def select_folder():
    xlsx_file_paths.clear()

    folder_path = filedialog.askdirectory()
    if folder_path:
        selected_folder_label.config(text=f"Selected Folder: {folder_path}")
        for root_folder, subfolders, filenames in os.walk(folder_path):
            for filename in filenames:
                if filename.endswith(".xlsx"):
                    xlsx_file_paths.append(os.path.join(root_folder, filename))

        for varg in xlsx_file_paths:
            print(varg)

    else:
        selected_folder_label.config(text="No folder selected")



root=tk.Tk()

style=ttk.Style(root)
root.tk.call("source","forest-dark.tcl")
style.theme_use('forest-dark')



frame=ttk.Frame(root)
frame.pack()


features_label_1=ttk.LabelFrame(frame,text='User Interface  ')
features_label_1.grid(row=0,column=0,padx=21,pady=22)

folder_path_label = tk.Label(features_label_1, text="Select Excel file folder: ")
folder_path_label.grid(row=0,column=0,padx=10,pady=10)

select_button = tk.Button(features_label_1, text="Select File", command=select_folder)
select_button.grid(row=1,column=0,padx=10,pady=10)
selected_folder_label = tk.Label(root, text="")
selected_folder_label.pack(padx=10, pady=10)


pdf_file_label = tk.Label(features_label_1, text="Export to excel & PDF: ")
pdf_file_label.grid(row=2,column=0,padx=10,pady=10)

pdf_export_button = tk.Button(features_label_1, text="Export", command=export_pdf)
pdf_export_button.grid(row=3,column=0,padx=10,pady=10)




treeFrame=ttk.Frame(frame)
treeFrame.grid(row=0,column=1,pady=10)
treescroll=ttk.Scrollbar(treeFrame)
treescroll.pack(side='right',fill='y')


treeview=ttk.Treeview(treeFrame,columns=('Division','RollNo','Name','Marks'),
                      yscrollcommand=treescroll.set,height=14)

treeview.column('Division',width=50)
treeview.column('RollNo',width=90)
treeview.column('Name',width=190)
treeview.column('Marks',width=65)


treeview.pack()
treescroll.config(command=treeview.yview)

cols=('Rank','RollNo','Name','Division','Marks')


output_frame=ttk.Frame(frame)
output_frame.grid(row=0,column=2,padx=15,pady=10,sticky='ew')

cols2=('median','avg','mod','maxi')
treeview2=ttk.Treeview(output_frame,show='headings',columns=cols2,height=3)
treeview2.column('median',width=45)
treeview2.column('avg',width=45)
treeview2.column('mod',width=45)
treeview2.column('maxi',width=45)
treeview2.pack()


root.mainloop()



data_frames_list=[]

for file_path in xlsx_file_paths:
    if file_path.endswith('.xlsx'):
        df = pd.read_excel(file_path,header=1)
        # Group by 'RollNo' and calculate the average marks
        avg_marks_df = df.groupby('RollNo')['Total'].mean().reset_index()
        # Add the calculated average marks to the original data frame
        df = pd.merge(df, avg_marks_df, on='RollNo', how='left', suffixes=('', '_avg'))
        data_frames_list.append(df)

# Concatenate the data frames
master = pd.concat(data_frames_list, ignore_index=True)

# Drop duplicate rows based on 'RollNo' to keep only the first occurrence
master = master.drop_duplicates(subset='RollNo', keep='first')


avg_marks_df = master.groupby('RollNo')['Total'].mean().reset_index()
avg_marks_df.rename(columns={'Total': 'avg_mark'}, inplace=True)


finalx_df=pd.DataFrame({'Division':master['Division'],
                        'RollNo':master['RollNo'],
                        'Student name':master['Name'],
                        'avg_marks':avg_marks_df['avg_mark'],
                        'Category':master['Category']
                        })




sorted_data_final = finalx_df.sort_values(by='avg_marks', ascending=False)
sorted_data_final['avg_marks'].plot()
sorted_data_final['SerialNumber'] = range(1, len(sorted_data_final) + 1)
# Move 'SerialNumber' column to the leftmost position
sorted_data_final = sorted_data_final[['SerialNumber'] + [col for col in sorted_data_final.columns if col != 'SerialNumber']]

plt.ylabel('avg_marks')
plt.xlabel('RollNo')
plt.show(block=True)
plt.savefig('my_plot.pdf', format='pdf')


sorted_data_final.to_excel('output_gen_V.xlsx',index=False)

#_________________________________________________________________________________________________________


data_analyser=pd.DataFrame({''

                        })

#__________________________________________________________________________________________________________


pdf_file = 'output_gen_V.pdf'

doc = SimpleDocTemplate(pdf_file, pagesize=letter)


# Convert the DataFrame to a list of lists (table data)
table_data = [sorted_data_final.columns.tolist()] + sorted_data_final.values.tolist()
# Move 'SerialNumber' column to the leftmost position in table_data
table_data = [table_data[0]] + [table_data[i][-1:] + table_data[i][:-1] for i in range(1, len(table_data))]


# Create a Table object
table = Table(table_data)

# Add style to the table (optional)
style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), (30 / 255, 31 / 255, 30 / 255)),  # Header row background color
                        ('TEXTCOLOR', (0, 0), (-1, 0), (1, 1, 1)),  # Header text color
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center alignment
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Header font
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Header padding
                        ('BACKGROUND', (0, 1), (-1, -1), (0.9, 0.9, 0.9)),  # Table body background color
                        ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0)),  # Table grid lines
                        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),  # Body font
                        ('ALIGN', (0, 1), (-1, -1), 'CENTER'),  # Body alignment
                        ('LEFTPADDING', (0, 0), (-1, -1), 6),  # Body padding
                        ('RIGHTPADDING', (0, 0), (-1, -1), 6)])  # Body padding

paragraph = Paragraph(thought)
table.setStyle(style)
spacing = Spacer(1, 50)
# Build the PDF document
elements = [table, spacing, paragraph]
doc.build(elements)
#print(f'PDF file "{pdf_file}" created successfully.')
#print(sorted_data_final)



#-----------------------------------------------------------------------------------------------------------------------------------------------------