# download
Service Pack 6 for Visual Basic 6.0, Visual C++ 6.0 with Visual Source Safe 6.0d http://www.microsoft.com/en-us/download/details.aspx?id=9183

# prepare
```
$ 7z x Vs6sp6.exe -oVs6sp6
$ cd Vs6sp6
$ 7z x VS6sp61.cab -oVS6sp61
```

# get lib/obj files
```
$ find Vs6sp61/ -iname "*.lib"
Vs6sp61/vc98/lib/atl.lib
Vs6sp61/vc98/lib/atldload.lib
Vs6sp61/vc98/lib/comsupp.lib
Vs6sp61/vc98/lib/libc.lib
Vs6sp61/vc98/lib/libcd.lib
Vs6sp61/vc98/lib/libcimt.lib
Vs6sp61/vc98/lib/libcimtd.lib
Vs6sp61/vc98/lib/libcmt.lib
Vs6sp61/vc98/lib/libcmtd.lib
Vs6sp61/vc98/lib/libcp.lib
Vs6sp61/vc98/lib/libcpd.lib
Vs6sp61/vc98/lib/libcpmt.lib
Vs6sp61/vc98/lib/libcpmtd.lib
Vs6sp61/vc98/lib/mfcdload.lib
Vs6sp61/vc98/lib/msvcprt.lib
Vs6sp61/vc98/lib/msvcprtd.lib
Vs6sp61/vc98/lib/msvcrt.lib
Vs6sp61/vc98/lib/msvcrtd.lib
Vs6sp61/vc98/lib/oleaut32.lib
Vs6sp61/vc98/lib/uuid.Lib
Vs6sp61/vc98/mfc/lib/eafxis.lib
Vs6sp61/vc98/mfc/lib/eafxisd.lib
Vs6sp61/vc98/mfc/lib/mfc42.lib
Vs6sp61/vc98/mfc/lib/mfc42d.lib
Vs6sp61/vc98/mfc/lib/mfc42u.lib
Vs6sp61/vc98/mfc/lib/mfc42ud.lib
Vs6sp61/vc98/mfc/lib/mfcd42d.lib
Vs6sp61/vc98/mfc/lib/mfcd42ud.lib
Vs6sp61/vc98/mfc/lib/mfcn42d.lib
Vs6sp61/vc98/mfc/lib/mfcn42ud.lib
Vs6sp61/vc98/mfc/lib/mfco42d.lib
Vs6sp61/vc98/mfc/lib/mfco42ud.lib
Vs6sp61/vc98/mfc/lib/mfcs42.lib
Vs6sp61/vc98/mfc/lib/mfcs42d.lib
Vs6sp61/vc98/mfc/lib/mfcs42u.lib
Vs6sp61/vc98/mfc/lib/mfcs42ud.lib
Vs6sp61/vc98/mfc/lib/nafxcw.lib
Vs6sp61/vc98/mfc/lib/nafxcwd.lib
Vs6sp61/vc98/mfc/lib/nafxis.lib
Vs6sp61/vc98/mfc/lib/nafxisd.lib
Vs6sp61/vc98/mfc/lib/uafxcw.lib
Vs6sp61/vc98/mfc/lib/uafxcwd.lib

$ find Vs6sp61/ -iname "*.obj"
```

# generate and zip .pat

focus on C/C++ run time libraries

