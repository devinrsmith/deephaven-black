import pathlib
import importlib.metadata
import importlib.resources
from deephaven.plugin.js import JsPlugin


class BlackJs(JsPlugin):
    def path(self) -> pathlib.Path:
        with importlib.resources.as_file(
            importlib.resources.files(__package__).joinpath("_data")
        ) as tmp_path:
            data_path = tmp_path
        if not data_path.exists():
            raise Exception(
                f"Package is not installed in a normal python filesystem, '{data_path}' does not exist"
            )
        return data_path

    @property
    def name(self) -> str:
        return "deephaven-black"

    @property
    def version(self) -> str:
        return importlib.metadata.version("deephaven-black")

    @property
    def main(self) -> str:
        # todo
        return "index.js"
