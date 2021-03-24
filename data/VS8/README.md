# VS8 / Visual Studio 2005

# download
Visual Studio 2005 Professional
`en_vs_2005_pro_dvd.iso`

# prepare
run setup

# get lib/obj files
```
$ find /cygdrive/c/Program\ Files\ \(x86\)/Microsoft\ Visual\ Studio\ 8/VC/ -iname "*.lib"
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/atldload.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/atlmincrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/eafxis.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/eafxisd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/mfc80.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/mfc80d.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/mfc80u.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/mfc80ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/mfcdload.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/MFCM80.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/MFCM80D.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/MFCM80U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/MFCM80UD.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/mfcs80.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/mfcs80d.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/mfcs80u.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/mfcs80ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/nafxcw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/nafxcwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/nafxis.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/nafxisd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/uafxcw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/uafxcwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/Atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/atldload.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/atlmincrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/eafxis.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/eafxisd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/mfc80.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/mfc80d.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/mfc80u.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/mfc80ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/mfcdload.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/mfcm80.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/mfcm80d.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/mfcm80u.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/mfcm80ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/mfcs80.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/mfcs80d.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/mfcs80u.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/mfcs80ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/nafxcw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/nafxcwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/nafxis.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/nafxisd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/uafxcw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/uafxcwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/armv4/atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/armv4/atlosapis.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/armv4/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/armv4/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/armv4/MFC80U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/armv4/MFC80Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/armv4/mfcs80U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/armv4/mfcs80Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/armv4/UafxcW.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/armv4/UafxcWD.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/armv4i/atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/armv4i/atlosapis.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/armv4i/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/armv4i/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/armv4i/MFC80U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/armv4i/MFC80Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/armv4i/mfcs80U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/armv4i/mfcs80Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/armv4i/UafxcW.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/armv4i/UafxcWD.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsii/atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsii/atlosapis.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsii/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsii/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsii/MFC80U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsii/MFC80Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsii/mfcs80U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsii/mfcs80Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsii/UafxcW.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsii/UafxcWD.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsii_fp/atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsii_fp/atlosapis.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsii_fp/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsii_fp/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsii_fp/MFC80U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsii_fp/MFC80Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsii_fp/mfcs80U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsii_fp/mfcs80Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsii_fp/UafxcW.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsii_fp/UafxcWD.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsiv/atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsiv/atlosapis.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsiv/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsiv/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsiv/MFC80U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsiv/MFC80Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsiv/mfcs80U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsiv/mfcs80Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsiv/UafxcW.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsiv/UafxcWD.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsiv_fp/atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsiv_fp/atlosapis.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsiv_fp/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsiv_fp/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsiv_fp/MFC80U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsiv_fp/MFC80Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsiv_fp/mfcs80U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsiv_fp/mfcs80Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsiv_fp/UafxcW.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsiv_fp/UafxcWD.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/sh4/atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/sh4/atlosapis.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/sh4/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/sh4/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/sh4/MFC80U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/sh4/MFC80Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/sh4/mfcs80U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/sh4/mfcs80Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/sh4/UafxcW.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/sh4/UafxcWD.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/x86/atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/x86/atlosapis.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/x86/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/x86/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/x86/MFC80U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/x86/MFC80Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/x86/mfcs80U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/x86/mfcs80Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/x86/UafxcW.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/x86/UafxcWD.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/armv4/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/armv4/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/armv4/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/armv4/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/armv4/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/armv4/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/armv4/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/armv4/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/armv4i/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/armv4i/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/armv4i/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/armv4i/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/armv4i/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/armv4i/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/armv4i/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/armv4i/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsii/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsii/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsii/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsii/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsii/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsii/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsii/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsii/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsii_fp/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsii_fp/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsii_fp/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsii_fp/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsii_fp/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsii_fp/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsii_fp/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsii_fp/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsiv/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsiv/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsiv/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsiv/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsiv/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsiv/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsiv/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsiv/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsiv_fp/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsiv_fp/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsiv_fp/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsiv_fp/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsiv_fp/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsiv_fp/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsiv_fp/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsiv_fp/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/sh4/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/sh4/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/sh4/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/sh4/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/sh4/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/sh4/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/sh4/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/sh4/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/x86/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/x86/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/x86/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/x86/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/x86/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/x86/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/x86/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/x86/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/almap.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/almapdll.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/conv.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/eh.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/rtc.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/tran.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/mt_lib/conv.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/mt_lib/eh.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/mt_lib/rtc.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/mt_lib/tran.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/sdknames.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/tcmap.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/tcmapdll.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/conv.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/eh.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/rtc.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/tran.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xmt_lib/conv.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xmt_lib/eh.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xmt_lib/rtc.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xmt_lib/tran.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/almap.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/almapdll.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/conv.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/eh.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/rtc.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/tran.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/conv.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/eh.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/rtc.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/tran.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/sdknames.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/tcmap.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/tcmapdll.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/conv.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/eh.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/rtc.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/tran.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/conv.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/eh.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/rtc.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/tran.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/comsupp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/comsuppd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/delayimp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/msvcmrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/msvcmrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/msvcprt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/msvcprtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/msvcurt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/msvcurtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/oldnames.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/pgobootrun.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/pgort.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/ptrustm.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/ptrustmd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/ptrustu.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/ptrustud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/runtmchk.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/vcomp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/vcompd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/comsupp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/comsuppd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/delayimp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/msvcmrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/msvcmrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/msvcprt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/msvcprtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/msvcurt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/msvcurtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/oldnames.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/opends60.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/pgobootrun.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/pgort.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/ptrustm.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/ptrustmd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/ptrustu.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/ptrustud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/RunTmChk.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/vcomp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/vcompd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AclUI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/ActiveDS.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Ad1.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Adptif.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/ADSIid.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AdvAPI32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/AclUI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/ActiveDS.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Adptif.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/ADSIid.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/AdvAPI32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/AuthZ.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Bits.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/bufferoverflowu.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Cabinet.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/CertIdl.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/ClusApi.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/ComCtl32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/ComDlg32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/ComSvcs.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Crypt32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/cryptui.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/DbgEng.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/DbgHelp.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/dciman32.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/DhcpCSvc.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/DlcAPI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/DnsAPI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/DSProp.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/DSUIExt.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/DtcHelp.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/FaultRep.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Fci.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Fdi.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/FrameDyD.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/FrameDyn.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Gdi32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/GdiPlus.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/GlAux.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/GlU32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/GPEdit.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/gtrts32w.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/gtrtst32.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/HLink.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Htmlhelp.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/httpapi.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Icm32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Icmui.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/ImageHlp.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Imm32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/inetcomm.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/IPHlpApi.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Iprop.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Kernel32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/KSProxy.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/ksuser.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/LoadPerf.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Lz32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/MAPI32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/MgmtAPI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/MMC.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/MobSync.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Mpr.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Mprapi.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/MqOA.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/MqRt.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/MSAcm32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Mscms.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/msdasc.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Msi.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/MSImg32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/MSRating.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/MSTask.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/MsWSock.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/MsXml2.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Mtx.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/NetAPI32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/nmapi.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/NMSupp.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/normaliz.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/npptools.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/NtDsAPI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/NtDsBCli.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/NTMSAPI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/NtQuery.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/odbc32.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/odbcbcp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/odbccp32.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Ole32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/OleAcc.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/OleAut32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/oledb.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/OleDlg.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/OlePro32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/OpenGL32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/osptk.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/parser.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Pdh.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/powrprof.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Psapi.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/QosName.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/RASAPI32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/RASDlg.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/RASsAPI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/ResUtils.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/RpcNdr.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Rpcns4.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/RpcRT4.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Rtm.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Rtutils.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/SCardDlg.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/ScrnSave.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/ScrnSavW.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Secur32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/SensAPI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/SetupAPI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Sfc.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Shell32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/ShFolder.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/ShLwApi.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/sisbkup.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/SnmpAPI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/SpOrder.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Sti.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/strsafe.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Svcguid.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Tapi32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Traffic.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Urlmon.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/User32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/UserEnv.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/USP10.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Uuid.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Uxtheme.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Version.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Vfw32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/WbemUuid.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/WiaGuid.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/WinInet.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/WinMM.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/WinSCard.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/WinSpool.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/WinStrm.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/WinTrust.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Wldap32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/wmiutils.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/WS2_32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/WSnmp32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/WSock32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/WtsApi32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/xaSwitch.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/xoleHlp.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/ASycFilt.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AuthZ.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/bhsupp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Bits.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/bufferoverflowu.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Cabinet.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Cap.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/certadm.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/certidl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/CiUuid.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/ClusApi.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/ComCtl32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/ComDlg32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/ComSvcs.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/credui.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Crypt32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/CryptNet.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/cryptui.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/d3d8thk.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/daouuid.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/DbgEng.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/DbgHelp.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/dciman32.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/ddao35.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/ddao35d.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/ddao35u.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/ddao35ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/DhcpCSvc.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/dhcpsapi.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/DlcAPI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/DnsAPI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/DSProp.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/DSUIExt.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/DtcHelp.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/FaultRep.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/FCachDll.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Fci.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Fdi.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/FrameDyD.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/FrameDyn.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Gdi32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/GdiPlus.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/GlAux.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/GlU32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/GPEdit.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/gpmuuid.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/gtrts32w.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/gtrtst32.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/HLink.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Htmlhelp.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/httpapi.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/IA64/AuthZ.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Icm32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Icmui.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/ImageHlp.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Imm32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/IPHlpApi.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Iprop.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Kernel32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/KSGuid.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/KSProxy.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/ksuser.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/LoadPerf.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Lz32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/MAPI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/MAPI32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/MgmtAPI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/MiniDump.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/MMC.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/MobSync.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Mpr.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Mprapi.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/MqOA.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/MqRt.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/MSAcm32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Mscms.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/mscoree.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/msdasc.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/MSImg32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/MSRating.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/MSTask.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/MsWSock.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/MsXml2.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Mtx.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/mtxdm.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/NetAPI32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/nmapi.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/NMSupp.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/npptools.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/NtDsAPI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/NtDsBCli.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/NTMSAPI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/NtQuery.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/odbc32.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/odbcbcp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/odbccp32.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Ole32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/OleAcc.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/OleAut32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/oledb.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/OleDlg.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/OlePro32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/OpenGL32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/osptk.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/parser.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Pdh.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/PEnter.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/powrprof.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Psapi.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/QosName.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/RASAPI32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/RASDlg.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/RASsAPI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/ResUtils.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/RichEd20.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/RpcNdr.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Rpcns4.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/RpcRT4.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Rtm.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Rtutils.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/SCardDlg.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/ScrnSave.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/ScrnSavW.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Secur32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/SensAPI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/SetupAPI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Sfc.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Shell32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/ShFolder.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/ShLwApi.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/sisbkup.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/SnmpAPI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/SpOrder.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/SrClient.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Sti.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/strsafe.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Svcguid.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Tapi32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Thunk32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Traffic.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/unicows.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Url.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Urlmon.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/User32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/UserEnv.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/USP10.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Uuid.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Uxtheme.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/VdmDbg.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Version.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Vfw32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/WbemUuid.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/WebPost.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/WiaGuid.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/WinInet.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/WinMM.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/WinSCard.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/WinSpool.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/WinStrm.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/WinTrust.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Wldap32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/wmiutils.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Wow32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/WS2_32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/WSnmp32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/WSock32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Wst.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/WtsApi32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/xaSwitch.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/xoleHlp.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/misc/mdac2.8/Conformance/Tests/Libs/amd64/ModuleCore.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/misc/mdac2.8/Conformance/Tests/Libs/x86/ModuleCore.lib


$ find /cygdrive/c/Program\ Files\ \(x86\)/Microsoft\ Visual\ Studio\ 8/VC/ -iname "*.obj"
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/amdsecgs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/chandler.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/chkstk2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/clr_obj/managdeh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/clr_obj/mehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/clr_obj/mehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/clr_obj/mehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/clr_obj/mehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/clr_obj/mehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/clr_obj/mstdexpt.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/ehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/ehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/ehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/ehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/ehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/gshandler.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/gshandlereh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/gshandlerseh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/jmpuwind.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/longjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/matherr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/oldexcpt.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/pure_obj/managdeh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/pure_obj/mehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/pure_obj/mehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/pure_obj/mehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/pure_obj/mehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/pure_obj/mehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/pure_obj/rtti.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/rtcmd.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/setjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/setjmpex.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/tncleanup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/mt_lib/amdsecgs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/mt_lib/chandler.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/mt_lib/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/mt_lib/chkstk2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/mt_lib/gshandler.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/mt_lib/gshandlereh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/mt_lib/gshandlerseh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/mt_lib/jmpuwind.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/mt_lib/longjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/mt_lib/matherr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/mt_lib/rtcmd.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/mt_lib/setjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/mt_lib/setjmpex.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/amdsecgs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/chandler.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/chkstk2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/clr_obj/managdeh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/clr_obj/mehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/clr_obj/mehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/clr_obj/mehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/clr_obj/mehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/clr_obj/mehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/clr_obj/mstdexpt.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/ehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/ehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/ehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/ehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/ehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/gshandler.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/gshandlereh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/gshandlerseh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/jmpuwind.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/longjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/matherr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/oldexcpt.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/pure_obj/managdeh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/pure_obj/mehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/pure_obj/mehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/pure_obj/mehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/pure_obj/mehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/pure_obj/mehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/pure_obj/rtti.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/rtcmd.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/setjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/setjmpex.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/tncleanup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xmt_lib/amdsecgs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xmt_lib/chandler.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xmt_lib/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xmt_lib/chkstk2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xmt_lib/gshandler.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xmt_lib/gshandlereh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xmt_lib/gshandlerseh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xmt_lib/jmpuwind.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xmt_lib/longjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xmt_lib/matherr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xmt_lib/rtcmd.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xmt_lib/setjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xmt_lib/setjmpex.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/alloca16.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/atlssup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/calldtor.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/chandler4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/chandler4gs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/chkesp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/clr_obj/managdeh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/clr_obj/mehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/clr_obj/mehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/clr_obj/mehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/clr_obj/mehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/clr_obj/mehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/clr_obj/mstdexpt.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/cpu_disp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/dllsupp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/eh3valid.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/ehprolg2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/ehprolg3.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/ehprolg3a.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/ehprolog.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/ehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/ehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/ehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/ehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/ehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/enable.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/exsup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/exsup2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/exsup3.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/exsup4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/ftol2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/inp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/lldiv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/lldvrm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/llmul.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/llrem.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/llshl.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/llshr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/longjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/matherr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/memccpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/memchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/memcmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/memcpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/memmove.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/memset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/oldexcpt.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/outp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/p4_memcpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/p4_memset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/pure_obj/managdeh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/pure_obj/mehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/pure_obj/mehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/pure_obj/mehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/pure_obj/mehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/pure_obj/mehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/pure_obj/rtti.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/sehprolg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/sehprolg4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/sehprolg4gs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/sehsupp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/setjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/setjmp3.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/setjmpex.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/strcat.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/strchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/strcmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/strcspn.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/strlen.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/strncat.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/strncpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/strnset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/strpbrk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/strrchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/strrev.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/strset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/strspn.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/strstr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/tncleanup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/ulldiv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/ulldvrm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/ullrem.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/ullshr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/_memicmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/_strnicm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/alloca16.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/atlssup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/calldtor.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/chandler4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/chandler4gs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/chkesp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/eh3valid.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/enable.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/exsup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/exsup2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/exsup3.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/exsup4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/inp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/lldiv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/lldvrm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/llmul.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/llrem.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/llshl.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/llshr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/longjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/matherr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/memccpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/memchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/memcmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/memcpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/memmove.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/memset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/outp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/p4_memcpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/p4_memset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/sehprolg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/sehprolg4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/sehprolg4gs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/sehsupp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/setjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/setjmp3.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/setjmpex.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/strcat.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/strchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/strcmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/strcspn.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/strlen.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/strncat.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/strncpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/strnset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/strpbrk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/strrchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/strrev.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/strset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/strspn.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/strstr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/ulldiv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/ulldvrm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/ullrem.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/ullshr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/_memicmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/_strnicm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/alloca16.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/atlssup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/calldtor.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/chandler4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/chandler4gs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/chkesp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/clr_obj/managdeh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/clr_obj/mehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/clr_obj/mehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/clr_obj/mehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/clr_obj/mehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/clr_obj/mehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/clr_obj/mstdexpt.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/cpu_disp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/dllsupp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/eh3valid.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/ehprolg2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/ehprolg3.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/ehprolg3a.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/ehprolog.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/ehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/ehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/ehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/ehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/ehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/enable.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/exsup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/exsup2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/exsup3.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/exsup4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/ftol2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/inp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/lldiv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/lldvrm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/llmul.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/llrem.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/llshl.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/llshr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/longjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/matherr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/memccpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/memchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/memcmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/memcpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/memmove.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/memset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/oldexcpt.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/outp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/p4_memcpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/p4_memset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/pure_obj/managdeh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/pure_obj/mehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/pure_obj/mehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/pure_obj/mehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/pure_obj/mehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/pure_obj/mehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/pure_obj/rtti.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/sehprolg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/sehprolg4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/sehprolg4gs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/sehsupp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/setjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/setjmp3.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/setjmpex.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/strcat.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/strchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/strcmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/strcspn.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/strlen.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/strncat.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/strncpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/strnset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/strpbrk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/strrchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/strrev.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/strset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/strspn.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/strstr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/tncleanup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/ulldiv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/ulldvrm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/ullrem.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/ullshr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/_memicmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/_strnicm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/alloca16.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/atlssup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/calldtor.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/chandler4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/chandler4gs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/chkesp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/eh3valid.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/enable.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/exsup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/exsup2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/exsup3.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/exsup4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/inp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/lldiv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/lldvrm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/llmul.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/llrem.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/llshl.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/llshr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/longjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/matherr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/memccpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/memchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/memcmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/memcpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/memmove.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/memset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/outp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/p4_memcpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/p4_memset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/sehprolg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/sehprolg4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/sehprolg4gs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/sehsupp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/setjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/setjmp3.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/setjmpex.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/strcat.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/strchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/strcmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/strcspn.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/strlen.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/strncat.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/strncpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/strnset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/strpbrk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/strrchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/strrev.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/strset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/strspn.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/strstr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/ulldiv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/ulldvrm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/ullrem.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/ullshr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/_memicmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/_strnicm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/binmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/commode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/invalidcontinue.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/loosefpmath.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/newmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/noarg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/nochkclr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/noenv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/nothrownew.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/pbinmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/pcommode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/pinvalidcontinue.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/pnewmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/pnoarg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/pnoenv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/pnothrownew.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/psetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/pthreadlocale.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/pwsetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/setargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/smalheap.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/threadlocale.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/wsetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/binmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/commode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/fp10.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/invalidcontinue.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/loosefpmath.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/newmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/noarg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/nochkclr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/noenv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/nothrownew.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/pbinmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/pcommode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/pinvalidcontinue.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/pnewmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/pnoarg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/pnoenv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/pnothrownew.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/psetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/pthreadlocale.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/pwsetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/setargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/smalheap.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/threadlocale.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/wsetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/ComMode.Obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/sehprolg.obj


$ rsync -a --prune-empty-dirs --include '*/' --include '*.obj' --include '*.Obj' --include '*.lib' --include '*.Lib' --exclude '*' /cygdrive/c/Program\ Files\ \(x86\)/Microsoft\ Visual\ Studio\ 8/VC/ VS8/
```

