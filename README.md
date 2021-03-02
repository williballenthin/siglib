## build

```sh
docker build -t buildtools:latest --isolation=hyperv --network "Default Switch"  --memory 2GB .
```

## contents

```
PS C:\> dir -Path C:\ -Filter libcmt.lib -Recurse -ErrorAction SilentlyContinue -Force | %{$_.FullName}
C:\BuildTools\VC\Tools\MSVC\14.16.27023\lib\onecore\x64\libcmt.lib
C:\BuildTools\VC\Tools\MSVC\14.16.27023\lib\onecore\x86\libcmt.lib
C:\BuildTools\VC\Tools\MSVC\14.16.27023\lib\x64\libcmt.lib
C:\BuildTools\VC\Tools\MSVC\14.16.27023\lib\x86\libcmt.lib
C:\BuildTools\VC\Tools\MSVC\14.28.29333\lib\onecore\x64\libcmt.lib
C:\BuildTools\VC\Tools\MSVC\14.28.29333\lib\onecore\x86\libcmt.lib
C:\BuildTools\VC\Tools\MSVC\14.28.29333\lib\x64\libcmt.lib
C:\BuildTools\VC\Tools\MSVC\14.28.29333\lib\x86\libcmt.lib
C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\lib\libcmt.lib
C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\lib\amd64\libcmt.lib
C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\lib\arm\libcmt.lib
C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\lib\onecore\libcmt.lib
C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\lib\onecore\amd64\libcmt.lib
C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\lib\onecore\arm\libcmt.lib
PS C:\> ```


MSVC++ version  _MSC_VER 
?????   ??? Visual Studio 2015                   v140
14.16 	1916 (Visual Studio 2017 version 15.9)   v141
14.2 	1920 (Visual Studio 2019 Version 16.0)
14.21 	1921 (Visual Studio 2019 Version 16.1)
14.22 	1922 (Visual Studio 2019 Version 16.2)
14.23 	1923 (Visual Studio 2019 Version 16.3)
14.24 	1924 (Visual Studio 2019 Version 16.4)
14.25 	1925 (Visual Studio 2019 Version 16.5)
14.26 	1926 (Visual Studio 2019 Version 16.6)
14.27 	1927 (Visual Studio 2019 Version 16.7)
14.28 	1928 (Visual Studio 2019 Version 16.8)   v142
https://en.wikipedia.org/wiki/Microsoft_Visual_C%2B%2B


Microsoft.VisualStudio.Component.VC.140              MSVC v140 - VS 2015 C++ build tools (v14.00)

Microsoft.VisualStudio.Component.VC.v141.x86.x64     MSVC v141 - VS 2017 C++ x64/x86 build tools (v14.16)
Microsoft.VisualStudio.Component.VC.v141.CLI.Support C++/CLI support for v141 build tools (14.16)

Microsoft.VisualStudio.Component.VC.Tools.x86.x64    MSVC v142 - VS 2019 C++ x64/x86 build tools (v14.28)
Microsoft.VisualStudio.Component.VC.CLI.Support      C++/CLI support for v142 build tools (14.28)