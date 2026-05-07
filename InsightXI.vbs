Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "cmd.exe /c LaunchInsightXI.bat", 0, False
Set WshShell = Nothing
