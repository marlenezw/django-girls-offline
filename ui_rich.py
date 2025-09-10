"""
A lightweight Rich-based conversational UI for the Django Girls tutorial agent.

This module provides an async-friendly interface compatible with the previous
Textual wrapper used by `test.py`. It intentionally avoids Textual and instead
uses `rich.console.Console` to render a clean, ChatGPT-like conversation view
that adapts to terminal splits and smaller widths.

Public surface (used by test.py):
- class RichChatUI:
    - async start()
    - async get_user_input() -> str
    - async add_agent_markdown(md: str)
    - async add_system_markdown(md: str)
    - show_loading(text: str)
    - hide_loading()

Notes:
- This UI runs in the main terminal and adapts to terminal size changes.
- It's designed to work well in split terminals for side-by-side usage.
- Uses Rich Panels and Markdown with responsive sizing.
"""
from __future__ import annotations

import asyncio
import os
from dataclasses import dataclass
from typing import Optional

from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.text import Text
from rich.prompt import Prompt

# Create console that adapts to current terminal size
console = Console(force_terminal=True, legacy_windows=False)


@dataclass
class RichChatUI:
    """Simple Rich-based chat UI that adapts to terminal size and splits.

    This class provides the minimal async-friendly API required by
    `test.py`. It renders messages using Rich panels that adapt to
    the current terminal width, making it suitable for split terminals.
    """

    _input_queue: asyncio.Queue[str] = None
    _running: bool = False

    def __post_init__(self):
        if self._input_queue is None:
            self._input_queue = asyncio.Queue()

    def _refresh_console_size(self) -> None:
        """Force console to refresh its size information."""
        try:
            # Force Rich to re-detect terminal size
            console._width = None
            console._height = None
            # This will cause Rich to re-detect size on next access
        except:
            pass  # Fallback gracefully if this internal API changes

    def _get_panel_width(self) -> Optional[int]:
        """Calculate appropriate panel width based on terminal size."""
        try:
            # Refresh console size information
            self._refresh_console_size()
            
            # Get current terminal size
            terminal_width = console.size.width
            
            # For very narrow terminals (less than 40 chars), use full width
            if terminal_width <= 40:
                return None  # Use full available width
            
            # For narrow terminals (split view), use full width with minimal padding
            elif terminal_width <= 60:
                return None  # Use full available width
            
            # For medium terminals, use 90% of width to maximize space usage
            elif terminal_width <= 100:
                return max(40, int(terminal_width * 0.9))
            
            # For wide terminals, cap at reasonable width for readability
            else:
                return 90
                
        except (AttributeError, OSError):
            # Fallback if we can't determine terminal size
            return None  # Use full width as safest fallback

    async def start(self) -> None:
        if self._running:
            return
        self._running = True
        
        # Clear screen and show a compact header
        console.clear()
        console.print("")

    async def get_user_input(self) -> str:
        # Use synchronous input with responsive prompt
        try:
            # Refresh console size and get terminal width for prompt formatting
            self._refresh_console_size()
            terminal_width = console.size.width
            
            if terminal_width <= 30:
                # Ultra-compact prompt for very narrow terminals
                text = Prompt.ask("[bold purple]>[/]")
            elif terminal_width <= 50:
                # Compact prompt for narrow terminals
                text = Prompt.ask("[bold purple]You>[/]")
            else:
                # Full prompt for wider terminals
                text = Prompt.ask("[bold purple]You[/]")
            return text if text else ""
        except (EOFError, KeyboardInterrupt):
            return ""

    async def add_agent_markdown(self, md: str) -> None:
        # Responsive panel design based on current terminal width
        width = self._get_panel_width()
        terminal_width = console.size.width
        
        console.print()
        
        # Ultra-narrow terminals (less than 30 chars) - minimal UI
        if terminal_width <= 30:
            console.print(Panel(
                Markdown(md),
                title="🤖",
                title_align="left",
                border_style="orange1",
                padding=(0, 0),
                width=width,
                expand=True
            ))
        # Very narrow terminals (30-50 chars) - compact styling
        elif terminal_width <= 50:
            console.print(Panel(
                Markdown(md),
                title="🤖",
                title_align="left",
                border_style="orange1",
                padding=(0, 1),
                width=width,
                expand=True
            ))
        # Medium terminals (50-80 chars) - balanced styling
        elif terminal_width <= 80:
            console.print(Panel(
                Markdown(md),
                title="🤖 AI",
                title_align="left",
                border_style="orange1",
                padding=(0, 1),
                width=width,
                expand=False
            ))
        # Wide terminals - full styling
        else:
            console.print(Panel(
                Markdown(md),
                title="🤖 Assistant",
                title_align="left",
                border_style="orange1",
                padding=(1, 2),
                width=width,
                expand=False
            ))

    async def add_system_markdown(self, md: str) -> None:
        # Responsive panel design based on current terminal width
        width = self._get_panel_width()
        terminal_width = console.size.width
        
        console.print()
        
        # Ultra-narrow terminals (less than 30 chars) - minimal UI
        if terminal_width <= 30:
            console.print(Panel(
                Markdown(md),
                title="ℹ️",
                title_align="left", 
                border_style="blue",
                padding=(0, 0),
                width=width,
                expand=True
            ))
        # Very narrow terminals (30-50 chars) - compact styling
        elif terminal_width <= 50:
            console.print(Panel(
                Markdown(md),
                title="ℹ️",
                title_align="left", 
                border_style="blue",
                padding=(0, 1),
                width=width,
                expand=True
            ))
        # Medium terminals (50-80 chars) - balanced styling
        elif terminal_width <= 80:
            console.print(Panel(
                Markdown(md),
                title="ℹ️ Sys",
                title_align="left", 
                border_style="blue",
                padding=(0, 1),
                width=width,
                expand=False
            ))
        # Wide terminals - full styling
        else:
            console.print(Panel(
                Markdown(md),
                title="ℹ️ System",
                title_align="left", 
                border_style="blue",
                padding=(1, 2),
                width=width,
                expand=False
            ))

    def show_loading(self, text: str = "Loading tools") -> None:
        # Loading indicator removed per request (no-op)
        return

    def hide_loading(self) -> None:
        # No-op (loading removed)
        return


# Provide the same name the rest of the code expects
TextualChatUI = RichChatUI
