try:
    from hashlib import md5
except ImportError:
    from md5 import md5
import base64
import re


_default_length = 16
_legacy_length = 8


def _raw_hash(label, password):
    """Generate a unique hash from a label and master password."""
    hash_object = md5()
    hash_object.update(password)
    hash_object.update(label)
    return base64.urlsafe_b64encode(hash_object.digest())


def create(label, master):
    """Create a password from a label and master password.
       Default password length is 16.
       If label is prefixed with '{n}*' (where {n} is a 1-2 digit number), n is used as length.
       If label is prefixed with *, length is 8 (backward compatibility mode).
       If you need the label to start with *, you should prefix it with 16* (or * for backward cmpatibility)
       If n>=23, you'll still get a 22 character long password (that's what md5 provides)
    """
    m = re.search('^(\d*)\*(.*)$',label)
    len_,label_ = m and m.groups() or (_default_length,label)
    len_ = int(len_ or _legacy_length)
    encoded_label = label_.encode("utf-8")
    encoded_master = master.encode("utf-8")
    hash_ = _raw_hash(encoded_label, encoded_master).replace('=','').decode("ascii")
    found = re.search(r"\d+", hash_)
    if not found:
        hash_ = '1' + hash_
    elif found.start() >= len_:
        hash_ = found.group() + hash_

    return hash_[:len_]
