import gen
import pathlib

this_file = pathlib.PurePosixPath(
    pathlib.Path(__file__).relative_to(pathlib.Path().resolve())
)

target = "package.json"

content = {
    "dependencies": {"bootstrap": "5.3.7"},
    "description": f"This file ({target}) was generated from {this_file}",
    "license": "UNLICENSED",
    "name": "ellie.subtlecoolness.com",
    "private": True,
    "version": "1.0.0",
}

gen.gen(content, target)
