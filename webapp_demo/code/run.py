#!/usr/bin/env python3

import logging
import sys
import signal

from app import app

logger = logging.getLogger('webapp_demo')
logging.basicConfig(stream=sys.stderr, level=getattr(logging, 'INFO'))


def handler(signum=None, frame=None):
    logger.info('Signal handler called with signal {}'.format(signum))
    logger.info('Stop webapp_demo')
    ## check if process is done
    # time.sleep(1)
    # logger.info('Wait done')
    sys.exit()


def main():
    for sign in [signal.SIGTERM, signal.SIGINT, signal.SIGHUP, signal.SIGQUIT]:
        signal.signal(sign, handler)

    app.run(host='0.0.0.0', debug=app.debug)


if __name__ == '__main__':
    main()
