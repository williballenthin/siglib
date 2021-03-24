# VS12 / Visual Studio 2013

# download
Visual Studio 2013 Professional
`en_visual_studio_professional_2013_x86_dvd_3175298.iso`

# prepare
run setup

# get lib/obj files
```
$ find /cygdrive/c/Program\ Files\ \(x86\)/Microsoft\ Visual\ Studio\ 12.0/VC/ -iname "*.lib"
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/afxnmcd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/afxnmcdd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/amd64/afxnmcd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/amd64/afxnmcdd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/amd64/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/amd64/mfc120u.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/amd64/mfc120ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/amd64/MFCM120U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/amd64/MFCM120Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/amd64/mfcs120u.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/amd64/mfcs120ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/amd64/uafxcw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/amd64/uafxcwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/arm/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/mfc120u.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/mfc120ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/MFCM120U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/MFCM120Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/mfcs120u.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/mfcs120ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/uafxcw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/uafxcwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/comsupp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/comsuppd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/delayimp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/libcpmt1.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/libcpmtd0.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/libcpmtd1.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/msvcmrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/msvcmrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/msvcprt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/msvcprtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/msvcurt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/msvcurtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/oldnames.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/pgobootrun.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/pgort.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/ptrustm.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/ptrustmd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/ptrustu.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/ptrustud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/runtmchk.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/vcamp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/vcampd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/vccorlib.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/vccorlibd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/vcomp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/vcompd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/VsGraphicsHelper.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/comsupp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/comsuppd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/delayimp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/libcpmt1.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/libcpmtd0.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/libcpmtd1.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/msvcmrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/msvcmrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/msvcprt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/msvcprtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/msvcurt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/msvcurtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/oldnames.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/pgobootrun.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/pgort.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/ptrustm.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/ptrustmd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/ptrustu.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/ptrustud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/runtmchk.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/vcamp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/vcampd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/vccorlib.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/vccorlibd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/vcomp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/vcompd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/VsGraphicsHelper.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/comsupp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/comsuppd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/delayimp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/libcpmt1.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/libcpmtd0.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/libcpmtd1.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/msvcmrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/msvcmrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/msvcprt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/msvcprtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/msvcurt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/msvcurtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/oldnames.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/pgobootrun.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/pgort.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/ptrustm.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/ptrustmd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/ptrustu.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/ptrustud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/RunTmChk.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/amd64/msvcprt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/amd64/msvcprtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/amd64/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/amd64/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/amd64/oldnames.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/amd64/vcamp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/amd64/vcampd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/amd64/vccorlib.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/amd64/vccorlibd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/amd64/vcomp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/amd64/vcompd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/arm/msvcprt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/arm/msvcprtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/arm/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/arm/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/arm/oldnames.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/arm/vcamp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/arm/vcampd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/arm/vccorlib.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/arm/vccorlibd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/arm/vcomp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/arm/vcompd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/msvcprt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/msvcprtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/oldnames.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/vcamp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/vcampd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/vccorlib.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/vccorlibd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/vcomp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/vcompd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/vcamp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/vcampd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/vccorlib.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/vccorlibd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/vcomp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/vcompd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/VsGraphicsHelper.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/UnitTest/lib/amd64/Microsoft.VisualStudio.TestTools.CppUnitTestFramework.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/UnitTest/lib/arm/Microsoft.VisualStudio.TestTools.CppUnitTestFramework.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/UnitTest/lib/Microsoft.VisualStudio.TestTools.CppUnitTestFramework.lib


$ find /cygdrive/c/Program\ Files\ \(x86\)/Microsoft\ Visual\ Studio\ 12.0/VC/ -iname "*.obj"
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/binmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/commode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/invalidcontinue.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/loosefpmath.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/newmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/noarg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/noenv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/nothrownew.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/pbinmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/pcommode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/pinvalidcontinue.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/pnewmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/pnoarg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/pnoenv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/pnothrownew.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/psetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/pthreadlocale.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/pwsetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/setargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/smalheap.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/threadlocale.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/wsetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/binmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/commode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/invalidcontinue.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/loosefpmath.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/newmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/noarg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/noenv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/nothrownew.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/setargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/smalheap.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/threadlocale.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/wsetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/binmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/commode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/fp10.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/invalidcontinue.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/loosefpmath.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/newmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/noarg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/noenv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/nohetoc.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/nothrownew.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/pbinmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/pcommode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/pinvalidcontinue.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/pnewmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/pnoarg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/pnoenv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/pnothrownew.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/psetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/pthreadlocale.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/pwsetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/setargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/smalheap.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/threadlocale.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/wsetargv.obj


$ rsync -a --prune-empty-dirs --include '*/' --include '*.obj' --include '*.lib' --exclude '*' /cygdrive/c/Program\ Files\ \(x86\)/Microsoft\ Visual\ Studio\ 12.0/VC/ VS12/
```

