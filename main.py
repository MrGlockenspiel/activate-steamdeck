import subprocess

class Plugin:
    # this is horrendous
    async def enable(self):
        subprocess.Popen(["gcc", "activate-steamdeck.c", "-o", "activate-steamdeck", "-lX11", "-lXfixes", "-lXinerama", "-lcairo", "-I/usr/include/cairo"])
        subprocess.Popen(["./activate-steamdeck"])

    # just when you thought it couldnt get worse
    async def disable(self):
        subprocess.Popen(["pkill", "-9", "activate-steamdeck"])

    # ran on plugin load
    async def _main(self):
        pass