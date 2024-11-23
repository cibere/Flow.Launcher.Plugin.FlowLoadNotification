from flowpy import Plugin

plugin = Plugin()

@plugin.event
async def on_initialization():
    for keyword in plugin.metadata.keywords:
        await plugin.metadata.remove_keyword(keyword)
        
    await plugin.api.show_notification("Flow Load Notification", "Flow Load Notification has loaded. Flow Launcher should finish loading monetarily.")