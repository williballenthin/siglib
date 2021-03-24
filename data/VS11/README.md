# VS11 / Visual Studio 2012

# download
Visual Studio 2012 Professional
`en_visual_studio_professional_2012_x86_dvd_2262334.iso`

# prepare
run `setup.exe`

# get lib/obj files
```
$ find /cygdrive/c/Program\ Files\ \(x86\)/Microsoft\ Visual\ Studio\ 11.0/VC/ -iname "*.lib"
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/afxnmcd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/afxnmcdd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/afxnmcd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/afxnmcdd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/atlsn.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/atlsnd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/mfc110.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/mfc110d.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/mfc110u.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/mfc110ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/MFCM110.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/MFCM110d.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/MFCM110U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/MFCM110Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/mfcs110.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/mfcs110d.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/mfcs110u.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/mfcs110ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/nafxcw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/nafxcwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/uafxcw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/uafxcwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/arm/atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/arm/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/arm/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/arm/atlsn.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/arm/atlsnd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/Atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/atlsn.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/atlsnd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/mfc110.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/mfc110d.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/mfc110u.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/mfc110ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/MFCM110.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/MFCM110d.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/MFCM110U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/MFCM110Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/mfcs110.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/mfcs110d.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/mfcs110u.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/mfcs110ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/nafxcw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/nafxcwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/uafxcw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/uafxcwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/comsupp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/comsuppd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/delayimp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/libcpmt1.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/libcpmtd0.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/libcpmtd1.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/msvcmrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/msvcmrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/msvcprt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/msvcprtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/msvcurt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/msvcurtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/oldnames.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/pgobootrun.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/pgort.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/ptrustm.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/ptrustmd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/ptrustu.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/ptrustud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/runtmchk.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/vcamp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/vcampd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/vccorlib.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/vccorlibd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/vcomp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/vcompd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/VsGraphicsHelper.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/comsupp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/comsuppd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/delayimp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/libcpmt1.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/libcpmtd0.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/libcpmtd1.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/msvcmrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/msvcmrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/msvcprt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/msvcprtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/msvcurt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/msvcurtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/oldnames.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/pgobootrun.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/pgort.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/ptrustm.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/ptrustmd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/ptrustu.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/ptrustud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/runtmchk.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/vcamp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/vcampd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/vccorlib.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/vccorlibd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/vcomp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/vcompd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/VsGraphicsHelper.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/comsupp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/comsuppd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/delayimp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/libcpmt1.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/libcpmtd0.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/libcpmtd1.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/msvcmrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/msvcmrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/msvcprt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/msvcprtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/msvcurt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/msvcurtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/oldnames.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/pgobootrun.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/pgort.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/ptrustm.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/ptrustmd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/ptrustu.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/ptrustud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/RunTmChk.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/vcamp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/vcampd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/vccorlib.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/vccorlibd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/vcomp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/vcompd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/VsGraphicsHelper.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/UnitTest/lib/amd64/Microsoft.VisualStudio.TestTools.CppUnitTestFramework.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/UnitTest/lib/arm/Microsoft.VisualStudio.TestTools.CppUnitTestFramework.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/UnitTest/lib/Microsoft.VisualStudio.TestTools.CppUnitTestFramework.lib


$ find /cygdrive/c/Program\ Files\ \(x86\)/Microsoft\ Visual\ Studio\ 11.0/VC/ -iname "*.obj"
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/binmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/commode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/invalidcontinue.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/loosefpmath.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/newmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/noarg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/noenv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/nothrownew.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/pbinmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/pcommode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/pinvalidcontinue.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/pnewmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/pnoarg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/pnoenv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/pnothrownew.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/psetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/pthreadlocale.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/pwsetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/setargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/smalheap.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/threadlocale.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/wsetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/binmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/commode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/invalidcontinue.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/loosefpmath.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/newmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/noarg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/noenv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/nothrownew.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/setargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/smalheap.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/threadlocale.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/wsetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/binmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/commode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/fp10.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/invalidcontinue.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/loosefpmath.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/newmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/noarg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/noenv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/nohetoc.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/nothrownew.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/pbinmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/pcommode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/pinvalidcontinue.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/pnewmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/pnoarg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/pnoenv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/pnothrownew.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/psetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/pthreadlocale.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/pwsetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/setargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/smalheap.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/threadlocale.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/wsetargv.obj


$ rsync -a --prune-empty-dirs --include '*/' --include '*.obj' --include '*.lib' --exclude '*' /cygdrive/c/Program\ Files\ \(x86\)/Microsoft\ Visual\ Studio\ 11.0/VC/ VS11/
```

