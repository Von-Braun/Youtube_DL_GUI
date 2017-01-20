from Tkinter import *
import os, tkFileDialog
from subprocess import call
from subprocess import Popen, CREATE_NEW_CONSOLE
import ttk
import tkFont
import tkMessageBox, subprocess
from time import sleep
import ConfigParser

if not os.path.exists('config.ini'):
    config_file=file('config.ini', 'w')
    config = ConfigParser.ConfigParser()
    config.read('config.ini')
    config.add_section('checkboxes')
    config.add_section('entryboxes')
    config.add_section('log')
    config.set('checkboxes','checkbox_value_temporary', 0)
    config.set('checkboxes','checkbox_value_subs', 0)
    config.set('checkboxes','checkbox_value_format', 0)
    config.set('checkboxes','checkbox_value_quality', 0)
    config.set('checkboxes','checkbox_value_extra', 0)
    config.set('checkboxes','checkbox_value_convert', 0)
    config.set('checkboxes','checkbox_value_audio_format', 0)

    config.set('entryboxes','drop_text_subs', '')
    config.set('entryboxes','drop_text_format', '')
    config.set('entryboxes','drop_text_convert', '')
    config.set('entryboxes','drop_text_quality', '')
    config.set('entryboxes','entry_text_extra', '')
    config.set('entryboxes','entry_text_temporary', '')
    config.set('entryboxes','drop_text_audio_format', '')
    config.set('entryboxes','downloads_directory', os.getcwd())

    config.set('log','records', '')
    config.write(config_file)
    config_file.close()
    print 'hill'
else:
    config = ConfigParser.ConfigParser()
    config.read('config.ini')

main_directory=os.getcwd()
downloads_directory=config.get('entryboxes', 'downloads_directory')
if not os.path.exists(downloads_directory):
    os.makedirs(downloads_directory)
os.chdir(downloads_directory)

directory='downloads'
if not os.path.exists(directory):
    os.makedirs(directory)
os.chdir(directory) #makes downloads go to this folder
root = Tk() #create the window
root.wm_title("Youtube-dl") #name the window
root.resizable(0,0)
default_font = tkFont.Font(size=9,weight='bold')
#default_font.configure(size=10)
root.option_add("*Font", default_font)
index_extra=0
reset_temporary=os.getcwd()
checkbox_value_temporary=IntVar()
checkbox_value_subs=IntVar()
checkbox_value_format=IntVar()
checkbox_value_quality=IntVar()
checkbox_value_extra=IntVar()
checkbox_value_convert=IntVar()
checkbox_value_audio_format=IntVar()

subtitles=[]
qualitys=[]
top=None
drop_text_subs=StringVar()
drop_text_format=StringVar()
drop_text_convert=StringVar()
drop_text_quality=StringVar()
entry_text_extra=StringVar()
entry_text_temporary=StringVar()
drop_text_audio_format=StringVar()
text=''


checkbox_value_temporary.set(config.getint('checkboxes', 'checkbox_value_temporary'))
checkbox_value_subs.set( config.getint('checkboxes', 'checkbox_value_subs'))
checkbox_value_format.set( config.getint('checkboxes', 'checkbox_value_format'))
checkbox_value_quality.set( config.getint('checkboxes', 'checkbox_value_quality'))
checkbox_value_extra.set(config.getint('checkboxes', 'checkbox_value_extra'))
checkbox_value_convert.set( config.getint('checkboxes', 'checkbox_value_convert'))
checkbox_value_audio_format.set( config.getint('checkboxes', 'checkbox_value_audio_format'))

drop_text_subs.set(config.get('entryboxes', 'drop_text_subs'))
drop_text_format.set( config.get('entryboxes', 'drop_text_format'))
drop_text_convert.set( config.get('entryboxes', 'drop_text_convert'))
drop_text_quality.set(config.get('entryboxes', 'drop_text_quality'))
entry_text_extra.set( config.get('entryboxes', 'entry_text_extra'))
entry_text_temporary.set( config.get('entryboxes', 'entry_text_temporary'))
drop_text_audio_format.set( config.get('entryboxes', 'drop_text_audio_format'))

