import PySimpleGUI as sg
import time

def show_loading():
    sg.PopupAnimated('images/searching.gif',
    message='Searching for Results...',
    background_color=None,
    text_color=None,
    font=None,
    no_titlebar=True,
    grab_anywhere=True,
    keep_on_top=True,
    location=(None, None),
    alpha_channel=None,
    time_between_frames=500,
    transparent_color=None)

def remove_loading():
    sg.PopupAnimated(image_source=None)