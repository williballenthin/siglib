# VS9 / Visual Studio 2008

# download
Visual Studio 2008 Professional Edition
`en_visual_studio_2008_professional_x86_dvd_x14-26326.iso`

# prepare
run setup

# get lib/obj files
```
$ find /cygdrive/c/Program\ Files\ \(x86\)/Microsoft\ Visual\ Studio\ 9.0/VC/ -iname "*.lib"
$ find /cygdrive/c/Program\ Files\ \(x86\)/Microsoft\ Visual\ Studio\ 9.0/VC/ -iname "*.lib"
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/atldload.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/mfc90.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/mfc90d.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/mfc90u.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/mfc90ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/mfcdload.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/MFCM90.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/MFCM90D.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/MFCM90U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/MFCM90UD.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/mfcs90.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/mfcs90d.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/mfcs90u.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/mfcs90ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/nafxcw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/nafxcwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/uafxcw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/uafxcwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/Atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/atldload.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/mfc90.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/mfc90d.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/mfc90u.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/mfc90ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/mfcdload.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/mfcm90.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/mfcm90d.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/mfcm90u.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/mfcm90ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/mfcs90.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/mfcs90d.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/mfcs90u.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/mfcs90ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/nafxcw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/nafxcwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/uafxcw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/uafxcwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/armv4/atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/armv4/atlosapis.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/armv4/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/armv4/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/armv4/MFC90U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/armv4/MFC90Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/armv4/mfcs90U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/armv4/mfcs90Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/armv4/UafxcW.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/armv4/UafxcWD.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/armv4i/atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/armv4i/atlosapis.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/armv4i/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/armv4i/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/armv4i/MFC90U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/armv4i/MFC90Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/armv4i/mfcs90U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/armv4i/mfcs90Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/armv4i/UafxcW.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/armv4i/UafxcWD.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsii/atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsii/atlosapis.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsii/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsii/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsii/MFC90U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsii/MFC90Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsii/mfcs90U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsii/mfcs90Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsii/UafxcW.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsii/UafxcWD.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsii_fp/atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsii_fp/atlosapis.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsii_fp/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsii_fp/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsii_fp/MFC90U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsii_fp/MFC90Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsii_fp/mfcs90U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsii_fp/mfcs90Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsii_fp/UafxcW.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsii_fp/UafxcWD.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsiv/atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsiv/atlosapis.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsiv/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsiv/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsiv/MFC90U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsiv/MFC90Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsiv/mfcs90U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsiv/mfcs90Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsiv/UafxcW.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsiv/UafxcWD.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsiv_fp/atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsiv_fp/atlosapis.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsiv_fp/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsiv_fp/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsiv_fp/MFC90U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsiv_fp/MFC90Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsiv_fp/mfcs90U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsiv_fp/mfcs90Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsiv_fp/UafxcW.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsiv_fp/UafxcWD.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/sh4/atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/sh4/atlosapis.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/sh4/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/sh4/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/sh4/MFC90U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/sh4/MFC90Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/sh4/mfcs90U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/sh4/mfcs90Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/sh4/UafxcW.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/sh4/UafxcWD.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/x86/atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/x86/atlosapis.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/x86/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/x86/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/x86/MFC90U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/x86/MFC90Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/x86/mfcs90U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/x86/mfcs90Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/x86/UafxcW.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/x86/UafxcWD.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/armv4/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/armv4/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/armv4/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/armv4/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/armv4/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/armv4/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/armv4/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/armv4/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/armv4i/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/armv4i/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/armv4i/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/armv4i/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/armv4i/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/armv4i/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/armv4i/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/armv4i/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsii/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsii/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsii/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsii/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsii/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsii/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsii/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsii/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsii_fp/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsii_fp/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsii_fp/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsii_fp/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsii_fp/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsii_fp/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsii_fp/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsii_fp/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsiv/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsiv/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsiv/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsiv/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsiv/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsiv/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsiv/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsiv/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsiv_fp/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsiv_fp/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsiv_fp/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsiv_fp/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsiv_fp/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsiv_fp/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsiv_fp/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsiv_fp/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/sh4/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/sh4/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/sh4/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/sh4/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/sh4/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/sh4/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/sh4/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/sh4/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/x86/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/x86/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/x86/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/x86/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/x86/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/x86/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/x86/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/x86/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/almap.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/almapdll.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/conv.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/eh.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/rtc.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/tran.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/mt_lib/conv.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/mt_lib/eh.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/mt_lib/rtc.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/mt_lib/tran.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/sdknames.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/tcmap.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/tcmapdll.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/conv.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/eh.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/rtc.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/tran.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xmt_lib/conv.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xmt_lib/eh.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xmt_lib/rtc.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xmt_lib/tran.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/almap.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/almapdll.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/conv.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/eh.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/rtc.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/tran.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/conv.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/eh.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/rtc.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/tran.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/sdknames.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/tcmap.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/tcmapdll.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/conv.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/eh.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/rtc.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/tran.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/conv.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/eh.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/rtc.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/tran.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/comsupp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/comsuppd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/delayimp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/msvcmrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/msvcmrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/msvcprt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/msvcprtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/msvcurt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/msvcurtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/oldnames.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/pgobootrun.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/pgort.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/ptrustm.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/ptrustmd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/ptrustu.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/ptrustud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/runtmchk.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/vcomp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/vcompd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/comsupp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/comsuppd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/delayimp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/msvcmrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/msvcmrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/msvcprt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/msvcprtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/msvcurt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/msvcurtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/oldnames.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/opends60.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/pgobootrun.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/pgort.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/ptrustm.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/ptrustmd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/ptrustu.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/ptrustud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/RunTmChk.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/vcomp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/vcompd.lib


$ find /cygdrive/c/Program\ Files\ \(x86\)/Microsoft\ Visual\ Studio\ 9.0/VC/ -iname "*.obj"
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/amdsecgs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/chandler.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/chkstk2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/clr_obj/managdeh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/clr_obj/mehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/clr_obj/mehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/clr_obj/mehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/clr_obj/mehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/clr_obj/mehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/clr_obj/mstdexpt.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/ehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/ehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/ehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/ehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/ehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/gshandler.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/gshandlereh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/gshandlerseh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/jmpuwind.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/longjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/matherr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/memcpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/oldexcpt.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/pure_obj/managdeh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/pure_obj/mehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/pure_obj/mehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/pure_obj/mehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/pure_obj/mehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/pure_obj/mehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/pure_obj/rtti.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/rtcmd.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/setjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/setjmpex.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/tncleanup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/unhandld.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/mt_lib/amdsecgs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/mt_lib/chandler.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/mt_lib/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/mt_lib/chkstk2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/mt_lib/gshandler.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/mt_lib/gshandlereh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/mt_lib/gshandlerseh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/mt_lib/jmpuwind.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/mt_lib/longjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/mt_lib/matherr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/mt_lib/memcpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/mt_lib/rtcmd.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/mt_lib/setjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/mt_lib/setjmpex.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/amdsecgs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/chandler.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/chkstk2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/clr_obj/managdeh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/clr_obj/mehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/clr_obj/mehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/clr_obj/mehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/clr_obj/mehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/clr_obj/mehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/clr_obj/mstdexpt.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/ehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/ehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/ehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/ehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/ehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/gshandler.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/gshandlereh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/gshandlerseh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/jmpuwind.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/longjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/matherr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/memcpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/oldexcpt.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/pure_obj/managdeh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/pure_obj/mehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/pure_obj/mehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/pure_obj/mehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/pure_obj/mehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/pure_obj/mehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/pure_obj/rtti.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/rtcmd.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/setjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/setjmpex.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/tncleanup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/unhandld.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xmt_lib/amdsecgs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xmt_lib/chandler.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xmt_lib/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xmt_lib/chkstk2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xmt_lib/gshandler.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xmt_lib/gshandlereh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xmt_lib/gshandlerseh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xmt_lib/jmpuwind.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xmt_lib/longjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xmt_lib/matherr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xmt_lib/memcpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xmt_lib/rtcmd.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xmt_lib/setjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xmt_lib/setjmpex.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/alloca16.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/atlssup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/calldtor.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/chandler4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/chandler4gs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/chkesp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/clr_obj/managdeh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/clr_obj/mehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/clr_obj/mehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/clr_obj/mehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/clr_obj/mehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/clr_obj/mehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/clr_obj/mstdexpt.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/cpu_disp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/dllsupp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/eh3valid.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/ehprolg2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/ehprolg3.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/ehprolg3a.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/ehprolog.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/ehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/ehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/ehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/ehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/ehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/enable.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/exsup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/exsup2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/exsup3.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/exsup4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/ftol2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/inp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/lldiv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/lldvrm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/llmul.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/llrem.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/llshl.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/llshr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/longjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/matherr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/memccpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/memchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/memcmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/memcpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/memmove.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/memset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/oldexcpt.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/outp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/p4_memcpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/p4_memset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/pure_obj/managdeh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/pure_obj/mehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/pure_obj/mehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/pure_obj/mehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/pure_obj/mehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/pure_obj/mehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/pure_obj/rtti.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/sehprolg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/sehprolg4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/sehprolg4gs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/sehsupp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/setjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/setjmp3.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/setjmpex.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/strcat.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/strchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/strcmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/strcspn.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/strlen.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/strncat.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/strncpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/strnset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/strpbrk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/strrchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/strrev.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/strset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/strspn.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/strstr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/tncleanup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/ulldiv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/ulldvrm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/ullrem.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/ullshr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/unhandld.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/_memicmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/_strnicm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/alloca16.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/atlssup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/calldtor.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/chandler4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/chandler4gs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/chkesp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/eh3valid.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/enable.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/exsup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/exsup2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/exsup3.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/exsup4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/inp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/lldiv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/lldvrm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/llmul.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/llrem.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/llshl.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/llshr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/longjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/matherr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/memccpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/memchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/memcmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/memcpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/memmove.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/memset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/outp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/p4_memcpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/p4_memset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/sehprolg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/sehprolg4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/sehprolg4gs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/sehsupp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/setjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/setjmp3.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/setjmpex.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/strcat.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/strchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/strcmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/strcspn.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/strlen.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/strncat.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/strncpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/strnset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/strpbrk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/strrchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/strrev.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/strset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/strspn.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/strstr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/ulldiv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/ulldvrm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/ullrem.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/ullshr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/_memicmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/_strnicm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/alloca16.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/atlssup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/calldtor.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/chandler4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/chandler4gs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/chkesp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/clr_obj/managdeh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/clr_obj/mehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/clr_obj/mehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/clr_obj/mehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/clr_obj/mehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/clr_obj/mehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/clr_obj/mstdexpt.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/cpu_disp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/dllsupp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/eh3valid.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/ehprolg2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/ehprolg3.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/ehprolg3a.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/ehprolog.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/ehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/ehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/ehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/ehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/ehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/enable.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/exsup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/exsup2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/exsup3.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/exsup4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/ftol2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/inp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/lldiv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/lldvrm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/llmul.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/llrem.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/llshl.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/llshr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/longjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/matherr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/memccpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/memchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/memcmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/memcpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/memmove.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/memset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/oldexcpt.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/outp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/p4_memcpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/p4_memset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/pure_obj/managdeh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/pure_obj/mehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/pure_obj/mehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/pure_obj/mehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/pure_obj/mehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/pure_obj/mehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/pure_obj/rtti.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/sehprolg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/sehprolg4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/sehprolg4gs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/sehsupp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/setjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/setjmp3.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/setjmpex.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/strcat.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/strchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/strcmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/strcspn.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/strlen.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/strncat.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/strncpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/strnset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/strpbrk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/strrchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/strrev.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/strset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/strspn.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/strstr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/tncleanup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/ulldiv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/ulldvrm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/ullrem.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/ullshr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/unhandld.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/_memicmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/_strnicm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/alloca16.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/atlssup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/calldtor.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/chandler4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/chandler4gs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/chkesp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/eh3valid.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/enable.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/exsup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/exsup2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/exsup3.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/exsup4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/inp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/lldiv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/lldvrm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/llmul.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/llrem.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/llshl.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/llshr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/longjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/matherr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/memccpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/memchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/memcmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/memcpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/memmove.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/memset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/outp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/p4_memcpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/p4_memset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/sehprolg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/sehprolg4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/sehprolg4gs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/sehsupp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/setjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/setjmp3.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/setjmpex.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/strcat.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/strchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/strcmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/strcspn.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/strlen.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/strncat.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/strncpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/strnset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/strpbrk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/strrchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/strrev.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/strset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/strspn.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/strstr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/ulldiv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/ulldvrm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/ullrem.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/ullshr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/_memicmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/_strnicm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/binmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/commode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/invalidcontinue.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/loosefpmath.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/newmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/noarg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/nochkclr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/noenv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/nothrownew.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/pbinmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/pcommode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/pinvalidcontinue.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/pnewmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/pnoarg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/pnoenv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/pnothrownew.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/psetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/pthreadlocale.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/pwsetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/setargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/smalheap.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/threadlocale.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/wsetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/binmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/commode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/fp10.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/invalidcontinue.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/loosefpmath.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/newmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/noarg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/nochkclr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/noenv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/nothrownew.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/pbinmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/pcommode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/pinvalidcontinue.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/pnewmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/pnoarg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/pnoenv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/pnothrownew.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/psetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/pthreadlocale.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/pwsetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/setargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/smalheap.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/threadlocale.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/wsetargv.obj


$ rsync -a --prune-empty-dirs --include '*/' --include '*.obj' --include '*.Obj' --include '*.lib' --include '*.Lib' --exclude '*' /cygdrive/c/Program\ Files\ \(x86\)/Microsoft\ Visual\ Studio\ 9.0/VC/ VS9/
```