# generate and zip .pat

focus on C/C++ run time libraries

```
$ find VS11/ -type f \( -iname "*libc*" -o -iname "*msvc*" -o -iname "*libvc*" -o -iname "*vcruntime*" -o -iname "*libucrt*" \) -exec md5sum {} \;
625c7d7a45e810e39da0e3459e8f8091 *VS11/VC/lib/amd64/libcmt.lib
84782cd8084001b30bdf133525cdae01 *VS11/VC/lib/amd64/libcmtd.lib
b6f20a821197699cd2d2dbcb93c6a4ef *VS11/VC/lib/amd64/libcpmt.lib
25d9e78773a3d62b0ca60c3fdb4bfe38 *VS11/VC/lib/amd64/libcpmt1.lib
17974debb1007b308afdc12e6c36afb6 *VS11/VC/lib/amd64/libcpmtd.lib
fb9b43c4aa68d8ef0c3637005fde9ee3 *VS11/VC/lib/amd64/libcpmtd0.lib
44fd1f6f6ee715017b76498e7d121b13 *VS11/VC/lib/amd64/libcpmtd1.lib
e8ce196212fc8c549f967a1469736dcf *VS11/VC/lib/amd64/msvcmrt.lib
4fd3d6a5d8f8f7c8af4743fa2ffe0393 *VS11/VC/lib/amd64/msvcmrtd.lib
91e532e859b36cdc6f99be11efd1a17d *VS11/VC/lib/amd64/msvcprt.lib
d858184fc6f3669fe749b5c6be12946e *VS11/VC/lib/amd64/msvcprtd.lib
d75c651ddc1c864c9f162ac4509c63a7 *VS11/VC/lib/amd64/msvcrt.lib
656b5599c3f3dba04e4cf0876e477169 *VS11/VC/lib/amd64/msvcrtd.lib
62a2380a4844f8bff0625b59a350a138 *VS11/VC/lib/amd64/msvcurt.lib
855bce1a7c2eb1e68db3534a4a8dd5bb *VS11/VC/lib/amd64/msvcurtd.lib
e9c06eb62fc3a90eb4d4f3cd16fadd1b *VS11/VC/lib/libcmt.lib
8d367236bedd1461348971d888749740 *VS11/VC/lib/libcmtd.lib
6107a7b9cac8acf4bc18d1a8099c7416 *VS11/VC/lib/libcpmt.lib
61048d8a9090112e8665e92b4bacf419 *VS11/VC/lib/libcpmt1.lib
2271770d19f55f52b878aa57bf0a5267 *VS11/VC/lib/libcpmtd.lib
fcbab6878371f2b1e37299d98c40e340 *VS11/VC/lib/libcpmtd0.lib
89046c7b1ce92cc74ea95c8ebadaf72c *VS11/VC/lib/libcpmtd1.lib
17b59912e897a651396e59e73036dc34 *VS11/VC/lib/msvcmrt.lib
a88cbccbe18a730e693e2d8324ee534d *VS11/VC/lib/msvcmrtd.lib
540095f4376282444a96e5f315835347 *VS11/VC/lib/msvcprt.lib
0cb0cda4453162a67b952b4761bc1c74 *VS11/VC/lib/msvcprtd.lib
f0271eda37dd690112b0d34e73ddbfff *VS11/VC/lib/msvcrt.lib
6516a12b9ea118431533e3c97c4ded80 *VS11/VC/lib/msvcrtd.lib
1cece1efb82c18cbe59d07db37a2b1f4 *VS11/VC/lib/msvcurt.lib
1cbd218b140786941bd5f580e92a6091 *VS11/VC/lib/msvcurtd.lib
```