# generate and zip .pat

focus on C/C++ run time libraries

```
$ find VS8/ -type f \( -iname "*libc*" -o -iname "*msvc*" -o -iname "*libvc*" -o -iname "*vcruntime*" -o -iname "*libucrt*" \) -exec md5sum {} \;
d8381f54ae916eb65e73cba5cfaf0a36 *VS8/ce/lib/armv4/libcmt.lib
b14698e6c4c55a118562c1948c3f5f59 *VS8/ce/lib/armv4/libcmtd.lib
16415601f3ce0ecb66c003033626b3e6 *VS8/ce/lib/armv4/libcpmt.lib
a562b1c1100aa036c9c5b04d1b596c63 *VS8/ce/lib/armv4/libcpmtd.lib
062574f05d73a6945a3cfb4b322cccd4 *VS8/ce/lib/armv4/msvcrt.lib
745bfe6181ff0cda513e6885db7f8be6 *VS8/ce/lib/armv4/msvcrtd.lib
eb39426f1e03fbab2cfbf5d938e82556 *VS8/ce/lib/armv4i/libcmt.lib
dc6be913ab7eb25075db0ad1dd1d2928 *VS8/ce/lib/armv4i/libcmtd.lib
20c1e038f1ae52537b30d7b76c157eef *VS8/ce/lib/armv4i/libcpmt.lib
feb5411d97d9a637bdb0a747ccf870e1 *VS8/ce/lib/armv4i/libcpmtd.lib
be2358512e854938d453990f8a39752f *VS8/ce/lib/armv4i/msvcrt.lib
34ac8b4a2d2dc29a18fb495a55fc9952 *VS8/ce/lib/armv4i/msvcrtd.lib
78d0b0e186656f9afd63cb0e57b51719 *VS8/ce/lib/mipsii/libcmt.lib
dcc2311bc6a9098800881dfd83343f58 *VS8/ce/lib/mipsii/libcmtd.lib
15bff5b4f083bbf56577ba4203c3f78a *VS8/ce/lib/mipsii/libcpmt.lib
2dc908fddc58f0985aed83201a6ac6ad *VS8/ce/lib/mipsii/libcpmtd.lib
bc80dc012c2ca8e8a6d049c099247227 *VS8/ce/lib/mipsii/msvcrt.lib
e8623fbc478249df5417128fb8cf6787 *VS8/ce/lib/mipsii/msvcrtd.lib
96ea82e8fd4331e1bc44a3237d0d6276 *VS8/ce/lib/mipsii_fp/libcmt.lib
0462aa7519982a17caeaaed11a769de3 *VS8/ce/lib/mipsii_fp/libcmtd.lib
9731db9916968def162cfe38c10945b2 *VS8/ce/lib/mipsii_fp/libcpmt.lib
574632e31d615f31a7d29c825b9d0428 *VS8/ce/lib/mipsii_fp/libcpmtd.lib
bc80dc012c2ca8e8a6d049c099247227 *VS8/ce/lib/mipsii_fp/msvcrt.lib
fe733d12a98a9a0d9f00522e26776112 *VS8/ce/lib/mipsii_fp/msvcrtd.lib
7e7730f88959a187d375a5d8cc9e7b8c *VS8/ce/lib/mipsiv/libcmt.lib
f9231fb966058f6c25f5b959a6ed03e2 *VS8/ce/lib/mipsiv/libcmtd.lib
25f030aebc5413a78f2d498010d7cd1a *VS8/ce/lib/mipsiv/libcpmt.lib
92b671fe17fbeb32946430d6d6fb2add *VS8/ce/lib/mipsiv/libcpmtd.lib
ff3a7de8361affad45c8fb9ba65c39f3 *VS8/ce/lib/mipsiv/msvcrt.lib
548e830fd73950beb00f898417f0a42c *VS8/ce/lib/mipsiv/msvcrtd.lib
cb94a7ae825d09bf2b4e05decc0ae580 *VS8/ce/lib/mipsiv_fp/libcmt.lib
c30d313893b3698a603c92019b94c32e *VS8/ce/lib/mipsiv_fp/libcmtd.lib
92fdafb7aad3fcfb8de0dcde1f92cc39 *VS8/ce/lib/mipsiv_fp/libcpmt.lib
3cd242dbb0e6e1951ac2f939589cf098 *VS8/ce/lib/mipsiv_fp/libcpmtd.lib
ff3a7de8361affad45c8fb9ba65c39f3 *VS8/ce/lib/mipsiv_fp/msvcrt.lib
612e9b5679bb3ef2ab350534f582ade7 *VS8/ce/lib/mipsiv_fp/msvcrtd.lib
ef78fa77601e6b7047dedac20256093c *VS8/ce/lib/sh4/libcmt.lib
1820fb2ab92ebec0fd28deec4e5c4044 *VS8/ce/lib/sh4/libcmtd.lib
b96a45e5fca3fdb21d0de07aa13d9f6a *VS8/ce/lib/sh4/libcpmt.lib
7b65a1175b674ce868149b2940c96bb0 *VS8/ce/lib/sh4/libcpmtd.lib
db4b6c741c5935b72c05483bd99344a5 *VS8/ce/lib/sh4/msvcrt.lib
ed3d552e68d95a9b3767d1206ed49ff4 *VS8/ce/lib/sh4/msvcrtd.lib
595d5454ca909477ca536a4a2ea9e8ef *VS8/ce/lib/x86/libcmt.lib
323e78895c2518ed8fc03b0a0a69543d *VS8/ce/lib/x86/libcmtd.lib
11f5d1a0dbbd5d6b9ffd43b0c59ce886 *VS8/ce/lib/x86/libcpmt.lib
68532423105f2a79882ee7a55622c797 *VS8/ce/lib/x86/libcpmtd.lib
c036e5caaf60855e7e31ae0d8ab94283 *VS8/ce/lib/x86/msvcrt.lib
3068fd4c0f78ed0220e9784f7da0adbd *VS8/ce/lib/x86/msvcrtd.lib
ca159acd326aac9050847c38fd194572 *VS8/lib/amd64/libcmt.lib
4639f1d8d36ce6efd512bcdb86b60057 *VS8/lib/amd64/libcmtd.lib
35abd4aca812bc94c8473eb74817ebb7 *VS8/lib/amd64/libcpmt.lib
0d0f3aa1aa1806c1c0b7385c3a68346e *VS8/lib/amd64/libcpmtd.lib
008b9c76edb1cc7e40fe9befbc3d7c06 *VS8/lib/amd64/msvcmrt.lib
9708e0b0cdbc3d201e572667f57a099f *VS8/lib/amd64/msvcmrtd.lib
1ee69764c278e9c6534d334acfae5593 *VS8/lib/amd64/msvcprt.lib
28761739551a09b1eb53c2adda4d6290 *VS8/lib/amd64/msvcprtd.lib
ac009abd3b6218e9b3b152e643233bc1 *VS8/lib/amd64/msvcrt.lib
089469be976852a65dac0675cbfebdb3 *VS8/lib/amd64/msvcrtd.lib
949739a9b628af3b297e67e3a6de4573 *VS8/lib/amd64/msvcurt.lib
a5efef335f5cd6412bd0d3685aca229a *VS8/lib/amd64/msvcurtd.lib
23a5a91898e5387327d1b7f55d3975c4 *VS8/lib/libcmt.lib
29e9d2a0aeed593ce7b72205ed120db2 *VS8/lib/libcmtd.lib
89a8ef9a81454dba9c1d882aa2b8dc4f *VS8/lib/libcpmt.lib
4812dbad4d97d3d9fa13fda4e938f85b *VS8/lib/libcpmtd.lib
7a1efaa21907e0b4efd55dbb556c0c32 *VS8/lib/msvcmrt.lib
aad004e115f8fb59853ac5f8ce4667eb *VS8/lib/msvcmrtd.lib
20d64a73a00a7cb0d5118cdce669e143 *VS8/lib/msvcprt.lib
1eb3c50986d54150a4f7daf2ca672df7 *VS8/lib/msvcprtd.lib
9b2e7bce92d7e14136e8332172507eb8 *VS8/lib/msvcrt.lib
9dc7b725adcd5f83ea10ca1a3fa15654 *VS8/lib/msvcrtd.lib
255876bb93f96e559124a55956e2c705 *VS8/lib/msvcurt.lib
cadfec2211d5f4fab19726ac9f05077d *VS8/lib/msvcurtd.lib
e96d56366492a85815b8e82389a60bd8 *VS8/PlatformSDK/Lib/AMD64/ComSvcs.Lib
6fb5becd40ab71b027515172c4545cb4 *VS8/PlatformSDK/Lib/ComSvcs.Lib
```

