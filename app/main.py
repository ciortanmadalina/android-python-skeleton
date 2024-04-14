from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.utils import platform
from kivy.logger import Logger
if platform == 'android':
    from kivmob_mod import KivMob, TestIds

class Welcome(BoxLayout):
    pass

class MainApp(App):
    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)
        self.title = "IQ"
    def build(self):
        if platform == 'android':
            self.ads = KivMob(TestIds.APP) 
            #banner
            self.ads.new_banner(TestIds.BANNER,top_pos=False)
            self.ads.request_banner()
            self.ads.show_banner()
            self.ads.load_interstitial(TestIds.INTERSTITIAL) 

        return Welcome()
    def on_resume(self):
        Logger.info("kivmob_test: on_resume()")
        if platform == 'android':
            self.load_ads()
    def load_ads(self):
        if platform == 'android':
            Logger.info("kivmob_test: load_ads() fired")
            #banner
            self.ads.request_banner()
            #interstitial
            self.ads.load_interstitial(TestIds.INTERSTITIAL) 
    def show_banner(self):
        if platform == 'android':
            Logger.info("kivmob_test: show_banner() fired")
            self.ads.show_banner()
    def hide_banner(self):
        if platform == 'android':
            Logger.info("kivmob_test: hide_banner() fired")
            self.ads.hide_banner()
    def load_interstitial(self):
        if platform == 'android':
            Logger.info("kivmob_test: load_interstitial() fired")
            self.ads.load_interstitial(TestIds.INTERSTITIAL)
    def show_interstitial(self):
        if platform == 'android':
            Logger.info("kivmob_test: show_interstitial() fired")
            self.ads.show_interstitial()

if __name__ == '__main__':
    MainApp().run()