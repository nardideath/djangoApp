import uuid


def get_random_uuid(delimiter=False):
    id = "%s" % uuid.uuid4()
    if not delimiter:
        id = id.replace("-","")
    return id


def get_big_random_uuid(delimiter=False):
    id = "%s" % uuid.uuid4()
    id2 = "%s" % uuid.uuid4()
    if not delimiter:
        id = id.replace("-","")
        id2 = id2.replace("-", "")
    return "%s%s" % (id, id2)


def get_small_random_uuid():
    id = "%s" % uuid.uuid4()
    return id.split("-")[-1]

