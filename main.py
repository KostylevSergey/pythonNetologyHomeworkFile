# from datetime import datetime
# from time import sleep
# import os
#
# log_catalog_name = 'logs'
# log_file_name = 'log.txt'
# base_path = os.getcwd()
#
# full_path = os.path.join(base_path, log_catalog_name, log_file_name)
# print(full_path)
# #
# #
# # def catalog_reader(file_name):
# #     with open(file_name) as file_obj:
# #         result = {}
# #         for line in file_obj:
# #             shop_name = line.strip()
# #             goods = []
# #             for item in range(int(file_obj.readline())):
# #                 good = file_obj.readline()
# #                 goods.append(good.strip())
# #             result[shop_name] = goods
# #             file_obj.readline()
# #         return result
# #
# #
# #
# #
# # #
# # catalog = catalog_reader(file_name)
# # pprint(catalog)
#
# def logger(file_path, data):
#     with open(file_path, 'a') as file_obj:
#         prepare_data = f'{datetime.now()} | {data}'
#         file_obj.write(f'{prepare_data}\n')
#
# for i in range(30):
#     logger(full_path, 'data')
#     print('...')

cp_file = 'cp1251.txt'
utf_file = 'utf.txt'
data = 'Привет Мир'
# with open(utf_file, 'w', encoding='cp1251') as file:
#     file.read()

with open(cp_file, 'r', encoding='utf-8') as file:
    print(file.read())



