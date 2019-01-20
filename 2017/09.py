import logging

log = logging.getLogger()
logging.basicConfig(level=logging.DEBUG)

def read_garbage():
    pass

def append_garbage(state):
    if state:
        if state[0] == 'garbage':
            return state
    state.append('garbage')
    return state

def print_error(inp, i, msg):
    print "%s @ %s" % (msg, i)
    print inp
    print "".join(i * ' ') + '^'

def parser(inp):
    l = len(inp)
    i = 0
    level = 0
    s = 0
    sg = 0
    state = []
    garbage_in = 0
    ignored = 0
    while i < l:
        c = inp[i]
        log.debug("c[%05d] = '%s'", i, c)
        if c == '{':
#            i = read_group(inp, i+1)
            # in garbage?
            if not (state and state[-1] == 'garbage'):
                state.append('group')
                log.debug('opening group (@%s), current sum %s', i, s)
                level += 1
        elif c == '<':
#            i = read_garbage(inp, i+1)
            # already in garbage?
            if not (state and state[-1] == 'garbage'):
                garbage_in = i
                ignored = 0
                log.debug('opening garbage (@%s), currennt garbage sum %s', i, sg)
                state.append('garbage')
#                state = append_garbage(state)
        elif c == '!':
            # '!' + next character
            ignored += 2
            i += 1
        elif c == '>':
            if state and state[-1] == 'garbage':
                log.debug('garbage_in: %s, garbage_out: %s, ignored: %s', garbage_in, i, ignored)
                sg += max(i - garbage_in - 1, 0) - ignored
                log.debug('closing garbage (@%s), current garbage sum %s', i, sg)
                state.pop()
            else:
                print_error (inp, i, "error closing garbage")
                return
        elif c == '}':
            if state and state[-1] == 'group':
                log.debug('closing group (@%s) level %s, current sum %s', i, level, s)
                s += level
                level -= 1
                state.pop()
            elif state and state[-1] == 'garbage':
                # expected, do nothing
                pass
            else:
                print_error (inp, i, "error closing group")
                return
        else:
            # some character
            pass
 #       log.debug("state: %s", state)
        i += 1

    return s, sg


with open("09-input", "r") as f:
    inp = f.read().splitlines()[0]