## x86
```
$ find VS11/VC/lib/ -maxdepth 1 -type f \( -iname "*libc*" -o -iname "*msvc*" -o -iname "*libvc*" -o -iname "*vcruntime*" -o -iname "*libucrt*" \) -exec ../../pcf.exe {} {}.pat \;
.\VS11\VC\lib\libcmt.lib: skipped 664, total 6887
.\VS11\VC\lib\libcmtd.lib: skipped 134, total 7300
.\VS11\VC\lib\libcpmt.lib: skipped 1108, total 10080
.\VS11\VC\lib\libcpmt1.lib: skipped 1313, total 10929
.\VS11\VC\lib\libcpmtd.lib: skipped 1, total 11899
.\VS11\VC\lib\libcpmtd0.lib: skipped 1, total 10579
.\VS11\VC\lib\libcpmtd1.lib: skipped 1, total 11611
.\VS11\VC\lib\msvcmrt.lib: skipped 285, total 549
.\VS11\VC\lib\msvcmrtd.lib: skipped 285, total 570
.\VS11\VC\lib\msvcprt.lib: skipped 1591, total 1599
.\VS11\VC\lib\msvcprtd.lib: skipped 1602, total 1616
.\VS11\VC\lib\msvcrt.lib: skipped 1976, total 2261
.\VS11\VC\lib\msvcrtd.lib: skipped 2037, total 2328
.\VS11\VC\lib\msvcurt.lib: skipped 3563, total 25379
.\VS11\VC\lib\msvcurtd.lib: skipped 3639, total 26812

$ tar -czvf VS11/VS11.tar.gz VS11/VC/lib/*.pat
VS11/VC/lib/libcmt.lib.pat
VS11/VC/lib/libcmtd.lib.pat
VS11/VC/lib/libcpmt.lib.pat
VS11/VC/lib/libcpmt1.lib.pat
VS11/VC/lib/libcpmtd.lib.pat
VS11/VC/lib/libcpmtd0.lib.pat
VS11/VC/lib/libcpmtd1.lib.pat
VS11/VC/lib/msvcmrt.lib.pat
VS11/VC/lib/msvcmrtd.lib.pat
VS11/VC/lib/msvcprt.lib.pat
VS11/VC/lib/msvcprtd.lib.pat
VS11/VC/lib/msvcrt.lib.pat
VS11/VC/lib/msvcrtd.lib.pat
VS11/VC/lib/msvcurt.lib.pat
VS11/VC/lib/msvcurtd.lib.pat
```

## amd64
```
$ find VS11/VC/lib/amd64/ -type f \( -iname "*libc*" -o -iname "*msvc*" -o -iname "*libvc*" -o -iname "*vcruntime*" -o -iname "*libucrt*" \) -exec ../../pcf.exe {} {}.pat \;
.\VS11\VC\lib\amd64\libcmt.lib: skipped 561, total 7084
.\VS11\VC\lib\amd64\libcmtd.lib: skipped 149, total 7514
.\VS11\VC\lib\amd64\libcpmt.lib: skipped 1263, total 10110
.\VS11\VC\lib\amd64\libcpmt1.lib: skipped 1505, total 10951
.\VS11\VC\lib\amd64\libcpmtd.lib: skipped 0, total 11818
.\VS11\VC\lib\amd64\libcpmtd0.lib: skipped 0, total 10498
.\VS11\VC\lib\amd64\libcpmtd1.lib: skipped 0, total 11530
.\VS11\VC\lib\amd64\msvcmrt.lib: skipped 283, total 547
.\VS11\VC\lib\amd64\msvcmrtd.lib: skipped 283, total 568
.\VS11\VC\lib\amd64\msvcprt.lib: skipped 1591, total 1599
.\VS11\VC\lib\amd64\msvcprtd.lib: skipped 1598, total 1612
.\VS11\VC\lib\amd64\msvcrt.lib: skipped 1932, total 2203
.\VS11\VC\lib\amd64\msvcrtd.lib: skipped 1994, total 2269
.\VS11\VC\lib\amd64\msvcurt.lib: skipped 3519, total 25335
.\VS11\VC\lib\amd64\msvcurtd.lib: skipped 3590, total 26679

$ tar -czvf VS11/VS11_amd64.tar.gz VS11/VC/lib/amd64/*.pat
VS11/VC/lib/amd64/libcmt.lib.pat
VS11/VC/lib/amd64/libcmtd.lib.pat
VS11/VC/lib/amd64/libcpmt.lib.pat
VS11/VC/lib/amd64/libcpmt1.lib.pat
VS11/VC/lib/amd64/libcpmtd.lib.pat
VS11/VC/lib/amd64/libcpmtd0.lib.pat
VS11/VC/lib/amd64/libcpmtd1.lib.pat
VS11/VC/lib/amd64/msvcmrt.lib.pat
VS11/VC/lib/amd64/msvcmrtd.lib.pat
VS11/VC/lib/amd64/msvcprt.lib.pat
VS11/VC/lib/amd64/msvcprtd.lib.pat
VS11/VC/lib/amd64/msvcrt.lib.pat
VS11/VC/lib/amd64/msvcrtd.lib.pat
VS11/VC/lib/amd64/msvcurt.lib.pat
VS11/VC/lib/amd64/msvcurtd.lib.pat
```

