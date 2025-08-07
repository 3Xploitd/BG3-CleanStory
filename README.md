# Introduction
This python script is for use for Mod Authors that utilize the BG3 Toolkit for mods that have Osiris scripts created within the Toolkit. The script can clean a single mod directory or all your mod directories of the following files:

- goals.raw
- log.txt
- story.div
- story.div.osi
- story_ac.dat

These files are created by the BG3 tookit story editor and are not needed. Keeping them just creates bloat in the PAK file once packaged up into a mod.

# Usage

```
usage: bg3_clean_story.py [-h] [-s SOURCE_DIRECTORY] [-m MOD]

options:
  -h, --help            show this help message and exit
  -s, --source-directory SOURCE_DIRECTORY
                        The full path of your BG3 Data directory
  -m, --mod MOD         The mod name (the entire modname ex.TESTMOD_67d6dc31-b234-46fb-b8f9-11611b7a16bb) you want to
                        remove bloated story files from. If you want to do it for all mods then specify "ALL" or omit
                        this comandline option
```

Neither commandline option is necessary but if you don't specify them the script will assume your BG3 Data folder is `C:\Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3\Data\` and that you want to clean all mods of the files. There is also a config file `config.json` if you specify your path there if it is different than the default you don't have to specify the path each time.

If you'd like to just clean a single mod run the following command:

`python bg3_clean_story.py -m <modname>` 

The `modname` needs to be the entire name of the folder inside your Mods folder if you are just cleaning a single mod, otherwise you can omit the commandline option and it will automatically find all of the mods for you.

You can also just make a copy of your Mods folder and run the script on that, just need to have the mods you want to clean inside a folder called `Mods`, other than that the path can be anything you want.

Once you run the tool you will get a JSON printout of each of the mods that had story files deleted, this way you can easily go back and update your mod on modio.


# Important

I would suggest making a backup of your mod folder before attempting to run the tool and either run it on the backup folder and just replace the mods in the BG3 mods folder or then run it on the BG3 mods folder. This way if anything goes wrong you still have the backup.