records=set(config.get('log', 'records').split(','))

def paste():
    text = root.selection_get(selection='CLIPBOARD')
    entry.delete(0, END)
    entry.insert(0, text)

def clear():
    if drop_text1.get() != '':
        save= os.getcwd()
        if not os.path.exists(drop_text1.get()):
            print '\a'
            if tkMessageBox.askyesno('Directory not found', 'This directory does not excist.\nWould you like to create it?'):
                os.makedirs(drop_text1.get())
        os.chdir(drop_text1.get())
        X=Popen('explorer '+ os.getcwd())
        os.chdir(save)
    else:
        X=Popen('explorer '+ os.getcwd())

def get_audio_and_video():
    paste()
    records.add(entry_text.get())
    set_config()
    options='-f bestaudio '
    if checkbox_value.get():
        options=options+' --ignore-errors '
    else:
        options=options+' --no-playlist '
    if drop_text_audio_format.get()!='':
        options=options+str(' -x --audio-format '+drop_text_audio_format.get()+' ')
    P=Popen("youtube-dl " +options+entry_text.get(), creationflags=CREATE_NEW_CONSOLE) #downloads the available playlist
    root.after(30, lambda: root.focus_force())

    records.add(entry_text.get())
    set_config()
    if checkbox_value.get():
        options=' --ignore-errors '
    else:
        options=' --no-playlist '
    if drop_text_convert.get()!='':
        options=options+str(' --recode-video '+drop_text_convert.get()+' ')
    P=Popen("youtube-dl " +options+entry_text.get(), creationflags=CREATE_NEW_CONSOLE) #downloads the available playlist
    root.after(30, lambda: root.focus_force())


def directory():
    if entry_text_extra.get()!='both':
        if drop_text1.get() != '':
            save= os.getcwd()
            if not os.path.exists(drop_text1.get()):
                os.makedirs(drop_text1.get())
            os.chdir(drop_text1.get())
            download()
            os.chdir(save)
        else:
            download()
    else:
        if drop_text1.get() != '':
            save= os.getcwd()
            if not os.path.exists(drop_text1.get()):
                os.makedirs(drop_text1.get())
            os.chdir(drop_text1.get())
            get_audio_and_video()
            os.chdir(save)
        else:
            get_audio_and_video()


def download():
    #-f bestaudio
    #best, bestvideo, bestaudio and worst
    paste()
    temprary_on()
    options=' '
    if drop_text_format.get()!='':
        options=options+drop_text_format.get()+' '
    if checkbox_value.get():
        options=options+' --ignore-errors'
    else:  
        options=options+' --no-playlist '
    if drop_text_subs.get()!='':
        options=options+str(' --sub-lang '+drop_text_subs.get()+' --write-sub')
    if drop_text_convert.get()!='':
        options=options+str(' --recode-video '+drop_text_convert.get()+' ')
    if drop_text_audio_format.get()!='':
        options=options+str(' -x --audio-format '+drop_text_audio_format.get()+' ')
    if drop_text_quality.get()!='':
        options=options+str(' -f '+drop_text_quality.get().split(',')[2]+' ')
    if entry_text_extra.get()!='':
        options=options+' '+entry_text_extra.get()
    options=options+' '
    records.add(entry_text.get())
    set_config()
    P=Popen("youtube-dl " +options+entry_text.get(), creationflags=CREATE_NEW_CONSOLE) #downloads the available playlist
    root.after(30, lambda: root.focus_force())
    temprary_off()
    
def temprary_on():
    global entry_text_temporary, reset_temporary
    reset_temporary=os.getcwd()
    if entry_text_temporary.get()!='':
        os.chdir(entry_text_temporary.get())

def temprary_off():
    os.chdir(reset_temporary)

def update_drop1(x):
    drop1['values'] = next(os.walk('.'))[1]

