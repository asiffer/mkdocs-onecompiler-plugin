import random

import pytest
from pydantic_core import ValidationError

from mkdocs_onecompiler_plugin.schema import OneCompiler


def test_schema():
    OneCompiler(lang="python")


def test_bad_schema():
    for f in OneCompiler.model_fields.keys():
        if f == "lang":
            continue
        try:
            # pass bad types to schema
            attrs = {f: random.randint(2, 100)}
            OneCompiler(lang="c", **attrs)
            pytest.fail(
                reason=f"an exception must raise because of "
                f"bad input ({f}: {attrs[f]})"
            )
        except ValidationError:
            pass
