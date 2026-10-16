# Demo Video

## What to show

- Action from the first frame: cut loading screens, countdowns and idle walking. Twenty seconds of the claim beat a minute of setup.
- One thing that proves the claim at a glance. For "multiplayer in the browser", that is two different browsers side by side, each with its own player, visibly interacting: chat, a duel with skills, players facing each other.
- No burned-in captions unless the user asks: the post text carries the message.

## Recording a real app

- Script the scene with the app's own test hooks or autopilot instead of manual play. Stage it deterministically: positions, facing, levels, unlocked abilities, test accounts.
- Drive real browsers with Playwright persistent profiles that already hold the app's installed data. Use the installed Chrome channel without the automation infobar, and Firefox with the preferences the app needs. Give each browser its own configuration by intercepting its config request.
- Place the windows side by side with the operating system's window API. Record the desktop with ffmpeg (`gdigrab` on Windows, about 30 fps), stopped by the script once the scene reports its end.
- Before a take, tell the user how long it lasts. During it, send no messages, because notifications appear on screen. Do not kill a take halfway: the file ends up unreadable and the browsers come back with crash-restore prompts. Pass `--hide-crash-restore-bubble` to Chrome anyway.

## Review and edit

- Extract a few frames and look at them before showing anyone: popups, restore prompts, identifying text (tab titles, window names), players out of view, effects visible.
- Edit with ffmpeg: trim the idle start, blur identifying text, crop the taskbar, and encode H.264 `yuv420p` with `+faststart`. Keep it under the upload path's size limit by raising CRF, for example to stay under 10 MB.
- Send the file to the user for approval before attaching it to a post.

## Bugs the demo finds

A crash during a take is a real bug in the product, not a recording problem. Find the cause in the logs or stack, fix it in the product with the usual review, then record again.
