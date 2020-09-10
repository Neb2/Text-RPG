import ctypes


def maximize_console():
    kernel32 = ctypes.WinDLL('kernel32')
    user32 = ctypes.WinDLL('user32')

    sw_maximize = 3

    h_wnd = kernel32.GetConsoleWindow()
    user32.ShowWindow(h_wnd, sw_maximize)
