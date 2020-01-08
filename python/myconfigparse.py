import configparser

config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())

# 即使读取文件不存在 也不会抛错  只是内容为空

config.read('efi.ini')
print(config.sections())   #  []



"""  file like :
[DEFAULT]
ServerAliveInterval = 45
Compression = yes
CompressionLevel = 9
ForwardX11 = yes

[bitbucket.org]
User = hg

[topsecret.server.com]
Port = 50022
ForwardX11 = no

[getmethod]
t1= yes
t2 = on
t3 = true
t4 = True
t5 = 1
f1 = no
f2 = off
f3 = false
f4 = 0

"""
config.read('resource/efi.ini')
print(config.sections())    # ['bitbucket.org', 'topsecret.server.com']
print(config['topsecret.server.com'].get('ForwardX112', "must use section"))

# 默认section里的所有参数 都会出现在其他section里
for key in config['bitbucket.org']:
    print(key)
"""
    user
    compressionlevel
    serveraliveinterval
    compression
    forwardx11
"""



getbool = config['getmethod']
assert getbool.getboolean('t1') is True
assert getbool.getboolean('t2') is True
assert getbool.getboolean('t3') is True
assert getbool.getboolean('t4') is True
assert getbool.getboolean('t5') is True
assert getbool.getboolean('f1') is False
assert getbool.getboolean('f2') is False
assert getbool.getboolean('f3') is False
assert getbool.getboolean('f4') is False


# 在创建时需要interpolation=configparser.ExtendedInterpolation()
paths = config['Paths']
print(paths['home_dir'])    # /Users
print(paths['my_dir'])      # /Users/lumberjack
paths['output'] = '/coffee'
print(paths['my_custom_dir'])   #   /coffee/logs
