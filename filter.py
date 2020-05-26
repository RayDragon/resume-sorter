from pprint import pprint
import os
from findNames import get_human_names
from toText import text
from word_count import w_count
from extract_phone import extract_phone
import pandas as pd
from shutil import move

base = os.path.dirname(os.path.realpath(__file__))

files = [os.path.join(base, 'data', f) for f in os.listdir(
    os.path.join(base, 'data')) if os.path.isfile(os.path.join(base, 'data', f))]

skills = [x.strip() for x in 'python,php,sql, git'.split(',')]
data = []
for index in range(len(files)):
    print("Done : ", (index+1)*100//len(files), ' %')
    f = files[index]
    try:
        t = text(f)
        #names = get_human_names(data)
        #print('Names found:', names)
        # print(t)
        phone = extract_phone(t)
        wc = w_count(t, skills)
        wc['phone'] = ', '.join(phone)
        wc['file'] = f
        if wc['score'] > 0:
            data.append(wc)
            f = move(f, os.path.join(base, 'sortlisted'))
            wc['file'] = f
    except Exception as e:
        print("Some error occurred, skipping file...", str(e))

if len(data) != 0:
    data.sort(key=lambda x: x['score'], reverse=True)
    cols = ['phone', 'score']
    cols.extend(skills)
    cols.append('file')
    df = pd.DataFrame(data).loc[:, cols]
    df.to_excel('result.xlsx', sheet_name='default')
else:
    print("Sorry, no such result found")
