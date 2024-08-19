# import the main window object (mw) from aqt
from aqt import mw

# import all of the Qt GUI library
from aqt.qt import *

from aqt import gui_hooks

guiApplication = QGuiApplication.instance()


def getRemainingCardCount() -> int:
    scheduler = mw.col.sched
    cardCount = sum(scheduler.counts())
    return cardCount


def displayCardCount(*_) -> None:
    cardCount = getRemainingCardCount()
    guiApplication.setBadgeNumber(cardCount)


gui_hooks.operation_did_execute.append(displayCardCount)
