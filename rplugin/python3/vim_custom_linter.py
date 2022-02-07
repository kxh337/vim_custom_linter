import pynvim

@pynvim.plugin
class CustomLinter:

    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.command('TestParser')
    def testcommand():
        self.nvim.command('echo Test')

