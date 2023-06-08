data = "level=info msg='C:\Program Files\Lacework\osqueryi.exe has a valid signature' caller='Util.cpp:206' pid=1048"


if 'has a valid signature' in data:
    print('yes')
else:
    print('NO')
