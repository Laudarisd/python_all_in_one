
# # Break csv rows and generate multiple csv files

# In[24]:


from itertools import groupby
import csv

with open('train.csv') as csv_file:
    reader = csv.reader(csv_file)
    next(reader) #skip header
    
    #Group by column (id)
    lst = sorted(reader, key=lambda x : x[6])
    groups = groupby(lst, key=lambda x : x[6])

    #Write file for each id
    for k,g in groups:
        filename = k + '.csv'
        with open(filename, 'w', newline='') as fout:
            csv_output = csv.writer(fout)
            csv_output.writerow(["x","y","z","vx","fz","time","id","type"])  #header
            #sortedlist = sorted(lst, key=lambda row: row[5], reverse=True)
            for line in g:
                #csv_output.writerow(line)
                csv_output.writerow(line)


# # Sort csv columns at once in multiple csv files

# In[119]:


import csv
import operator
import glob
import pandas as pd

data = dict() # filename : lists

path="./csv/*.csv"
files=glob.glob(path)
for filename in files:
    df = pd.read_csv(sorted(filename))
    df.sort_values('time', inplace=True)
    df.to_csv(filename, index=False)


# In[145]:


import os
import glob
import pandas as pd
import shutil
from natsort import natsorted
extension = 'csv'
all_filenames = [i for i in natsorted(glob.glob('*.{}'.format(extension)))]
#srt_files = natsorted(all_filenames)
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')



# # Combined all csv files in one csv

# In[107]:


extension = 'csv'
all_filenames = [i for i in sorted(glob.glob('*.{}'.format(extension)))]


# In[ ]:


#sorted(glob.glob('/home/c/*.csv'))
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')

