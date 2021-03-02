# escape=`

FROM mcr.microsoft.com/windows/servercore:ltsc2019

# visual studio 2019
ADD https://aka.ms/vs/16/release/channel C:\TEMP\VisualStudio2019.chman
ADD https://aka.ms/vs/16/release/vs_buildtools.exe C:\TEMP\vs_buildtools2019.exe

SHELL ["cmd", "/S", "/C"]

# from: https://docs.microsoft.com/en-us/visualstudio/install/workload-component-id-vs-build-tools?view=vs-2019
#
# Microsoft.VisualStudio.Component.VC.140              MSVC v140 - VS 2015 C++ build tools (v14.00)
# Microsoft.VisualStudio.Component.VC.v141.x86.x64     MSVC v141 - VS 2017 C++ x64/x86 build tools (v14.16)
# Microsoft.VisualStudio.Component.VC.Tools.x86.x64    MSVC v142 - VS 2019 C++ x64/x86 build tools (v14.28)
# Microsoft.VisualStudio.Component.VC.v141.CLI.Support C++/CLI support for v141 build tools (14.16)
# Microsoft.VisualStudio.Component.VC.CLI.Support      C++/CLI support for v142 build tools (14.28)
RUN C:\TEMP\vs_buildtools2019.exe --quiet --wait --norestart --nocache `
    --installPath C:\BuildTools `
    --channelUri C:\Temp\VisualStudio2019.chman `
    --installChannelUri C:\Temp\VisualStudio2019.chman `
    --add Microsoft.VisualStudio.Workload.VCTools;includeRecommended `
    --add Microsoft.Component.MSBuild `
    --add Microsoft.VisualStudio.Component.VC.140 `
    --add Microsoft.VisualStudio.Component.VC.v141.x86.x64 `
    --add Microsoft.VisualStudio.Component.VC.v141.CLI.Support `
    --add Microsoft.VisualStudio.Component.VC.Tools.x86.x64 `
    --add Microsoft.VisualStudio.Component.VC.CLI.Support `
|| IF "%ERRORLEVEL%"=="3010" EXIT 0

SHELL ["powershell", "-Command", "$ErrorActionPreference = 'Stop'; $ProgressPreference = 'SilentlyContinue';"]

RUN Invoke-WebRequest https://github.com/Microsoft/vcpkg/archive/master.zip -OutFile vcpkg.zip;
RUN Expand-Archive vcpkg.zip -DestinationPath vcpkg;

WORKDIR C:/vcpkg/vcpkg-master
RUN New-Item -ItemType Directory -Path downloads;
RUN New-Item -ItemType File -Path downloads\AlwaysAllowEverything;
RUN scripts\bootstrap.ps1;

RUN .\vcpkg.exe integrate install

# prime tools (cmake, git, nuget, 7z, etc)
RUN .\vcpkg.exe install zlib

ADD x64-windows-static-v140.cmake C:/vcpkg/vcpkg-master/triplets/
ADD x64-windows-static-v141.cmake C:/vcpkg/vcpkg-master/triplets/
ADD x64-windows-static-v142.cmake C:/vcpkg/vcpkg-master/triplets/
ADD x86-windows-static-v140.cmake C:/vcpkg/vcpkg-master/triplets/
ADD x86-windows-static-v141.cmake C:/vcpkg/vcpkg-master/triplets/
ADD x86-windows-static-v142.cmake C:/vcpkg/vcpkg-master/triplets/

ENTRYPOINT ["powershell.exe", "-NoLogo", "-ExecutionPolicy", "Bypass"]
CMD ["powershell.exe", "-NoLogo", "-ExecutionPolicy", "Bypass"]