## manually deleted
- `PlatformSDK`
- `ce`

## x86
```
$ find VS8/VC/lib/ -maxdepth 1 -type f \( -iname "*libc*" -o -iname "*msvc*" -o -iname "*libvc*" -o -iname "*vcruntime*" -o -iname "*libucrt*" \) -exec ../../pcf.exe {} {}.pat \;
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS8\VC\lib\libcmt.lib: skipped 283, total 3056
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS8\VC\lib\libcmtd.lib: skipped 121, total 3174
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS8\VC\lib\libcpmt.lib: skipped 272, total 4734
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS8\VC\lib\libcpmtd.lib: skipped 0, total 5938
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS8\VC\lib\msvcmrt.lib: skipped 284, total 500
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS8\VC\lib\msvcmrtd.lib: skipped 293, total 510
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS8\VC\lib\msvcprt.lib: skipped 3172, total 3174
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS8\VC\lib\msvcprtd.lib: skipped 3408, total 3411
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS8\VC\lib\msvcrt.lib: skipped 1708, total 1835
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS8\VC\lib\msvcrtd.lib: skipped 1776, total 1908
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS8\VC\lib\msvcurt.lib: skipped 1874, total 4862
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS8\VC\lib\msvcurtd.lib: skipped 1962, total 5290

$ tar -czvf VS8/VS8.tar.gz VS8/VC/lib/*.pat
VS8/VC/lib/libcmt.lib.pat
VS8/VC/lib/libcmtd.lib.pat
VS8/VC/lib/libcpmt.lib.pat
VS8/VC/lib/libcpmtd.lib.pat
VS8/VC/lib/msvcmrt.lib.pat
VS8/VC/lib/msvcmrtd.lib.pat
VS8/VC/lib/msvcprt.lib.pat
VS8/VC/lib/msvcprtd.lib.pat
VS8/VC/lib/msvcrt.lib.pat
VS8/VC/lib/msvcrtd.lib.pat
VS8/VC/lib/msvcurt.lib.pat
VS8/VC/lib/msvcurtd.lib.pat
```

