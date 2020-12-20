The CFMC Stands for CurseForge Minecraft Modpack Installer, and is a blueprint-modpack installer.

# Blueprints

Blueprints are JSON files formatted specially for the program to understand. They must be placed inside the mods folder, and incase one isn't located there, it'll be created.
To acquire the necessary resources to create a blueprint, you need to:

### Get the Modname 

1. Go to a CurseForge MC Mod page, such as https://www.curseforge.com/minecraft/mc-mods/big-reactors
2. Go to Files > Choose a version
3. Find the "filename" field
4. Save the filename somewhere for the blueprint

### Get the Mod ID

1. Go to a CurseForge MC Mod page, such as https://www.curseforge.com/minecraft/mc-mods/big-reactors
2. Go to Files > Choose a version
3. Get the last 7 numbers in the website link, e.g "2282591"
4. Save the ID somewhere for the blueprint

### Create a blueprint

1. Create a file named "blueprint.json"
2. Open the file; You may use any text editor / The default notepad
3. Follow the Blueprint Format. For the spaces before the entries, press tab.
4. (OPTIONAL) To use the blueprint, move it your mods folder, located at C:\Users\USER\AppData\Roaming\.minecraft\mods

## Blueprint Format
```json
{
  "CurseForge Modname":"CurseForge ModID",
  "CurseForge Modname1":"CurseForge ModID1",
  "CurseForge Modname2":"CurseForge ModID2"
  (...)
}
```
You may add as many mods as you want inside the JSON.

# Using the CFMC

Place your blueprint inside the mods folder, this is the blueprint the program will read.
Run the CFMC.exe file / main.py. Your mods will then be installed, if they're valid, and any pre-existant mods will be backed up in a folder called Mod_Backups.
