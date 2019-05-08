from oa.core.util import command_registry

from oa.modules.abilities.interact import say, play, mind
from oa.modules.abilities.other import read_news_feed, diagnostics, read_forecast
from oa.modules.abilities.other import say_day, say_last_command, say_time

kws = {}

command = command_registry(kws)

@command(["hello elsa", "hi elsa"])
def hello_world():
     say('Hi William')

@command("close assistant")
def close_assistant():
    play('beep_close.wav')
    mind('boot')

@command("who are you")
def who():
    say('Hi William, this is elsa')

@command(["list commands", "what can i say"])
def list_commands():
    say('- The currently available voice commands are:\n{}'.format(',\n'.join(kws.keys())))

@command("read world news")
def read_world_news():
    read_news_feed('https://www.reddit.com/r/worldnews/.rss', 'world')

@command("run diagnostics")
def run_diagnostics():
    diagnostics()

@command("sing a song")
def sing_a_song():
    play('daisy.wav')

@command("what day is it")
def what_day():
    say_day()

@command("what did I say")
def what_command():
    say_last_command('You just said:')

@command("what is the weather")
def what_weather():
    read_forecast()

@command("what time is it")
def what_time():
    say_time()

@command(["thanks", "thank you"])
def thank_you():
     say("you're welcome, fucker")