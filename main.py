from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.utils import get_color_from_hex
from jnius import autoclass

PythonActivity = autoclass('org.kivy.android.PythonActivity')
Context = autoclass('android.content.Context')

class BatteryApp(App):
    def build(self):
        self.layout = BoxLayout(
            orientation='vertical',
            padding=25,
            spacing=20
        )

        self.layout.add_widget(Label(
            text='AI BATRE PRO',
            font_size=30,
            color=get_color_from_hex('#00D4FF')
        ))

        self.info = Label(text='Memuat baterai...', font_size=20)
        self.layout.add_widget(self.info)

        Clock.schedule_interval(self.update_battery, 5)
        return self.layout

    def update_battery(self, dt):
        try:
            activity = PythonActivity.mActivity
            manager = activity.getSystemService(Context.BATTERY_SERVICE)
            level = manager.getIntProperty(4)
            temp = manager.getIntProperty(6)

            self.info.text = (
                f'BATERAI: {level}%\n'
                f'SUHU: {temp / 10:.1f} C\n'
                f'KONDISI: {"LEMAH" if level <= 30 else "NORMAL"}'
            )
        except Exception as e:
            self.info.text = 'Data baterai belum tersedia'

if __name__ == '__main__':
    BatteryApp().run()
