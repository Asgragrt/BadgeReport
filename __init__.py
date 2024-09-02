# import the main window object (mw) from aqt
from aqt import mw

# import all of the Qt GUI library
from aqt.qt import *

from aqt import gui_hooks

guiApplication = QGuiApplication.instance()


cardCount = 0


def getRemainingCardCount() -> int:
    try:
        scheduler = mw.col.sched
        count = sum(scheduler.counts())
        return count
    except:
        return cardCount


def displayCardCount(*_) -> None:
    global cardCount

    newCount = getRemainingCardCount()

    # Clamp value
    if newCount > 99:
        newCount = 100

    if newCount == cardCount:
        return

    cardCount = newCount
    guiApplication.setBadgeNumber(cardCount)


gui_hooks.operation_did_execute.append(displayCardCount)
gui_hooks.focus_did_change.append(displayCardCount)
