# import re
#
# with open('day1.txt', 'r') as file:
#     # 逐行读取文件内容
#     for line in file:
#         # 检查行中是否包含AM或PM
#         if 'AM' in line or 'PM' in line:
#             # 如果包含AM或PM，打印该行文本
#             print(line.strip())

# import openpyxl
#
# # 创建一个新的Excel工作簿
# workbook = openpyxl.Workbook()
# # 选择第一个工作表
# sheet = workbook.active
#
# # 打开包含AM和PM的文本文件
# with open('day2.txt', 'r') as file:
#     row_index = 1  # 从第一行开始写入Excel
#     # 逐行读取文件内容
#     for line in file:
#         # 检查行中是否包含AM或PM
#         if 'AM' in line or 'PM' in line:
#             # 将该行文本写入Excel的第一行第一列
#             sheet.cell(row=row_index, column=1, value=line.strip())
#             row_index += 1
#         if 'October 15, 2023' in line:
#             sheet.cell(row=row_index, column=2, value=line.strip())
#             row_index += 1
#         if 'PAID' in line or 'UNPAID' in line:
#             # 将该行文本写入Excel的第一行第一列
#             sheet.cell(row=row_index, column=3, value=line.strip())
#             row_index += 1
#     # row_index = 1  # 从第一行开始
#     # for line in file:
#     #     # 在第一行第二列写入文本
#
#
#
# # 保存Excel文件
# workbook.save('output.xlsx')


# -------------------------------------------
# import openpyxl
#
# # 创建一个新的Excel工作簿
# workbook = openpyxl.Workbook()
# # 选择第一个工作表
# sheet = workbook.active
#
# # 打开包含AM和PM的文本文件
# with open('day6.txt', 'r') as file:
#     row_index = 1  # 从第一行开始写入Excel
#     for line in file:
#         # # 检查行中是否包含AM或PM
#         # if 'AM' in line or 'PM' in line:
#         #     # 将该行文本写入Excel的第一行第一列
#         #     sheet.cell(row=row_index, column=1, value=line.strip())
#         #     row_index += 1
#         # # 检查行中是否包含日期
#         if ' Minutes' in line:
#             # 将日期信息写入Excel的第一行第二列
#             sheet.cell(row=row_index, column=2, value=line.strip())
#             row_index += 1
#         # 检查行中是否包含"PAID"或"UNPAID"
#         # if 'PAID' in line or 'UNPAID' in line:
#         #     # 将付款状态信息写入Excel的第一行第三列
#         #     sheet.cell(row=row_index, column=3, value=line.strip())
#         #     row_index += 1
#
# # 保存工作簿为Excel文件
# workbook.save('output.xlsx')



# --------------------------------------
# import openpyxl
#
# # 创建一个新的Excel工作簿
# workbook = openpyxl.Workbook()
# # 选择第一个工作表
# sheet = workbook.active
#
# # 打开包含AM和PM的文本文件
# with open('day2.txt', 'r') as file:
#     row_index = 1  # 从第一行开始写入Excel
#     for line in file:
#         # 检查行中是否包含AM或PM
#         if 'AM' in line or 'PM' in line:
#             # 将该行文本写入Excel的第一行第一列
#             sheet.cell(row=row_index, column=1, value=line.strip())
#
#         # 检查行中是否包含日期
#         if ' Minutes' in line:
#             # 将日期信息写入Excel的第一行第二列
#             sheet.cell(row=row_index, column=2, value=line.strip())
#
#         # 检查行中是否包含"PAID"或"UNPAID"
#         if 'PAID' in line or 'UNPAID' in line:
#             # 将付款状态信息写入Excel的第一行第三列
#             sheet.cell(row=row_index, column=3, value=line.strip())
#
#         # 每次迭代都增加行索引
#         row_index += 1
#
# # 保存工作簿为Excel文件
# workbook.save('output.xlsx')


