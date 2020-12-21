"""
© Copyright Alexandre Silva - 2020

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

Created at 19/12/2020
"""
from datetime import datetime
from betterdatamanagement.bfile import Bfile
from textwrap import wrap
import pathlib
import time
import pygetwindow
import requests
import shutil
import json
import os

mods = pathlib.Path(os.getenv('APPDATA')) / '.minecraft' / "mods"
zipbuild = os.path.join(mods, "Mod_Backups", "ZipBuild")
modbackups = os.path.join(mods, "Mod_Backups")


def update_output(main, text):

    # Updates the output view

    now = datetime.now()
    main.output.config(state="normal")
    main.output.insert('end', f"[{now.hour}:{now.minute}] {text}\n")
    main.output.config(state="disabled")
    main.output.yview('end')


def archive_mods(main):

    update_output(main, 'Finding possible mods for archiving...')
    _mods = [f for r, d, f in os.walk(mods)][0]

    # Halts the archiving if there are no mods
    if not _mods:
        update_output(main, f"No mods found. Skipping archivement")
        return

    # Makes a list with the paths of the mods
    modlist = list()
    for mod in _mods:

        if mod.endswith('.json'):
            continue

        modpath = os.path.join(mods, mod)
        update_output(main, f'Found possible mod "{mod}" at "{modpath}"')
        modlist.append(modpath)

    if not modlist:
        update_output(main, f"No mods found. Skipping archivement")
        return

    del _mods

    # Creates a build directory and makes the archive out of it, renames it to the correct name
    os.makedirs(zipbuild, exist_ok=True)
    update_output(main, f"Building archive")
    for mod in modlist:
        update_output(main, f'Loading "{mod}" into archive')
        shutil.move(mod, zipbuild)

    shutil.make_archive(zipbuild, "zip", zipbuild)
    arch = Bfile(os.path.join(modbackups, 'ZipBuild.zip'))
    now = datetime.now()
    arch.rename(f"SPI-ModBackup.{now.year}.{now.day}.{now.hour}.{now.minute}.{now.second}.zip")
    update_output(main, f'Mods found in "{mods}" backed up and saved at "{f"SPI-ModBackup.{now.year}.{now.day}.{now.hour}.{now.minute}.{now.second}.zip"}"')

    # Deletes build
    shutil.rmtree(zipbuild)


def on_install_click_wrapper(main):
    try:
        # Clears the output
        main.output.config(state="normal")
        main.output.delete(0.0, "end")
        main.output.config(state="disabled")

        # Hides the install button
        main.install.place_forget()
        main.wait.place(anchor='center', relx='.5', rely='.9', x='0', y='0')

        # Closes all minecraft related windows so the program can use the .minecraft folder.
        mc_windows = pygetwindow.getWindowsWithTitle("Minecraft")

        if mc_windows is not None:

            for window in mc_windows:
                update_output(main, f'Closing MC Window "{window.title}"')
                window.close()

        # Archives the mods in the mods folder
        archive_mods(main)

        update_output(main, f"Loading blueprint")
        # Creates the blueprint.json file if it doesn't exist
        if not os.path.isfile(os.path.join(mods, "blueprint.json")):

            with open(os.path.join(mods, "blueprint.json"), 'w+') as bpcreator:

                bpcreator.write('{}')

        installed_count = 0

        # Installs the mods listed in the blueprint
        with open(os.path.join(mods, "blueprint.json"), 'r') as blueprint:

            # Reads the blueprint and requests the file for each line
            blueprint_data = json.load(blueprint)

            for modname in blueprint_data:

                update_output(main, f'Attempting "{modname}" installation')

                # Parses out the information for each mod and sends the request for the file download
                modid = wrap(blueprint_data[modname], 4)

                data = requests.get(f"https://media.forgecdn.net/files/{modid[0]}/{modid[1]}/{modname}")
                modpath = os.path.join(mods, modname)

                # Checks if response is authorized
                if data.status_code != 200:

                    update_output(main, f'Could not install "{modname}" - Bad code ({data.status_code})')
                    update_output(main, f'Check the params for the mod in the blueprint and try again!')
                    continue

                # Puts the mod into the mods folder
                with open(modpath, 'wb+') as mod:

                    mod.write(data.content)
                    update_output(main, f'Installed "{modname}" into mods folder at "{mods}"')
                    installed_count += 1

        if installed_count == 0:
            update_output(main, f'Error: Blueprint has no valid mods')
            update_output(main, f'To fill in mods inside the blueprint, edit the JSON file in the with the format CFModname:CFID')
            update_output(main, f'Check out the github page at https://github.com/mrkelpy/CFMA for a more detailed tutorial.')

    except Exception as err:

        update_output(main, f'[ERROR] {err}')
        # Shows the install button again

    time.sleep(1.5)
    main.wait.place_forget()
    main.install.place(anchor='center', relwidth='.5', relx='.5', rely='.9', x='0', y='0')