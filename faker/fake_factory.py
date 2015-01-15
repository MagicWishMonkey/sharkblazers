from django.conf import settings
from sharkblazers import util
import random






class Factory(object):
    LETTERS = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    NUMBERS = ["0","1","2","3","4","5","6","7","8","9"]
    prefixes = ["Mr.", "Mrs.", "Ms.", "Dr."]
    suffixes = ["Jr.", "Esq."]
    tags = ["Personal", "Business", "Work", "Office", "Home", "Cell", "Fax", "Mobile"]

    __first_names__ = None
    __last_names__ = None
    __titles__ = None
    __companies__ = None
    __phones__ = None
    __domains__ = None
    __locations__ = None

    def __init__(self):
        if Factory.__first_names__ is None:
            labels = util.io.read_file(util.io.path_concat(settings.PROJECT_PATH, "../resources/first_names.txt"))
            labels = labels.split("\n")
            while labels[len(labels) - 1] == "":
                labels = labels[0:len(labels) - 1]
            Factory.__first_names__ = labels

            labels = util.io.read_file(util.io.path_concat(settings.PROJECT_PATH, "../resources/last_names.txt"))
            labels = labels.split("\n")
            while labels[len(labels) - 1] == "":
                labels = labels[0:len(labels) - 1]
            Factory.__last_names__ = labels

            labels = util.io.read_file(util.io.path_concat(settings.PROJECT_PATH, "../resources/titles.txt"))
            labels = labels.split("\n")
            while labels[len(labels) - 1] == "":
                labels = labels[0:len(labels) - 1]
            Factory.__titles__ = labels

            labels = util.io.read_file(util.io.path_concat(settings.PROJECT_PATH, "../resources/companies.txt"))
            labels = labels.split("\n")
            while labels[len(labels) - 1] == "":
                labels = labels[0:len(labels) - 1]
            Factory.__companies__ = labels

            labels = util.io.read_file(util.io.path_concat(settings.PROJECT_PATH, "../resources/phones.txt"))
            labels = labels.split("\n")
            while labels[len(labels) - 1] == "":
                labels = labels[0:len(labels) - 1]
            Factory.__phones__ = labels

            labels = util.io.read_file(util.io.path_concat(settings.PROJECT_PATH, "../resources/domains.txt"))
            labels = labels.split("\n")
            while labels[len(labels) - 1] == "":
                labels = labels[0:len(labels) - 1]
            Factory.__domains__ = labels

            labels = util.io.read_file(util.io.path_concat(settings.PROJECT_PATH, "../resources/locations.txt"))
            labels = labels.split("\n")
            while labels[len(labels) - 1] == "":
                labels = labels[0:len(labels) - 1]
            Factory.__locations__ = labels

        self.firsts = Factory.__first_names__
        self.lasts = Factory.__last_names__
        self.titles = Factory.__titles__
        self.companies = Factory.__companies__
        self.phones = Factory.__phones__
        self.domains = Factory.__domains__
        self.locations = Factory.__locations__


    def create(self):
        name = {
            "first": self.get_first_name(),
            "last": self.get_last_name()
        }
        if self.__tossup__(4):
            name["middle"] = self.get_middle_name()

        o = {}
        o["name"] = name
        if self.__tossup__(2):
            o["title"] = self.get_title()
        if self.__tossup__(2):
            o["company"] = self.get_company()

        bias = 1
        while self.__tossup__(bias):
            bias = (bias * 2)
            phone = {"tag": self.get_tag(), "label": self.get_phone()}
            try:
                o["phones"].append(phone)
            except KeyError:
                o["phones"] = [phone]


        bias = 1
        while self.__tossup__(bias):
            bias = (bias * 2)
            email = {"tag": self.get_tag(), "label": self.get_email(name)}
            try:
                o["emails"].append(email)
            except KeyError:
                o["emails"] = [email]

        return o

    def get_first_name(self):
        labels = self.firsts
        label = random.choice(labels)
        return label

    def get_last_name(self):
        labels = self.lasts
        label = random.choice(labels)
        return label

    def get_middle_name(self):
        if self.__tossup__(4) is False:
            initial = random.choice(Factory.LETTERS)
            return "%s." % initial.upper()

        name = self.get_first_name()
        name = name.split(" ")[0]
        if self.__tossup__() is True:
            name = self.__mutate__(name)
        return name

    def get_title(self):
        labels = self.titles
        label = random.choice(labels)
        return label

    def get_company(self):
        labels = self.companies
        label = random.choice(labels)
        return label

    def get_phone(self):
        labels = self.phones
        label = random.choice(labels)
        return label

    def get_domain(self):
        labels = self.domains
        label = random.choice(labels)
        return label

    def get_location(self):
        labels = self.locations
        label = random.choice(labels)
        return label

    def get_tag(self):
        tags = Factory.tags
        tag = random.choice(tags)
        if self.__tossup__() is True:
            if self.__tossup__() is True:
                tag = tag.lower()
            elif self.__tossup__(3) is True:
                tag = tag.upper()
        return tag

    def get_email(self, *name):
        domain = self.get_domain()
        first, last = None, None
        if len(name) > 0:
            first, last = name[0]["first"], name[0]["last"]
        else:
            first, last = self.get_first_name(), self.get_last_name()

        first, last = util.to_ascii(first).lower(), util.to_ascii(last).lower()
        #first = first.replace(",", "").replace("(", "").replace(")", "").replace("@", "")
        #last = last.replace(",", "").replace("(", "").replace(")", "").replace("@", "")
        label = None
        if self.__tossup__() is True:
            if self.__tossup__() is True:
                label = "%s.%s" % (first, last)
            else:
                label = "%s%s" % (first, last)
        elif self.__tossup__() is True:
            label = "%s%s" % (first[0], last)
        elif self.__tossup__() is True:
            label = "%s" % first
        elif self.__tossup__() is True:
            label = "%s" % last
        else:
            numbers = self.__random_numbers__()
            numbers = numbers[0:3]
            if self.__tossup__() is True:
                label = "%s.%s%s" % (first, last, numbers)
            elif self.__tossup__() is True:
                label = "%s%s" % (first, numbers)
            else:
                label = "%s%s" % (last, numbers)

        label = label.replace(",", "").replace("(", "").replace(")", "").replace("@", "")
        label = label.replace(" ", ".")
        while label.find("..") > -1:
            label = label.replace("..", ".")
        email = "%s@%s" % (label, domain)
        return email

    def __tossup__(self, *bias):
        if len(bias) == 0 or bias[0] < 2:
            return True if random.randrange(0, 2) == 1 else False

        bias = bias[0]
        if bias < 0:
            bias = (-1 * bias)
            for x in xrange(bias):
                if random.randrange(0, 2) == 1:
                    return True

            return False

        bias = (bias + 1)
        return True if random.randrange(0, bias) == 1 else False

    def __mutate__(self, txt, *amount):
        amount = 1 if len(amount) == 0 else amount[0]
        letters = Factory.LETTERS
        buffer = [c for c in txt]
        indexes = []
        bias, swaps = 1, 0
        for x, c in enumerate(buffer):
            if x == 0:
                continue

            if self.__tossup__(bias) is True:
                indexes.append(x)
                swaps = (swaps + 1)
                bias = (bias * 2) if swaps < amount else (bias * 3)

        for ix in indexes:
            # c = buffer[ix]
            swap = random.choice(letters).lower()
            buffer[x] = swap

        txt = "".join(buffer)
        return txt

    def __random_numbers__(self, *count):
        count = 8 if len(count) == 0 else count[0]
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        buffer = []
        for x in xrange(count):
            number = random.choice(numbers)
            buffer.append(str(number))

        txt = "".join(buffer)
        return txt


        # from fusion import tools
