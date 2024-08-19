# import the main window object (mw) from aqt
from aqt import mw

# import all of the Qt GUI library
from aqt.qt import *

from aqt import gui_hooks

guiApplication = QGuiApplication.instance()


def getRemainingCardCount() -> int:
    # Get queued cards (new/learning cards)
    queuedCards = mw.col.sched.get_queued_cards()
    cardCount = queuedCards.new_count + queuedCards.learning_count

    # Get due cards
    cardCount += len(mw.col.find_cards("is:due"))
    return cardCount


def displayCardCount(*_) -> None:
    cardCount = getRemainingCardCount()
    guiApplication.setBadgeNumber(cardCount)


gui_hooks.operation_did_execute.append(displayCardCount)
