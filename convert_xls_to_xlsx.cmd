@ECHO OFF
FOR %%X in ("data\*.xls") DO IF NOT %%~xX == .xlsx echo Converting "%%~dpnxX"  & "C:\Program Files\Microsoft Office\Office16\excelcnv.exe"  -nme -oice "%%~dpnxX" "%%~dpnX.xlsx"