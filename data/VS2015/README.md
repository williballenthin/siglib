# VS14.0 / Visual Studio 2015 / v140

## download

Visual Studio 2019 installer and release channel (used to install Visual Studio 2015 tools):
  - https://aka.ms/vs/16/release/vs_buildtools.exe
  - https://aka.ms/vs/16/release/channel

Install [components](https://docs.microsoft.com/en-us/visualstudio/install/workload-component-id-vs-build-tools?view=vs-2019):
  - `Microsoft.VisualStudio.Component.VC.140`: MSVC v140 - VS 2015 C++ build tools (v14.00)

(See [Dockerfile](../../Dockerfile))

This results in:
  - `C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\`: Visual Studio 2015 tools
  - `C:\Program Files (x86)\Windows Kits\10\Lib\10.0.10240.0\`: Windows Standalone SDK for Windows 10 from VS2015

## archive files

```
PS C:\> 
@(
    "libucrt.lib",
    "libucrtd.lib",
    "ucrt.lib",
    "ucrtd.lib",
    "libvcruntime.lib",
    "libvcruntimed.lib",
    "vcruntime.lib",
    "vcruntimed.lib",
    "libcmt.lib",
    "libcmtd.lib",
    "msvcrt.lib",
    "msvcrtd.lib",
    "msvcmrt.lib",
    "msvcmrtd.lib",
    "msvcurt.lib",
    "msvcurtd.lib",
    "libcpmt.lib",
    "msvcprt.lib",
    "libcpmtd.lib",
    "msvcprtd.lib"
) | `
% { dir -Path C:\ -Filter $_ -Recurse -ErrorAction SilentlyContinue -Force } | `
% { Get-FileHash -Algorithm md5 $_.FullName }

Algorithm       Hash                                                                   Path
---------       ----                                                                   ----
MD5             16F93B7E2C612AE84B96CE46A5BDD637                                       C:\Program Files (x86)\Windows Kits\10\Lib\10.0.10240.0\ucrt\x64\libucrt.lib
MD5             0FB2C1D5ADE60005456B447A285368D7                                       C:\Program Files (x86)\Windows Kits\10\Lib\10.0.10240.0\ucrt\x86\libucrt.lib
MD5             92DCD14F9D99F4CE36619B201EA0B7D0                                       C:\Program Files (x86)\Windows Kits\10\Lib\10.0.10240.0\ucrt\x64\libucrtd.lib
MD5             2065FCDF73BC47DD90D3C8834AC5486D                                       C:\Program Files (x86)\Windows Kits\10\Lib\10.0.10240.0\ucrt\x86\libucrtd.lib
MD5             F83E39D7CBE39437FB0202C7A8C36C83                                       C:\Program Files (x86)\Windows Kits\10\Lib\10.0.10240.0\ucrt\x64\ucrt.lib
MD5             7910EA07C7110572C1427C587EA501B6                                       C:\Program Files (x86)\Windows Kits\10\Lib\10.0.10240.0\ucrt\x86\ucrt.lib
MD5             91675612F322B415E42F0B89E229FA4A                                       C:\Program Files (x86)\Windows Kits\10\Lib\10.0.10240.0\ucrt\x64\ucrtd.lib
MD5             93468959D04C958338FF99F5331757FF                                       C:\Program Files (x86)\Windows Kits\10\Lib\10.0.10240.0\ucrt\x86\ucrtd.lib
MD5             480EBA2BC3925E66773C0EBCEDEF14DB                                       C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\lib\libvcruntime.lib
MD5             4091C506300368D01BB470E4814A86A9                                       C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\lib\libvcruntimed.lib
MD5             EDE62B117642FC600935037DEB669630                                       C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\lib\vcruntime.lib
MD5             C86DAF84C55AC8A893B80C1ACF6EF366                                       C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\lib\vcruntimed.lib
MD5             D1CFAB7EAF7A198E10BBD44B498EEF3C                                       C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\lib\libcmt.lib
MD5             C834109599BD0AF776763B649BCE4F92                                       C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\lib\libcmtd.lib
MD5             27F10DB674F10BC34633424300D7A785                                       C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\lib\msvcrt.lib
MD5             52AC4FE1BF5736EC58BF32D029B359E6                                       C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\lib\msvcrtd.lib
MD5             B79806DE7591FDD6DB8D005541A81025                                       C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\lib\msvcmrt.lib
MD5             8BF525BAEAC5DFE4E618ED899D5FE8E0                                       C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\lib\msvcmrtd.lib
MD5             8109D5A995B18A4DCD011CD49DD3B067                                       C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\lib\msvcurt.lib
MD5             CBF35AB927F7908EBE24E43E8EF51750                                       C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\lib\msvcurtd.lib
MD5             CC50F9B05B0808102F1EDDF00642D455                                       C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\lib\libcpmt.lib
MD5             48AE6BD51072D760890FDC49C5581312                                       C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\lib\msvcprt.lib
MD5             A60E3B7C00F7B04F54D917C59294FCCD                                       C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\lib\libcpmtd.lib
MD5             71596C97F8D6C9AC8B03F30FEF5D3A50                                       C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\lib\msvcprtd.lib
```

## pat files

## contents