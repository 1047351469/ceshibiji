import pytest, os, sys

sys.path.append(os.getcwd())

from base.base_yml import yaml_data_with_file


def data_with_key(key):
    return yaml_data_with_file("display_data", key)


class TestDisplay:

    @pytest.mark.parametrize("args", data_with_key("test_display_color"))
    def test_display_color(self, args):
        print("test_display_color")
        print(args["isred"])

    @pytest.mark.parametrize("args", data_with_key("test_display_text_size"))
    def test_display_text_size(self, args):
        print("test_display_text_size")
        print(args["width"])
        print(args["height"])