# generate and zip .pat

focus on C/C++ run time libraries

```
$ find VS12/ -type f \( -iname "*libc*" -o -iname "*msvc*" -o -iname "*libvc*" -o -iname "*vcruntime*" -o -iname "*libucrt*" \) -exec md5sum {} \;
ddbdbc8ee25b65d9f907fe03ae4dbe76 *VS12/VC/lib/amd64/libcmt.lib
c2029b8268677cf6a0cde48ae9c41c7a *VS12/VC/lib/amd64/libcmtd.lib
3e180e3a5ef5048c9b121831b5d40413 *VS12/VC/lib/amd64/libcpmt.lib
58eed00bbd2ccb244381c6f65e1aeeaa *VS12/VC/lib/amd64/libcpmt1.lib
bff9427565611ba8b205c06d9f6c5406 *VS12/VC/lib/amd64/libcpmtd.lib
a3a0d2b0badbecd4609f33b406953d20 *VS12/VC/lib/amd64/libcpmtd0.lib
e842063ead0e6c0b9a377d4811ee8fd7 *VS12/VC/lib/amd64/libcpmtd1.lib
7158f882e1c5d0be36cba1f36b484174 *VS12/VC/lib/amd64/msvcmrt.lib
3294a294632a16a58c0008b196ae9610 *VS12/VC/lib/amd64/msvcmrtd.lib
adf6d7320f8431901ea684a1b51c185f *VS12/VC/lib/amd64/msvcprt.lib
4440cb998b339932ed199d1491726e66 *VS12/VC/lib/amd64/msvcprtd.lib
42ef3ffe36b890adef8bbbbf2b2d60c7 *VS12/VC/lib/amd64/msvcrt.lib
e86e7e97b49dff5da178711c37edf218 *VS12/VC/lib/amd64/msvcrtd.lib
d9cd84cc802065f24097f370ffc7a9dc *VS12/VC/lib/amd64/msvcurt.lib
42cace273de1c6426a661f62868f750c *VS12/VC/lib/amd64/msvcurtd.lib
112f030229f0403d5617d5692ff65316 *VS12/VC/lib/libcmt.lib
0f00fe36ba33cae9608b95dc9e39b8c3 *VS12/VC/lib/libcmtd.lib
a4735b868c1e5cd3c18fa8b4b6eadb75 *VS12/VC/lib/libcpmt.lib
2ae3b60205f4795f90b873df62f46e09 *VS12/VC/lib/libcpmt1.lib
e78602726fa396735eec0c0caf76aa42 *VS12/VC/lib/libcpmtd.lib
d9df0aac90c328bc1b2f9844e6526207 *VS12/VC/lib/libcpmtd0.lib
c5d9538addd18b75e28f5132345406d7 *VS12/VC/lib/libcpmtd1.lib
971c04eaedb8417652b1d8c2167caa6e *VS12/VC/lib/msvcmrt.lib
781d4cf77bef264561f04b562ff93b81 *VS12/VC/lib/msvcmrtd.lib
edf5ed4648eeae547032a0143557488d *VS12/VC/lib/msvcprt.lib
157afcfd489c09f202b1372b7066770b *VS12/VC/lib/msvcprtd.lib
8bf2e8bb8815472b3c9cea487c5bbf23 *VS12/VC/lib/msvcrt.lib
7d9d8ad3a5d2092571e062851bafc10c *VS12/VC/lib/msvcrtd.lib
09ef762f303a2e1bb618b3bca7879d71 *VS12/VC/lib/msvcurt.lib
582823dbaefb9e0a115e6822611b235d *VS12/VC/lib/msvcurtd.lib
```

