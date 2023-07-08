# import re

# x = """do do declare `zaqute := #(#8103 . #-5943 );done. do declare
# `argeed_327:=#( #2053 .#9360 . #9638 );done. done"""
# r = r"`(\w+)\s*:=\s*#\(\s?([^)]+)\)"
# z = re.findall(r, x)

# # res = []
# # for token in z:
# #     numbers = []
# #     for i in token[1].split("."):
# #         #print(int(i.lstrip(" #")))
# #         print(i.strip(" #")+"|")


# res = []
# for key, token in z:
#     numbers = []
#     for i in token.split("."):
#         numbers.append(int(i.lstrip(" #")))
#     res.append((key, numbers))
# print(res)
#############################################################################################################
# import re

# x = """<% do loc @'eraries' <== list("madi" "veedes_1" ). done do loc
# @'inarat_946' <== list( "reatbi" "zaenar_273"). done do loc @'atlebe'
# <== list( "zaraes""esinra""cerari"). done %>"""
# r = r"@'(\w+)'\s*<==\s*list\(([\"\w\s]+)\)"
# z = re.findall(r, x)

# res = []
# for key, values in z:
#     buff = []
#     for i in values.split('"'):
#         if i != "" and i != " ":
#             print(i)
#     #     buff.append(i.strip("\""))
#     # res.append((key, buff))
# # print(res)
#############################################################################################################
# import re

# x = """.begin {{ declare array( labige_268 vetiat )=> q(atceat_746); }}; {{
# declare array( rabite zavema dior_805 )=> q(zausri_313); }}; .end"""
# r = r"array\(([ \w]+)\)\s?=>\s?q\(([\w]+)\)"
# z = re.findall(r, x)
# print(z)

# res = []
# for values, key in z:
#     buff = []
#     for token in values.split():
#         buff.append(token)
#     res.append((key, buff))

# print(res)

#############################################################################################################
# import re

# x = """do<data> declare leer is { @'ertia' ; @'enbebi' ; @'reat_768'
# ;@'ator_627'}. </data>. <data> declare onan_197 is { @'isceis' ;
# @'ercean'; @'vebi' }. </data>. od"""
# r = r"declare \b(\w+)\b is\s?{([^}]+)}"
# z = re.findall(r, x)
# print(z)

# res = {}
# for key, values in z:
#     buff = []
#     for token in values.split(";"):
#         # print(token)
#         # print(token.strip("@' "))
#         buff.append(token.strip("@' \n"))
#     res[key] = buff
# print(res)
