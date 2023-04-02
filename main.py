import json
import threading
import time
import asyncio
from typing import List

import cv2
from cv2 import *
from numpy import *

import aiohttp
import os
from PyQt6 import uic
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtWidgets import QApplication, QWidget, QSystemTrayIcon, QMenu, QMainWindow, QTextEdit, QPushButton, \
    QInputDialog, QLabel
import sys
from PyQt6 import QtCore, QtWidgets, QtGui


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        exitAction = QAction(QIcon('exit24.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')
        self.show()


class Ui2(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui2, self).__init__()
        uic.loadUi('uic.ui', self)

        self.pushButtonDownload = self.findChild(QtWidgets.QPushButton, 'pushButtonDownload')
        self.pushButtonDownload.clicked.connect(self.download_images)

        self.show()

    async def download_image(self, session: aiohttp.ClientSession, url: str, filename: str):
        async with session.get(url) as response:
            with open(filename, 'wb') as f:
                while True:
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    f.write(chunk)

    async def download_images_async(self, urls: List[str]):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for i, url in enumerate(urls):
                filename = f"temp/image{i}.jpg"
                task = asyncio.create_task(self.download_image(session, url, filename))
                tasks.append(task)
            await asyncio.gather(*tasks)

    def download_images(self):
        os.makedirs("temp", exist_ok=True)

        n_images, ok = QInputDialog.getInt(self, "Download Images", "How many images do you want to download?", 10, 1,
                                           100)
        if not ok:
            return

        urls = []
        for i in range(n_images):
            url, ok = QInputDialog.getText(self, f"Download Images ({i + 1}/{n_images})",
                                           f"Enter URL for image {i + 1}")
            if not ok:
                return
            urls.append(url.strip())

        asyncio.run(self.download_images_async(urls))

    def how_many_images(self):
        value = self.spinBoxDelayHowMany.value()
        return value


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('uic.ui', self)

        self.pause = False

        self.setWindowTitle("My App")
        self.setWindowIcon(QtGui.QIcon("./src/images/icon.png"))
        # self.setStyle()
        self.resize(1280, 720)
        self.setMinimumSize(640, 480)
        self.setMaximumSize(1920, 1080)

        self.button1.clicked.connect(self.start)
        self.button2.clicked.connect(self.stop)

        layout = QtWidgets.QGridLayout()

        layout.addWidget(self.button1, 0, 0)
        layout.addWidget(self.button2, 1, 0)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    @staticmethod
    def init():
        app = QApplication([])
        window = Ui2()

        window.show()
        app.exec()


if __name__ == "__main__":
    Ui.init()