```
$ wc -l VS11/VC/lib/*.pat
    6224 VS11/VC/lib/libcmt.lib.pat
    7167 VS11/VC/lib/libcmtd.lib.pat
    8973 VS11/VC/lib/libcpmt.lib.pat
    9617 VS11/VC/lib/libcpmt1.lib.pat
   11899 VS11/VC/lib/libcpmtd.lib.pat
   10579 VS11/VC/lib/libcpmtd0.lib.pat
   11611 VS11/VC/lib/libcpmtd1.lib.pat
     265 VS11/VC/lib/msvcmrt.lib.pat
     286 VS11/VC/lib/msvcmrtd.lib.pat
       9 VS11/VC/lib/msvcprt.lib.pat
      15 VS11/VC/lib/msvcprtd.lib.pat
     286 VS11/VC/lib/msvcrt.lib.pat
     292 VS11/VC/lib/msvcrtd.lib.pat
   21817 VS11/VC/lib/msvcurt.lib.pat
   23174 VS11/VC/lib/msvcurtd.lib.pat
  112214 total

$ wc -l VS11/VC/lib/amd64/*.pat
    6524 VS11/VC/lib/amd64/libcmt.lib.pat
    7366 VS11/VC/lib/amd64/libcmtd.lib.pat
    8848 VS11/VC/lib/amd64/libcpmt.lib.pat
    9447 VS11/VC/lib/amd64/libcpmt1.lib.pat
   11819 VS11/VC/lib/amd64/libcpmtd.lib.pat
   10499 VS11/VC/lib/amd64/libcpmtd0.lib.pat
   11531 VS11/VC/lib/amd64/libcpmtd1.lib.pat
     265 VS11/VC/lib/amd64/msvcmrt.lib.pat
     286 VS11/VC/lib/amd64/msvcmrtd.lib.pat
       9 VS11/VC/lib/amd64/msvcprt.lib.pat
      15 VS11/VC/lib/amd64/msvcprtd.lib.pat
     272 VS11/VC/lib/amd64/msvcrt.lib.pat
     276 VS11/VC/lib/amd64/msvcrtd.lib.pat
   21817 VS11/VC/lib/amd64/msvcurt.lib.pat
   23090 VS11/VC/lib/amd64/msvcurtd.lib.pat
  112064 total


$ gzip -v -k VS11.pat
VS11.pat:        87.7% -- created VS11.pat.gz

$ gzip -v -k VS11_amd64.pat
VS11_amd64.pat:  87.6% -- created VS11_amd64.pat.gz

$ du -h VS11/*.tar.gz
5.0M    VS11/VS11.tar.gz
5.1M    VS11/VS11_amd64.tar.gz
```
