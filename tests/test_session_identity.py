from unittest.mock import MagicMock

from ascii_rts_castle.config import create_default_game_config
from ascii_rts_castle.server.network import ClientSession, GameServer
from ascii_rts_castle.shared.models import PlayerId


def test_default_server_only_binds_loopback():
    assert GameServer(create_default_game_config()).host == '127.0.0.1'


def test_connection_sessions_can_be_registered_and_removed_after_join():
    server = GameServer(create_default_game_config())
    first = ClientSession(reader=MagicMock(), writer=MagicMock())
    second = ClientSession(reader=first.reader, writer=first.writer)
    server._all_sessions.add(first)
    server._all_sessions.add(second)
    assert len(server._all_sessions) == 2
    first.player_id = PlayerId(1)
    server._all_sessions.remove(first)
    assert server._all_sessions == {second}