## amd64
```
$ find VS8/VC/lib/amd64/ -type f \( -iname "*libc*" -o -iname "*msvc*" -o -iname "*libvc*" -o -iname "*vcruntime*" -o -iname "*libucrt*" \) -exec ../../pcf.exe {} {}.pat \;
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS8\VC\lib\amd64\libcmt.lib: skipped 281, total 3018
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS8\VC\lib\amd64\libcmtd.lib: skipped 122, total 3126
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS8\VC\lib\amd64\libcpmt.lib: skipped 262, total 4248
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS8\VC\lib\amd64\libcpmtd.lib: skipped 0, total 5149
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS8\VC\lib\amd64\msvcmrt.lib: skipped 282, total 498
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS8\VC\lib\amd64\msvcmrtd.lib: skipped 291, total 508
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS8\VC\lib\amd64\msvcprt.lib: skipped 3180, total 3181
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS8\VC\lib\amd64\msvcprtd.lib: skipped 3408, total 3411
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS8\VC\lib\amd64\msvcrt.lib: skipped 1661, total 1755
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS8\VC\lib\amd64\msvcrtd.lib: skipped 1728, total 1825
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS8\VC\lib\amd64\msvcurt.lib: skipped 1827, total 4815
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS8\VC\lib\amd64\msvcurtd.lib: skipped 1912, total 5240

$ tar -czvf VS8/VS8_amd64.tar.gz VS8/VC/lib/amd64/*.pat
VS8/VC/lib/amd64/libcmt.lib.pat
VS8/VC/lib/amd64/libcmtd.lib.pat
VS8/VC/lib/amd64/libcpmt.lib.pat
VS8/VC/lib/amd64/libcpmtd.lib.pat
VS8/VC/lib/amd64/msvcmrt.lib.pat
VS8/VC/lib/amd64/msvcmrtd.lib.pat
VS8/VC/lib/amd64/msvcprt.lib.pat
VS8/VC/lib/amd64/msvcprtd.lib.pat
VS8/VC/lib/amd64/msvcrt.lib.pat
VS8/VC/lib/amd64/msvcrtd.lib.pat
VS8/VC/lib/amd64/msvcurt.lib.pat
VS8/VC/lib/amd64/msvcurtd.lib.pat
```

