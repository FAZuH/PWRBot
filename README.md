# PWRBot (In Development)

Music bot for FAZuH's private discord server PWR. <br>
MIT License. Meaning you can do whatever the hell you want with it.


## Table of Contents
- [PWRBot (In Development)](#pwrbot-in-development)
  - [Table of Contents](#table-of-contents)
  - [Workflow](#workflow)
  - [Todo](#todo)
    - [Database](#database)
    - [Cogs](#cogs)

## Workflow
- [ ] Logger
- [ ] Cog
- [ ] Database
- [ ] Command
  - [ ] Admin
  - [ ] Help
  - [ ] Bot Info
  - [ ] Playback
  - [ ] Song
  - [ ] Queue
  - [ ] Playlist
- [ ] Lavalink
- [ ] Heartbeat
  - [ ] Report

## Todo

### Database

- **user**
    - user_id: `(PK, integer)`

- **user_playlist**: *Maps playlist_id with user_id*
    - playlist_id: `(integer)`
    - user_id: `(integer)`

- **playlist_info**
    - playlist_id: `(PK, integer)`
    - playlist_name: `(varchar 16)`
    - song_id: `(integer)`
    - date_added: `(datetime)`

- **song_info**
    - song_id: `(integer)`
    - song_link: `(varchar 255)`
    - song_name: `(varchar 255)`
    - song_duration: `(int, unsigned)`

### Cogs

**Playback**: Commands for controlling the queue
| Command | Description |
| ------ | ------ |
| play | *<query: string>* `play a song (link/title)` |
| search | *<query: string>* `search available music by query and select (link/title) -> (select option)` |
| skip | `go to next song in queue` |
| previous | `go to previously played song` |
| goto | *<destination: integer>* `skip to a specific song in queue` |

**Song**: Commands for controlling currently playing song
| Command | Description |
| ------ | ------ |
| pause | `toggles pause for current song` |
| volume | *<vol: integer>* `changes volume` |
| replay | `go to the start of current song` |
| nowplaying | `shows current song` |
| lyrics | `show current song lyrics` |

**Queue**: Commands for modifying the queue
| Command | Description |
| ------ | ------ |
| move | *<source: integer>* *<destination: integer>* `move songs between queue` |
| shuffle | `shuffles the queue` |
| reverse | `reverses the queue` |
| autoqueue | `toggles automatic queuing` |
| loop |*[loop_times: integer]* `loops current song` |
| loopqueue | `loops entire queue` |
| autopause | `pauses song when no one is on vc` |
| stay | `toggles bot leaving when no one is on vc` |
| recent | `views 10 recently played song` |

**Playlist**: Commands for managing playlists
| Command | Description |
| ------ | ------ |
| list |  `view list of playlists` |
| view |  `view a playlist` |
| save | *<name: string>* `saves current queue` |
| delete | *<name: string>* `deletes a saved playlist` |
| add | *<name: string>* *<link: string>* `adds a song to playlist` |
| remove | *<name: string>* *<index: integer>* `removs a song from playlist` |
| share |  `creates a shareable id for sharing playlists` |
| copy | *<share_id: integer>* `copies playlists from a shared id` |
| export |  `exports playlist in a .csv file` |
| import |  `imports a playlist from a valid .csv file` |
| merge | *<to: string>* *<from: string>* `merges two playlists together` |

**Bot Info**
| Command | Description |
| ------ | ------ |
| stats | `basic bot stats` |
| top | `views top played song on server` |
| topuser | `views top queued song by an user` |
