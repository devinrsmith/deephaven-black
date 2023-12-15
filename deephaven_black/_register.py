from ._object_type import BlackObjectType
from ._js import BlackJs
from deephaven.plugin import Registration, Callback


class BlackRegistration(Registration):
    @classmethod
    def register_into(cls, callback: Callback) -> None:
        callback.register(BlackObjectType)
        callback.register(BlackJs)
