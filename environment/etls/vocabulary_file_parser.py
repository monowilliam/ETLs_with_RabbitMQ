import utils

REF=0
NAME=1
URL=2
VERSION=3
DESCRIPTION=4
STATUS=5

def get_vocabulary(item):
    return dict(ref=utils.get_value_or_default(item[REF]),
                name=utils.get_value_or_default(item[NAME]),
                url=utils.get_value_or_default(item[URL]),
                version=utils.get_value_or_default(item[VERSION]),
                description=utils.get_value_or_default(item[DESCRIPTION]),
                status = utils.get_value_or_default(item[STATUS]))
