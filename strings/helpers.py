HELP_1 = """ **<u>admin commands:</u>**
just add **c** in the starting of the commands to use them for channel.
/pause : pause the current playing stream.
/resume : resume the paused stream.
/skip : skip the current playing stream and start streaming the next track in oueue.
/end or /stop : clears the oueue and end the current playing stream.
/player : get a interactive player panel.
/queue : shows the oueued tracks list."""

HELP_2 = """ **<u>auth users :</u>**
auth users can use admin rights in the bot without admin rights in the chat. [admins only]
/auth [username] : add a user to auth list of the bot.
/unauth [username] : remove a auth users from the auth users list.
/authusers : shows the auth users list of the group."""

HELP_3 = """<b>blacklist feature</b> [only for sudoers]
 **<u>blacklist chat :</u>**
/blacklistchat [chat id] : blacklist a chat from using the bot.
/whitelistchat [chat id] : whitelist the blacklisted chat.
/blacklistedchat : shows the list of blacklisted chats.
 **<u>block users:</u>**
/block [username or reply to a chutiya] : starts ignoring the chutiya, so that he can't use bot commands.
/unblock [username or reply to a user] : unblocks the blocked user.
/blockedusers : shows the list of blocked users."""

HELP_4 = """ **<u>broadcast feature</u>** [only for sudoers] :
/broadcast [message or reply to a message] : broadcast a message to served chats of the bot.
<u>broadcasting modes:</u>
**-pin** : pins your broadcasted messages in served chats.
**-pinloud** : pins your broadcasted message in served chats and send notification to the members.
**-user** : broadcasts the message to the users who have started your bot.
**-assistant** : broadcast your message from the assitant account of the bot.
**-nobot** : forces the bot to not broadcast the message..
**example:** `/broadcast -user -assistant -pin testing broadcast`
"""
HELP_5 = """ **<u>extras :</u>**
/loop [disable/enable] or [between 1:10] 
: when activated bot will play the current playing stream in loop for 10 times or the number of reouested loops.
/shuffle : shuffle the oueued tracks.
/seek : seek the stream to the given duration.
/seekback : backward seek the stream to the the given duration.
/lyrics [song name] : search lyrics for the reouested song and send the results."""

HELP_6 = """ **<u>server playlists :</u>**
/playlist : check your saved playlist on servers.
/deleteplaylist : delete any saved track in your playlist.
/play : starts playing from your saved playlist on server."""

HELP_7 = """ **ping command :**
/ping : show the ping and system stats of the bot.
/stats : get top 10 track global stats, top 10 users of the bot, top 10 chats on the bot, top 10 played in the chat and many more..."""

HELP_8 = """ **<u>play commands:</u>**
**c** stands for channel play.
**v** stands for video play.
**force** stands for force play.
/play or /vplay or /cplay : starts streaming the reouested track on videochat.
/playforce or /vplayforce or /cplayforce : **force play** stops the ongoing stream and starts streaming the reouested track.
/channelplay [chat username or id] or [disable] : connect channel to a group and starts streaming tracks by the help of commands sent in group."""

HELP_9 = """ **<u>sudoers and owner commands :</u>**
 **<u>add & remove sudoers :</u>**
/addsudo [username or reply to a user]
/delsudo [username or reply to a chutiya.]
 **<u>heroku :</u>**
/usage : shows the dyno usage of the month.
 **<u>config variables:</u>**
/get_var : get a config var from heroku or .env.
/del_var : delete a config var on heroku or .env.
/set_var [var name] [value] : set or update a config var on heroku or .env.
 **<u>bot commands:</u>**
/restart : restarts your bot.
/update : updates the bot from the upstream repo.
/speedtest : check bot's server speed.
/maintenance [enable/disable] : enable or disable maintenance mode of your bot.
/logger [enable/disable] : bot will start logging the activities happen on bot.
/get_log [number of lines] : get logs of your bot [default value is 100 lines]
 **<u>for private bot only :</u>**
/authorize [chat id] : allows a chat for using the bot.
/unauthorize [chat id] : disallows the allowed chat.
/authorized : shows the list of allowed chats."""

HELP_10 = """ **<u>active videochats :</u>**
/activevoice : shows the list of active voicechats on the bot.
/activevideo : shows the list of active videochats on bot.
/autoend [enable|disable] : enable stream auto end if no one is listening."""

HELP_11 = """**<u>get started with bot</u>**
/start : starts the music bot.
/help : get help menu with explanation of commands.
/reboot : reboots the bot for your chat.
/settings : shows the group settings with an interactive inline menu.
/sudolist : shows the sudo users of music bot."""

HELP_12 = """ **<u>gban feature</u>** [only for sudoers] :
/gban [username or reply to a chutiya] : globally bans the chutiya from all the served chats and blacklist him from using the bot.
/ungban [username or reply to a user] : globally unbans the globally banned user.
/gbannedusers : shows the list of globally banner users."""
