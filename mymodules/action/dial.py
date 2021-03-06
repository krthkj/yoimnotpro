import os
from random import choice
from configparser import ConfigParser
from gi.repository import Gtk

class ChangeLang(object):
    def save_lang(self, lang):
        with open('/tmp/.yoimnotpro.conf', 'wt') as f:
            f.write(lang)
    def combo_changed(self, combobox):
        from mymodules.builder import SetMenuCategoriesTooltipNames
        active = self.combobox.get_active_text()
        local_dict = {'English':'english,utf-8', 'Deutsch':'german,cp1252',
        'Русский':'russian,cp855', 'Български':'bulgarian,cp1251'}
        if active in local_dict:
            self.save_lang(local_dict[active])
            OpenCFGnSetLang()
            SetMenuCategoriesTooltipNames()
    def __init__(self):
        self.window = Gtk.Window()
        self.combobox = Gtk.ComboBoxText()
        self.combobox.append("", "Languages:")
        self.combobox.append("", "English")
        self.combobox.append("", "Български"\
            .encode('cp1251').decode('cp1251'))
        self.combobox.append("", "Русский"\
            .encode('cp855').decode('cp855'))
        self.combobox.append("", "Deutsch")
        self.combobox.set_active(0)
        self.combobox.connect("changed", self.combo_changed)
        self.window.add(self.combobox)
        self.window.show_all()
        self.window.connect("destroy", lambda q: Gtk.main_quit())
        Gtk.main()
class OpenCFGnSetLang(object):
    def __init__(self):
        if os.path.isfile("/tmp/.yoimnotpro.conf"):
            with open('/tmp/.yoimnotpro.conf', 'rt') as f:
               read = f.read().split(',')
               action.encoding = read[1]
               action.section = read[0]
        else:
            action.encoding = 'utf-8'
            action.section = 'english'
        cfg = ConfigParser()
        cfg.read('translations/langs.ini')
        enc = action.encoding
        for key, val in cfg.items(action.section):
            dec = val.encode(enc).decode(enc)
            if key in ['development','graphics','internet','system',
            'multimedia','utilities','about', 'langs']:
                setattr(action, key, '<b>{}</b>'.format(dec))
            elif key in ['installed', 'not_here']:
                setattr(action, key, '<span foreground="{0}" weight="bold">{1}</span>'
                    .format(('green' if key == 'installed' else 'red'), dec))
            else:
                setattr(action, key, dec)
class CurrentCategoryDict(object):
    pass
class dial(object):
    def display_message(self, action2):
        dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
            Gtk.ButtonsType.OK, "{program_name} {was2} {inst_or_rem} {sucs}."
                .format(program_name=self._name, was2=action.was,
                    inst_or_rem=action2, sucs=action.successfully),
                title="{program_name} {random_message}"
                .format(program_name=self._name,
                    random_message=choice(self._dict_with_phrases[action2])))
        dialog.run()
        dialog.destroy()
    def __init__(self, *arg):
        self._name = arg[0]
        self._action = arg[1]
        self._dict_with_phrases = {
        action.installed2: (action.good_choice, action.thats_my_boy, action.i_like_it_too,
                    action.cheers, '>:-)', action.eyecandy),
        (action.not_here2 if not action.section
            == 'english' else 'removed'): (action.how_dare_you, action.pitty_to_see_it_go, '>:-(',
                    action.was_douchebag, 'LMAO', 'LOL', action.damn_you_bro)}
        self.display_message(action.installed2
                        if self._action == action.installed else (action.not_here2 
                            if not action.section == 'english' else 'removed'))
class SetToolTip(object):
    def __init__(self, *arg):
        self._arg = arg
    def __repr__(self):
        return '<b><i>{program_name}</i></b> {iz2} {maybe_here}.\n{click_to2} {apply_some_action_to} {it2}'\
        .format(program_name=self._arg[0].capitalize(), iz2=(('is' if action.section == 'english' else
         action.iz if self._arg[1] == action.installed else str())),
            maybe_here=self._arg[1], click_to2=action.click_to, apply_some_action_to=self._arg[2],
            it2=('it' if action.section == 'english' else action.it))
class action(object):
    encoding, section, langs, damn_you_bro = str(), str(), str(), str()
    was_douchebag, pitty_to_see_it_go, how_dare_you, cheers = str(), str(), str(), str()
    eyecandy, i_like_it_too, good_choice, thats_my_boy = str(), str(), str(), str()
    program_description, dev_website, license, suggestions = str(), str(), str(), str()
    comments, program_name, not_here, install_it, remove_it = str(), str(), str(), str(), str()
    installed, development, graphics, internet = str(), str(), str(), str()
    multimedia, system, utilities, about, was = str(), str(), str(), str(), str()
    successfully, installed2, not_here2, iz, click_to, it = str(), str(), str(), str(), str(), str()
    gtk_yes = './categories/gtk-yes.png'
    gtk_no = './categories/gtk-no.png'
    menu_img_66 = './categories/menu66.png'
    menu_img_5 = './categories/menu5.xpm'
    menu_img_4 = './categories/menu4.png'
    menu_img_3 = './categories/menu3.png'
    menu_img_2 = './categories/menu2.png'
    menu_img_1 = './categories/menu1.png'
    menu_img_55 = './categories/menu55.xpm'
    menu_img_11 = './categories/menu11.png'
    menu_img_22 = './categories/menu22.png'
    menu_img_33 = './categories/menu33.png'
    menu_img_44 = './categories/menu44.png'
    menu_img_6 = './categories/menu6.png'