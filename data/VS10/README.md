# VS10 / Visual Studio 2010

# download
Visual Studio 2010 Professional
`en_visual_studio_2010_professional_x86_dvd_509727.iso`

# prepare
run `setup.exe`

# get lib/obj files
```
$ find /cygdrive/c/Program\ Files\ \(x86\)/Microsoft\ Visual\ Studio\ 10.0/VC/ -iname "*.lib"
./VC/atlmfc/lib/amd64/atl.lib
./VC/atlmfc/lib/amd64/atls.lib
./VC/atlmfc/lib/amd64/atlsd.lib
./VC/atlmfc/lib/amd64/mfc100.lib
./VC/atlmfc/lib/amd64/mfc100d.lib
./VC/atlmfc/lib/amd64/mfc100u.lib
./VC/atlmfc/lib/amd64/mfc100ud.lib
./VC/atlmfc/lib/amd64/MFCM100.lib
./VC/atlmfc/lib/amd64/MFCM100d.lib
./VC/atlmfc/lib/amd64/MFCM100U.lib
./VC/atlmfc/lib/amd64/MFCM100Ud.lib
./VC/atlmfc/lib/amd64/mfcs100.lib
./VC/atlmfc/lib/amd64/mfcs100d.lib
./VC/atlmfc/lib/amd64/mfcs100u.lib
./VC/atlmfc/lib/amd64/mfcs100ud.lib
./VC/atlmfc/lib/amd64/nafxcw.lib
./VC/atlmfc/lib/amd64/nafxcwd.lib
./VC/atlmfc/lib/amd64/uafxcw.lib
./VC/atlmfc/lib/amd64/uafxcwd.lib
./VC/atlmfc/lib/Atl.lib
./VC/atlmfc/lib/atls.lib
./VC/atlmfc/lib/atlsd.lib
./VC/atlmfc/lib/mfc100.lib
./VC/atlmfc/lib/mfc100d.lib
./VC/atlmfc/lib/mfc100u.lib
./VC/atlmfc/lib/mfc100ud.lib
./VC/atlmfc/lib/MFCM100.lib
./VC/atlmfc/lib/MFCM100d.lib
./VC/atlmfc/lib/MFCM100U.lib
./VC/atlmfc/lib/MFCM100Ud.lib
./VC/atlmfc/lib/mfcs100.lib
./VC/atlmfc/lib/mfcs100d.lib
./VC/atlmfc/lib/mfcs100u.lib
./VC/atlmfc/lib/mfcs100ud.lib
./VC/atlmfc/lib/nafxcw.lib
./VC/atlmfc/lib/nafxcwd.lib
./VC/atlmfc/lib/uafxcw.lib
./VC/atlmfc/lib/uafxcwd.lib
./VC/lib/amd64/comsupp.lib
./VC/lib/amd64/comsuppd.lib
./VC/lib/amd64/comsuppw.lib
./VC/lib/amd64/comsuppwd.lib
./VC/lib/amd64/delayimp.lib
./VC/lib/amd64/libcmt.lib
./VC/lib/amd64/libcmtd.lib
./VC/lib/amd64/libcpmt.lib
./VC/lib/amd64/libcpmt1.lib
./VC/lib/amd64/libcpmtd.lib
./VC/lib/amd64/libcpmtd0.lib
./VC/lib/amd64/libcpmtd1.lib
./VC/lib/amd64/msvcmrt.lib
./VC/lib/amd64/msvcmrtd.lib
./VC/lib/amd64/msvcprt.lib
./VC/lib/amd64/msvcprtd.lib
./VC/lib/amd64/msvcrt.lib
./VC/lib/amd64/msvcrtd.lib
./VC/lib/amd64/msvcurt.lib
./VC/lib/amd64/msvcurtd.lib
./VC/lib/amd64/oldnames.lib
./VC/lib/amd64/pgobootrun.lib
./VC/lib/amd64/pgort.lib
./VC/lib/amd64/ptrustm.lib
./VC/lib/amd64/ptrustmd.lib
./VC/lib/amd64/ptrustu.lib
./VC/lib/amd64/ptrustud.lib
./VC/lib/amd64/runtmchk.lib
./VC/lib/amd64/vcomp.lib
./VC/lib/amd64/vcompd.lib
./VC/lib/comsupp.lib
./VC/lib/comsuppd.lib
./VC/lib/comsuppw.lib
./VC/lib/comsuppwd.lib
./VC/lib/delayimp.lib
./VC/lib/libcmt.lib
./VC/lib/libcmtd.lib
./VC/lib/libcpmt.lib
./VC/lib/libcpmt1.lib
./VC/lib/libcpmtd.lib
./VC/lib/libcpmtd0.lib
./VC/lib/libcpmtd1.lib
./VC/lib/msvcmrt.lib
./VC/lib/msvcmrtd.lib
./VC/lib/msvcprt.lib
./VC/lib/msvcprtd.lib
./VC/lib/msvcrt.lib
./VC/lib/msvcrtd.lib
./VC/lib/msvcurt.lib
./VC/lib/msvcurtd.lib
./VC/lib/oldnames.lib
./VC/lib/pgobootrun.lib
./VC/lib/pgort.lib
./VC/lib/ptrustm.lib
./VC/lib/ptrustmd.lib
./VC/lib/ptrustu.lib
./VC/lib/ptrustud.lib
./VC/lib/RunTmChk.lib
./VC/lib/vcomp.lib
./VC/lib/vcompd.lib

$ find /cygdrive/c/Program\ Files\ \(x86\)/Microsoft\ Visual\ Studio\ 10.0/ -iname "*.obj"
./VC/lib/amd64/binmode.obj
./VC/lib/amd64/chkstk.obj
./VC/lib/amd64/commode.obj
./VC/lib/amd64/invalidcontinue.obj
./VC/lib/amd64/loosefpmath.obj
./VC/lib/amd64/newmode.obj
./VC/lib/amd64/noarg.obj
./VC/lib/amd64/nochkclr.obj
./VC/lib/amd64/noenv.obj
./VC/lib/amd64/nohetoc.obj
./VC/lib/amd64/nothrownew.obj
./VC/lib/amd64/pbinmode.obj
./VC/lib/amd64/pcommode.obj
./VC/lib/amd64/pinvalidcontinue.obj
./VC/lib/amd64/pnewmode.obj
./VC/lib/amd64/pnoarg.obj
./VC/lib/amd64/pnoenv.obj
./VC/lib/amd64/pnothrownew.obj
./VC/lib/amd64/psetargv.obj
./VC/lib/amd64/pthreadlocale.obj
./VC/lib/amd64/pwsetargv.obj
./VC/lib/amd64/setargv.obj
./VC/lib/amd64/smalheap.obj
./VC/lib/amd64/threadlocale.obj
./VC/lib/amd64/wsetargv.obj
./VC/lib/binmode.obj
./VC/lib/chkstk.obj
./VC/lib/commode.obj
./VC/lib/fp10.obj
./VC/lib/invalidcontinue.obj
./VC/lib/loosefpmath.obj
./VC/lib/newmode.obj
./VC/lib/noarg.obj
./VC/lib/nochkclr.obj
./VC/lib/noenv.obj
./VC/lib/nohetoc.obj
./VC/lib/nothrownew.obj
./VC/lib/pbinmode.obj
./VC/lib/pcommode.obj
./VC/lib/pinvalidcontinue.obj
./VC/lib/pnewmode.obj
./VC/lib/pnoarg.obj
./VC/lib/pnoenv.obj
./VC/lib/pnothrownew.obj
./VC/lib/psetargv.obj
./VC/lib/pthreadlocale.obj
./VC/lib/pwsetargv.obj
./VC/lib/setargv.obj
./VC/lib/smalheap.obj
./VC/lib/threadlocale.obj
./VC/lib/wsetargv.obj

$ rsync -a --prune-empty-dirs --include '*/' --include '*.obj' --include '*.lib' --exclude '*' /cygdrive/c/Program\ Files\ \(x86\)/Microsoft\ Visual\ Studio\ 10.0/VC/ VS10/
```

