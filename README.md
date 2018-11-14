# mimiciii-AI
This repository contains various format adaptions to convert and process [MIMIC-III](https://github.com/MIT-LCP/mimic-code)  datasets for use in machine learning environments. For all tasks PostgreSQL with [Psycopg](https://github.com/psycopg/psycopg2) python adapter has been used.

# fastText
The [fastText](https://github.com/facebookresearch/fastText) library can be used for ICD label prediction task. For this purpose a text file with the format of containing one training sentence per line with the labels is required. In order to apply fastText to MIMIC noteevents ICD labels have to be prefixed by a `__label__` string among discharge summary text (per line).
