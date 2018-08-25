@ECHO OFF
FOR %%X in ("data\*.xls") DO IF NOT %%~xX == .xlsx echo Converting "%%~dpnxX"  & "%OFFICE_HOME%\excelcnv.exe"  -nme -oice "%%~dpnxX" "%%~dpnX.xlsx"