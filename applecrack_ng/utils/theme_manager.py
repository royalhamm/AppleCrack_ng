from PyQt5.QtWidgets import QApplication

from PyQt5.QtGui import QPalette, QColor



class ThemeManager:

    """Manage application themes (dark/light)."""



    def __init__(self):

        self.current_theme = 'dark'  # Default theme



    def apply_dark_theme(self, app):

        """Apply dark theme to the application."""



        # Set palette for dark theme

        palette = QPalette()

        palette.setColor(QPalette.Window, QColor(53, 53, 53))

        palette.setColor(QPalette.WindowText, QColor(255, 255, 255))

        palette.setColor(QPalette.Base, QColor(42, 42, 42))

        palette.setColor(QPalette.AlternateBase, QColor(66, 66, 66))

        palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))

        palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))

        palette.setColor(QPalette.Text, QColor(255, 255, 255))

        palette.setColor(QPalette.Button, QColor(53, 53, 53))

        palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))

        palette.setColor(QPalette.BrightText, QColor(255, 0, 0))

        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))

        palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))



        app.setPalette(palette)

        # Remove the problematic setStyle call

        # app.setStyle('Fusion')



    def apply_light_theme(self, app):

        """Apply light theme to the application."""



        # Set palette for light theme

        palette = QPalette()

        palette.setColor(QPalette.Window, QColor(240, 240, 240))

        palette.setColor(QPalette.WindowText, QColor(0, 0, 0))

        palette.setColor(QPalette.Base, QColor(255, 255, 255))

        palette.setColor(QPalette.AlternateBase, QColor(210, 210, 210))

        palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))

        palette.setColor(QPalette.ToolTipText, QColor(0, 0, 0))

        palette.setColor(QPalette.Text, QColor(0, 0, 0))

        palette.setColor(QPalette.Button, QColor(240, 240, 240))

        palette.setColor(QPalette.ButtonText, QColor(0, 0, 0))

        palette.setColor(QPalette.BrightText, QColor(255, 0, 0))

        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))

        palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))



        app.setPalette(palette)

        # Remove the problematic setStyle call

        # app.setStyle('Fusion')



    def switch_theme(self, app, theme_name):

        """Switch between themes."""

        if theme_name == 'dark':

            self.apply_dark_theme(app)

            self.current_theme = 'dark'

        else:

            self.apply_light_theme(app)

            self.current_theme = 'light'
