# VS14.28 / Visual Studio 2019 / v142

## download

Visual Studio 2019 installer and release channel (used to install Visual Studio 2015 tools):
  - https://aka.ms/vs/16/release/vs_buildtools.exe
  - https://aka.ms/vs/16/release/channel

Install [components](https://docs.microsoft.com/en-us/visualstudio/install/workload-component-id-vs-build-tools?view=vs-2019):
  - `Microsoft.VisualStudio.Component.VC.Tools.x86.x64`: MSVC v142 - VS 2019 C++ x64/x86 build tools (v14.28)
  - `Microsoft.VisualStudio.Component.VC.CLI.Support`: C++/CLI support for v142 build tools (14.28)
  - `microsoft.visualstudio.component.vc.atl`: C++ ATL for latest v142 build tools (x86 & x64), version 16.4.29313.120
  - `microsoft.visualstudio.component.vc.atlmfc`: C++ MFC for latest v142 build tools (x86 & x64), version 16.4.29313.120
  - `Microsoft.VisualStudio.Component.Windows10SDK.18362`: Windows 10 SDK (10.0.18362.0), version 16.1.28829.92, usually bundled with Visual Studio 2019

(See [Dockerfile](../../Dockerfile))

This results in:
  - `C:\BuildTools\VC\Tools\MSVC\14.28.29910`: MSVC v142 - VS 2019 C++ x64/x86 build tools (v14.28)
  - `C:\BuildTools\VC\Tools\MSVC\14.28.29910\atlmfc\lib\`: C++ MFC for latest v142 build tools (x86 & x64), version 16.4.29313.120
  - `C:\Program Files (x86)\Windows Kits\10\lib\10.0.18362.0`: Windows 10 SDK (10.0.18362.0), version 16.1.28829.92, usually bundled with Visual Studio 2019
  - `C:\Program Files (x86)\Windows Kits\10\lib\10.0.19041.0`: Windows 10 SDK (10.0.19041.0), version ???, bundled with VS2019???
  - TODO: where is ATL?

## prepare

## get lib/obj files

## generate .pat

### x86

### amd64

## contents