# generate and zip .pat

focus on C/C++ run time libraries

```
$ find VS9/ -type f \( -iname "*libc*" -o -iname "*msvc*" -o -iname "*libvc*" -o -iname "*vcruntime*" -o -iname "*libucrt*" \) -exec md5sum {} \;
a40a6ea3b70580e783c3d06a60a44589 *VS9/ce/lib/armv4/libcmt.lib
d347148c5ab91fef1f0e66c6112ebbd2 *VS9/ce/lib/armv4/libcmtd.lib
46cfad6c9c3482771ab7e4dfb0bc75b0 *VS9/ce/lib/armv4/libcpmt.lib
01c6a31987840eac8e89ecf4eb2b6857 *VS9/ce/lib/armv4/libcpmtd.lib
17a99fa3aa419d9e4619b4d48fea8620 *VS9/ce/lib/armv4/msvcrt.lib
341bbe8fddef8f8d29e4d79e0bfb88d4 *VS9/ce/lib/armv4/msvcrtd.lib
0801f30109736aa5bcc71f2571a2f4c8 *VS9/ce/lib/armv4i/libcmt.lib
753c878c48421aead82065b2b21247d5 *VS9/ce/lib/armv4i/libcmtd.lib
95b4f19741c61342d1eb1518f8194d19 *VS9/ce/lib/armv4i/libcpmt.lib
80231383ff4a93f062edaac5df2523f1 *VS9/ce/lib/armv4i/libcpmtd.lib
e70ac7d2f75222904bb940aa526a2ee4 *VS9/ce/lib/armv4i/msvcrt.lib
b5c14d6ac7d8b4e126932a4d1cedd25c *VS9/ce/lib/armv4i/msvcrtd.lib
3e68949deb964554f54c8d330609505f *VS9/ce/lib/mipsii/libcmt.lib
1534284da1680320ed2d6c9e569bbee0 *VS9/ce/lib/mipsii/libcmtd.lib
6c1fbc296cb8d84478cd02572dcf6e37 *VS9/ce/lib/mipsii/libcpmt.lib
8d1c71a74000314c0eb40b68e20b5295 *VS9/ce/lib/mipsii/libcpmtd.lib
0258814f0601e0c76e601548f0362e1c *VS9/ce/lib/mipsii/msvcrt.lib
2e956b91ec01ca64da0faea953bcf22c *VS9/ce/lib/mipsii/msvcrtd.lib
d6060d1767a1cbb0734a6ea84f9d0c6c *VS9/ce/lib/mipsii_fp/libcmt.lib
81a630a77b419630492fdcfa09ed4df4 *VS9/ce/lib/mipsii_fp/libcmtd.lib
c8593f3066c365be4fb5d41bf1b4bcff *VS9/ce/lib/mipsii_fp/libcpmt.lib
d1e0670953606e5f563bc247c8cb0ead *VS9/ce/lib/mipsii_fp/libcpmtd.lib
d05729abb8b03e1538bdaf62a61b771a *VS9/ce/lib/mipsii_fp/msvcrt.lib
e770f05f42f764d451e481038714ec27 *VS9/ce/lib/mipsii_fp/msvcrtd.lib
a8caa373f2e9038c5969682eb0874eda *VS9/ce/lib/mipsiv/libcmt.lib
0999a6b2ac91a66c2f0207d899eb2f5e *VS9/ce/lib/mipsiv/libcmtd.lib
dfcb8f105fa3aeee93d91fa2a6ac0372 *VS9/ce/lib/mipsiv/libcpmt.lib
7516884d379c826b577a333497035cef *VS9/ce/lib/mipsiv/libcpmtd.lib
d3e4a97f1dee1525bee91ddb2c9969e7 *VS9/ce/lib/mipsiv/msvcrt.lib
e29927360cab22e0d4e23be71962fe88 *VS9/ce/lib/mipsiv/msvcrtd.lib
ee39e9be1df4b6d8fca8f1ca2c389341 *VS9/ce/lib/mipsiv_fp/libcmt.lib
dc8979af35886aa621865861fe5c764a *VS9/ce/lib/mipsiv_fp/libcmtd.lib
791afa630d370d1c5d75a59f9a280ba7 *VS9/ce/lib/mipsiv_fp/libcpmt.lib
2c25288f502bc10e62d21d2b58267c4c *VS9/ce/lib/mipsiv_fp/libcpmtd.lib
d57685d8a2eb57eca20208fd07530d67 *VS9/ce/lib/mipsiv_fp/msvcrt.lib
4fde636c1e0edeb571d77d599d75cb71 *VS9/ce/lib/mipsiv_fp/msvcrtd.lib
9f767d5d20d912b508c71af1df0ef5a8 *VS9/ce/lib/sh4/libcmt.lib
b4364d95a0af8b99b1b66a033462c324 *VS9/ce/lib/sh4/libcmtd.lib
4bc80b35fb1540f52390a4755f2a5cfd *VS9/ce/lib/sh4/libcpmt.lib
db7c908d7d90e40384434b5d72d401d6 *VS9/ce/lib/sh4/libcpmtd.lib
d925e2674e391814dd1b9e4e581e97f9 *VS9/ce/lib/sh4/msvcrt.lib
9f62cda1b0a330f5490d6b629e3bca54 *VS9/ce/lib/sh4/msvcrtd.lib
20696bb33526394747dc47bd7021cc33 *VS9/ce/lib/x86/libcmt.lib
e01047d812ad163dc7c73aff453b66f4 *VS9/ce/lib/x86/libcmtd.lib
bf74bf1dfa542751c0ce98fd9a6f9f21 *VS9/ce/lib/x86/libcpmt.lib
0e56fc7e4619e4b339ffeebe7644a7b0 *VS9/ce/lib/x86/libcpmtd.lib
33812950e9f9c4d3d929def71504575d *VS9/ce/lib/x86/msvcrt.lib
95b66d43b683faf52daee5160d173a29 *VS9/ce/lib/x86/msvcrtd.lib
0af1d9dfe3c508f94060064f4bf738aa *VS9/lib/amd64/libcmt.lib
928d5df1155060ad39bbb787a75c50e0 *VS9/lib/amd64/libcmtd.lib
a348682c533736f0ece2db6a7ad933f1 *VS9/lib/amd64/libcpmt.lib
947b99f514a780e5c28da47221635517 *VS9/lib/amd64/libcpmtd.lib
251972ffb7dc9b2d2b908a048cd7da2d *VS9/lib/amd64/msvcmrt.lib
706f336c55a7d06be9b1471e5905330f *VS9/lib/amd64/msvcmrtd.lib
6b7cbcad13f114f3df1b47b001217c03 *VS9/lib/amd64/msvcprt.lib
b8473a900af9362de690f1645961a438 *VS9/lib/amd64/msvcprtd.lib
1dcf85c4890aee05f21e5c5a172d416a *VS9/lib/amd64/msvcrt.lib
f12ea6b8fee8ee555a35edb22f02c87e *VS9/lib/amd64/msvcrtd.lib
3986f9ea774baf0f017303e3a4be0b20 *VS9/lib/amd64/msvcurt.lib
33caec1be5220ab99472b58eed663b60 *VS9/lib/amd64/msvcurtd.lib
4504ce5c6ed2b431d2dfb694fe369764 *VS9/lib/libcmt.lib
ddb31aee384cafac3f8a2a8f96a24ec0 *VS9/lib/libcmtd.lib
694018acf53223228da7abdda150391a *VS9/lib/libcpmt.lib
7e876a095106916849d2e9b145cc8bd5 *VS9/lib/libcpmtd.lib
f2255d37a65bd4f2ab21aacc00f910ae *VS9/lib/msvcmrt.lib
83e6e9987e424926fb7196c0d457e76c *VS9/lib/msvcmrtd.lib
c786e09ed40f90b4d3e4d4783dfc1e32 *VS9/lib/msvcprt.lib
1d6ce2560f171297ee60344bbc198b78 *VS9/lib/msvcprtd.lib
f15b300c823a13d63121e666b2433672 *VS9/lib/msvcrt.lib
f6b8803049df0b827bceead808e68b34 *VS9/lib/msvcrtd.lib
c4c1643aeb554e3480d8fc918454f345 *VS9/lib/msvcurt.lib
cda86607643fc50b66ae11200735dab9 *VS9/lib/msvcurtd.lib
```