```
$ wc -l VS8/VC/lib/*.pat
   2774 VS8/VC/lib/libcmt.lib.pat
   3054 VS8/VC/lib/libcmtd.lib.pat
   4463 VS8/VC/lib/libcpmt.lib.pat
   5939 VS8/VC/lib/libcpmtd.lib.pat
    217 VS8/VC/lib/msvcmrt.lib.pat
    218 VS8/VC/lib/msvcmrtd.lib.pat
      3 VS8/VC/lib/msvcprt.lib.pat
      4 VS8/VC/lib/msvcprtd.lib.pat
    128 VS8/VC/lib/msvcrt.lib.pat
    133 VS8/VC/lib/msvcrtd.lib.pat
   2989 VS8/VC/lib/msvcurt.lib.pat
   3329 VS8/VC/lib/msvcurtd.lib.pat
  23251 total

$ wc -l VS8/VC/lib/amd64/*.pat
    2738 VS8/VC/lib/amd64/libcmt.lib.pat
    3005 VS8/VC/lib/amd64/libcmtd.lib.pat
    3987 VS8/VC/lib/amd64/libcpmt.lib.pat
    5150 VS8/VC/lib/amd64/libcpmtd.lib.pat
     217 VS8/VC/lib/amd64/msvcmrt.lib.pat
     218 VS8/VC/lib/amd64/msvcmrtd.lib.pat
       2 VS8/VC/lib/amd64/msvcprt.lib.pat
       4 VS8/VC/lib/amd64/msvcprtd.lib.pat
      95 VS8/VC/lib/amd64/msvcrt.lib.pat
      98 VS8/VC/lib/amd64/msvcrtd.lib.pat
    2989 VS8/VC/lib/amd64/msvcurt.lib.pat
    3329 VS8/VC/lib/amd64/msvcurtd.lib.pat
   21832 total

$ du -h VS8/*.tar.gz
1.5M    VS8/VS8.tar.gz
1.7M    VS8/VS8_amd64.tar.gz
```
