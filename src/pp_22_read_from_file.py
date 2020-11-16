from typing import List

with open('resources/nameslist.txt', 'r') as open_file:
    all_text = open_file.read().split('\n')
print(all_text)

my_dict = {i:all_text.count(i) for i in all_text}
print(my_dict)

open_file.close()

with open('resources/Training_01.txt') as open_images:
    list_images = open_images.read().split('\n')
# print(list_images)

new_list_images: List[str] = []
for path in list_images:
    cut_pref = path[3:]
    new_list_images.append(cut_pref)

# print(new_list_images)

category_list: List[str] = []
for i in new_list_images:
    category = i.split('/', 1)
    category_list.append(category[0])

# print(category_list)

category_dict = {i:category_list.count(i) for i in category_list}
print(category_dict)

open_images.close()