## manually deleted
- `ce`

## x86
```
$ find VS9/VC/lib/ -maxdepth 1 -type f \( -iname "*libc*" -o -iname "*msvc*" -o -iname "*libvc*" -o -iname "*vcruntime*" -o -iname "*libucrt*" \) -exec ../../pcf.exe {} {}.pat \;
.\VS9\VC\lib\libcmt.lib: skipped 294, total 3038
.\VS9\VC\lib\libcmtd.lib: skipped 132, total 3164
.\VS9\VC\lib\libcpmt.lib: skipped 262, total 4648
.\VS9\VC\lib\libcpmtd.lib: skipped 0, total 5784
.\VS9\VC\lib\msvcmrt.lib: skipped 306, total 578
.\VS9\VC\lib\msvcmrtd.lib: skipped 315, total 598
.\VS9\VC\lib\msvcprt.lib: skipped 3174, total 3182
.\VS9\VC\lib\msvcprtd.lib: skipped 3417, total 3429
.\VS9\VC\lib\msvcrt.lib: skipped 1724, total 1853
.\VS9\VC\lib\msvcrtd.lib: skipped 1788, total 1922
.\VS9\VC\lib\msvcurt.lib: skipped 1823, total 8951
.\VS9\VC\lib\msvcurtd.lib: skipped 1905, total 9703

$ tar -czvf VS9.tar.gz VS9/VC/lib/*.pat
VS9/VC/lib/libcmt.lib.pat
VS9/VC/lib/libcmtd.lib.pat
VS9/VC/lib/libcpmt.lib.pat
VS9/VC/lib/libcpmtd.lib.pat
VS9/VC/lib/msvcmrt.lib.pat
VS9/VC/lib/msvcmrtd.lib.pat
VS9/VC/lib/msvcprt.lib.pat
VS9/VC/lib/msvcprtd.lib.pat
VS9/VC/lib/msvcrt.lib.pat
VS9/VC/lib/msvcrtd.lib.pat
VS9/VC/lib/msvcurt.lib.pat
VS9/VC/lib/msvcurtd.lib.pat
```

