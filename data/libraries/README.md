## create .tgz with .lib and .pat

```sh
for TRIPLET in \
        x64-windows-static-v140 \
        x64-windows-static-v141 \
        x64-windows-static-v142 \
        x86-windows-static-v140 \
        x86-windows-static-v141 \
        x86-windows-static-v142 \
        ; do
    find "./$TRIPLET" -name "*.lib" | while read -r L; do 
        pcf "$L" "$L".pat;
        tar --append --file="$TRIPLET".tar "$L";
        tar --append --file="$TRIPLET".tar "$L".pat;
    done
    gzip "$TRIPLET".tar;
done
```


## show .tgz contents

```sh
ls -lah *.tar.gz && \
for TRIPLET in \
        x64-windows-static-v140 \
        x64-windows-static-v141 \
        x64-windows-static-v142 \
        x86-windows-static-v140 \
        x86-windows-static-v141 \
        x86-windows-static-v142 \
        ; do
    echo "$TRIPLET".tar.gz;
    tar -tvf "$TRIPLET".tar.gz;
done
```