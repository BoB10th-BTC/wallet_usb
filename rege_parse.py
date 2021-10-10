import winreg as reg
import os     

key = reg.HKEY_LOCAL_MACHINE
regPath = r"SYSTEM\ControlSet001\Enum\USB"
result = []
flag = 0
op = reg.OpenKey(key,regPath,0,reg.KEY_ALL_ACCESS)
#name, value, type = reg.EnumKey(op,0)
try :
    count = 0
    while 1:    
        name = reg.EnumKey(op,count)
        result.append(name)
        count += 1
except WindowsError:
    pass

for i in result:
    key_value = r"SYSTEM\ControlSet001\Enum\USB\%s" % i
    op = reg.OpenKey(key,key_value,0,reg.KEY_ALL_ACCESS)
    name = reg.EnumKey(op,0)
    key_value = key_value +'\\'+ name
    print(key_value)
    op = reg.OpenKey(key,key_value,0,reg.KEY_ALL_ACCESS)
    try:
        count = 0
        while 1:
            #value, type = reg.QueryValueEx(open,"FriendlyName")
            name, value, type = reg.EnumValue(op,count)
            #print(name)
            if "FriendlyName" in name:
                value, type = reg.QueryValueEx(op,"FriendlyName")
                if value == "Nano S":
                    flag = 1
                    break
            count +=1
    except FileNotFoundError:
        pass
    except WindowsError:
        pass
if flag == 1:
    print('-------NANO S Found-------')
else:
    print("FriendlyName not found")

reg.CloseKey(op)
 