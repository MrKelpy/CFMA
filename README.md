The CFMA Stands for CurseForge Modpack Architect, and is a blueprint-modpack installer.

## DISCLAIMER
This software is not associated in any way to the CurseForge authors or to the website itself. The only instance where CurseForge is used is to download the Minecraft Modifications that are stored within.

# Installation

```bash
Download the executable available in the repository, or the source code.
```

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
```python
{
  "CurseForge Modname":"CurseForge ModID",
  "CurseForge Modname1":"CurseForge ModID1",
  "CurseForge Modname2":"CurseForge ModID2"
  (...)
}
```
You may add as many mods as you want inside the JSON.
Example:

```python
{
  "BigReactors-0.4.3A.jar":"2282591",
  "ironchest-1.16.4-11.2.10.jar1":"3105315"
}
```

## Custom Blueprint Mods
```python
{
  "custom_SOMEMOD.jar": "https://direct-download-link-to-the-mod"
}
```
For custom mods, the prefix "custom_" is required.

# Using the CFMA

Place your blueprint inside the mods folder, this is the blueprint the program will read.
Run the CFMA.exe file / main.py. <br>
Your mods will then be installed, if they're valid, and any pre-existent mods will be backed up in a folder called Mod_Backups.

# Known Glitches
### All fixed! (For now)