```
$ find VS6/ -type f \( -iname "*libc*" -o -iname "*msvc*" -o -iname "*libvc*" -o -iname "*vcruntime*" -o -iname "*libucrt*" \) -exec md5sum {} \;
d7b98b1a1acb7830c0492a5a6c067aae *VS6/vc98/lib/libc.lib
9afe7b97ba936b5e0c48b912b2b42b87 *VS6/vc98/lib/libcd.lib
3137d04020f1caa342db588e9c0cdacb *VS6/vc98/lib/libcimt.lib
bae8a55e608457ceb8f4254080df0c92 *VS6/vc98/lib/libcimtd.lib
2cfcb0ef30f936e434d7d3be11bef2c7 *VS6/vc98/lib/libcmt.lib
b9e55116a92eb94a449ca041c185b4a3 *VS6/vc98/lib/libcmtd.lib
8dbda62901721e2569853189d1b5d967 *VS6/vc98/lib/libcp.lib
84f9ff2267dc6d42514c369c0d7aed00 *VS6/vc98/lib/libcpd.lib
ef2f398fb9522fb133070ffb5741ae90 *VS6/vc98/lib/libcpmt.lib
b437028fd12ce3db5baf857c21ac0718 *VS6/vc98/lib/libcpmtd.lib
07dfa8c351b6481c92ac8a9aaab1f125 *VS6/vc98/lib/msvcprt.lib
571aee70ce8d993094157957398b5f04 *VS6/vc98/lib/msvcprtd.lib
380dd6cd28ab53a7e22ad9bf902135fd *VS6/vc98/lib/msvcrt.lib
336549a15d5b8d389a29c573ccba6846 *VS6/vc98/lib/msvcrtd.lib

$ find VS6/ -type f \( -iname "*libc*" -o -iname "*msvc*" -o -iname "*libvc*" -o -iname "*vcruntime*" -o -iname "*libucrt*" \) -exec ../../pcf.exe {} {}.pat \;
.\VS6\vc98\lib\libc.lib: skipped 50, total 1203
.\VS6\vc98\lib\libcd.lib: skipped 40, total 1281
.\VS6\vc98\lib\libcimt.lib: skipped 12, total 315
.\VS6\vc98\lib\libcimtd.lib: skipped 0, total 571
.\VS6\vc98\lib\libcmt.lib: skipped 50, total 1271
.\VS6\vc98\lib\libcmtd.lib: skipped 40, total 1351
.\VS6\vc98\lib\libcp.lib: skipped 70, total 1122
.\VS6\vc98\lib\libcpd.lib: skipped 0, total 1829
.\VS6\vc98\lib\libcpmt.lib: skipped 66, total 1168
.\VS6\vc98\lib\libcpmtd.lib: skipped 0, total 1820
.\VS6\vc98\lib\msvcprt.lib: skipped 2104, total 2106
.\VS6\vc98\lib\msvcprtd.lib: skipped 2104, total 2107
.\VS6\vc98\lib\msvcrt.lib: skipped 854, total 944
.\VS6\vc98\lib\msvcrtd.lib: skipped 883, total 977

tar -czvf VS6/VS6.tar.gz VS6/vc98/lib/*.pat
VS6/vc98/lib/libc.lib.pat
VS6/vc98/lib/libcd.lib.pat
VS6/vc98/lib/libcimt.lib.pat
VS6/vc98/lib/libcimtd.lib.pat
VS6/vc98/lib/libcmt.lib.pat
VS6/vc98/lib/libcmtd.lib.pat
VS6/vc98/lib/libcp.lib.pat
VS6/vc98/lib/libcpd.lib.pat
VS6/vc98/lib/libcpmt.lib.pat
VS6/vc98/lib/libcpmtd.lib.pat
VS6/vc98/lib/msvcprt.lib.pat
VS6/vc98/lib/msvcprtd.lib.pat
VS6/vc98/lib/msvcrt.lib.pat
VS6/vc98/lib/msvcrtd.lib.pat

$ wc -l VS6/vc98/lib/*.pat
   1154 VS6/vc98/lib/libc.lib.pat
   1242 VS6/vc98/lib/libcd.lib.pat
    304 VS6/vc98/lib/libcimt.lib.pat
    572 VS6/vc98/lib/libcimtd.lib.pat
   1222 VS6/vc98/lib/libcmt.lib.pat
   1312 VS6/vc98/lib/libcmtd.lib.pat
   1053 VS6/vc98/lib/libcp.lib.pat
   1830 VS6/vc98/lib/libcpd.lib.pat
   1103 VS6/vc98/lib/libcpmt.lib.pat
   1821 VS6/vc98/lib/libcpmtd.lib.pat
      3 VS6/vc98/lib/msvcprt.lib.pat
      4 VS6/vc98/lib/msvcprtd.lib.pat
     91 VS6/vc98/lib/msvcrt.lib.pat
     95 VS6/vc98/lib/msvcrtd.lib.pat
  11806 total

$ du -h VS6/*.tar.gz
952K    VS6/VS6.tar.gz
```
