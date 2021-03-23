# VS14.16 / Visual Studio 2017 / v141

## download

Visual Studio 2019 installer and release channel (used to install Visual Studio 2015 tools):
  - https://aka.ms/vs/16/release/vs_buildtools.exe
  - https://aka.ms/vs/16/release/channel

Install [components](https://docs.microsoft.com/en-us/visualstudio/install/workload-component-id-vs-build-tools?view=vs-2019):
  - `Microsoft.VisualStudio.Component.VC.v141.x86.x64`: MSVC v141 - VS 2017 C++ x64/x86 build tools (v14.16)
  - `Microsoft.VisualStudio.Component.VC.v141.CLI.Support`: C++/CLI support for v141 build tools (14.16)
  - `Microsoft.VisualStudio.Component.VC.v141.ATL`: C++ ATL for v141 build tools (x86 & x64), version 16.0.28625.61
  - `Microsoft.VisualStudio.Component.VC.v141.MFC`: C++ MFC for v141 build tools (x86 & x64), version 16.0.28625.61
  - `Microsoft.VisualStudio.Component.Windows10SDK.16299`: Windows 10 SDK (10.0.16299.0), version 16.9.31004.209, usually bundled with Visual Studio 2017 ver.15.4 
  - `Microsoft.VisualStudio.Component.Windows10SDK.17134`: Windows 10 SDK (10.0.17134.0), version 16.9.31004.209, usually bundled with Visual Studio 2017 ver.15.7 
  - `Microsoft.VisualStudio.Component.Windows10SDK.17763`: Windows 10 SDK (10.0.17763.0), version 16.0.28517.75, usually bundled with Visual Studio 2017 ver.15.8 

(See [Dockerfile](../../Dockerfile))

This results in:
  - `C:\BuildTools\VC\Tools\MSVC\14.16.27023\`: MSVC v141 - VS 2017 C++ x64/x86 build tools (v14.16)
  - `C:\BuildTools\VC\Tools\MSVC\14.16.27023\atlmfc`: C++ MFC for v141 build tools (x86 & x64)
  - `C:\Program Files (x86)\Windows Kits\10\lib\10.0.16299.0`: Windows 10 SDK (10.0.16299.0), version 16.9.31004.209, usually bundled with Visual Studio 2017 ver.15.4 
  - `C:\Program Files (x86)\Windows Kits\10\lib\10.0.17134.0`: Windows 10 SDK (10.0.17134.0), version 16.9.31004.209, usually bundled with Visual Studio 2017 ver.15.7 
  - `C:\Program Files (x86)\Windows Kits\10\lib\10.0.17763.0`: Windows 10 SDK (10.0.17763.0), version 16.0.28517.75, usually bundled with Visual Studio 2017 ver.15.8 

## archive files

## pat files

## contents