# import random
#
#
# class Faker(object):
#     __instance__ = None
#     LETTERS = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#     NUMBERS = ["0","1","2","3","4","5","6","7","8","9"]
#     prefixes = ["Mr.", "Mrs.", "Ms.", "Dr."]
#     suffixes = ["Jr.", "Esq."]
#     tags = ["Personal", "Business", "Work", "Office", "Home", "Cell", "Fax", "Mobile"]
#
#     def __init__(self, db, *formatter):
#         if Faker.__instance__ is None:
#             Faker.__instance__ = self
#
#         self.db = db
#         self.formatter = None
#         self.counter = 1
#
#         if len(formatter) > 0:
#             self.connect_formatter(formatter[0])
#
#         tables = self.db.tables()
#         for table_name in tables:
#             if table_name == "sequences":
#                 continue
#
#             alias = table_name
#             max = self.db.scalar("SELECT id FROM %s ORDER BY id DESC;" % table_name)
#             if table_name.find("_names") > -1:
#                 alias = table_name.split("_")[0]
#                 alias = "{table}s".format(table=alias)
#             self.__dict__[alias] = (table_name, 1, max)
#
#     @property
#     def formatters(self):
#         from faker import formatters
#         return formatters
#         #return __formatters__
#
#     def connect_formatter(self, formatter):
#         formatter = tools.curry(formatter, self)
#         self.formatter = formatter
#         return self
#
#     def coin_flip(self, *bias):
#         if len(bias) == 0 or bias[0] < 2:
#             return True if random.randrange(0, 2) == 1 else False
#
#         bias = bias[0]
#         if bias < 0:
#             bias = (-1 * bias)
#             for x in xrange(bias):
#                 if random.randrange(0, 2) == 1:
#                     return True
#
#             return False
#
#         bias = (bias + 1)
#         return True if random.randrange(0, bias) == 1 else False
#
#
#     def get_first_name(self):
#         schema = self.firsts
#         a, b = schema[1], schema[2]
#
#         while True:
#             id = random.randint(a, b)
#             label = self.db.scalar("SELECT label FROM %s WHERE id=%s;" % (schema[0], str(id)))
#             try:
#                 int(label)
#             except:
#                 return label
#
#     def get_last_name(self):
#         schema = self.lasts
#         a, b = schema[1], schema[2]
#         id = random.randint(a, b)
#         #label = self.db.scalar("SELECT label FROM %s WHERE id=%s;" % (schema[0], str(id)))
#         #return label
#         while True:
#             id = random.randint(a, b)
#             label = self.db.scalar("SELECT label FROM %s WHERE id=%s;" % (schema[0], str(id)))
#             try:
#                 int(label)
#             except:
#                 return label
#
#     def get_middle_name(self):
#         if self.coin_flip(2) is False:
#             return None
#
#         if self.coin_flip(2) is True:
#             initial = random.choice(Faker.LETTERS)
#             return "%s." % initial.upper()
#         name = self.get_first_name()
#         name = name.split(" ")[0]
#         if self.coin_flip() is True:
#             name = self.mutate(name)
#         return name
#
#     def get_prefix(self):
#         if self.coin_flip(3) is False:
#             return None
#
#         prefix = random.choice(Faker.prefixes)
#         return prefix
#
#     def get_suffix(self):
#         if self.coin_flip(4) is False:
#             return None
#         suffix = random.choice(Faker.suffixes)
#         return suffix
#
#     def get_domain(self):
#         schema = self.domains
#         a, b = schema[1], schema[2]
#         id = random.randint(a, b)
#         label = self.db.scalar("SELECT label FROM %s WHERE id=%s;" % (schema[0], str(id)))
#         return label
#
#     def get_phone(self):
#         schema = self.phones
#         a, b = schema[1], schema[2]
#         id = random.randint(a, b)
#         label = self.db.scalar("SELECT label FROM %s WHERE id=%s;" % (schema[0], str(id)))
#         label = self.scramble_phone_number(label)
#         return label
#
#
#     def get_city(self):
#         schema = self.cities
#         a, b = schema[1], schema[2]
#         id = random.randint(a, b)
#         record = self.db.record("SELECT label, city, state, zipcode, area_codes FROM %s WHERE id=%s;" % (schema[0], str(id)))
#         area_codes = record["area_codes"]
#         area_codes = area_codes.split(",")
#         record["area_codes"] = area_codes
#         return record
#
#     def get_title(self):
#         schema = self.titles
#         a, b = schema[1], schema[2]
#         id = random.randint(a, b)
#         label = self.db.scalar("SELECT label FROM %s WHERE id=%s;" % (schema[0], str(id)))
#         return label
#
#     def get_company(self):
#         schema = self.companies
#         a, b = schema[1], schema[2]
#         id = random.randint(a, b)
#         label = self.db.scalar("SELECT label FROM %s WHERE id=%s;" % (schema[0], str(id)))
#         return label
#
#     def random_numbers(self, *count):
#         count = 8 if len(count) == 0 else count[0]
#         numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#         buffer = []
#         for x in xrange(count):
#             number = random.choice(numbers)
#             buffer.append(str(number))
#
#         txt = "".join(buffer)
#         return txt
#
#     def get_address(self):
#         city = self.get_city()
#         address = {
#             "city": city["city"],
#             "zipcode": city["zipcode"]
#         }
#         if self.coin_flip() is True:
#             address["state"] = city["state"]
#
#         if self.coin_flip() is True:
#             street_number = self.random_numbers(8)
#
#             while street_number[0] == "0":
#                 street_number = street_number[1:]
#                 if street_number[0] != "0":
#                     break
#                 street_number = self.random_numbers(8)
#
#             while len(street_number) > 4:
#                 street_number = street_number[0:len(street_number) - 1]
#
#             if self.coin_flip() is True:
#                 street_number = street_number[0:len(street_number) - 1]
#
#             street_number = "".join(street_number)
#             street_name = self.get_first_name() if self.coin_flip() else self.get_last_name()
#             street_name = street_name.split(" ")[0]
#             street = "%s %s" % (street_number, street_name)
#             if self.coin_flip() is True:
#                 if self.coin_flip() is True:
#                     street = "%s Blvd" % street
#                 elif self.coin_flip() is True:
#                     street = "%s Ave." % street
#                 elif self.coin_flip() is True:
#                     street = "%s Ln." % street
#                 else:
#                     street = "%s St." % street
#
#             address["street"] = street
#
#         if self.coin_flip(2) is True:
#             unit_number = self.random_numbers()
#             while len(unit_number) > 4:
#                 unit_number = unit_number[0:len(unit_number) - 1]
#
#             if self.coin_flip() is True:
#                 unit_number = unit_number[0:len(unit_number) - 1]
#
#             if self.coin_flip() is True:
#                 unit_number = unit_number[0:len(unit_number) - 1]
#
#             unit = "#".join(unit_number) if self.coin_flip() else "Ste: %s" % "".join(unit_number)
#             address["unit"] = unit
#
#         label = []
#         try:
#             label.append(address["street"])
#         except KeyError:
#             pass
#
#         try:
#             label.append(address["unit"])
#         except KeyError:
#             pass
#
#         try:
#             label.append("%s, %s %s" % (address["city"], address["state"], address["zipcode"]))
#         except KeyError:
#             label.append("%s %s" % (address["city"], address["zipcode"]))
#
#         label = "\n".join(label)
#         address["label"] = label
#         if self.coin_flip() is True:
#             tag = self.get_address_tag()
#             address["tag"] = tag
#
#         return address
#
#     def get_email(self, *name):
#         domain = self.get_domain()
#         first, last = None, None
#         if len(name) > 0:
#             first, last = name[0]["first"], name[0]["last"]
#         else:
#             first, last = self.get_first_name(), self.get_last_name()
#
#         first, last = tools.to_ascii(first).lower(), tools.to_ascii(last).lower()
#         #first = first.replace(",", "").replace("(", "").replace(")", "").replace("@", "")
#         #last = last.replace(",", "").replace("(", "").replace(")", "").replace("@", "")
#         label = None
#         if self.coin_flip() is True:
#             if self.coin_flip() is True:
#                 label = "%s.%s" % (first, last)
#             else:
#                 label = "%s%s" % (first, last)
#         elif self.coin_flip() is True:
#             label = "%s%s" % (first[0], last)
#         elif self.coin_flip() is True:
#             label = "%s" % first
#         elif self.coin_flip() is True:
#             label = "%s" % last
#         else:
#             numbers = self.random_numbers()
#             numbers = numbers[0:3]
#             if self.coin_flip() is True:
#                 label = "%s.%s%s" % (first, last, numbers)
#             elif self.coin_flip() is True:
#                 label = "%s%s" % (first, numbers)
#             else:
#                 label = "%s%s" % (last, numbers)
#
#         label = label.replace(",", "").replace("(", "").replace(")", "").replace("@", "")
#         label = label.replace(" ", ".")
#         while label.find("..") > -1:
#             label = label.replace("..", ".")
#         email = "%s@%s" % (label, domain)
#         return email
#
#     def get_email_tag(self):
#         tags = Faker.tags
#         tags = tags[0:len(tags) - 3]
#         tag = random.choice(tags)
#         if self.coin_flip() is True:
#             if self.coin_flip() is True:
#                 tag = tag.lower()
#             elif self.coin_flip(3) is True:
#                 tag = tag.upper()
#         return tag
#
#     def get_tag(self):
#         tags = Faker.tags
#         tag = random.choice(tags)
#         if self.coin_flip() is True:
#             if self.coin_flip() is True:
#                 tag = tag.lower()
#             elif self.coin_flip(3) is True:
#                 tag = tag.upper()
#         return tag
#
#     def get_address_tag(self):
#         return self.get_email_tag()
#
#     def build_name(self, **kwd):
#         first = kwd.get("first", self.get_first_name())
#         last = kwd.get("last", self.get_last_name())
#         if first is None:
#             first = self.get_first_name()
#         if last is None:
#             last = self.get_last_name()
#
#         middle = self.get_middle_name()
#         pfx = None#self.get_prefix()
#         sfx = self.get_suffix()
#         label = "%s %s" % (first, last) if middle is None else "%s %s %s" % (first, middle, last)
#         if pfx is not None:
#             label = "%s %s" % (pfx, label)
#         if sfx is not None:
#             label = "%s %s" % (label, sfx)
#
#         name = {
#             "first": first,
#             "last": last,
#             "label": label
#         }
#         if middle is not None:
#             name["middle"] = middle
#         if pfx is not None:
#             name["prefix"] = pfx
#         if sfx is not None:
#             name["suffix"] = sfx
#         return name
#
#     def scramble_phone_number(self, txt):
#         numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#         swaps = 0
#         buffer = []
#         for x, c in enumerate(txt):
#             if x < 6:
#                 buffer.append(c)
#                 continue
#             if c.isdigit() is True:
#                 if swaps > 1:
#                     if self.coin_flip() is False:
#                         buffer.append(c)
#                         continue
#                 swaps = (swaps + 1)
#                 digit = random.choice(numbers)
#                 c = str(digit)
#             buffer.append(c)
#
#         txt = "".join(buffer)
#         return txt
#
#     def mutate(self, txt, *amount):
#         amount = 1 if len(amount) == 0 else amount[0]
#         letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#         buffer = [c for c in txt]
#         indexes = []
#         bias, swaps = 1, 0
#         for x, c in enumerate(buffer):
#             if x == 0:
#                 continue
#
#             if self.coin_flip(bias) is True:
#                 indexes.append(x)
#                 swaps = (swaps + 1)
#                 bias = (bias * 2) if swaps < amount else (bias * 3)
#
#         for ix in indexes:
#             c = buffer[ix]
#             swap = random.choice(letters).lower()
#             buffer[x] = swap
#
#         txt = "".join(buffer)
#         return txt
#
#
#     def append_email(self, contact, label, *tag):
#         tag = None if len(tag) == 0 else tag[0]
#         lst = contact.get("emails", None)
#         if lst is None:
#             lst = []
#             contact["emails"] = lst
#         o = {"label": label} if tag is None else {"label": label, "tag": tag}
#         lst.append(o)
#         return self
#
#     def append_phone(self, contact, label, *tag):
#         tag = None if len(tag) == 0 else tag[0]
#         lst = contact.get("phones", None)
#         if lst is None:
#             lst = []
#             contact["phones"] = lst
#         o = {"label": label} if tag is None else {"label": label, "tag": tag}
#         lst.append(o)
#         return self
#
#
#     def create(self, *format, **kwd):
#         first, last = kwd.get("first", None), kwd.get("last", None)
#         domain = kwd.get("domain", None)
#         name = self.build_name(first=first, last=last) if len(kwd) > 0 else self.build_name()
#         id = self.counter
#         self.counter = (self.counter + 1)
#         contact = {
#             "id": id,
#             "name": name
#         }
#
#         phones, emails, addresses = [], [], []
#         if kwd.get("emails", True) is True:
#             bias = 1
#             while self.coin_flip(bias) is True:
#                 bias = (bias + 1)
#                 email = self.get_email(name)
#                 tag = self.get_tag()
#                 emails.append({"label": email, "tag": tag})
#
#         if kwd.get("phones", True) is True:
#             bias = 1
#             while self.coin_flip(bias) is True:
#                 bias = (bias + 1)
#                 phone = self.get_phone()
#                 tag = self.get_tag()
#                 phones.append({"label": phone, "tag": tag})
#
#         if kwd.get("addresses", True) is True:
#             while self.coin_flip(3) is True:
#                 address = self.get_address()
#                 addresses.append(address)
#
#         if len(phones) > 0:
#             contact["phones"] = phones
#         if len(emails) > 0:
#             contact["emails"] = emails
#         if len(addresses) > 0:
#             contact["addresses"] = addresses
#
#         title = kwd.get("title", None)
#         if title is None:
#             if self.coin_flip(-1) is True:
#                 title = self.get_title()
#         if title is not None:
#             contact["title"] = title
#
#         company = kwd.get("company", None)
#         if company is None:
#             if self.coin_flip(-1) is True:
#                 company = self.get_company()
#         if company is not None:
#             contact["company"] = company
#
#         if domain is not None:
#             emails = contact.get("emails", None)
#             if emails:
#                 cnt = len(emails)
#                 if cnt == 0:
#                     cnt = 1
#                 for x in xrange(cnt):
#                     email = emails[x]
#                     username = email["label"].split("@")[0]
#                     email["label"] = "%s@%s" % (username, domain)
#
#
#         formatter = self.formatter if len(format) == 0 else format[0]
#         if formatter is not None:
#             contact = self.format(formatter, contact)
#         return contact
#
#     def format(self, fn, contact):
#         o = fn(contact)
#         return o if o is not None else contact
#
#     @staticmethod
#     def activate(db):
#         faker = Faker(db)
#         return faker
#
#     @staticmethod
#     def get(*formatter):
#         db = Faker.__instance__.db
#         faker = Faker(db, *formatter)
#         return faker