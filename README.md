# PWRBot (In Development)
Music bot for FAZuH's private discord server PWR.
MIT License. Meaning you can do whatever the hell you want with it.

# TODO
## Add these commands
### playback: commands for controlling the queue
- **play** <query: string>: `play a song (link/title)`
- **search** <query: string>: `search available music by query and select (link/title) -> (select option)`
- **skip**: `go to next song in queue`
- **previous**: `go to previously played song`
- **goto** <destination: integer>: `skip to a specific song in queue`

### song state: commands for controlling currently playing song
- **pause**: `toggles pause for current song`
- **volume** <vol: integer>: `changes volume`
- **replay**: `go to the start of current song`
- **nowplaying**: `shows current song`

### queue state: commands for modifying the queue
- **move** <source: integer> <destination: integer> : `move songs between queue`
- **shuffle**: `shuffles the queue`
- **reverse**: `reverses the queue`
- **autoqueue**: `toggles automatic queuing`
- **loop** [loop_times: integer] : `loops current song`
- **loopqueue**: `loops entire queue`
- **autopause**: `pauses song when no one is on vc`
- **stay**: `toggles bot leaving when no one is on vc`
- **recent**: `views 10 recently played song`

### playlist: commands for managing playlists
(all commands here starts with playlist)
- **list**: `view list of playlists`
- **view**: `view a playlist`
- **save** <name: string>: `saves current queue`
- **delete** <name: string>: `deletes a saved playlist`
- **add** <name: string> <link: string>: `adds a song to playlist`
- **remove** <name: string> <index: integer>: `removs a song from playlist`
- **share**: `creates a shareable id for sharing playlists`
- **copy** <share_id: integer>: `copies playlists from a shared id`
- **export**: `exports playlist in a .csv file`
- **import**: `imports a playlist from a valid .csv file`
- **merge** <to: string> <from: string>: `merges two playlists together`

### bot info
- **stats**: `basic bot stats`
- **top**: `views top played song on server`
- **topuser**: `views top queued song by an user`
