from mymodules.buttons_images import Img
from mymodules.builder import Builder
from mymodules.action.dial import action

class Menu5:

    # get menu 5 application buttons
    gparted = Builder.builder6.get_object("gparted")
    guake = Builder.builder6.get_object("guake")
    hardinfo = Builder.builder6.get_object("hardinfo")
    htop = Builder.builder6.get_object("htop")
    keepassx = Builder.builder6.get_object("keepassx")
    playonlinux = Builder.builder6.get_object("playonlinux")
    terminator = Builder.builder6.get_object("terminator")
    thunar = Builder.builder6.get_object("thunar")
    truecrypt = Builder.builder6.get_object("truecrypt")
    unetbootin = Builder.builder6.get_object("unetbootin")
    virtualbox = Builder.builder6.get_object("virtualbox")
    wine = Builder.builder6.get_object("wine")
    wireshark = Builder.builder6.get_object("wireshark")
    xbmc = Builder.builder6.get_object("xbmc")
    gufw = Builder.builder6.get_object("gufw")
    octopi = Builder.builder6.get_object("octopi")
    pamac = Builder.builder6.get_object("pamac")
    gnome_system_monitor = Builder.builder6.get_object("gnome_system_monitor")
    # add tooltip for each application icon
    gparted_icon_tooltip = Builder.builder6.get_object("gparted_icon_tooltip")
    gparted_icon_tooltip.set_tooltip_text("GParted is a free partition editor for graphically managing your disk partitions. ")
    guake_icon_tooltip = Builder.builder6.get_object("guake_icon_tooltip")
    guake_icon_tooltip.set_tooltip_text("Guake is a drop-down terminal.")
    hardinfo_icon_tooltip = Builder.builder6.get_object("hardinfo_icon_tooltip")
    hardinfo_icon_tooltip.set_tooltip_text("Hardinfo provides comprehensive details of your PC's software and hardware and allows you to benchmark its performance.")
    htop_icon_tooltip = Builder.builder6.get_object("htop_icon_tooltip")
    htop_icon_tooltip.set_tooltip_text("Htop is an interactive process viewer.")
    keepassx_icon_tooltip = Builder.builder6.get_object("keepassx_icon_tooltip")
    keepassx_icon_tooltip.set_tooltip_text("KeePassX is an application for people with extremly high demands on secure personal data management.")
    playonlinux_icon_tooltip = Builder.builder6.get_object("playonlinux_icon_tooltip")
    playonlinux_icon_tooltip.set_tooltip_text("PlayOnLinux will allow you to play your favorite games on Linux easily.")
    terminator_icon_tooltip = Builder.builder6.get_object("terminator_icon_tooltip")
    terminator_icon_tooltip.set_tooltip_text(" Terminator is a cross-platform GPL terminal emulator with advanced features not yet found elsewhere.")
    thunar_icon_tooltip = Builder.builder6.get_object("thunar_icon_tooltip")
    thunar_icon_tooltip.set_tooltip_text("Thunar is a file manager.")
    truecrypt_icon_tooltip = Builder.builder6.get_object("truecrypt_icon_tooltip")
    truecrypt_icon_tooltip.set_tooltip_text("TrueCrypt is free open-source disk encryption software.")
    unetbootin_icon_tooltip = Builder.builder6.get_object("unetbootin_icon_tooltip")
    unetbootin_icon_tooltip.set_tooltip_text("UNetbootin allows you to create bootable Live USB drives for GNU/Linux distributions without burning a CD")
    virtualbox_icon_tooltip = Builder.builder6.get_object("virtualbox_icon_tooltip")
    virtualbox_icon_tooltip.set_tooltip_text("VirtualBox is a powerful x86 and AMD64/Intel64 virtualization product for enterprise as well as home use.\nThe program is similar to Virtual PC.")
    wine_icon_tooltip = Builder.builder6.get_object("wine_icon_tooltip")
    wine_icon_tooltip.set_tooltip_text("Wine is a compatibility layer for running windows applications on GNU/Linux.")
    wireshark_icon_tooltip = Builder.builder6.get_object("wireshark_icon_tooltip")
    wireshark_icon_tooltip.set_tooltip_text("Wireshark is a free and open-source packet analyzer. It is used for network troubleshooting, analysis,\nsoftware and communications protocol development.")
    xbmc_icon_tooltip = Builder.builder6.get_object("xbmc_icon_tooltip")
    xbmc_icon_tooltip.set_tooltip_text("XBMC Media Center is a free cross-platform media player software and entertainment system application framework.")
    gufw_icon_tooltip = Builder.builder6.get_object("gufw_icon_tooltip")
    gufw_icon_tooltip.set_tooltip_text("One of the easiest firewalls in the world!")
    octopi_icon_tooltip = Builder.builder6.get_object("octopi_icon_tooltip")
    octopi_icon_tooltip.set_tooltip_text("Octopi is a powerful tool to manage (Arch | Manjaro) Linux packages.")
    pamac_icon_tooltip = Builder.builder6.get_object("pamac_icon_tooltip")
    pamac_icon_tooltip.set_tooltip_text("pamac - simple graphical package manager for Manjaro Linux.")
    gnome_system_monitor_icon_tooltip = Builder.builder6.get_object("gnome_system_monitor_icon_tooltip")
    gnome_system_monitor_icon_tooltip.set_tooltip_text("Gnome System Monitor is a GNOME process viewer and system monitor with a nice easy-to-use interface")

    @staticmethod
    def on_button5_clicked():
        Img.image1.set_from_file(action.menu_img_1)
        Img.image2.set_from_file(action.menu_img_2)
        Img.image3.set_from_file(action.menu_img_3)
        Img.image4.set_from_file(action.menu_img_4)
        Img.image5.set_from_file(action.menu_img_55)
        Img.image6.set_from_file(action.menu_img_6)

        from somesome import menu5
        menu5.load()