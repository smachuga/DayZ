import enaml
from enaml.qt.qt_application import QtApplication

if __name__ == '__main__':
    with enaml.imports():
        from views.Main import MainView

    app = QtApplication()

    view = MainView()
    view.show()

    app.start()