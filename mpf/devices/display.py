""" Implements a display in MPF """

from collections import deque

from mpf.system.device import Device


class Segment(Device):
    """Implements a segment display in a pinball machine.

    Args: Same as the Device parent class.
    """

    config_section = 'displays'
    collection = 'displays'
    class_label = 'display'

    def __init__(self, machine, name, config, collection=None, validate=True):
        super().__init__(machine, name, config, collection,
                         validate=validate, platform_section='displays')

        # for digit in self.config['digits']:
        #     self.machine.events.add_handler(self.config['positions'][position],
        #                                     self._position_event,
        #                                     position=position)

    def update_score(self, player=0, score=0):
        # for pos in self.display_size:
        #     self.display[pos] = score[pos]
        # set value of each digit in score to position on the display

    def reset(self, **kwargs):
        #  for each display registered set value to **kwargs else 0
        self.digits(self.config['reset_position'])


