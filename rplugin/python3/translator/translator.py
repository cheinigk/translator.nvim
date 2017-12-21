class TranslatorMonad(object):

    """Translates strings."""

    def __init__(self, string):
        """Initializes a translator instance.

        :string: The string to be translated.

        """
        self._string = string

    def translate(self, source, target):
        """Translates the string from source to target language.

        :source: Source language.
        :target: Target language.
        :returns: TranslatorMonad with translated string.

        """
        # TODO: Use deepl jsonrpc API directly from within python and not this subprocess non-sense.
        import deepl
        deepl.translate(self._string, source=source, target=target)
        translated_string = completed_process.stdout.strip()
        return TranslatorMonad(translated_string)

    def result(self):
        """Returns the string that is held by the TranslatorMonad.

        :returns: The string property.

        """
        return self._string
