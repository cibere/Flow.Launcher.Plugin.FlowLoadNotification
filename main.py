import os
import sys

parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, "lib"))
sys.path.append(os.path.join(parent_folder_path, ".venv", "lib", "site-packages"))

import asyncio
import logging

from flogin import Plugin

log = logging.getLogger("plugin")

plugin = Plugin()


@plugin.event
async def on_initialization() -> None:
    for keyword in plugin.metadata.keywords:
        await plugin.metadata.remove_keyword(keyword)

    if plugin.metadata.disabled:
        log.info("plugin disabled, not sending notification")
        await asyncio.sleep(2)
    else:
        await plugin.api.show_notification(
            "Flow Load Notification",
            "Flow Load Notification has loaded. Flow Launcher should finish loading monetarily.",
        )
        log.info("Notification sent")

    sys.exit()


plugin.run()
