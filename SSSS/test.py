import os

print("当前工作目录为:", os.getcwd())
topic = "sssssssss"

# # Create folder structure
# if not os.path.isdir("D:/afterWork/SSSS/results/"):
#     os.mkdir('D:/afterWork/SSSS/results/')

# Create folder structure
if not os.path.isdir("./results/"):
    os.mkdir('D:/afterWork/SSSS/results/')
    print("???")
else:
    print("!!!")
    # os.mkdir('../results')

# if not os.path.isdir("../results/topics/"):
#     os.mkdir('../results/topics/')

# if not os.path.isdir("../results/topics/{}/".format(topic)):
#     os.mkdir('../results/topics/{}/'.format(topic))