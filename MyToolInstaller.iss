[Setup]
AppName=MyTool
AppVersion=1.0
DefaultDirName={pf}\MyTool
DefaultGroupName=MyTool
OutputDir=.
OutputBaseFilename=MyToolSetup
Compression=lzma
SolidCompression=yes

[Files]
Source: "MyTool.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "MyTool.ini"; DestDir: "{app}"; Flags: ignoreversion
Source: "MyTool.script"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\MyTool"; Filename: "{app}\MyTool.exe"
Name: "{commondesktop}\MyTool"; Filename: "{app}\MyTool.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create a desktop icon"
