from pathlib import Path
import os
import shutil
import argparse
import json
from time import time

def bg3_clean_story(config,mod):
    mods_directory = f'{config}\\Mods\\'
    mod_list = []
    if mod.upper() == 'ALL':
        try:
            for mods in Path(mods_directory).glob('*'):
                if mods.name in ['Gustav','Shared','SharedDev','GustavDev','GustavX']:
                    continue
                else:
                    mod_list.append(mods)
            
        except Exception as e:
            print('Something went wrong when trying gather the list of mods to clean the story files from. Check the specified BG3 directory for errors.')

    if mod.upper() != 'ALL':
        try:
            mod_list.append(f'{config}\\Mods\\{mod}')
        except Exception as e:
            print('Something went wrong trying to locate the specified mod, check the specified modname and bg3 directory for correctness')
    return mods_directory,mod_list
        

def bg3_delete_story_files(mods_directory,mod_list):

    story_file_list = ['goals.raw','log.txt','story.div','story.div.osi','story_ac.dat']
    mods_json = {"mods":{}}
          
    for mod_name in mod_list:
        deleted_files = []
        try:
            story_directory = f'{mod_name}\\Story\\'
            for story_file in story_file_list:
                try:
                    story_file_path = f'{story_directory}\\{story_file}'
                    if Path(story_file_path).is_file():
                        os.remove(Path(story_file_path))
                        deleted_files.append(story_file)
                    
                except FileNotFoundError:
                    print('File not found')
                    continue
                except PermissionError:
                    print(f'Invalid permission to delete story files for {mod_name}')
                except Exception as e:
                    print(f'An error occurred when attempting to delete {story_file_path}')
                    print(e)
        except Exception as e:
            print(e)
            continue
        if deleted_files != []:
            mods_json['mods'][mod_name.name] = deleted_files
    logfile = f'storyfiles_cleaned_{time()}'
    
    if len(mods_json) != 0:

        with open(logfile,'a') as fh:
            fh.write(json.dumps(mods_json,indent=4))
            fh.close()
        print(f'Deleted files logged at {Path(logfile)}')
    else:
        print('No bloated story files were detected. No files were deleted.')

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-s','--source-directory',help='The full path of your BG3 Data directory',action='store',default='C:\\Program Files (x86)\\Steam\\steamapps\\common\\Baldurs Gate 3\\Data\\')
    parser.add_argument('-m','--mod',help='The mod name (the entire modname ex.TESTMOD_67d6dc31-b234-46fb-b8f9-11611b7a16bb) you want to remove bloated story files from. If you want to do it for all mods then specify "ALL" or omit this comandline option',action='store',default='ALL')
    args = parser.parse_args()
    if Path('config.json').is_file():
        config = json.loads(open('config.json','r').read())['BG3_Directory']
    else:
        config = args.source_directory

    mod = args.mod
    
    mod_directory,mod_list = bg3_clean_story(config,mod)
    bg3_delete_story_files(mod_directory,mod_list)

