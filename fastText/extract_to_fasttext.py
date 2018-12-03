
# -*- coding: utf-8 -*-
# Copyright (C) 2018 Henning S.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import psycopg2

#connection string
conn=psycopg2.connect("dbname='mimic' user='postgres' host='localhost' password='xx'")

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
   
