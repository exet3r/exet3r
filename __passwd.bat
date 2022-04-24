@ECHO OFF
:: ----------------------------------------------------------------------------
:: Run the password generator                                                  
:: ----------------------------------------------------------------------------


:SETUP

    set SCRIPT=genpass.py


:INITIALIZE_PYTHON

    set PYTHON=C:\Software\Python310\python.exe

	set PY_DIR=C:\Software\Python310
	set TCL_LIBRARY=C:\Software\Python310\tcl\tcl8.6
	set TK_LIBRARY=C:\Software\Python310\tcl\tcl8.6
	set TCLLIBPATH=%TCL_LIBRARY%

	set ROOT_DRV=L


:RUN_SCRIPT

    set ROOT_DIR=%ROOT_DRV%:\Projects\Passgen
    set PY_SCRIPT=%ROOT_DIR%\%SCRIPT%

    %ROOT_DRV%:
    cd %ROOT_DIR%

    %PYTHON% %SCRIPT%


:DONE

    pause