## amd64
```
$ find VS9/VC/lib/amd64/ -type f \( -iname "*libc*" -o -iname "*msvc*" -o -iname "*libvc*" -o -iname "*vcruntime*" -o -iname "*libucrt*" \) -exec ../../pcf.exe {} {}.pat \;
.\VS9\VC\lib\amd64\libcmt.lib: skipped 310, total 3232
.\VS9\VC\lib\amd64\libcmtd.lib: skipped 133, total 3384
.\VS9\VC\lib\amd64\libcpmt.lib: skipped 294, total 4716
.\VS9\VC\lib\amd64\libcpmtd.lib: skipped 0, total 5737
.\VS9\VC\lib\amd64\msvcmrt.lib: skipped 304, total 576
.\VS9\VC\lib\amd64\msvcmrtd.lib: skipped 313, total 596
.\VS9\VC\lib\amd64\msvcprt.lib: skipped 3182, total 3189
.\VS9\VC\lib\amd64\msvcprtd.lib: skipped 3413, total 3425
.\VS9\VC\lib\amd64\msvcrt.lib: skipped 1677, total 1787
.\VS9\VC\lib\amd64\msvcrtd.lib: skipped 1740, total 1853
.\VS9\VC\lib\amd64\msvcurt.lib: skipped 1776, total 8905
.\VS9\VC\lib\amd64\msvcurtd.lib: skipped 1855, total 9640

$ tar -czvf VS9_amd64.tar.gz VS9/VC/lib/amd64/*.pat
VS9/VC/lib/amd64/libcmt.lib.pat
VS9/VC/lib/amd64/libcmtd.lib.pat
VS9/VC/lib/amd64/libcpmt.lib.pat
VS9/VC/lib/amd64/libcpmtd.lib.pat
VS9/VC/lib/amd64/msvcmrt.lib.pat
VS9/VC/lib/amd64/msvcmrtd.lib.pat
VS9/VC/lib/amd64/msvcprt.lib.pat
VS9/VC/lib/amd64/msvcprtd.lib.pat
VS9/VC/lib/amd64/msvcrt.lib.pat
VS9/VC/lib/amd64/msvcrtd.lib.pat
VS9/VC/lib/amd64/msvcurt.lib.pat
VS9/VC/lib/amd64/msvcurtd.lib.pat
```

