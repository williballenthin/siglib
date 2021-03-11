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
```
$ find VS6/ -type f -exec ../../pcf.exe -a {} vs6.pat \;
..\VS\VS6\vc98\lib\atl.lib: skipped 48, total 48
..\VS\VS6\vc98\lib\atldload.lib: skipped 0, total 9
..\VS\VS6\vc98\lib\comsupp.lib: skipped 1, total 21
..\VS\VS6\vc98\lib\libc.lib: skipped 50, total 1203
..\VS\VS6\vc98\lib\libcd.lib: skipped 40, total 1281
..\VS\VS6\vc98\lib\libcimt.lib: skipped 12, total 315
..\VS\VS6\vc98\lib\libcimtd.lib: skipped 0, total 571
..\VS\VS6\vc98\lib\libcmt.lib: skipped 50, total 1271
..\VS\VS6\vc98\lib\libcmtd.lib: skipped 40, total 1351
..\VS\VS6\vc98\lib\libcp.lib: skipped 70, total 1122
..\VS\VS6\vc98\lib\libcpd.lib: skipped 0, total 1829
..\VS\VS6\vc98\lib\libcpmt.lib: skipped 66, total 1168
..\VS\VS6\vc98\lib\libcpmtd.lib: skipped 0, total 1820
..\VS\VS6\vc98\lib\mfcdload.lib: skipped 0, total 16
..\VS\VS6\vc98\lib\msvcprt.lib: skipped 2104, total 2106
..\VS\VS6\vc98\lib\msvcprtd.lib: skipped 2104, total 2107
..\VS\VS6\vc98\lib\msvcrt.lib: skipped 854, total 944
..\VS\VS6\vc98\lib\msvcrtd.lib: skipped 883, total 977
..\VS\VS6\vc98\lib\oleaut32.lib: skipped 0, total 354
..\VS\VS6\vc98\lib\uuid.Lib: skipped 0, total 0
..\VS\VS6\vc98\mfc\lib\eafxis.lib: skipped 7, total 94
..\VS\VS6\vc98\mfc\lib\eafxisd.lib: skipped 0, total 11
..\VS\VS6\vc98\mfc\lib\mfc42.lib: skipped 6385, total 6385
..\VS\VS6\vc98\mfc\lib\mfc42d.lib: skipped 4850, total 4850
..\VS\VS6\vc98\mfc\lib\mfc42u.lib: skipped 6376, total 6376
..\VS\VS6\vc98\mfc\lib\mfc42ud.lib: skipped 4856, total 4856
..\VS\VS6\vc98\mfc\lib\mfcd42d.lib: skipped 705, total 705
..\VS\VS6\vc98\mfc\lib\mfcd42ud.lib: skipped 705, total 705
..\VS\VS6\vc98\mfc\lib\mfcn42d.lib: skipped 110, total 110
..\VS\VS6\vc98\mfc\lib\mfcn42ud.lib: skipped 111, total 111
..\VS\VS6\vc98\mfc\lib\mfco42d.lib: skipped 2914, total 2914
..\VS\VS6\vc98\mfc\lib\mfco42ud.lib: skipped 2910, total 2910
..\VS\VS6\vc98\mfc\lib\mfcs42.lib: skipped 2, total 27
..\VS\VS6\vc98\mfc\lib\mfcs42d.lib: skipped 0, total 26
..\VS\VS6\vc98\mfc\lib\mfcs42u.lib: skipped 2, total 27
..\VS\VS6\vc98\mfc\lib\mfcs42ud.lib: skipped 0, total 26
..\VS\VS6\vc98\mfc\lib\nafxcw.lib: skipped 481, total 8548
..\VS\VS6\vc98\mfc\lib\nafxcwd.lib: skipped 0, total 2057
..\VS\VS6\vc98\mfc\lib\nafxis.lib: skipped 7, total 92
..\VS\VS6\vc98\mfc\lib\nafxisd.lib: skipped 0, total 11
..\VS\VS6\vc98\mfc\lib\uafxcw.lib: skipped 481, total 8547
..\VS\VS6\vc98\mfc\lib\uafxcwd.lib: skipped 0, total 2006

$ wc -l vs6.pat
32684 vs6.pat

$ gzip -v -k VS6.pat
VS6.pat:         80.1% -- created VS6.pat.gz
```
