from xtrabot import client, Var
from telethon import events
import re
xconfig = {}
func_name = {}

class Module():
    def __init__(self, cls):
        try:
            self.name
        except NameError:
            self.name = "untitled"
        cmd = cls.__dict__
        for i in cmd:
            if not cmd.endswith("cmd"):
                del cmd[i]
        for i in cmd:
            func = cmd[i]
            funcmd = re.compile("^."+func.__name__.replace("cmd", ""))
            try:
                func_name[self.name].append(func)
            except KeyError:
                func_name.update({self.name: [func]})
            self.xconfig = xconfig
            self.client = client
            self.config = Var
            client.add_event_handler(func, events.NewMessage(pattern=funcmd, outgoing=True))

    def addxconfig(self, name, value, about=""):
        def attr(e,n,v): #will work for any object you feed it, but only that object
            class tmp(type(e)):
                def attr(self,n,v):
                    setattr(self,n,v)
                    return self
            return tmp(e).attr(n,v)
        object=attr(value,about,about)
        self.xconfig.update({name: object1})
