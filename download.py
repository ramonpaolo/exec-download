import os
import argparse

argparser = argparse.ArgumentParser()

argparser.add_argument("-l", "--link", type=str,
                       help="Link(url) of Video or Image", required=True)
argparser.add_argument("-n", "--name-file", type=str,
                       help="Output Name of File")
argparser.add_argument("-p", "--path-save", type=str,
                       help="Path to Save File", required=True)

arguments = argparser.parse_args()

link = f"{arguments.__dict__['link'].__str__()}"
name_file_output = arguments.__dict__['name_file'].__str__()
path_to_save = arguments.__dict__['path_save'].__str__()

if path_to_save == "." or None:
    path_to_save = os.getcwd()

link = str(link).replace("&", "EGRANDE")

print("\n")


def show_details(link: str):
    print("*" * 120)
    print("\n")

    print("-" * 60)
    print(f"Length Link: {len(str(link).replace('EGRANDE', '&'))}")
    print(link)
    print("Path save file: " + path_to_save)
    print("-" * 60)

    print("\n")
    print("*" * 120)


if str(link).__contains__("youtube"):
    print("Link do YouTube")
    show_details(link)
    os.chdir(path_to_save)
    os.system(f"youtube-dl {str(link).replace('EGRANDE', '&')}")
    print("\n")
    print(f"Name file '{name_file_output}' not used in this case")

else:
    os.chdir("ffmpeg")
    error = os.system(
        f'ffmpeg -i "{str(link).replace("EGRANDE", "&")}" -c copy -bsf:a aac_adtstoasc "{path_to_save}/{name_file_output}.mp4"')
    if error == 1:
        print("Error with ffmpeg")
        error = os.system(
            f"wget {str(link).replace('EGRANDE', '&')}")
        if error == 1:
            print("Error all")
    show_details(link)
