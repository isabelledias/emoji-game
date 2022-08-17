import setuptools

VERSION = '0.0.2' 
DESCRIPTION = 'Emoji Game'

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='emoji_game',
    version=VERSION,
    author='Isabelle Dias',
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/isabelledias/emoji-game',
    license='GNU General Public License',
    packages=['emoji_game'],
    install_requires=['emoji'], # add any additional packages that 
                                   # needs to be installed along with your package.
)
