"""Shared analytical model placeholders."""

from dataclasses import dataclass


@dataclass(frozen=True)
class AnalysisRecord:
    """Placeholder record shape for analytical inputs."""

    raw: dict[str, object]
