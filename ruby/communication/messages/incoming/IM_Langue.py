from ruby.communication.messages.Incoming import Incoming
from ruby.utils.Language import Language


class IM_Langue(Incoming):
    tokens = [8, 2]

    def dispatch(self, Session, BufferArray):
        langueCode = BufferArray.readByte()
        Session.language = Language(langueCode)
