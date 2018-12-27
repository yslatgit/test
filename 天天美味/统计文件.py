import os
os.chdir(r'C:\Users\Administrator\Downloads')
# list = os.listdir(r'C:\Users\Administrator\Downloads')
list = os.listdir()

rule = ['xlsx','docx','zip']

# def filterFile(kzm):
#     global m
#     m = 0
#     for i in list:
#         # if kzm in i:
#         #     m += 1
#         #     print(m,i)
#         if u'微信' in i:
#             print(i)
#             path = os.getcwd() + '\\' + i
#             os.remove(path)



if __name__ == '__main__':
    # filterFile('zip')
    print(list)