def set_config(x=1):
    global config, main_directory
    backup=os.getcwd()
    os.chdir(main_directory)
        
    config.set('checkboxes','checkbox_value_temporary', checkbox_value_temporary.get())
    config.set('checkboxes','checkbox_value_subs', checkbox_value_subs.get())
    config.set('checkboxes','checkbox_value_format', checkbox_value_format.get())
    config.set('checkboxes','checkbox_value_quality', checkbox_value_quality.get())
    config.set('checkboxes','checkbox_value_extra', checkbox_value_extra.get())
    config.set('checkboxes','checkbox_value_convert', checkbox_value_convert.get())
    config.set('checkboxes','checkbox_value_audio_format', checkbox_value_audio_format.get())
        

    config.set('entryboxes','drop_text_subs', drop_text_subs.get())
    config.set('entryboxes','drop_text_format', drop_text_format.get())
    config.set('entryboxes','drop_text_convert', drop_text_convert.get())
    config.set('entryboxes','drop_text_quality', drop_text_quality.get())
    config.set('entryboxes','entry_text_extra', entry_text_extra.get())
    config.set('entryboxes','entry_text_temporary', entry_text_temporary.get())
    config.set('entryboxes','drop_text_audio_format', drop_text_audio_format.get())
    config.set('entryboxes','downloads_directory', downloads_directory)

    config.set('log','records', ','.join(list(records)))
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    os.chdir(backup)

