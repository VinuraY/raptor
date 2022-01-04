# First you have to install pytube lib using pip or pipwin eg:- pip install pytube.
from pytube import YouTube, Playlist
import platform
import os
from termcolor import colored

system = platform.platform()

if('Linux' in system):

    os.system('clear')

elif('Windows' in system):
    os.system('cls')

# Resolution function for video downloading.


def resolution():
    res = input('Resolution of the video (360p,720p..) : ')
    return res

# Path to download file.


def location():
    path = input('Path : ')
    return path


print(colored('''

	██████╗  █████╗ ██████╗ ████████╗ ██████╗ ██████╗ 
	██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
	██████╔╝███████║██████╔╝   ██║   ██║   ██║██████╔╝
	██╔══██╗██╔══██║██╔═══╝    ██║   ██║   ██║██╔══██╗
	██║  ██║██║  ██║██║        ██║   ╚██████╔╝██║  ██║
	╚═╝  ╚═╝╚═╝  ╚═╝╚═╝        ╚═╝    ╚═════╝ ╚═╝  ╚═╝

	created by : Vinura Yashohara (AnonyMSAV)
	''', 'blue', attrs=['bold']))

# Options of the program.
print(colored('''
	Options : 
		1. To download individual video.
		2. To download playlist.
		3. To download all videos in channel.
		4. To download audio from video.
		''', 'red', attrs=['bold']))

options = int(input(colored('Enter : ', 'blue', attrs=['bold'])))


match options:

    case 1:

        url = input('\nURL of the video : ')
        resolution = resolution()
        link = YouTube(url)
        path = location()

        print(f'\n[+]Downloading "{link.title}" .. ')

        # Set resolution and download.
        link.streams.filter(
            res=resolution, file_extension='mp4').first().download(path)

        print(f'\n[+]Downloaded')

    case 2:

        url = input('\nURL of a playlist : ')
        resolution = resolution()
        link = Playlist(url)
        path = location()

        # Get videos in playlist one by one and download them using for loop.

        for i in link.videos:

            print(f'\n[+] Downloading "{i.title}" .. ')

            # Set resolution and download.
            i.streams.filter(
                res=resolution, file_extension='mp4').first().download(path)
            print(f'\n[+]Downloaded')

    case 3:

        url = input('\nURL of a channel : ')
        resolution = resolution()
        path = location()
        link = YouTube(url)

        # Get videos in channel one by one and download them using for loop.

        for i in link.videos:
            print(f'\n[+] Downloading "{i.title}" .. ')

            # Set resolution and download.
            i.streams.filter(
                res=resolution, file_extension='mp4').first().download(path)

            print(f'\n[+]Downloaded')

    case 4:

        url = input('\nURL of a video : ')
        link = YouTube(url)
        path = location()

        print(f'\n[+] Downloading "{link.title}" .. ')

        link.streams.filter(
            only_audio=True, file_extension='mp4').first().download(path)

        print(f'\n[+]Downloaded')

    case default:

        print('Error occured. Try again!')
