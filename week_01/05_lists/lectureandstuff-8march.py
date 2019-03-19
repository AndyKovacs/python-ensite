my_list= [1,2,3,4,5,42]

for index, value in enumerate(my_list):
    print(f"at{index} lives {values}")



def my:function(name, age=13,*args,**kwargs):
    print(name)
    print(args[-1])
    for item in args:
        print(item)


my_funct('martin',1,4,'hello','etc.')

def fun(**kwargs): # two stars creates a dict, * star creates a tuple
    for key, value in kwargs.items():
        print(f"{key}maps to{value}.")
    fun(name="martin", number=1,greetings="hello")
