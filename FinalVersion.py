import pandas as pd
import re
import sys
from collections import Counter
with open('info.txt','w') as f:
	choice = input("1 excel file\n2 text file\nEnter choice: ")
	filename = input("Enter filename: ")
	try:
		if choice == "1":
			df = pd.read_excel(f'{filename}.xlsx',usecols=[0], names=['colA'],header=None)
		elif choice == "2":
			df = pd.read_csv(f'{filename}.txt',usecols=[0], names=['colA'],header=None)
		else:
			print("Please enter correct file choice.")
			sys.exit()
	except:
		print("Please enter correct filename.")
		sys.exit()
	ext_code = input("Enter extension code: ")
	unit = int(input("1 unit for 300k\n2 unit for 150K\n3 unit for 100K\n4 unit for 75k\n5 unit for 60k\n6 unit for 50k\n7 unit for 42k\n8 unit for 37k\n9 unit for 33k\n10 unit for 30K\nEnter the unit of the message body: "))
	if unit == 1:
		unit = 300000
	elif unit == 2:
		unit = 150000
	elif unit == 3:
		unit = 100000
	elif unit == 4:
		unit = 75000
	elif unit == 5:
		unit = 60000
	elif unit == 6:
		unit = 50000
	elif unit == 7:
		unit = 42000
	elif unit == 8:
		unit = 37000
	elif unit == 9:
		unit = 33000
	elif unit == 10:
		unit = 30000
	else:
		unit=unit
	df_list = df['colA'].astype(str).to_list()
	cleanedList = [x for x in df_list if str(x) != 'nan']
	null_count = len(df_list)-len(cleanedList)
	duplicate_removed_list = list(set(cleanedList))
	duplicate_count = len(cleanedList)-len(duplicate_removed_list)
	chunks = [duplicate_removed_list[x:x+unit] for x in range(0, len(duplicate_removed_list), unit)]
	length = []
	wrong_numbers = []
	for i,chunk in enumerate(chunks):		
		speciall_list = list(map(lambda x: re.sub(r'\W+', '', str(x)),chunk))
		correct_numbers = []
		for item in speciall_list:
			if item.isdigit():
				if len(item) == 10 and list(item)[0] == '0':
					new_item = list(item)
					new_item.pop(0)
					correct_numbers.append(ext_code+"".join(new_item))
					length.append(len(item))
					continue
				if len(item) == 13:
					if list(item)[3]== '0':
						correct_numbers.append(item[:3] + item[(3+1):])
						length.append(len(item))
						continue
				if (len(item) == 12 and list(item)[0] != '0' ) or (len(item) == 9 and list(item)[0] != '0'):
					if len(item) == 9:
						correct_numbers.append(ext_code+item)
					else:
						correct_numbers.append(item)
				else:
					wrong_numbers.append(item)
			else:
				wrong_numbers.append(item)
			length.append(len(item))
		correct_numbers = list(map(int, correct_numbers))
		print(len(correct_numbers))
		dic = {
		"Numbers": correct_numbers
		}

		final_df = pd.DataFrame(dic)

		final_df.to_excel(f"{filename}-correct-{i+1}.xlsx",index=False,header=None)
	if len(wrong_numbers) > 0:

		dic1 = {
		"Numbers": wrong_numbers
		}

		final_df = pd.DataFrame(dic1)
		final_df.to_excel(f"{filename}-wrong.xlsx",index=False,header=None)
	
	f.write(f"{null_count} empty numbers\n")
	f.write(f"{duplicate_count} duplicate numbers\n")
	for key,value in Counter(length).items():
		f.write(f"{value} number with {key} digits\n")
	print("complete")

	# ext_code = input("Enter extension code: ")
	# # drop null
	# df_null=df.dropna()
	# null_count = len(df) - len(df_null)
	# f.write(f"{null_count} empty numbers\n")
	# # drop duplicate
	# df_duplicate = df_null.drop_duplicates()
	# duplicate_count = len(df) - len(df_duplicate)
	# f.write(f"{duplicate_count} duplicate numbers\n")
	# # print(df_duplicate['colA'])
	
	# # #remove special characters

	# speciall_df = df_duplicate['colA'].map(lambda x: re.sub(r'\W+', '', str(x)))
	
	# count = speciall_df.str.len()
	# value_count_dic = count.value_counts().to_dict()

	# for key,value in value_count_dic.items():
	# 	f.write(f"{value} number with {key} digits\n")
	
	# # # count frequency 

	# def add_code(numbers):
	# 	num_list = []
	# 	for num in numbers:
	# 		if len (num) == 12 or len (num) == 9:
	# 			if len (num) == 9:
	# 				num_list.append(ext_code+num)
	# 			else:
	# 				num_list.append(num)
	
	# 	return num_list

	
	

	# # # f.write(f"Duplicates - {duplicate_len}\n")
	# # # chunks = [df[x:x+100] for x in range(0, len(df), 100)]
	# # # chunk = pd.Series(chunks[0].values.flatten())
	# # # new_chunk = chunk.str.replace('\W', '')
	# # # # print(new_chunk)

	# # # for data in new_chunk:
	# # # 	print(data)
