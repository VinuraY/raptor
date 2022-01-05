# First you have to install pytube lib using pip or pipwin eg:- pip install pytube.
from pytube import YouTube, Playlist, Channel
import platform
import os
import math
from pytube.request import filesize
from termcolor import colored

system = platform.platform()


if('Linux' in system):

    os.system('clear')

elif('Windows' in system):
    os.system('cls')

# Resolution function for video downloading.

home_dir = os.path.expanduser('~')


def all_filesize(link):
    resolution = ['144p', '240p', '360p', '480p', '720p', '1080p']

    print('\n[+]File sizes')

    for i in resolution:
        size = math.ceil(link.streams.filter(res=i).first().filesize/1024/1024)
        print(f'{i} : {size}MB')


def filesize(link, resolution):
    size = math.ceil(link.streams.filter(
        res=resolution).first().filesize/1024/1024)

    return size


def resolution():
    res = input(colored('\nResolution of the video (360p,720p..) : ',
                'red'))
    return res


# Path to download file.

def location():
    if('Linux' in system):
        path = f'{home_dir}/Downloads'
        return path

    elif('Windows' in system):
        path = f'{home_dir}\\Downloads'
        return path


print(colored('''

	██████╗  █████╗ ██████╗ ████████╗ ██████╗ ██████╗
	██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
	██████╔╝███████║██████╔╝   ██║   ██║   ██║██████╔╝
	██╔══██╗██╔══██║██╔═══╝    ██║   ██║   ██║██╔══██╗
	██║  ██║██║  ██║██║        ██║   ╚██████╔╝██║  ██║
	╚═╝  ╚═╝╚═╝  ╚═╝╚═╝        ╚═╝    ╚═════╝ ╚═╝  ╚═╝ v2.0

	created by : Vinura Yashohara (AnonyMSAV)
	''', 'blue'))

# Options of the program.
print(colored('''
	Options :
		1. To download individual video.
		2. To download playlist.
		3. To download all videos in channel.
		4. To download audio from video.
		''', 'yellow'))

options = int(input(colored('Enter : ', 'red')))


match options:

    case 1:

        url = input(colored('\nURL of the video : ', 'red'))
        link = YouTube(url)
        option = input(
            colored('\nDo you need all the file sizes [1,0] : ', 'red'))

        if(option == 1):
            all_filesize(link, option)

        resolution = resolution()
        size = filesize(link, resolution)

        path = location()

        print(colored(f'''\n[+]File size : {size} MB
\n[+]Downloading "{link.title}" ..''', 'yellow'))

        # Set resolution and download.
        link.streams.filter(
            res=resolution, file_extension='mp4').first().download(path)

        print(colored(
            f'\n[+]Downloaded and stored in the {path} folder', 'yellow'))

    case 2:

        url = input(colored('\nURL of a playlist : ', 'red'))
        resolution = resolution()
        link = Playlist(url)
        path = location()
        size = filesize(link, resolution)

        # Get videos in playlist one by one and download them using for loop.

        for i in link.videos:

            print(colored(f'''\n[+]File size : {size} MB
\n[+]Downloading "{i.title}" ..''', 'yellow'))

            # Set resolution and download.
            i.streams.filter(
                res=resolution, file_extension='mp4').first().download(path)
            print(colored(
                f'\n[+]Downloaded and stored in the {path} folder', 'yellow'))

    case 3:

        url = input(colored('\nURL of a channel : ', 'red'))
        resolution = resolution()
        path = location()
        link = Channel(url)
        size = filesize(link, resolution)

        # Get videos in channel one by one and download them using for loop.

        for i in link.videos:
            print(colored(f'''\n[+]File size : {size} MB
\n[+]Downloading "{i.title}" ..''', 'yellow'))

            # Set resolution and download.
            i.streams.filter(
                res=resolution, file_extension='mp4').first().download(path)

            print(colored(
                f'\n[+]Downloaded and stored in the {path} folder', 'yellow'))

    case 4:

        url = input(colored('\nURL of a video : ', 'red'))
        link = YouTube(url)
        path = location()
        size = math.ceil(link.streams.filter(
            only_audio=True, file_extension='mp4').first().filesize/1024/1024)

        print(colored(f'''\n[+]File size : {size} MB
\n[+]Downloading "{link.title}" ..''', 'yellow'))

        link.streams.filter(
            only_audio=True, file_extension='mp4').first().download(path)

        print(colored(
            f'\n[+]Downloaded and stored in the {path} folder', 'yellow'))

    case default:

        print(colored('Error occured. Try again!', 'red'))
