user_name_ = input("请输入名字:")
user_year = int(input("请输入年龄:"))
print(f"您好，尊敬的{user_name_}您今年{user_year}岁了")


user_name=input("请输入姓名：")
age = int(input("请输入年龄"))
if age < 18:
    print(f"您好，尊敬的{user_name},您今年{age}岁了,属于未成年哟！")
if age>=18 and age <60:
    print(f"您好，尊敬的{user_name},您今年{age}岁了,属于强壮的大好青年！今天的你也要好好的加油哟！")
if age >=60:
    print(f"您好，尊敬的{user_name},您今年{age}岁了,属于老年人了，要注意身体健康，每日放松心情，维持好的身心！")

user_name=input("请输入姓名：")
age = int(input("请输入年龄"))
if age < 18:
    print(f"您好，尊敬的{user_name},您今年{age}岁了,属于未成年哟！")
elif age < 60:
    print(f"您好，尊敬的{user_name},您今年{age}岁了,属于强壮的大好青年！今天的你也要好好的加油哟！")
else:
    print(f"您好，尊敬的{user_name},您今年{age}岁了,属于老年人了，要注意身体健康，每日放松心情，维持好的身心！")