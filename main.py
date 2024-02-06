import abc
from typing import Optional


# Interfaces

class WordVersion(abc.ABC):
    """Word implementation"""

    @property
    @abc.abstractmethod
    def version(self) -> str:
        ...


class WidgetType(abc.ABC):
    """Widget implementation"""

    @property
    @abc.abstractmethod
    def name(self) -> str:
        ...


class Test(abc.ABC):
    """Test Abstraction"""

    def __init__(self, word_impl: WordVersion, widget_impl: WidgetType):
        self.word_impl = word_impl
        self.widget_impl = widget_impl

    def test(self):
        print(f"{self.widget_impl.name} {self.word_impl.version}")


class WordTestAbstractFactory(abc.ABC):

    @abc.abstractmethod
    def create_panel_test(self) -> Test:
        ...

    @abc.abstractmethod
    def create_text_test(self) -> Test:
        ...

    @abc.abstractmethod
    def create_button_test(self) -> Test:
        ...


# Impls

class Word90(WordVersion):

    @property
    def version(self) -> str:
        return "Word90"


class Word00(WordVersion):

    @property
    def version(self) -> str:
        return "Word00"


class Word10(WordVersion):

    @property
    def version(self) -> str:
        return "Word10"


class Word24(WordVersion):

    @property
    def version(self) -> str:
        return "Word24"


class PanelWidget(WidgetType):

    @property
    def name(self) -> str:
        return "Panel"


class TextWidget(WidgetType):

    @property
    def name(self) -> str:
        return "TextBox"


class ButtonWidget(WidgetType):

    @property
    def name(self) -> str:
        return "Button"


# Factories

class Word90TestFactory(WordTestAbstractFactory):

    def create_panel_test(self) -> Test:
        return Test(Word90(), PanelWidget())

    def create_text_test(self) -> Test:
        return Test(Word90(), TextWidget())

    def create_button_test(self) -> Test:
        return Test(Word90(), ButtonWidget())


class Word00TestFactory(WordTestAbstractFactory):

    def create_panel_test(self) -> Test:
        return Test(Word00(), PanelWidget())

    def create_text_test(self) -> Test:
        return Test(Word00(), TextWidget())

    def create_button_test(self) -> Test:
        return Test(Word00(), ButtonWidget())


class Word10TestFactory(WordTestAbstractFactory):

    def create_panel_test(self) -> Test:
        return Test(Word10(), PanelWidget())

    def create_text_test(self) -> Test:
        return Test(Word10(), TextWidget())

    def create_button_test(self) -> Test:
        return Test(Word10(), ButtonWidget())


class Word24TestFactory(WordTestAbstractFactory):

    def create_panel_test(self) -> Test:
        return Test(Word24(), PanelWidget())

    def create_text_test(self) -> Test:
        return Test(Word24(), TextWidget())

    def create_button_test(self) -> Test:
        return Test(Word24(), ButtonWidget())


class WordTestAbstractFactoryFactory:
    def __init__(self):
        self.instance_count_90 = 0
        self.instance_count_00 = 0
        self.instance_count_10 = 0
        self.instance_count_24 = 0

    def get_factory(self, version_str: str) -> Optional[WordTestAbstractFactory]:
        """Gets a test factory for a given word version. Returns None if the test has been run twice already."""
        match version_str:
            case "Word90":
                if self.instance_count_90 == 2:
                    print("Word90 used twice already!")
                    return None
                else:
                    self.instance_count_90 += 1
                    return Word90TestFactory()
            case "Word00":
                if self.instance_count_00 == 2:
                    print("Word00 used twice already!")
                    return None
                else:
                    self.instance_count_00 += 1
                    return Word00TestFactory()
            case "Word10":
                if self.instance_count_10 == 2:
                    print("Word10 used twice already!")
                    return None
                else:
                    self.instance_count_10 += 1
                    return Word10TestFactory()
            case "Word24":
                if self.instance_count_24 == 2:
                    print("Word24 used twice already!")
                    return None
                else:
                    self.instance_count_24 += 1
                    return Word24TestFactory()


if __name__ == "__main__":
    fac = WordTestAbstractFactoryFactory()

    with open('example.txt') as file:
        for line in file.readlines():
            line = line.strip()

            maybe_factory = fac.get_factory(line)

            if maybe_factory:
                panel = maybe_factory.create_panel_test()
                button = maybe_factory.create_button_test()
                text = maybe_factory.create_text_test()

                panel.test()
                button.test()
                text.test()
