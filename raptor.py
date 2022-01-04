# First you have to install pytube lib using pip or pipwin eg:- pip install pytube.
from pytube import YouTube, Playlist, Channel
import platform
import os
from termcolor import colored

system = platform.platform()


if('Linux' in system):

    os.system('clear')

elif('Windows' in system):
    os.system('cls')

# Resolution function for video downloading.

home_dir = os.path.expanduser('~')


def resolution():
    res = input(colored('Resolution of the video (360p,720p..) : ',
                'red', attrs=['bold']))
    return res

# Path to download file.


def location():
    path = f'{home_dir}\\Downloads'
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
		''', 'yellow', attrs=['bold']))

options = int(input(colored('Enter : ', 'red', attrs=['bold'])))


match options:

    case 1:

        url = input(colored('\nURL of the video : ', 'red', attrs=['bold']))
        resolution = resolution()
        link = YouTube(url)
        path = location()

        print(
            colored(f'\n[+]Downloading "{link.title}" .. ', 'yellow', attrs=['bold']))

        # Set resolution and download.
        link.streams.filter(
            res=resolution, file_extension='mp4').first().download(path)

        print(colored(
            f'\n[+]Downloaded and stored in the Downloads folder', 'yellow', attrs=['bold']))

    case 2:

        url = input(colored('\nURL of a playlist : ', 'red', attrs=['bold']))
        resolution = resolution()
        link = Playlist(url)
        path = location()

        # Get videos in playlist one by one and download them using for loop.

        for i in link.videos:

            print(
                colored(f'\n[+]Downloading "{i.title}" .. ', 'yellow', attrs=['bold']))

            # Set resolution and download.
            i.streams.filter(
                res=resolution, file_extension='mp4').first().download(path)
            print(colored(
                f'\n[+]Downloaded and stored in the Downloads folder', 'yellow', attrs=['bold']))

    case 3:

        url = input(colored('\nURL of a channel : ', 'red', attrs=['bold']))
        resolution = resolution()
        path = location()
        link = Channel(url)

        # Get videos in channel one by one and download them using for loop.

        for i in link.videos:
            print(
                colored(f'\n[+]Downloading "{i.title}" .. ', 'yellow', attrs=['bold']))

            # Set resolution and download.
            i.streams.filter(
                res=resolution, file_extension='mp4').first().download(path)

            print(colored(
                f'\n[+]Downloaded and stored in the Downloads folder', 'yellow', attrs=['bold']))

    case 4:

        url = input(colored('\nURL of a video : ', 'red', attrs=['bold']))
        link = YouTube(url)
        path = location()

        print(
            colored(f'\n[+]Downloading "{link.title}" .. ', 'yellow', attrs=['bold']))

        link.streams.filter(
            only_audio=True, file_extension='mp4').first().download(path)

        print(colored(
            f'\n[+]Downloaded and stored in the Downloads folder', 'yellow', attrs=['bold']))

    case default:

        print(colored('Error occured. Try again!', 'red', attrs=['bold']))
