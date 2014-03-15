import os
from mymodules.buttons_images import Img
from mymodules.builder import Builder
from mymodules.action.find_program import Find

class Menu7:
    # get menu 7 application buttons
    geany_ = Builder.builder8.get_object("geany_")
    blender_ = Builder.builder8.get_object("blender_")
    ninja_ide_ = Builder.builder8.get_object("ninja_ide_")
    glade_ = Builder.builder8.get_object("glade_")
    audacious_ = Builder.builder8.get_object("audacious_")
    gimp_ = Builder.builder8.get_object("gimp_")
    evince_ = Builder.builder8.get_object("evince_")
    xfburn_ = Builder.builder8.get_object("xfburn_")
    flashplayer_ = Builder.builder8.get_object("flashplayer_")
    openshot_ = Builder.builder8.get_object("openshot_")
    chromium_ = Builder.builder8.get_object("chromium_")
    deluge_ = Builder.builder8.get_object("deluge_")
    liferea_ = Builder.builder8.get_object("liferea_")
    htop_ = Builder.builder8.get_object("htop_")
    skype_ = Builder.builder8.get_object("skype_")
    wireshark_ = Builder.builder8.get_object("wireshark_")
    virtualbox_ = Builder.builder8.get_object("virtualbox_")
    steam_ = Builder.builder8.get_object("steam_")
    xchat_ = Builder.builder8.get_object("xchat_")
    gedit_ = Builder.builder8.get_object("gedit_")
    # add tooltip for each application icon
    geany_icon_tooltip_ = Builder.builder8.get_object("geany_icon_tooltip_")
    geany_icon_tooltip_.set_tooltip_text("Geany is a small and lightweight integrated development environment.")
    blender_icon_tooltip_ = Builder.builder8.get_object("blender_icon_tooltip_")
    blender_icon_tooltip_.set_tooltip_text("Blender is the open source, cross platform suite of tools for 3D creation.")
    ninja_ide_icon_tooltip_ = Builder.builder8.get_object("ninja_ide_icon_tooltip_")
    ninja_ide_icon_tooltip_.set_tooltip_text("Ninja-IDE is a cross-platform integrated development environment designed to build Python applications.")
    glade_icon_tooltip_ = Builder.builder8.get_object("glade_icon_tooltip_")
    glade_icon_tooltip_.set_tooltip_text("Glade is a RAD tool to enable quick & easy development of user interfaces for the GTK+ toolkit and the GNOME desktop environment.")
    audacious_icon_tooltip_ = Builder.builder8.get_object("audacious_icon_tooltip_")
    audacious_icon_tooltip_.set_tooltip_text("Audio player with support for many formats, and it has support for third-party plugins.")
    gimp_icon_tooltip_ = Builder.builder8.get_object("gimp_icon_tooltip_")
    gimp_icon_tooltip_.set_tooltip_text("GIMP is an image retouching and editing tool, similar to Photoshop.")
    evince_icon_tooltip_ = Builder.builder8.get_object("evince_icon_tooltip_")
    evince_icon_tooltip_.set_tooltip_text("Evince is a document viewer for multiple document formats.")
    xfburn_icon_tooltip_ = Builder.builder8.get_object("xfburn_icon_tooltip_")
    xfburn_icon_tooltip_.set_tooltip_text("Xfburn is a simple CD/DVD burning tool")
    flashplayer_icon_tooltip_ = Builder.builder8.get_object("flashplayer_icon_tooltip_")
    flashplayer_icon_tooltip_.set_tooltip_text("Cross-platform plugin plays animations, videos and sound files.")
    openshot_icon_tooltip_ = Builder.builder8.get_object("openshot_icon_tooltip_")
    openshot_icon_tooltip_.set_tooltip_text("A simple, powerful, and free open-source video editor for Linux with a focus on usability, flexibility, and style")
    chromium_icon_tooltip_ = Builder.builder8.get_object("chromium_icon_tooltip_")
    chromium_icon_tooltip_.set_tooltip_text("Chromium is the open source web browser project from which Google Chrome draws its source code.")
    deluge_icon_tooltip_ = Builder.builder8.get_object("deluge_icon_tooltip_")
    deluge_icon_tooltip_.set_tooltip_text("Open source, cross-platform BitTorrent client.")
    liferea_icon_tooltip_ = Builder.builder8.get_object("liferea_icon_tooltip_")
    liferea_icon_tooltip_.set_tooltip_text("Liferea is an abbreviation for Linux Feed Reader, a news aggregator for online news feeds.")
    htop_icon_tooltip_ = Builder.builder8.get_object("htop_icon_tooltip_")
    htop_icon_tooltip_.set_tooltip_text("Htop is an interactive system-monitor process-viewer.")
    skype_icon_tooltip_ = Builder.builder8.get_object("skype_icon_tooltip_")
    skype_icon_tooltip_.set_tooltip_text("Skype is a freemium voice-over-IP service and instant messaging client")
    wireshark_icon_tooltip_ = Builder.builder8.get_object("wireshark_icon_tooltip_")
    wireshark_icon_tooltip_.set_tooltip_text("Wireshark is a free and open-source packet analyzer. It is used for network troubleshooting, analysis,\nsoftware and communications protocol development.")
    virtualbox_icon_tooltip_ = Builder.builder8.get_object("virtualbox_icon_tooltip_")
    virtualbox_icon_tooltip_.set_tooltip_text("VirtualBox is a powerful x86 and AMD64/Intel64 virtualization product for enterprise as well as home use.\nThe program is similar to Virtual PC.")
    steam_icon_tooltip_ = Builder.builder8.get_object("steam_icon_tooltip_")
    steam_icon_tooltip_.set_tooltip_text("Steam is a digital distribution, digital rights management, multiplayer, and communications platform developed by\nValve Corporation. It is used to distribute games and related media online, from small independent developers to larger software houses.")
    xchat_icon_tooltip_ = Builder.builder8.get_object("xchat_icon_tooltip_")
    xchat_icon_tooltip_.set_tooltip_text("XChat is a popular Internet Relay Chat (IRC) client.")
    gedit_icon_tooltip_ = Builder.builder8.get_object("gedit_icon_tooltip_")
    gedit_icon_tooltip_.set_tooltip_text("gedit is lightweight text editor.")

    # check if those programs are installed and set appropriate sign
    Img.geany__img = Builder.builder8.get_object("geany_img_")
    if os.path.isfile(Find.program['geany']):
        Img.geany__img.set_from_file('categories/gtk-yes.png')
        geany_.set_tooltip_text("Geany is installed.\nClick to remove it.")
    else:
        Img.geany__img.set_from_file('categories/gtk-no.png')
        geany_.set_tooltip_text("Geany is not installed.\nClick to install it.")

    Img.blender__img = Builder.builder8.get_object("blender_img_")
    if os.path.isfile(Find.program['blender']):
        Img.blender__img.set_from_file('categories/gtk-yes.png')
        blender_.set_tooltip_text("Blender is installed.\nClick to remove it.")
    else:
        Img.blender__img.set_from_file('categories/gtk-no.png')
        blender_.set_tooltip_text("Blender is not installed.\nClick to install it.")

    Img.ninja_ide__img = Builder.builder8.get_object("ninja_ide_img_")
    if os.path.isfile(Find.program['ninja-ide']):
        Img.ninja_ide__img.set_from_file('categories/gtk-yes.png')
        ninja_ide_.set_tooltip_text("Ninja-IDE is installed.\nClick to remove it.")
    else:
        Img.ninja_ide__img.set_from_file('categories/gtk-no.png')
        ninja_ide_.set_tooltip_text("Ninja-IDE is not installed.\nClick to install it.")

    Img.glade__img = Builder.builder8.get_object("glade_img_")
    if os.path.isfile(Find.program['glade']):
        Img.glade__img.set_from_file('categories/gtk-yes.png')
        glade_.set_tooltip_text("Glade is installed.\nClick to remove it.")
    else:
        Img.glade__img.set_from_file('categories/gtk-no.png')
        glade_.set_tooltip_text("Glade is not installed.\nClick to install it.")

    Img.audacious__img = Builder.builder8.get_object("audacious_img_")
    if os.path.isfile(Find.program['audacious']):
        Img.audacious__img.set_from_file('categories/gtk-yes.png')
        audacious_.set_tooltip_text("Audacious is installed.\nClick to remove it.")
    else:
        Img.audacious__img.set_from_file('categories/gtk-no.png')
        audacious_.set_tooltip_text("Audacious is not installed.\nClick to install it.")

    Img.gimp__img = Builder.builder8.get_object("gimp_img_")
    if os.path.isfile(Find.program['gimp']):
        Img.gimp__img.set_from_file('categories/gtk-yes.png')
        gimp_.set_tooltip_text("Gimp is installed.\nClick to remove it.")
    else:
        Img.gimp__img.set_from_file('categories/gtk-no.png')
        gimp_.set_tooltip_text("Gimp is not installed.\nClick to install it.")

    Img.evince__img = Builder.builder8.get_object("evince_img_")
    if os.path.isfile(Find.program['evince']):
        Img.evince__img.set_from_file('categories/gtk-yes.png')
        evince_.set_tooltip_text("Evince is installed.\nClick to remove it.")
    else:
        Img.evince__img.set_from_file('categories/gtk-no.png')
        evince_.set_tooltip_text("Evince is not installed.\nClick to install it.")

    Img.xfburn__img = Builder.builder8.get_object("xfburn_img_")
    if os.path.isfile(Find.program['xfburn']):
        Img.xfburn__img.set_from_file('categories/gtk-yes.png')
        xfburn_.set_tooltip_text("Xfburn is installed.\nClick to remove it.")
    else:
        Img.xfburn__img.set_from_file('categories/gtk-no.png')
        xfburn_.set_tooltip_text("Xfburn is installed.\nClick to install it.")

    Img.flashplayer__img = Builder.builder8.get_object("flashplayer_img_")
    if os.path.isfile(Find.program['flash-player']):
        Img.flashplayer__img.set_from_file('categories/gtk-yes.png')
        flashplayer_.set_tooltip_text("Flashplayer is installed.\nClick to remove it.")
    else:
        Img.flashplayer__img.set_from_file('categories/gtk-no.png')
        flashplayer_.set_tooltip_text("Flashplayer is not installed.\nClick to install it.")

    Img.openshot__img = Builder.builder8.get_object("openshot_img_")
    if os.path.isfile(Find.program['openshot']):
        Img.openshot__img.set_from_file('categories/gtk-yes.png')
        openshot_.set_tooltip_text("Openshot is installed.\nClick to remove it.")
    else:
        Img.openshot__img.set_from_file('categories/gtk-no.png')
        openshot_.set_tooltip_text("Openshot is not installed.\nClick to install it.")

    Img.chromium__img = Builder.builder8.get_object("chromium_img_")
    if os.path.isfile(Find.program['chromium']):
        Img.chromium__img.set_from_file('categories/gtk-yes.png')
        chromium_.set_tooltip_text("Chromium is installed.\nClick to remove it.")
    else:
        Img.chromium__img.set_from_file('categories/gtk-no.png')
        chromium_.set_tooltip_text("Chromium is not installed.\nClick to install it.")

    Img.deluge__img = Builder.builder8.get_object("deluge_img_")
    if os.path.isfile(Find.program['deluge']):
        Img.deluge__img.set_from_file('categories/gtk-yes.png')
        deluge_.set_tooltip_text("Deluge is installed.\nClick to remove it.")
    else:
        Img.deluge__img.set_from_file('categories/gtk-no.png')
        deluge_.set_tooltip_text("Deluge is notinstalled.\nClick to insall it.")

    Img.liferea__img = Builder.builder8.get_object("liferea_img_")
    if os.path.isfile(Find.program['liferea']):
        Img.liferea__img.set_from_file('categories/gtk-yes.png')
        liferea_.set_tooltip_text("Liferea is installed.\nClick to remove it.")
    else:
        Img.liferea__img.set_from_file('categories/gtk-no.png')
        liferea_.set_tooltip_text("Liferea is not installed.\nClick to install it.")

    Img.htop__img = Builder.builder8.get_object("htop_img_")
    if os.path.isfile(Find.program['htop']):
        Img.htop__img.set_from_file('categories/gtk-yes.png')
        htop_.set_tooltip_text("Htop is installed.\nClick to remove it.")
    else:
        Img.htop__img.set_from_file('categories/gtk-no.png')
        htop_.set_tooltip_text("Htop is not installed.\nClick to install it.")

    Img.skype__img = Builder.builder8.get_object("skype_img_")
    if os.path.isfile(Find.program['skype']):
        Img.skype__img.set_from_file('categories/gtk-yes.png')
        skype_.set_tooltip_text("Skype is installed.\nClick to remove it.")
    else:
        Img.skype__img.set_from_file('categories/gtk-no.png')
        skype_.set_tooltip_text("Skype is not installed.\nClick to install it.")

    Img.wireshark__img = Builder.builder8.get_object("wireshark_img_")
    if os.path.isfile(Find.program['wireshark']):
        Img.wireshark__img.set_from_file('categories/gtk-yes.png')
        wireshark_.set_tooltip_text("Wireshark is installed.\nClick to remove it.")
    else:
        Img.wireshark__img.set_from_file('categories/gtk-no.png')
        wireshark_.set_tooltip_text("Wireshark is not installed.\nClick to install it.")

    Img.virtualbox__img = Builder.builder8.get_object("virtualbox_img_")
    if os.path.isfile(Find.program['virtualbox']):
        Img.virtualbox__img.set_from_file('categories/gtk-yes.png')
        virtualbox_.set_tooltip_text("Virtualbox is installed.\nClick to remove it.")
    else:
        Img.virtualbox__img.set_from_file('categories/gtk-no.png')
        virtualbox_.set_tooltip_text("Virtualbox is not installed.\nClick to install it.")

    Img.steam__img = Builder.builder8.get_object("steam_img_")
    if os.path.isfile(Find.program['steam']):
        Img.steam__img.set_from_file('categories/gtk-yes.png')
        steam_.set_tooltip_text("Steam is installed.\nClick to remove it.")
    else:
        Img.steam__img.set_from_file('categories/gtk-no.png')
        steam_.set_tooltip_text("Steam is not installed.\nClick to insall it.")

    Img.xchat__img = Builder.builder8.get_object("xchat_img_")
    if os.path.isfile(Find.program['xchat']):
        Img.xchat__img.set_from_file('categories/gtk-yes.png')
        xchat_.set_tooltip_text("Xchat is installed.\nClick to remove it.")
    else:
        Img.xchat__img.set_from_file('categories/gtk-no.png')
        xchat_.set_tooltip_text("Xchat is not installed.\nClick to install it.")

    Img.gedit__img = Builder.builder8.get_object("gedit_img_")
    if os.path.isfile(Find.program['gedit']):
        Img.gedit__img.set_from_file('categories/gtk-yes.png')
        gedit_.set_tooltip_text("Gedit is installed.\nClick to remove it.")
    else:
        Img.gedit__img.set_from_file('categories/gtk-no.png')
        gedit_.set_tooltip_text("Gedit is not installed.\nClick to install it.")