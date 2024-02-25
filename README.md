# Pyrogram Clone Client Example

__This is just an example of a clone client in Pyrogram.__

## Commands
```markdown
- `/uclone <Session>`: For User Bots Cloning
- `/bclone <Token>`: For Bots Cloning
```

Follow this command format to use these commands in cloned clients.

```python
@Client.on_message(filters.command(["command"]) & filters.me)
async def example_cmd(client: Client, message: Message):
    # Your command logic here
```

__Note__: __This must be used to work.__

## Credits 🏅

- [The Dark](https://t.me/IkariS0_0)
- [Team X Devs](https://t.me/team_devsX)

<b>Special thanks to [Zaid](https://t.me/Timesisnotwaiting) for the base.</b>
