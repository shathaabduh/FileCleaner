# FileCleaner
Must have these two libraries:
- pandas
- openpyxl

The script accept either excel or text files which contains recipient numbers. The main purpose of this script is to ensure contact numbers are written in a proper format with no spaces, special characters, and duplicates. Furthermore, it adds the country code, removes all numbers that exceed 12 digits in respect of the country, and removes all banks from the excel file.
This is following the regulations of sending bulk messages for campaigns. In which each message body accept a particular number of recipients. Hence, this script ensures that the contact numbers are in the correct format to cut costs and the files are divided in respect of the message body size.

Message body takes 300K characters/ 30min 
1 unit = 300K
2 units = 150K
3 units = 100K
4 units = 75k
5 units = 60k
6 units = 50k
7 units = 42k
8 units =37.5k
9 units = 33k
10 units = 30K
