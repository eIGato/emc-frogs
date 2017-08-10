#!/usr/bin/env python3


import framework_mock as framework


class Frog(object):
    def __init__(self, step, start=0):
        self.step = step
        self.position = start

    def jump(self):
        self.position += self.step
        try:
            framework.press(self.position)
        except IndexError:
            self.position = None
        return self.position

    def finish(self):
        while self.jump():
            pass

    def __str__(self):
        return (' ' * (self.position - 1) + '&') if self.position else ''


frogs = [Frog(step) for step in range(1, 101)]


def main():
    print('All frogs are ready to start. Current lamp switches status:')
    print(framework.lamps)
    for i in range(100):
        for frog in frogs:
            old_position = frog.position
            if old_position is None:
                continue
            frog.jump()
            print('Frog #{} jumps from lamp #{} to lamp #{}:'.format(frog.step, old_position, frog.position))
            print(frog)
            print(framework.lamps)
    print('All frogs finished!')


if __name__ == '__main__':
    main()