def settings():
    global downloads_directory, checkbox_value_temporary,checkbox_value_subs,checkbox_value_format
    global checkbox_value_quality,checkbox_value_extra,checkbox_value_focus, subtitles, qualitys, checkbox_value_convert, top
    global drop_text_subs, drop_text_format, drop_text_convert, drop_text_quality, entry_text_extra, entry_text_temporary, config
    global checkbox_value_audio_format, drop_text_audio_format
    x = root.winfo_rootx()
    y = root.winfo_rooty()
    height = 0#root.winfo_height()
    width = 100
    geom = "+%d+%d" % (x+width,y+height)
    top = Toplevel()
    top.geometry(geom)
    top.title("YT-DL Settings")
    top.config(cursor="")
    button_3.config(state='disable')
    root.wm_attributes("-disabled", 1) 
    top.wm_attributes('-toolwindow',1)
    top.focus_force()    
    root.wm_attributes("-topmost", 1)
    top.wm_attributes("-topmost", 1)

    def quit_win():
        set_config()
        top.destroy()
        button_3.config(state='normal')
        root.wm_attributes("-disabled", 0)
        root.focus_force()     
        root.wm_attributes("-topmost", 0)
    
        #configfile.close()
        #print config.items('entryboxes')
        #config.write(config_file)
        #config_file.close()
    def clearall(x=1):
        global downloads_directory
        #entry boxes
        drop_text_subs.set('')
        drop_text_format.set('')
        drop_text_quality.set('')
        entry_text_extra.set('')
        entry_text_directory.set(downloads_directory)
        entry_text_temporary.set('')
        drop_text_convert.set('')
        drop_text_audio_format.set('')
        #checkboxes
        checkbox_value_subs.set(0)
        checkbox_value_format.set(0)
        checkbox_value_quality.set(0)
        checkbox_value_extra.set(0)
        checkbox_value_temporary.set(0)
        checkbox_value_convert.set(0)
        checkbox_value_audio_format.set(0)


    qualitys=['3gp,320x?,36', '3gp,176x144,17', 'flv,400x240,5', 'webm,640x360,43', 'mp4,640x360,18', 'mp4,1280x720,22']
    subtitles=sorted(['gu', 'ga', 'gl', 'la', 'lo', 'tr', 'lv', 'lt', 'th', 'tg', 'te', 'ta', 'yi', 'yo', 'de', 'da', 'el', 'eo', 'en', 'eu', 'et', 'es',
    'ru', 'ro', 'bn', 'be', 'bg', 'ms', 'jv', 'bs', 'ja', 'ca', 'cy', 'cs', 'pt', 'pa', 'vi', 'pl', 'hy', 'hr', 
    'ht', 'hu', 'hi', 'ha', 'mg', 'uz', 'ml', 'mn', 'mi', 'mk', 'ur', 'mt', 'uk', 'mr', 'my', 'af', 'sw', 'is', 'it', 'iw', 'kn', 'ar',
    'km', 'zu', 'az', 'id', 'ig', 'nl', 'no', 'ne', 'ny', 'fr', 'fa', 'fi', 'ka', 'kk', 'sr', 'sq', 'ko', 'sv', 'su', 'st', 'sk', 'si',
    'so', 'sl', 'el', 'fr', 'en', 'nl', 'pt', 'no', 'hr', 'sr', 'sv', 'de', 'ko', 'it', 'da', 'sk', 'es', 'th',
    'cs', 'hu', 'id', 'pl'])

    #create the widgets
    #create subtitle select
    if checkbox_value_subs.get()==0:
        drop_text_subs.set('')
    drop_subs = ttk.Combobox(top, textvariable=drop_text_subs)
    #subtitles=['english','spanish','danish','japanese']
    drop_subs['values'] = subtitles
    drop_subs.grid(row=0, column=1,sticky=W+E)
    label_subs = Label(top, text='Subtitles')
    label_subs.grid(row=0, column=0)
    checkbox_subs=Checkbutton(top, text='Keep', variable=checkbox_value_subs)
    checkbox_subs.grid(row=0, column=2)

    #create format select
    if checkbox_value_format.get()==0:
        drop_text_format.set('')
    drop_format = ttk.Combobox(top, textvariable=drop_text_format)
    formats=['-f bestaudio','-f bestvideo','-f worst','-f best']
    drop_format['values'] = formats
    drop_format.grid(row=1, column=1,sticky=W+E)
    label_format = Label(top, text='Formats')
    label_format.grid(row=1, column=0)
    checkbox_format=Checkbutton(top, text='Keep', variable=checkbox_value_format)
    checkbox_format.grid(row=1, column=2)

    #create convert_to select
    if checkbox_value_convert.get()==0:
        drop_text_convert.set('')
    drop_convert = ttk.Combobox(top, textvariable=drop_text_convert)
    convert=['mp4','flv','ogg','webm','mkv','avi']
    drop_convert['values'] = convert
    drop_convert.grid(row=2, column=1,sticky=W+E)
    label_convert = Label(top, text='Video Format')
    label_convert.grid(row=2, column=0)
    checkbox_convert=Checkbutton(top, text='Keep', variable=checkbox_value_convert)
    checkbox_convert.grid(row=2, column=2)

    #audio-format
    if checkbox_value_audio_format.get()==0:
        drop_text_audio_format.set('')
    drop_audio_format= ttk.Combobox(top, textvariable=drop_text_audio_format)
    audio_format=["best", "aac","vorbis", "mp3", "m4a", "opus", "wav"]
    drop_audio_format['values'] = audio_format
    drop_audio_format.grid(row=5, column=1,sticky=W+E)
    label_audio_format = Label(top, text='Audio Format')
    label_audio_format.grid(row=5, column=0)
    checkbox_audio_format=Checkbutton(top, text='Keep', variable=checkbox_value_audio_format)
    checkbox_audio_format.grid(row=5, column=2)

    #create quality select
    if checkbox_value_quality.get()==0:
        drop_text_quality.set('')
    drop_quality = ttk.Combobox(top, textvariable=drop_text_quality)
    drop_quality['values'] = qualitys
    drop_quality.grid(row=3, column=1,sticky=W+E)
    label_quality = Label(top, text='Quality')
    label_quality.grid(row=3, column=0)
    checkbox_quality=Checkbutton(top, text='Keep', variable=checkbox_value_quality)
    checkbox_quality.grid(row=3, column=2)
    
    #create extra entry box
    #Lucida Console
    helv36 = tkFont.Font(family='Lucida Console', size=10, weight='normal') 
    if checkbox_value_extra.get()==0:
        entry_text_extra.set('')
    entry_extra = ttk.Combobox(top, textvariable=entry_text_extra, font=helv36)
    entry_extra['values']=['both','--audio-quality <0-9>','--embed-subs','--embed-thumbnail','--convert-subs <srt,ass,vtt>','--write-auto-sub',
    '--write-thumbnail','--write-description','--playlist-reverse']
    entry_extra.grid(row=4, column=1,sticky=W+E)
    label_extra = Label(top, text='Arguments')
    label_extra.grid(row=4, column=0)
    checkbox_extra=Checkbutton(top, text='Keep', variable=checkbox_value_extra)
    checkbox_extra.grid(row=4, column=2)

    #dirctory entry
    def selectdir(x=1):
        global downloads_directory
        dir_opt = options = {}
        options['initialdir'] = 'C:\\'
        options['mustexist'] = False
        options['parent'] = root
        options['title'] = 'This is a title'
        new_directory=tkFileDialog.askdirectory(initialdir='.')
        if new_directory!='':
            entry_text_directory.set(new_directory)
            downloads_directory=new_directory
            os.chdir(downloads_directory)
            directory='downloads'
            if not os.path.exists(directory):
                os.makedirs(directory)
            os.chdir(directory)
        top.focus_force()

    entry_text_directory=StringVar()
    entry_text_directory.set(downloads_directory)
    entry_directory=Entry(top, textvariable=entry_text_directory)
    entry_directory.grid(row=7, column=1,sticky=W+E)
    label_directory = Label(top, text='Directory')
    label_directory.grid(row=7, column=0)
    entry_directory.bind('<FocusIn>',selectdir)
    
    #temporary directory entry
    def selectdir(x=1):
        new_temporary=tkFileDialog.askdirectory(initialdir='.')
        if new_temporary!='':
            entry_text_temporary.set(new_temporary)
        top.focus_force()

    if checkbox_value_temporary.get()==0:
        entry_text_temporary.set('')
    entry_temporary=Entry(top, textvariable=entry_text_temporary)
    entry_temporary.grid(row=6, column=1,sticky=W+E)
    label_temporary = Label(top, text='Temporary Directory')
    label_temporary.grid(row=6, column=0)
    entry_temporary.bind('<FocusIn>',selectdir)
    
    checkbox_temporary=Checkbutton(top, text='Keep', variable=checkbox_value_temporary)
    checkbox_temporary.grid(row=6, column=2)

    button_clear=Button(top, text='Clear', command=clearall, width=6)
    button_clear.grid(row=8, column=2)

    top.protocol("WM_DELETE_WINDOW", quit_win) 
    top.resizable(0,0)



checkbox_value=IntVar()
entry_text=StringVar() #create the variables where the input to the entry boxes is stored
drop_text1=StringVar()

label = Label(root, text='URL') #create the labels

entry = Entry(root, width=61, textvariable=entry_text) #create the entry boxes

button_1=Button(root, text='Paste & Download', command=directory, width=17) #create buttons
button_2=Button(root, text='Open Folder', command=clear, width=17) 
button_3=Button(root, text='Settings', command=settings, width=17) 
checkbox_1=Checkbutton(root, text='Download Playlist', variable=checkbox_value)



drop1 = ttk.Combobox(root, textvariable=drop_text1)
drop1['values'] = next(os.walk('.'))[1]



label.grid(row=0) #place the labels in the window

entry.grid(row=0, column=1,columnspan=3) #place the entry boxes in the window

button_1.grid(row=0, column=4) #place a button in the window
button_2.grid(row=1, column=4)
button_3.grid(row=1, column=3)
#drop.grid(row=1, column=2)
drop1.grid(row=1, column=1)
checkbox_1.grid(row=1,column=2)

drop1.bind('<FocusIn>', update_drop1)

root.mainloop() #stop the window from closing
