from black import format_file_contents, Mode
from dataclasses import dataclass
from deephaven.plugin.object_type import (
    BidirectionalObjectType,
    MessageStream,
)
from typing import Any, List


@dataclass
class BlackFormatFileContents:
    mode: Mode
    fast: bool

    def invoke(self, src_contents: str) -> str:
        return format_file_contents(src_contents, fast=self.fast, mode=self.mode)


@dataclass
class BlackFormatFileContentsStream(MessageStream):
    _config: BlackFormatFileContents
    _connection: MessageStream

    def on_data(self, payload: bytes, references: List[Any]) -> None:
        self._connection.on_data(
            self._config.invoke(payload.decode("utf-8")).encode("utf-8")
        )
        return None

    def on_close(self) -> None:
        pass


class BlackObjectType(BidirectionalObjectType):
    @property
    def name(self) -> str:
        return "deephaven-black"

    def is_type(self, obj: Any) -> bool:
        return isinstance(obj, BlackFormatFileContents)

    def create_client_connection(
        self, obj: object, connection: MessageStream
    ) -> MessageStream:
        return BlackFormatFileContentsStream(obj, connection)