```
$ wc -l VS9/VC/lib/*.pat
    2745 VS9/VC/lib/libcmt.lib.pat
    3033 VS9/VC/lib/libcmtd.lib.pat
    4387 VS9/VC/lib/libcpmt.lib.pat
    5785 VS9/VC/lib/libcpmtd.lib.pat
     273 VS9/VC/lib/msvcmrt.lib.pat
     284 VS9/VC/lib/msvcmrtd.lib.pat
       9 VS9/VC/lib/msvcprt.lib.pat
      13 VS9/VC/lib/msvcprtd.lib.pat
     130 VS9/VC/lib/msvcrt.lib.pat
     135 VS9/VC/lib/msvcrtd.lib.pat
    7129 VS9/VC/lib/msvcurt.lib.pat
    7799 VS9/VC/lib/msvcurtd.lib.pat
   31722 total

$ wc -l VS9/VC/lib/amd64/*.pat
    2923 VS9/VC/lib/amd64/libcmt.lib.pat
    3252 VS9/VC/lib/amd64/libcmtd.lib.pat
    4423 VS9/VC/lib/amd64/libcpmt.lib.pat
    5738 VS9/VC/lib/amd64/libcpmtd.lib.pat
     273 VS9/VC/lib/amd64/msvcmrt.lib.pat
     284 VS9/VC/lib/amd64/msvcmrtd.lib.pat
       8 VS9/VC/lib/amd64/msvcprt.lib.pat
      13 VS9/VC/lib/amd64/msvcprtd.lib.pat
     111 VS9/VC/lib/amd64/msvcrt.lib.pat
     114 VS9/VC/lib/amd64/msvcrtd.lib.pat
    7130 VS9/VC/lib/amd64/msvcurt.lib.pat
    7786 VS9/VC/lib/amd64/msvcurtd.lib.pat
   32055 total

$ du -h *.tar.gz
1.7M    VS9.tar.gz
1.8M    VS9_amd64.tar.gz
```
