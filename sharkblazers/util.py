try:
    import simplejson as __json__
except:
    #default to basic json library
    import json as __json__
import os
import sys
import csv
import codecs
import datetime
import dateutil.parser
from sharkblazers.utilities.wrapper import Wrapper


def extract_ip_address(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    except:
        return None


def wrap(**kwd):
    return Wrapper.create(**kwd)


def csv_to_list(csv_path):
    if os.path.exists(csv_path) is False:
        return []

    csv.field_size_limit(sys.maxsize)

    records = []
    with open(csv_path, 'r') as csv_file:
        dialect = csv.Sniffer().sniff(csv_file.read(1024))
        csv_file.seek(0)
        reader = csv.DictReader(csv_file, dialect=dialect)
        for row in reader:
            records.append(row)

    return records



def json(obj, indent=None, sort_keys=True, pretty=False):
    """Convert the object instance into a json blob."""
    assert obj is not None, "The input parameter is null!"

    try:
        if indent:
            return __json__.dumps(obj, check_circular=False, sort_keys=sort_keys, indent=indent)
        else:
            if pretty is True:
                return __json__.dumps(obj, check_circular=False, sort_keys=sort_keys, indent=2)
            return __json__.dumps(obj, check_circular=False, sort_keys=sort_keys)
    except Exception, ex:
        message = "Unable to encode the object to json-> %s" % ex.message
        raise Exception(message)


def unjson(data, silent=False):
    """Convert the json blob into an object instance."""
    assert data is not None, "The input parameter is null!"

    if silent is True:
        try:
            txt = data.strip()
            pfx, sfx = txt[0], txt[len(txt) - 1]
            if pfx == "[" and sfx == "]" or pfx == "{" and sfx == "}":
                try:
                    return __json__.loads(data, strict=False)
                except:
                    return None
            return None
        except:
            return None

    try:
        return __json__.loads(data, strict=False)
    except Exception, ex:
        message = "Unable to decode the json object-> %s" % ex.message
        raise Exception(message)


def timestamp():
    """Return a datetime instance representing the current date/time"""
    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return dt


def now():
    """Return a datetime instance"""
    return datetime.datetime.now()


def parse_date(txt):
    """Parse the date string"""
    try:
        return dateutil.parser.parse(txt)
    except Exception, ex:
        raise Exception("Invalid date format-> '%s' could not be parsed.\n%s" % (txt, ex.message))


def to_ascii(txt):
    if txt is None or not isinstance(txt, basestring):
        return txt
    try:
        return txt.encode("ascii", "ignore")
    except Exception, ex:
        raise ex


class io:
    @staticmethod
    def path_concat(uri, relative):
        """Find the normalized relative path for the given uris"""
        path = os.path.join(uri, relative)
        path = os.path.normpath(path)
        return path

    @staticmethod
    def read_file(path, text=True, fn=None):
        if text is True:
            with codecs.open(path, "r", "utf-8") as f:
                data = f.read()
                if fn is not None:
                    data = fn(data)
                return data
        with open(path, "rb") as f:
            data = f.read()
            if fn is not None:
                data = fn(data)
            return data

    @staticmethod
    def exists(path):
        if not os.path.exists(path):
            return False
        return True

