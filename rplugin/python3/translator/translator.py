import neovim


@neovim.plugin
class Translator(object):
    def __init__(self, vim):
        """Initializes the translator plugin.

        :vim: Holds the vim instance.
        :returns: The translator instance.

        """
        self.vim = vim

    @neovim.command('TranslateLine', range='', nargs='*', sync=True)
    def translate_line(self, args, nvim_range):
        """Translates line-wise.

        :args: A list containing 2 elements: [<source>, <target>]
        :nvim_range: The range of Lines to translate.
        :returns: Nothing. But replaces the current or selected lines.

        """
        source = args[0]
        target = args[1]
        lines = self.vim.current.buffer[nvim_range[0]-1 : nvim_range[1]]
        translated_lines = [self.translate(source, target, line) for line in lines]
        self.vim.current.buffer[nvim_range[0]-1 : nvim_range[1]] = translated_lines

    def translate(self, source, target, string):
        """Translates the string from source to target language.

        :source: Source language identifier.
        :target: Target language identifier.
        :string: The string to translate.
        :returns: The translated string or -1.

        """
        from subprocess import run
        from subprocess import PIPE

        completed_process = run(["deepl", "-s", source, "-t", target, "translate", string], stdout=PIPE, encoding="utf-8")
        return completed_process.stdout.strip()
