# # String, Interger, Boolean, List, Float

# # Dictionary (Object)

# information = {
#     # key: value
#     "do_kho": ['snack', 'thit bo kho'], 
#     "dong_lanh": {
#         "do_song": "",
#         "do_gan_chin": [],
#         "do_da_chin": "Khong co do"
#     }, 
#     "is_open": True, # Accepted all type of data with value
#     "gia_dung": "chao ran"
# }

# # C.R.U.D
# # Create
# # Read
# # Update
# # Delete

# # Get value by key

# print(
#     #  dictionary["key"]
#     information["do_kho"]
# )

# # Update value by value

# # information["dong_lanh"]["do_song"].append("ca che")
# # information['dong_lanh']["do_da_chin"] = "ca kho lang vu dai"
# # print(information["dong_lanh"]["do_song"])

# # Delete key from dictionary
# del information["is_open"]

# print(information)



class_info = [
    {
        "name": "Nam Khanh",
        "age":  16,
        "sex": "Male"
    },
    {
        "name": "Long",
        "age": 15,
        "sex": "Male",
    },
    {
        "name": "Linh",
        "age": 17,
        "sex": "Female"
    }
]

# for item in class_info:
#     print(item)

for item in class_info:
    if item["sex"] == "Female":
        print(item)
