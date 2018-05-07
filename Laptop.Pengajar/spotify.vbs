Set WshShell = WScript.CreateObject("WScript.Shell")
Comandline = "C:\Users\vesal\AppData\Roaming\Microsoft\Windows\Start Menu\Programs"
WScript.sleep 3000
CreateObject("WScript.Shell").Run("spotify:user:spotify:playlist:37i9dQZF1DX60EDqDORwwI")
WScript.sleep 3000
WshShell.SendKeys "{ENTER}"
WScript.sleep 1000
WshShell.SendKeys "^{s}"
WScript.sleep 100
WshShell.SendKeys "^{RIGHT}"