# ---------------------------------------------------------------
# import openpyxl
#
# # 创建一个新的Excel工作簿
# workbook = openpyxl.Workbook()
# # 选择第一个工作表
# sheet = workbook.active
#
# # 打开包含AM和PM的文本文件
# with open('day1.txt', 'r') as file:
#     row_index = 1  # 从第一行开始写入Excel
#     should_write_next_line = False  # 用于标记是否应该写入下一行文本
#     for line in file:
#         # 检查行中是否包含"UNPAID"或"PAID"
#         if 'PAID' in line or 'UNPAID' in line:
#             should_write_next_line = True
#         elif should_write_next_line:
#             # 将下一行文本写入Excel的第一行
#             sheet.cell(row=row_index, column=1, value=line.strip())
#             row_index += 2
#             should_write_next_line = False
#
# # 保存工作簿为Excel文件
# workbook.save('output.xlsx')



# ---------------------------------------------
# import openpyxl
#
# # 创建一个新的Excel工作簿
# workbook = openpyxl.Workbook()
# # 选择第一个工作表
# sheet = workbook.active
#
# # 打开包含AM和PM的文本文件
# with open('day6.txt', 'r') as file:
#     row_index = 1  # 从第一行开始写入Excel
#     should_write_next_line = False  # 用于标记是否应该写入下一行文本
#     should_write_next_next_line = False  # 用于标记是否应该写入下下行文本
#     for line in file:
#         # 检查行中是否包含"UNPAID"或"PAID"
#         if 'PAID' in line or 'UNPAID' in line:
#             should_write_next_line = True
#         elif should_write_next_line:
#             should_write_next_line = False
#             should_write_next_next_line = True
#         elif should_write_next_next_line:
#             # 将下下行文本写入Excel的第一行
#             sheet.cell(row=row_index, column=1, value=line.strip())
#             row_index += 1
#             should_write_next_next_line = False
#
# # 保存工作簿为Excel文件
# workbook.save('output.xlsx')


# ------------------------------------------------
# import openpyxl
#
# workbook = openpyxl.Workbook()
#
# sheet = workbook.active
#
# with open('day6.txt', 'r') as file:
#     row_index = 1  # 从第一行开始写入Excel
#     should_write_next_line = False  # 用于标记是否应该写入下一行文本
#     should_write_next_next_line = False  # 用于标记是否应该写入下下行文本
#     for line in file:
#         # 检查行中是否包含"UNPAID"或"PAID"
#         if 'PAID' in line or 'UNPAID' in line:
#             should_write_next_line = True
#         elif should_write_next_line:
#             should_write_next_line = False
#             should_write_next_next_line = True
#         elif should_write_next_next_line:
#             # 将下下行文本写入Excel的第一行
#             sheet.cell(row=row_index, column=1, value=line.strip())
#             row_index += 1
#             should_write_next_next_line = False
#
# workbook.save('output.xlsx')


# ------------------------------------------------
# import openpyxl
#
# workbook = openpyxl.Workbook()
# sheet = workbook.active
#
# with open('day1.txt', 'r') as file:
#     row_index = 1  # 从第一行开始写入Excel
#     should_append = False
#     speakers_text = []  # 用于存储匹配到的文本行
#     for line in file:
#         # 如果匹配到"UNPAID"或"PAID"行
#         if 'UNPAID' in line or 'PAID' in line:
#             should_append = True
#             speakers_text.append(line.strip())  # 存储匹配到的行
#         # 如果匹配到"SPEAKERS"行
#         elif 'SPEAKERS' in line and should_append:
#             should_append = False
#             # 将存储的文本行写入Excel的第一列，每行一个文本
#             for text in speakers_text:
#                 sheet.cell(row=row_index, column=1, value=text)
#                 row_index += 1
#             speakers_text = []  # 清空存储的文本行
#
# workbook.save('output.xlsx')

# ------------------------------------------------
# import openpyxl
#
# workbook = openpyxl.Workbook()
# sheet = workbook.active