# generate and zip .pat

focus on C/C++ run time libraries

```
$ find VS10/ -type f \( -iname "*libc*" -o -iname "*msvc*" -o -iname "*libvc*" -o -iname "*vcruntime*" -o -iname "*libucrt*" \) -exec md5sum {} \;
10f88aa58fb3877baefdae5b532e6c1d *VS10/VC/lib/amd64/libcmt.lib
73dc7c5fb28dde7c193535a7b3333f05 *VS10/VC/lib/amd64/libcmtd.lib
161d38672aa370c8b62d4e9741992d0f *VS10/VC/lib/amd64/libcpmt.lib
1d3473e1dbe799b3cd1cc601e8c2d864 *VS10/VC/lib/amd64/libcpmt1.lib
72346cff5dcdec9299707e9a3c1f82a4 *VS10/VC/lib/amd64/libcpmtd.lib
86c49065d430bb61a851653f25a640d5 *VS10/VC/lib/amd64/libcpmtd0.lib
c94274f781f6b070c237579c78ff31c1 *VS10/VC/lib/amd64/libcpmtd1.lib
14b9cbbe4fc25a89a2bfb5dc9a8f2320 *VS10/VC/lib/amd64/msvcmrt.lib
53f2bb449f38cbe9ba30935c753f4de1 *VS10/VC/lib/amd64/msvcmrtd.lib
099c98e974304dbbfb729031a4183ef2 *VS10/VC/lib/amd64/msvcprt.lib
2b8dff50fad19aba588ce3934078953f *VS10/VC/lib/amd64/msvcprtd.lib
d41a3905a2f29aabc15c7acf9c4b9f7f *VS10/VC/lib/amd64/msvcrt.lib
aaab48afa8a52d08f2abc461154cd50e *VS10/VC/lib/amd64/msvcrtd.lib
e37648c19862b1c44fe60dd7749ae58e *VS10/VC/lib/amd64/msvcurt.lib
73e6cec7786ae9d8cb5cef8394d2cc3b *VS10/VC/lib/amd64/msvcurtd.lib
6fd52b779b0b19f1b568f85401a9a367 *VS10/VC/lib/libcmt.lib
2cd424b214b90f06b50cd74286b45e00 *VS10/VC/lib/libcmtd.lib
262e0fe6c254c8cb23ec870284c88270 *VS10/VC/lib/libcpmt.lib
d8944ea54ec0744e62615ed42fdd9563 *VS10/VC/lib/libcpmt1.lib
32e3db44a101b3bd28420dc66d1285f9 *VS10/VC/lib/libcpmtd.lib
476b8d5ea8be69892977293870b54673 *VS10/VC/lib/libcpmtd0.lib
a32b036cf8a1e5e7f67b14ea0bd77df4 *VS10/VC/lib/libcpmtd1.lib
ec7579120740216007f7552324aebbe7 *VS10/VC/lib/msvcmrt.lib
f4f879d6496386220f9027e4e65834de *VS10/VC/lib/msvcmrtd.lib
7b80f3fdcf0e4ca25307cc49603b4a2b *VS10/VC/lib/msvcprt.lib
e7b2a8ace32a74231b3ae34500ef51dc *VS10/VC/lib/msvcprtd.lib
1b886a8520492228a52e7bea8263cd3e *VS10/VC/lib/msvcrt.lib
563d3aae805dc12abe7b1d7c324ad748 *VS10/VC/lib/msvcrtd.lib
11633ee4f0292bf9714ed64ec75c20a2 *VS10/VC/lib/msvcurt.lib
dec37089d5b6a08a0aa9fca460ad1f99 *VS10/VC/lib/msvcurtd.lib
```

