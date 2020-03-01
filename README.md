# My_Py_scripts
My_Py_scripts from Haifeng

# Usage:
```
python3 ./BED12_shift.py my_3UTR_12.bed > my_3UTR_12_fine.bed
```

# Example:

```
cat tmp.txt
chr3    108107279       108109421       ENSMUST00000000001      0       -       108107279       108109421       255,0,0 2       2037,19,        0,2123,
chrX    77837900        77841882        ENSMUST00000000003      0       -       77837900        77841882        255,0,0 2       214,23, 0,3959,
chr11   96274859        96276595        ENSMUST00000000010      0       +       96274859        96276595        255,0,0 1       1736,   0,
chr16   18780446        18781897        ENSMUST00000000028      0       -       18780446        18781897        255,0,0 2       127,2,  0,1449,
chr7    142650765       142653815       ENSMUST00000000033      0       -       142650765       142653815       255,0,0 1       3050,   0,
chr11   108414295       108414396       ENSMUST00000000049      0       +       108414295       108414396       255,0,0 1       101,    0,
chr6    17287047        17289115        ENSMUST00000000058      0       +       17287047        17289115        255,0,0 1       2068,   0,
chr13   5867283 5870394 ENSMUST00000000080      0       +       5867283 5870394 255,0,0 1       3111,   0,
chr4    120529259       120530184       ENSMUST00000000087      0       +       120529259       120530184       255,0,0 1       925,    0,
chr9    57531782        57532426        ENSMUST00000000090      0       +       57531782        57532426        255,0,0 2       10,145, 0,499,
```
```
python3 BED12_shift.py tmp.txt
chr3    108107279       108109424       ENSMUST00000000001      0       -       108107279       108109424       255,0,0 2037,22,        0,2123,
chrX    77837900        77841885        ENSMUST00000000003      0       -       77837900        77841885        255,0,0 214,26, 0,3959,
chr11   96274856        96276595        ENSMUST00000000010      0       +       96274856        96276595        255,0,0 1739,   0,
chr16   18780446        18781900        ENSMUST00000000028      0       -       18780446        18781900        255,0,0 127,5,  0,1449,
chr7    142650765       142653818       ENSMUST00000000033      0       -       142650765       142653818       255,0,0 3053,   0,
chr11   108414292       108414396       ENSMUST00000000049      0       +       108414292       108414396       255,0,0 104,    0,
chr6    17287044        17289115        ENSMUST00000000058      0       +       17287044        17289115        255,0,0 2071,   0,
chr13   5867280 5870394 ENSMUST00000000080      0       +       5867280 5870394 255,0,0 3114,   0,
chr4    120529256       120530184       ENSMUST00000000087      0       +       120529256       120530184       255,0,0 928,    0,
chr9    57531779        57532426        ENSMUST00000000090      0       +       57531779        57532426        255,0,0 13,145, 0,502,
```