# with open('day1.txt', 'r') as file:
#     row_index = 1
#     should_write_next_next_line = False
#     speakers_text = []
#
#     for line in file:
#         if 'PAID' in line or 'UNPAID' in line:
#             should_write_next_next_line = True
#         elif should_write_next_next_line:
#             should_write_next_next_line = False
#             speakers_text.append(line.strip())
#
#         if 'SPEAKERS' in line or 'PM ' in line or ' PM' in line or 'AM ' in line or ' AM' in line:
#             # 匹配到"SPEAKERS"行，将下下行文本与"SPEAKERS"行一起组成一句
#             combined_text = "\n".join(speakers_text)
#             # 将组合文本写入Excel
#             sheet.cell(row=row_index, column=1, value=combined_text)
#             row_index += 1
#             speakers_text = []  # 重置speakers_text
#
# workbook.save('output.xlsx')



# -----------------------------------
# 使用正则表达式匹配所需文本
# import re
# with open('day1.txt', 'r') as file:
#     # 使用正则表达式匹配所需文本
#     # import re
#
#     pattern = r"SPEAKERS(.*?)(?=\d{1,2}:\d{2} (?:AM|PM)|$)"
#     matches = re.findall(pattern, file.read(), re.DOTALL)
#
#     if matches:
#         combined_text = "*".join([match.strip() for match in matches])
#         with open("extracted_text.txt", "w") as file:
#             # 将合并后的文本写入文件的一行
#             file.write(combined_text)
#         print("匹配的文本已保存到 extracted_text.txt 文件中")
#     else:
#         print("未找到匹配的文本")
#
# 去除回车符
# 打开包含文本的输入文件
# with open('day1.txt', 'r') as file:
#     lines = file.readlines()
#
# # 初始化存储合并文本的变量
# merged_text = ""
# start_merge = False  # 用于标记何时开始合并
#
# # 遍历每一行文本
# for line in lines:
#     if "SPEAKERS" in line:
#         # 遇到"SPEAKERS"行时停止合并
#         start_merge = False
#     if start_merge:
#         # 合并匹配到的行
#         merged_text += line.strip() + " "
#     if "UNPAID" in line:
#         # 匹配到"UNPAID"行时开始合并
#         start_merge = True
#
# # 去除末尾的空格
# merged_text = merged_text.strip()
#
# # 将合并的文本写入输出文件
# with open('output.txt', 'w') as output_file:
#     output_file.write(merged_text)

# 打开包含文本的输入文件
# with open('day1.txt', 'r') as file:
#     lines = file.readlines()
#
# # 初始化存储匹配文本的变量
# matched_text = ""
# matching_unpaid = False  # 用于标记何时开始匹配"UNPAID"行的下三行
# matching_speakers = False  # 用于标记何时开始匹配"SPEAKERS"行
#
# # 遍历每一行文本
# for line in lines:
#     if matching_unpaid:
#         matched_text += line.strip() + " "
#         unpaid_line_count += 1
#         if unpaid_line_count >= 3:
#             matching_unpaid = False
#     elif "UNPAID" in line:
#         matching_unpaid = True
#         unpaid_line_count = 0
#     elif "SPEAKERS" in line:
#         matching_speakers = True
#     elif matching_speakers:
#         break  # 如果已经匹配到"SPEAKERS"行，则停止匹配
#
# # 去除末尾的空格
# matched_text = matched_text.strip()
#
# # 将匹配的文本写入输出文件
# with open('output.txt', 'w') as output_file:
#     output_file.write(matched_text)


import re
with open('day1.txt', 'r') as file:
    input_text = file.read()

# 使用正则表达式匹配UNPAID行和下三行文本
pattern = r'UNPAID\n(.+?)\n(.+?)\n(.+?)\n'
match = re.search(pattern, input_text, re.DOTALL)

if match:
    unpaid_text = match.group(0)
    before_text = input_text[:match.start()]
    after_text = input_text[match.end():]

    # 检查是否存在"AM"或"PM"行
    am_pm_pattern = r'AM|PM'
    am_pm_match = re.search(am_pm_pattern, input_text)

    if am_pm_match:
        am_pm_text = am_pm_match.group()

        # 将UNPAID行和下三行文本合并到"AM"或"PM"行之前
        modified_text = before_text + am_pm_text + unpaid_text  + after_text
    else:
        modified_text = before_text + "SPEAKERS\n" + unpaid_text  + after_text

    print(modified_text)
else:
    print("未找到匹配的UNPAID行")
