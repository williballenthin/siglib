## build

```sh
docker build -t buildtools:latest --isolation=hyperv --network "Default Switch"  --memory 2GB .
```

### build a lib via vcpkg

available triplets:

  - `x64-windows-static-v140` - VS 2015 x64
  - `x64-windows-static-v141` - VS 2017
  - `x64-windows-static-v142` - VS 2019
  - `x86-windows-static-v140` - VS 2015 x86
  - `x86-windows-static-v141` - VS 2017
  - `x86-windows-static-v142` - VS 2019

invoke vcpkg via Docker container:

```
docker volume create libs
docker run -it `
  --network "Default Switch" `
  -v libs:c:\vcpkg\vcpkg-master\installed `
  buildtools install `
  zlib:x64-windows-static-v140 `
  zlib:x64-windows-static-v141 `
  zlib:x64-windows-static-v142 `
  zlib:x86-windows-static-v140 `
  zlib:x86-windows-static-v141 `
  zlib:x86-windows-static-v142
```

or use the ps1 function `Build-Library`:

```
. .\buildtools.ps1
Build-Library -Verbose @("cryptopp", "curl", "detours", "openssl", "mbedtls", "zlib")
```

## standard library locations

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
```
