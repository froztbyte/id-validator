#!/usr/bin/python

"""
procedure to validate

a) add all but last odd digits together
b) create string of all even digits, multiply by 2
c) add digits of b's result
d) add c to a
e) subtract second digit of d from 10
f) the result must match the last digit of the input
     - if 2-digit result, use second digit
"""
import sys

if len(sys.argv) > 1:
    id = str(sys.argv[1])
else:
    print 'Please run this with ./id-validator.py <id number>'
    sys.exit(1)


demoid = '8404011234...'
if len(id) < len(demoid):
    print 'The input you provided is too short, validation failed'
    sys.exit(2)

a = sum([int(x) for x in id[1::2][:5]])
b = 2 * int(''.join([x for x in id[::2]]))
c = sum([int(x) for x in str(b)])
d = c + a
e = 10 - (d % 10)

if len(str(e)) > 1:
    f = str(e)[:-1]
else:
    f = e

if f == id[:-1]:
    print 'Success, your number %s validated!' % id
else:
    print 'Failure, your number "%s" failed to validate. "%s" would' \
          'have been correct' % (id, ''.join([id[:12], str(f)]))
