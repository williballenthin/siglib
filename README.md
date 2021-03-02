# siglib

configuration and tools to build function identification signatures, such as FLIRT.
provides a reproducible way to build object/archive files 
from [vcpkg](https://github.com/microsoft/vcpkg) using [Windows Containers via Docker](https://www.docker.com/products/windows-containers).

## prerequisites

  - Windows 10 with Hyper-V and Containers enabled
  - Docker for Windows, configured with Windows Containers
  - `pcf.exe` from Hex-Rays FLAIR utilities (place in this directory)

## setup

build the Windows container image named `buildtools`:

```sh
docker build -t buildtools:latest --isolation=hyperv --network "Default Switch" .
```

## collect archive files

### build a .lib via vcpkg

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

use `docker volume inspect sigs` to figure out where the volume data is stored.
by default, its probably `C:\ProgramData\Docker\volumes\libs\_data`.

### standard library and runtime locations

I don't think these are redistributable, but we can generate patterns from them.

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