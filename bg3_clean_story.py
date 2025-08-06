from pathlib import Path
import os
import shutil
import argparse
import json

def bg3_clean_story(bg3_directory,directive):
    mods_directory = f'{bg3_directory}\\Mods\\'
    mod_list = []
    if directive.upper() == 'ALL':
        try:
            for mod in Path(mods_directory).glob('*'):
                if mod.name in ['Gustav','Shared','SharedDev','GustavDev','GustavX']:
                    continue
                else:
                    mod_list.append(mod)
            
        except Exception as e:
            print('Something went wrong when trying gather the list of mods to clean the story files from. Check the specified BG3 directory for errors.')

    if directive.upper() != 'ALL':
        try:
            mod_list.append(f'{bg3_directory}\\Mods\\{directive}')
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
    print(json.dumps(mods_json,indent=4))
if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-s','--source-directory',help='The full path of your BG3 Data directory',action='store',default='C:\\Program Files (x86)\\Steam\\steamapps\\common\\Baldurs Gate 3\\Data\\')
    parser.add_argument('-d','--directive',help='The mod name you want to remove bloated story files from, if you want to do it for all mods then specify "ALL"',action='store',default='ALL')
    args = parser.parse_args()
    mod_directory,mod_list = bg3_clean_story(args.source_directory,args.directive)
    bg3_delete_story_files(mod_directory,mod_list)