## x86
```
$ find VS12/VC/lib/ -maxdepth 1 -type f \( -iname "*libc*" -o -iname "*msvc*" -o -iname "*libvc*" -o -iname "*vcruntime*" -o -iname "*libucrt*" \) -exec ../../pcf.exe {} {}.pat \;
.\VS12\VC\lib\libcmt.lib: skipped 662, total 9232
.\VS12\VC\lib\libcmtd.lib: skipped 134, total 9591
.\VS12\VC\lib\libcpmt.lib: skipped 1042, total 10522
.\VS12\VC\lib\libcpmt1.lib: skipped 1235, total 11302
.\VS12\VC\lib\libcpmtd.lib: skipped 1, total 12219
.\VS12\VC\lib\libcpmtd0.lib: skipped 1, total 11024
.\VS12\VC\lib\libcpmtd1.lib: skipped 1, total 11938
.\VS12\VC\lib\msvcmrt.lib: skipped 285, total 549
.\VS12\VC\lib\msvcmrtd.lib: skipped 285, total 572
.\VS12\VC\lib\msvcprt.lib: skipped 1569, total 1577
.\VS12\VC\lib\msvcprtd.lib: skipped 1580, total 1595
.\VS12\VC\lib\msvcrt.lib: skipped 2248, total 2549
.\VS12\VC\lib\msvcrtd.lib: skipped 2309, total 2616
.\VS12\VC\lib\msvcurt.lib: skipped 3813, total 25722
.\VS12\VC\lib\msvcurtd.lib: skipped 3889, total 27241

$ tar -czvf VS12/VS12.tar.gz VS12/VC/lib/*.pat
VS12/VC/lib/libcmt.lib.pat
VS12/VC/lib/libcmtd.lib.pat
VS12/VC/lib/libcpmt.lib.pat
VS12/VC/lib/libcpmt1.lib.pat
VS12/VC/lib/libcpmtd.lib.pat
VS12/VC/lib/libcpmtd0.lib.pat
VS12/VC/lib/libcpmtd1.lib.pat
VS12/VC/lib/msvcmrt.lib.pat
VS12/VC/lib/msvcmrtd.lib.pat
VS12/VC/lib/msvcprt.lib.pat
VS12/VC/lib/msvcprtd.lib.pat
VS12/VC/lib/msvcrt.lib.pat
VS12/VC/lib/msvcrtd.lib.pat
VS12/VC/lib/msvcurt.lib.pat
VS12/VC/lib/msvcurtd.lib.pat
```

