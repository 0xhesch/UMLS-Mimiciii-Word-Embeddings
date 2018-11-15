# -*- coding: utf-8 -*-
"""

"""
import psycopg2

conn=psycopg2.connect("dbname='mimic' user='postgres' host='localhost' password='root'")

cur = conn.cursor()
cur.execute("""SELECT text, hadm_id FROM mimiciii.noteevents WHERE category='Discharge summary'""")
raw_text = cur.fetchall()
f = open("fastformat.txt", "w+")
for entry in raw_text:
    cur.execute("""SELECT icd9_code FROM mimiciii.diagnoses_icd WHERE hadm_id=%s""", [entry[1]])
    icd_codes_per_note = cur.fetchall()
    for icd_code in icd_codes_per_note:
        if(icd_code[0] is not None):
            f.write("__label__" + icd_code[0] + " ")
    f.write(entry[0].replace('\n', '') + '\n')
            
