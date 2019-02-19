import nukescripts
import openfile

# Addon Menu
mb = menubar.addMenu("Penguin")
mb.addCommand("Issue_and_Bugs", "nukescripts.start('https://github.com/lazypic/nuke/issues')")
mb.addCommand("Slack", "nukescripts.start('https://lazypic.slack.com')")
mb.addCommand("Clip Library", "nukescripts.start('https://www.youtube.com/channel/UC0L_YtB4PWSkOwp2m9587MA/playlists?view_as=subscriber')")
mb.addCommand("Youtube", "nukescripts.start('https://www.youtube.com/channel/UCHsxW9hros1VlKKd4HAvG8A')")
mb.addCommand("-","","")
mb.addCommand("OpenFile", "openfile.openfile()", "F8", shortcutContext=2)
mb.addCommand("-","","")
mb.addCommand("StartPerformanceTimers", "nuke.startPerformanceTimers()")
mb.addCommand("StopPerformanceTimers", "nuke.stopPerformanceTimers()")

# Gizmo
tb = nuke.toolbar("Nodes")
m = tb.addMenu("Penguin", icon="lazypic_logo.png")
m.addMenu("Draw")
m.addCommand("Draw/Slate", "nuke.createNode('slate')")
m.addCommand("Draw/Timecode_burnin", "nuke.createNode('timecode_burnin')")
m.addMenu("Color")
m.addCommand("Color/mmColorTarget", "nuke.createNode('mmColorTarget')", icon="mmColorTarget.png")


## Format
nuke.addFormat("24 24 nukeIcon")
nuke.addFormat("360 360 kakaoEmoticon")