## x86
```
$ find VS10/VC/lib/ -maxdepth 1 -type f \( -iname "*libc*" -o -iname "*msvc*" -o -iname "*libvc*" -o -iname "*vcruntime*" -o -iname "*libucrt*" \) -exec ../../pcf.exe -a {} VS10.pat \;
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS10\VC\lib\libcmt.lib: skipped 586, total 5895
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS10\VC\lib\libcmtd.lib: skipped 132, total 6115
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS10\VC\lib\libcpmt.lib: skipped 381, total 5587
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS10\VC\lib\libcpmt1.lib: skipped 472, total 6005
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS10\VC\lib\libcpmtd.lib: skipped 0, total 6657
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS10\VC\lib\libcpmtd0.lib: skipped 0, total 5939
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS10\VC\lib\libcpmtd1.lib: skipped 0, total 6403
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS10\VC\lib\msvcmrt.lib: skipped 283, total 651
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS10\VC\lib\msvcmrtd.lib: skipped 283, total 700
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS10\VC\lib\msvcprt.lib: skipped 1676, total 1689
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS10\VC\lib\msvcprtd.lib: skipped 1687, total 1703
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS10\VC\lib\msvcrt.lib: skipped 1897, total 2023
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS10\VC\lib\msvcrtd.lib: skipped 1958, total 2089
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS10\VC\lib\msvcurt.lib: skipped 3569, total 21803
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS10\VC\lib\msvcurtd.lib: skipped 3645, total 23139
```

