from flogin import Plugin
import logging, os, sys

log = logging.getLogger("plugin")

plugin = Plugin()


@plugin.event
async def on_initialization():
    for keyword in plugin.metadata.keywords:
        await plugin.metadata.remove_keyword(keyword)

    await plugin.api.show_notification(
        "Flow Load Notification",
        "Flow Load Notification has loaded. Flow Launcher should finish loading monetarily.",
    )

    log.info(f"Notification sent, exiting pid {os.getpid()}")

    sys.exit()