## amd64
```
$ find VS12/VC/lib/amd64/ -type f \( -iname "*libc*" -o -iname "*msvc*" -o -iname "*libvc*" -o -iname "*vcruntime*" -o -iname "*libucrt*" \) -exec ../../pcf.exe {} {}.pat \;
.\VS12\VC\lib\amd64\libcmt.lib: skipped 614, total 9170
.\VS12\VC\lib\amd64\libcmtd.lib: skipped 147, total 9546
.\VS12\VC\lib\amd64\libcpmt.lib: skipped 1290, total 10543
.\VS12\VC\lib\amd64\libcpmt1.lib: skipped 1521, total 11322
.\VS12\VC\lib\amd64\libcpmtd.lib: skipped 2, total 12118
.\VS12\VC\lib\amd64\libcpmtd0.lib: skipped 2, total 10923
.\VS12\VC\lib\amd64\libcpmtd1.lib: skipped 2, total 11837
.\VS12\VC\lib\amd64\msvcmrt.lib: skipped 283, total 547
.\VS12\VC\lib\amd64\msvcmrtd.lib: skipped 283, total 570
.\VS12\VC\lib\amd64\msvcprt.lib: skipped 1569, total 1577
.\VS12\VC\lib\amd64\msvcprtd.lib: skipped 1576, total 1591
.\VS12\VC\lib\amd64\msvcrt.lib: skipped 2202, total 2488
.\VS12\VC\lib\amd64\msvcrtd.lib: skipped 2264, total 2554
.\VS12\VC\lib\amd64\msvcurt.lib: skipped 3767, total 25676
.\VS12\VC\lib\amd64\msvcurtd.lib: skipped 3838, total 27106

$ tar -czvf VS12/VS12_amd64.tar.gz VS12/VC/lib/amd64/*.pat
VS12/VC/lib/amd64/libcmt.lib.pat
VS12/VC/lib/amd64/libcmtd.lib.pat
VS12/VC/lib/amd64/libcpmt.lib.pat
VS12/VC/lib/amd64/libcpmt1.lib.pat
VS12/VC/lib/amd64/libcpmtd.lib.pat
VS12/VC/lib/amd64/libcpmtd0.lib.pat
VS12/VC/lib/amd64/libcpmtd1.lib.pat
VS12/VC/lib/amd64/msvcmrt.lib.pat
VS12/VC/lib/amd64/msvcmrtd.lib.pat
VS12/VC/lib/amd64/msvcprt.lib.pat
VS12/VC/lib/amd64/msvcprtd.lib.pat
VS12/VC/lib/amd64/msvcrt.lib.pat
VS12/VC/lib/amd64/msvcrtd.lib.pat
VS12/VC/lib/amd64/msvcurt.lib.pat
VS12/VC/lib/amd64/msvcurtd.lib.pat
```

```
$ wc -l VS12/VC/lib/*.pat
    8571 VS12/VC/lib/libcmt.lib.pat
    9458 VS12/VC/lib/libcmtd.lib.pat
    9481 VS12/VC/lib/libcpmt.lib.pat
   10068 VS12/VC/lib/libcpmt1.lib.pat
   12219 VS12/VC/lib/libcpmtd.lib.pat
   11024 VS12/VC/lib/libcpmtd0.lib.pat
   11938 VS12/VC/lib/libcpmtd1.lib.pat
     265 VS12/VC/lib/msvcmrt.lib.pat
     288 VS12/VC/lib/msvcmrtd.lib.pat
       9 VS12/VC/lib/msvcprt.lib.pat
      16 VS12/VC/lib/msvcprtd.lib.pat
     302 VS12/VC/lib/msvcrt.lib.pat
     308 VS12/VC/lib/msvcrtd.lib.pat
   21910 VS12/VC/lib/msvcurt.lib.pat
   23353 VS12/VC/lib/msvcurtd.lib.pat
  119210 total

$ wc -l VS12/VC/lib/amd64/*.pat
    8557 VS12/VC/lib/amd64/libcmt.lib.pat
    9400 VS12/VC/lib/amd64/libcmtd.lib.pat
    9254 VS12/VC/lib/amd64/libcpmt.lib.pat
    9802 VS12/VC/lib/amd64/libcpmt1.lib.pat
   12117 VS12/VC/lib/amd64/libcpmtd.lib.pat
   10922 VS12/VC/lib/amd64/libcpmtd0.lib.pat
   11836 VS12/VC/lib/amd64/libcpmtd1.lib.pat
     265 VS12/VC/lib/amd64/msvcmrt.lib.pat
     288 VS12/VC/lib/amd64/msvcmrtd.lib.pat
       9 VS12/VC/lib/amd64/msvcprt.lib.pat
      16 VS12/VC/lib/amd64/msvcprtd.lib.pat
     287 VS12/VC/lib/amd64/msvcrt.lib.pat
     291 VS12/VC/lib/amd64/msvcrtd.lib.pat
   21910 VS12/VC/lib/amd64/msvcurt.lib.pat
   23269 VS12/VC/lib/amd64/msvcurtd.lib.pat
  118223 total

$ du -h VS12/*.tar.gz
5.2M    VS12/VS12.tar.gz
5.4M    VS12/VS12_amd64.tar.gz
```