## amd64
```
$ find VS10/VC/lib/amd64/ -type f \( -iname "*libc*" -o -iname "*msvc*" -o -iname "*libvc*" -o -iname "*vcruntime*" -o -iname "*libucrt*" \) -exec ../../pcf.exe -a {} VS10_amd64.pat \;
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS10\VC\lib\amd64\libcmt.lib: skipped 513, total 6079
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS10\VC\lib\amd64\libcmtd.lib: skipped 147, total 6326
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS10\VC\lib\amd64\libcpmt.lib: skipped 435, total 5637
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS10\VC\lib\amd64\libcpmt1.lib: skipped 558, total 6083
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS10\VC\lib\amd64\libcpmtd.lib: skipped 0, total 6608
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS10\VC\lib\amd64\libcpmtd0.lib: skipped 0, total 5890
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS10\VC\lib\amd64\libcpmtd1.lib: skipped 0, total 6354
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS10\VC\lib\amd64\msvcmrt.lib: skipped 281, total 649
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS10\VC\lib\amd64\msvcmrtd.lib: skipped 281, total 698
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS10\VC\lib\amd64\msvcprt.lib: skipped 1678, total 1689
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS10\VC\lib\amd64\msvcprtd.lib: skipped 1683, total 1699
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS10\VC\lib\amd64\msvcrt.lib: skipped 1866, total 1975
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS10\VC\lib\amd64\msvcrtd.lib: skipped 1928, total 2040
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS10\VC\lib\amd64\msvcurt.lib: skipped 3538, total 21772
C:\Users\moritz.raabe\code\Exclusions\parse_lib\gh_siglib\data\VS10\VC\lib\amd64\msvcurtd.lib: skipped 3609, total 23049
```

```
$ wc -l VS10*.pat
   79830 VS10.pat
   80032 VS10_amd64.pat

$ gzip -v -k VS10.pat
VS10.pat:        86.8% -- created VS10.pat.gz

$ gzip -v -k VS10_amd64.pat
VS10_amd64.pat:  86.9% -- created VS10_amd64.pat.gz

$ du -h VS10*.pat*
27M     VS10.pat
3.5M    VS10.pat.gz
28M     VS10_amd64.pat
3.7M    VS10_amd64.pat.gz
```
