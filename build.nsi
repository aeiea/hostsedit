!include "MUI.nsh"
!define MUI_ABORTWARNING
!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_LANGUAGE "English"

Name "HostsEdit v0.0.1"
InstallDir "$PROGRAMFILES\aeiea\hostsedit\v0.0.1"
ShowInstDetails show

Section "HostsEdit"
    SetOutPath $INSTDIR
    File "icon.ico"
    File "main.py"
    File "LICENSE"
    File "python-3.11.0-amd64.exe"
    File "setup.bat"
    File "run.bat"
    Exec "python-3.11.0-amd64.exe"
    Exec "setup.bat"
SectionEnd
Section
    SetOutPath $INSTDIR
    WriteUninstaller "$INSTDIR\uninstall.exe"
    CreateShortcut "$SMPROGRAMS\HostsEdit.lnk" "$INSTDIR\run.bat" "$INSTDIR/icon.ico"
    CreateShortcut "$SMPROGRAMS\HostsEdit Uninstaller.lnk" "$INSTDIR\uninstall.exe"
SectionEnd
Section "uninstall"
    Delete "$INSTDIR\uninstall.exe"
    Delete "$SMPROGRAMS\HostsEdit.lnk"
    Delete "$SMPROGRAMS\HostsEdit Uninstaller.lnk"
    Delete $INSTDIR
SectionEnd