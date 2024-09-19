"""
Display remaining cards as app icon notification
"""

from aqt import mw, gui_hooks

if mw is None:
    raise TypeError("Main window is None!")


class Addon:
    """Main addon class"""

    def __init__(self) -> None:
        self._card_count: int = 0

    def get_card_count(self) -> int:
        """Obtain card count"""
        try:
            if mw.col is None:
                raise TypeError("Collection is None")

            scheduler = mw.col.sched
            count = sum(scheduler.counts())
            return count
        except:  # pylint: disable=bare-except
            return self._card_count

    def display_card_count(self) -> None:
        """Display the card count"""
        count = self.get_card_count()

        # Clamp value
        if count > 99:
            count = 100

        if count == self._card_count:
            return

        self._card_count = count
        mw.app.setBadgeNumber(self._card_count)


addon = Addon()


def display(*_) -> None:
    """Display card count"""
    addon.display_card_count()


gui_hooks.operation_did_execute.append(display)  # type: ignore
gui_hooks.focus_did_change.append(display)  # type: ignore
